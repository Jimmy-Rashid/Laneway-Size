def input_data():
    print("Please enter the following information:")
    lot_size_ft2 = float(input("Lot Size (in square feet): "))
    dimensions = input("Lot Dimensions (e.g., 33x122 Ft): ")
    floor_area_ft2 = float(input("Floor Area (in square feet): "))
    
    # Extract width and depth from dimensions
    width, depth = map(int, dimensions.split('x'))
    
    return lot_size_ft2, width, depth, floor_area_ft2

def calculate_coverage(lot_size_ft2, width, depth):
    sqft_to_sqm = 0.092903
    percent_to_decimal = 0.01
    
    # Setback and other requirements
    rear_setback_ft = 3
    side_setback_ft = 4
    minimum_separation_ft = 16
    
    # Calculations
    max_coverage_50_percent = lot_size_ft2 * 0.5
    gfa_limit_sqft = 186 / sqft_to_sqm
    gfa_25_percent_lot = lot_size_ft2 * (25 * percent_to_decimal)
    
    effective_width_ft = width - (2 * side_setback_ft)
    effective_depth_ft = depth - rear_setback_ft - minimum_separation_ft
    effective_buildable_area_ft2 = effective_width_ft * effective_depth_ft
    
    # Determine limiting factor
    limiting_values = {
        "50% Site Coverage": max_coverage_50_percent,
        "GFA 186 sqm": gfa_limit_sqft,
        "GFA 25% Lot": gfa_25_percent_lot,
        "Setbacks": effective_buildable_area_ft2
    }
    
    limiting_factor = min(limiting_values, key=limiting_values.get)
    max_coverage = limiting_values[limiting_factor]
    
    return max_coverage, limiting_factor

def main():
    lot_size_ft2, width, depth, floor_area_ft2 = input_data()
    max_coverage, limiting_factor = calculate_coverage(lot_size_ft2, width, depth)
    print(f"Maximum coverage is limited by {limiting_factor}, allowing for {max_coverage:.2f} sqft.")

if __name__ == "__main__":
    main()
