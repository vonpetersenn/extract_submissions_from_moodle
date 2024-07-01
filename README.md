# Project Title: PDF File Copier

This simple Python script takes a zip folder of submissions from Moodle and returns all the submissions with meaningful filenames. A batch of submissions from students with arbitrary filenames will be extracted from the zip folder and returned in a coherent format:
```
FirstName1 MiddleName1 LastName1 Assignment.pdf
FirstName2 MiddleName2 LastName2 Assignment.pdf
...
```

## Installation
Option a) Download repository.


Option b) Copy `main.py` file to a folder with the structure 
```
root/
├── main.py
├── input/
└── output/
```
## Usage
1. download all submissions from moodle as a zip-file (using the `Alle Abgaben Herunterladen`-button).
2. place the zip-file in the `input` folder
3. run the following command in the terminal from the root-folder 
```shell 
python main.py
``` 
or
```shell
python main.py --append " AssignmentTitle"
```

The PDF files will be copied to the `output` folder.

## Limitations
- The script assumes that the submission of every student is a single pdf file.
- If moodle changes the structure of the zip-file, the script will no longer work.

## Requirements
- Python 3.x