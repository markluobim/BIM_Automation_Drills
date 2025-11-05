# drill_02_string_cleaning_(view_name)

# simulate View Name data exported from Revit (list of dictionaries)
view_name_data = [
    {'view_ID':701, 'View_Name':' A-101 Floor Plan '},
    {'view_ID':702, 'View_Name':'A-201 Ceiling Plan - final'},
    {'view_ID':703, 'View_Name':'B-301 Section @ WALL 5'},
    {'view_ID':704, 'View_Name':'B-302 East Elevation  '},
    {'view_ID':705, 'View_Name':'C-100 Detail.  '},
    {'view_ID':706, 'View_Name':'D-500 SCHEDULES(T)'},
    {'view_ID':707, 'View_Name':None}
]

print('--- Original View Name Data ---')
for item in view_name_data:
    print(item)
print('\n' + '='*50 + '\n')

# define function to check Mixed Case
# Input: string s; Output: Boolean (True if mixed case)
def check_mixed_case(s):
    if s is None or not isinstance(s, str):
        return False

    s_cleaned = s.strip()
    s_alpha = ''.join(filter(str.isalpha, s_cleaned))

    if not s_alpha:
        return False

    return not (s_alpha.isupper() or s_alpha.islower())

# execute audit loop
audit_results = []
whitespace_count = 0
mixed_case_count = 0

for record in view_name_data:                # record is dict
    view_name = record.get('View_Name')

    has_whitespace = False
    is_mixed_case = False

    if view_name is not None and isinstance(view_name, str):

        if view_name.strip() != view_name:
            has_whitespace = True
            whitespace_count += 1

        if check_mixed_case(view_name):
            is_mixed_case = True
            mixed_case_count += 1

    record['Has_Whitespace_Issue'] = has_whitespace
    record['Has_Mixed_Case_Issue'] = is_mixed_case

    audit_results.append(record)

# print audit summary
print('--- Audit Summary ---')

total_views_count = len(view_name_data) - 1        # one missing value None

print('Total Views: ' + str(total_views_count) + '(Exclude None)')
print('Views with Whitespace Issues: ' + str(whitespace_count))
print('Views with Mixed Case Issues: ' + str(mixed_case_count))

print('\n--- Audit Results List ---')
for record in audit_results:
    if record['Has_Whitespace_Issue'] or record['Has_Mixed_Case_Issue']:

        output_line = 'ID: ' + str(record['view_ID'])
        output_line = output_line + "', Name: '" + str(record['View_Name'])
        output_line = output_line + "', WS: '" + str(record['Has_Whitespace_Issue'])
        output_line = output_line + "', MC: '" + str(record['Has_Mixed_Case_Issue'])

        print(output_line)
