# drill_01_batch_parameter_mapping

# define standards (some enterprise standard Set)
standard_parameters = {
    'Height',
    'Width',
    'Fire_Rating',
    'Material_Finish'
}

# define the safe mapping dictionary
safe_map = {
    'height':'Height',
    'width':'Width',
    'firerating':'Fire_Rating',
    'matlfnish':'Material_Finish',
    ' fire rating ':'Fire_Rating',
    'width_mm':'Width'
}

# define the raw parameter list (simulate batch input)
raw_parameters_batch = [
    'Height',
    'WIDTH',
    'fireRating',
    'MaterialFinish',
    'Length_Parameter',
    'Door_Height_Value',
    'matlfinish',
    '  height ',
    'Comments',
    'width_mm'
]

# define the batch safe mapping function
def batch_safe_map(raw_param, safe_map, standard_parameters):
    # raw_param (str), safe_map (dict), standard_parameters (set)
    # raw_param is a placeholder
    cleaned_key = raw_param.strip().lower()
    mapped_param = safe_map.get(cleaned_key)

    if mapped_param:
        return mapped_param
    elif raw_param in standard_parameters:
        return raw_param
    else:
        print("ALERT: Param '" + raw_param + "' is unmappable and will be skipped.")
        return None

# dictionary to store final mapped results
final_mapped_results = {}
unmapped_count = 0

print('--- START audit ---')
for raw_name in raw_parameters_batch:
    mapped_result = batch_safe_map(raw_name, safe_map, standard_parameters)
    final_mapped_results[raw_name] = mapped_result

    if mapped_result is None:
        unmapped_count += 1
    else:
        print("Mapped: '%s' --> '%s'" % (raw_name, mapped_result))

# Loop End
print('\n--- Summary Report ---')
print("Total Parameters Processed: %d" % len(raw_parameters_batch))
print("Successfully Mapped: %d" % (len(raw_parameters_batch) - unmapped_count))
print("Unmapped Count: %d" % unmapped_count)

print("\n--- Final Mapped Results ---")
print(final_mapped_results)
