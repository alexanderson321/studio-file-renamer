import os

# This script allows the user to rename a selected file
# Used in VFX pipelines to apply studio naming conventions to render output files
# Completed by Alex Anderson in April 2026

# The user inputs the filepath to the file they want to rename
original_path = input("Enter file location: ")
folder = os.path.dirname(original_path)

# Verify file exists, then prompt the user for shot info and rename accordingly
if os.path.exists(original_path):
    shot = input("Enter shot number: ")
    department = input("Enter department: ")
    version = input("Enter version number: ")
    new_filename = f"shot_{shot.zfill(3)}_{department}_v{version.zfill(3)}.exr"
    new_path = os.path.join(folder, new_filename)
    os.rename(original_path, new_path)
    print(f"Renamed to: {new_filename}")
else:
    print("Error. File location is incorrect")  
