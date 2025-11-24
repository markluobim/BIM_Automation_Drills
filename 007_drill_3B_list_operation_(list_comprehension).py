# drill_3B_list_operation_(list_comprehension)

# simulate data input (list all wall type names gathered from Revit)
allwalltype_names = [
    'Basic Wall: Generic - 200mm',
    'Basic Wall: Exterior - Brick on CMU',
    'Basic Wall: Fire-Rated - 1 HR',
    'Basic Wall: Interior - Fire 2 HR',
    'Basic Wall: Generic - 150mm',
    'Basic Wall: Interior - Partition 1200mm',
    'Curtain Wall: Exterior Glazing',
    'Basic Wall: Exterior - Fire 1 Hr Assembly'
]
print(f"Total Element Count: {len(allwalltype_names)}")

# define filtering criteria (keywords)
fire_keywords = ['Fire', 'Fire-Rated', '1 Hr', '2 Hr']
print(f"Keywords: {fire_keywords}")

# filtering using List Comprehension with IF Condition
non_fire_rated_walls = [
    wall_name for wall_name in allwalltype_names
    if not any(keyword.lower() in wall_name.lower() for keyword in fire_keywords)
]
# allwalltype_name & fire_keywords are Iterables (source lists)
# wall_name & keyword are Loop Variables

# print results
print(f"Non Fire-Rated Element Count: {len(non_fire_rated_walls)}")
print('List of Wall Names:')
for wall in non_fire_rated_walls:
    print(wall)
