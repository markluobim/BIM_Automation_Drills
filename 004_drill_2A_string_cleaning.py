# drill_2A_string_cleaning_(family_name)

# define standards (suppose family names: D-(Door),W-(Wall),F-(Floor))
standard_prefixes = ['D-','W-','F-']

# simulate name data exported from Revit
raw_family_names_from_revit = [
    ' W-EXT-300',
    'D-INT-90',
    'f-panel-60',
    '  Wall-Standard-125',
    'D-INT-2100- ',
    'Bad_Name_001',
    None
]

# define function to strip spaces, covert to uppercase, check prefix
# and to return the cleaned names or None
def clean_and_check(raw_family_name:str, valid_prefixes:list) -> str or None:
    if not isinstance(raw_family_name, str):
        return None

    cleaned_name = raw_family_name.strip().upper()

    is_valid = False

    for prefix in valid_prefixes:
        if cleaned_name.startswith(prefix):
            is_valid = True
            break

    if is_valid == True:
        return cleaned_name
    else:
        return None

# batch execution, iterate through the list of raw names
validated_names = []

for name in raw_family_names_from_revit:
    cleaned_name = clean_and_check(name, standard_prefixes)

    validated_names.append(cleaned_name)

# print results
print('--- RESULTS ---')
print('**RAW FAMILY NAMES**')
print('{}'.format(raw_family_names_from_revit))
print('**CLEANED FAMILY NAMES**')
print('{}'.format(validated_names))
