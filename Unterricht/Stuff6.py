import random

# Generate 10 students with random names
students = [{'first_name': f'Student{i}', 'last_name': f'Last{i}', 'id': i} for i in range(1, 11)]

# Access and print student information
for student in students:
    print(f"Student ID: {student['id']}, Name: {student['first_name']} {student['last_name']}")

# Extract first names into a list
first_names = [student['first_name'] for student in students]

# Use sets to find duplicates
duplicates = {name: first_names.count(name) for name in set(first_names) if first_names.count(name) > 1}

# Print duplicates
if duplicates:
    print("Duplicate first names:")
    for name, count in duplicates.items():
        print(f"{name}: {count}")
else:
    print("No duplicate first names.")
