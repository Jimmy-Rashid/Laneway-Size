from tkinter import *
from tkinter import ttk


def calculate(event):
    house_seperation = 16

    try:
        lot_width_calc = float(lot_width.get())
        lot_length_calc = float(lot_length.get())
        floor_area_calc = float(floor_area.get())  # Not used?

        frontage = lot_width_calc
        lot_area = lot_width_calc * lot_length_calc

        gfa_setback_label.set("Setbacks: ")
        gfa_site_coverage_label.set("Site Coverage: ")
        gfa_186sqm_label.set("186m² GFA: ")
        gfa_25percent_label.set("25% GFA: ")

        gfa_setback.set(
            format(
                (lot_area - (house_seperation * lot_width_calc) - (frontage * 10.7)),
                ".2f",
            )
            + " Ft²"
        )
        gfa_site_coverage.set(format((lot_area * 0.5), ".2f") + " Ft²")
        gfa_186sqm.set(str(2002) + " Ft²")
        gfa_25percent.set(format((lot_area * 0.25), ".2f") + " Ft²")
        
        gfa_values = {
            "Setbacks": str(gfa_setback.get()),
            "Site Coverage": str(gfa_site_coverage.get()),
            "186m² GFA": str(gfa_186sqm.get()),
            "25% GFA": str(gfa_25percent.get()),
        }
        limiting_criterion = min(gfa_values, key=gfa_values.get)
        limiting_gfa = str(gfa_values[limiting_criterion])
        gfa_results.set("\nThe limiting factor for GFA is the " + limiting_criterion + " criterion,\n which allows for a maximum of " + str(limiting_gfa) + " sqft.")

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
ttk.Label(mainframe, text="Enter existing structure floor area:").grid(
    column=1, row=3, sticky=(W, E)
)
ttk.Label(mainframe, text="Ft").grid(column=3, row=1, sticky=(W, E))
ttk.Label(mainframe, text="Ft").grid(column=3, row=2, sticky=(W, E))
ttk.Label(mainframe, text="Ft²").grid(column=3, row=3, sticky=(W, E))

gfa_setback_label = StringVar()
ttk.Label(mainframe, textvariable=gfa_setback_label).grid(
    column=1, row=5, sticky=(W, E)
)

gfa_setback = StringVar()
ttk.Label(mainframe, textvariable=gfa_setback).grid(column=2, row=5, sticky=(W, E))

gfa_site_coverage_label = StringVar()
ttk.Label(mainframe, textvariable=gfa_site_coverage_label).grid(
    column=1, row=6, sticky=(W, E)
)

gfa_site_coverage = StringVar()
ttk.Label(mainframe, textvariable=gfa_site_coverage).grid(
    column=2, row=6, sticky=(W, E)
)

gfa_186sqm_label = StringVar()
ttk.Label(mainframe, textvariable=gfa_186sqm_label).grid(column=1, row=7, sticky=(W, E))

gfa_186sqm = StringVar()
ttk.Label(mainframe, textvariable=gfa_186sqm).grid(column=2, row=7, sticky=(W, E))

gfa_25percent_label = StringVar()
ttk.Label(mainframe, textvariable=gfa_25percent_label).grid(
    column=1, row=8, sticky=(W, E)
)

gfa_25percent = StringVar()
ttk.Label(mainframe, textvariable=gfa_25percent).grid(column=2, row=8, sticky=(W, E))

gfa_results = StringVar()
ttk.Label(mainframe, textvariable=gfa_results).grid(column=1, row=10, columnspan=2, sticky=(W, E))

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

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)
width_entry.focus()
window.bind("<Return>", calculate)

window.mainloop()
