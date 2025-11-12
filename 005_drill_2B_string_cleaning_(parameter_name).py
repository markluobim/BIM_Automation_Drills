# drill_2B_string_cleaning_(parameter_name)

# simulate name data exported from Revit/Navisworks/Excel
raw_parameter_names = [
    'Revit_Level:1st Floor',
    'Wall Type Name [300mm]',
    'Door_ID/Mark',
    'HAVC-FLOW_RATE(m3/s)',
    'FURNITURE NAME',
    'Model.Status',
    'Asset Tag N°',
]

# list of illegal characters or delimiters (should be replaced with '_')
# a common requirement for data cleaning
illegal_characters = [':',' ','/','[',']','(',')','.','°','-']

# use a loop to iterate through each raw parameter
for index, raw_param in enumerate(raw_parameter_names):
    standardized_param = raw_param.lower()

    for char in illegal_characters:
        standardized_param = standardized_param.replace(char, '_')

    while '__' in standardized_param:
        standardized_param = standardized_param.replace('__','_')

    standardized_param = standardized_param.strip('_')

    # print results
    report_line = '{:<2} | {:<30} | {:<30}'.format(
        index +1,
        "'{}'".format(raw_param),
        "'{}'".format(standardized_param),
    )
    print(report_line)
