# Project Title: PDF File Copier

This Python script copies PDF files from subfolders with a specified specifier. It's designed to work with a .zip file that you get when you download all submissions of an assignment from Moodle. Each .zip file contains a folder of subfolders. Each subfolder, formatted as 'Firstname Name_number_assignesubmission_file', represents a student and is assumed to contain a single .pdf or .PDF file.

This script automates the process of extracting individual student submissions from the downloaded .zip file. Instead of manually going through each subfolder to find and copy the PDF file, or using the Moodle page and downloading each assignment one by one.

## How to Use

1. Place your .zip file in the 'input' folder.
2. Run the script using the command `python main.py` in the shell.
3. If you want to add a string to the end of the pdf name, use the --append argument. For example, python main.py --append _assignment1.

The script will copy all PDF files from the subfolders into the 'output' folder, appending the specified string to the end of each file name.

## Requirements
- Python 3.x