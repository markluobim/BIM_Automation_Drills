# drill_01_mapping

# define the BIM mapping dictionary
material_map = {
    'Concrete, Cast-in-Place, Gray':'03 30 00',
    'Metal - Steel':'05 29 00',
    'Gypsum Wallboard':'09 29 00',
}

# function encapsulation
# function: safely maps material names to MasterFormat standard codes.
def map_material_code(material_name):
    cleaned_name = material_name.strip()
    standard_code = material_map.get(cleaned_name,'NO STANDARD code')
    return standard_code

# test data
test_materials = [
    'Concrete, Cast-in-Place, Gray',
    'Metal - Steel',
    'Gypsum Wallboard',
    'Pine Wood',
]
# execute and validate results
print('--- START mapping ---')
for material in test_materials:
    result_code = map_material_code(material)
    output_string = 'Material: ' + material.strip() + ' --> MasterFormat Code:' + result_code
    print(output_string)
print('--- END mapping ---')

