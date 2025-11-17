# drill_3A_list_operation_(filter_data)

# simulate data exported from Revit/Dynamo (list of tuples)
# one tuple = (Category, Type Name, Level, Fire Rating Value)
raw_element_data = [
    ('Walls','Basic Wall-Exterior EIFS','Level 1','None'),
    ('Doors','M_Single-Flush-0915 x 2134','Level 1','90 Min'),
    ('Windows','M_Fixed-Picture','Level 2','None'),
    ('Doors','M_Double-Flush-1830 x 2134','Level 1','120 Min'),
    ('Doors','M_Single-Flush-0915 x 2134','Level 2','None'),
    ('Windows','M_Casement-Single-0450 x 0600','Level 2','60 Min'),
    ('Columns','W-Wide Flange Column','Level 1','None')
]

# define tuple index
IDX_CATEGORY = 0
IDX_TYPE_NAME = 1
IDX_FIRE_RATING = 3

# define function to loop and filter fire-rated data
def filter_fire_rated_elements(data_list):
    filtered_results = []

    for element_tuple in data_list:
        is_door = element_tuple[IDX_CATEGORY] == 'Doors'
        has_fire_rating = element_tuple[IDX_FIRE_RATING] != 'None'

        if is_door and has_fire_rating:
            result_item = (element_tuple[IDX_TYPE_NAME], element_tuple[IDX_FIRE_RATING])

            filtered_results.append(result_item)

    return filtered_results

filtered_results_doors = filter_fire_rated_elements(raw_element_data)

# print results
print('Raw Data Count: ' + str(len(raw_element_data)))
print('Filtered Results: ')

for item in filtered_results_doors:
    output_line = '  Type: {0}, Fire Rating: {1}'.format(item[0],item[1])
    print(output_line)

