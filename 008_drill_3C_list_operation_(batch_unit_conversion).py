# drill_3C_list_operation_(batch_unit_conversion)

# simulate list of Structural Framing Lengths (Feet units)
structural_length_feet = [
    12.5,
    24.0,
    8.125,
    15.75,
    30.0
]
print('--- Original Data ---')
print(structural_length_feet)

# define function to convert units (Feet to Millimeters)
# round to 0 decimal places for practical construction data
def convert_feet_to_mm(length_in_feet):
    conversion_factor = 304.8
    return round(length_in_feet * conversion_factor, 0)

# define function to execute batch process with List Comprehension
def get_mto_lengths(lengths_in_feet):
    mto_lengths_mm = [
        convert_feet_to_mm(length)
        for length in lengths_in_feet
        if length >= 10.0
    ]
    return mto_lengths_mm

# execute batch process
processed_lengths_mm = get_mto_lengths(structural_length_feet)

print('\n--- Processed Data ---')
print(processed_lengths_mm)
