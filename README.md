# Studio File Renamer
A Python script that renames files to studio naming conventions. Built for VFX pipeline use.

## What it Does
This script takes as input a file path and renames the file using input from the user. The output follows the convention shot_010_comp_v001.exr.

## Pipeline Context
This script allows the user to rename a file into a standard format. Consistent naming is important in a studio environment, as pipeline tools will not be able to locate and process files if the files are named incorrectly. 

## How to Use
Run the script via the terminal:

`python3 studio_file_renamer.py`

Then follow the prompts to enter the file path, shot number, department, and version number.

## Requirements
Python 3.6 or higher. No external libraries required.

## Sample Output
```
Enter file location: /Path/to/your/file/example.exr
Enter shot number: 30  
Enter department: comp
Enter version number: 002
Renamed to: shot_030_comp_v002.exr
```
