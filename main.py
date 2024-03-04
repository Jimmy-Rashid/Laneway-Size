from tkinter import *
from tkinter import ttk


def calculate(*args):
    house_seperation = 16

    try:
        lot_width_calc = int(lot_width.get())
        lot_length_calc = int(lot_length.get())
        floor_area_calc = int(floor_area.get()) # Not used?

        frontage = lot_width_calc
        lot_area = lot_width_calc * lot_length_calc
        gfa_setback.set(lot_area - (house_seperation * lot_width_calc) - (frontage * 10.7))
        gfa_site_coverage.set(lot_area * 0.5)
        gfa_186sqm.set(2002)
        gfa_25percent.set(lot_area * 0.25)

    except ValueError:
        pass


window = Tk()
window.title("Laneway Coverage Calculator")

mainframe = ttk.Frame(window, padding="5 5 20 20")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)

# Labels
# ----------------------------------------------------------------

ttk.Label(mainframe, text="Enter lot width/site frontage:").grid(
    column=1, row=1, sticky=(W, E)
)
ttk.Label(mainframe, text="Enter lot length:").grid(column=1, row=2, sticky=(W, E))
ttk.Label(mainframe, text="Enter the floor area of existing structures:").grid(
    column=1, row=3, sticky=(W, E)
)
ttk.Label(mainframe, text="Ft").grid(column=3, row=1, sticky=(W, E))
ttk.Label(mainframe, text="Ft").grid(column=3, row=2, sticky=(W, E))
ttk.Label(mainframe, text="Ft²").grid(column=3, row=3, sticky=(W, E))

gfa_setback = StringVar()
ttk.Label(mainframe, textvariable=gfa_setback).grid(column=1, row=5, sticky=(W, E))

gfa_site_coverage = StringVar()
ttk.Label(mainframe, textvariable=gfa_site_coverage).grid(
    column=1, row=6, sticky=(W, E)
)

gfa_186sqm = StringVar()
ttk.Label(mainframe, textvariable=gfa_186sqm).grid(column=1, row=7, sticky=(W, E))

gfa_25percent = StringVar()
ttk.Label(mainframe, textvariable=gfa_25percent).grid(column=1, row=8, sticky=(W, E))

# ----------------------------------------------------------------

# Entry
# ----------------------------------------------------------------

lot_width = StringVar()
width_entry = ttk.Entry(mainframe, width=5, textvariable=lot_width)
width_entry.grid(column=2, row=1, sticky=(W, E))

lot_length = StringVar()
length_entry = ttk.Entry(mainframe, width=5, textvariable=lot_length)
length_entry.grid(column=2, row=2, sticky=(W, E))

floor_area = StringVar()
floor_area_entry = ttk.Entry(mainframe, width=5, textvariable=floor_area)
floor_area_entry.grid(column=2, row=3, sticky=(W, E))

# ----------------------------------------------------------------

ttk.Button(mainframe, text="Calculate", command=calculate).grid(
    column=2, row=4, sticky=(W, E)
)


def calculate_gfa_criteria(
    lot_width_ft, lot_length_ft, existing_floor_area_sqft, main_house_separation_ft=16
):
    """
    Calculate the GFA under each criterion and determine the limiting factor.

    Parameters:
    - lot_width_ft: Width of the lot in feet (also used as site frontage)
    - lot_length_ft: Length of the lot in feet
    - existing_floor_area_sqft: Floor area of existing structures in square feet
    - main_house_separation_ft: Separation between the main house and laneway house in feet (fixed at 16ft)

    Returns:
    A dictionary containing the GFA under each criterion and the limiting factor.
    """
    # Convert site frontage to feet (in this case, it's the same as lot width)
    site_frontage_ft = lot_width_ft  # Since lot width = site frontage

    # Calculate the lot area in square feet
    lot_area_sqft = lot_width_ft * lot_length_ft

    # Calculate the GFA under each of the four criteria
    gfa_setbacks = (
        lot_area_sqft
        - (main_house_separation_ft * lot_width_ft)
        - (site_frontage_ft * 10.7)
    )  # Deduct the rear yard depth, assuming 10.7ft is the depth to be deducted
    gfa_site_coverage = lot_area_sqft * 0.50  # 50% site coverage
    gfa_186sqm = 2002  # GFA of 186 sqm in square feet
    gfa_25percent_lot = lot_area_sqft * 0.25

    # Determine the limiting criterion
    gfa_values = {
        "setbacks": gfa_setbacks,
        "site_coverage": gfa_site_coverage,
        "gfa_186sqm": gfa_186sqm,
        "gfa_25percent_lot": gfa_25percent_lot,
    }
    limiting_criterion = min(gfa_values, key=gfa_values.get)
    limiting_gfa = gfa_values[limiting_criterion]

    # Create a result dictionary
    result = {
        "gfa_criteria": gfa_values,
        "limiting_criterion": limiting_criterion,
        "limiting_gfa": limiting_gfa,
    }
    return result


def get_user_input():
    """
    Prompts the user for input and returns it as a dictionary.
    """
    inputs = {}
    inputs["lot_width_ft"] = float(input("Enter lot width/site frontage in feet: "))
    inputs["lot_length_ft"] = float(input("Enter lot length in feet: "))
    inputs["existing_floor_area_sqft"] = float(
        input("Enter the floor area of existing structures in square feet: ")
    )

    # Since main house separation is fixed, it's not requested from the user
    # inputs['main_house_separation_ft'] = 16 is predefined in the function parameters

    return inputs


def main():
    # Get user input
    user_inputs = get_user_input()

    # Calculate the GFA with the user input
    gfa_results = calculate_gfa_criteria(**user_inputs)

    # Output the GFA under each criterion
    print("\nGross Floor Area (GFA) by criteria:")
    for criterion, gfa in gfa_results["gfa_criteria"].items():
        limiting_factor_note = (
            " <-- Limiting factor"
            if criterion == gfa_results["limiting_criterion"]
            else ""
        )
        print(f"{criterion}: {gfa} sqft{limiting_factor_note}")

    # Provide a descriptive note for the user
    print(
        f"\nThe limiting factor for GFA is the '{gfa_results['limiting_criterion']}' criterion, which allows for a maximum of {gfa_results['limiting_gfa']} sqft."
    )


for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)
# number_entry.focus()
window.bind("<Return>", calculate_gfa_criteria)

window.mainloop()
