# CSV Writer

A simple program that can create csv/tsv files, append new rows to existing csv/tsv files, and convert existing files between the csv or tsv formats. 

## Developer Instructions


### Dependencies

* [Poetry](https://python-poetry.org/) for dependency management.
* [Python (3.12-3.14)](https://www.python.org/downloads/)

### Directory Structure

* `csv_writer/main.py` is the file containing all of the code for the program.
* `pyproject.toml` is the configuration file used by poetry.
* `poetry.lock` controls dependency versions.
* `dist/main` the executable file created by [PyInstaller](https://pyinstaller.org/en/stable/) (the current one is only for mac).

### Development Instructions

* After the project has been git cloned, run `poetry install` to install the relevant dependencies from the `pyproject.toml`.
* To add a dependency, run `poetry add <dependency>`.
* To run the script via the poetry virtual environment, run `poetry run csv_writer`.
* To create a new executable, run `poetry run pyinstaller --onefile csv_writer/main.py`. This pyinstaller command will also produce other artifacts: the `build/` directory and `main.spec` file. I do not need these so I delete them. 


## User Instructions

### Running the program

There are two ways to run this program:

* Using the executable file `main`. Using a GUI this file can simply be clicked and using the command line you can just run `main`.
* Running `poetry run csv_writer` after the dependencies have been installed. 

### File Paths

Any file path you specify will always be created relative to the executable or the main.py file (whichever you are using). 

### How it works

* The program might take a few seconds to start up after running.
* You will first be asked if you want to create a new file. Answering no will allow you to edit an existing one.
* The rest of the on-screen instructions should be clear. 
* Remember, if the `main` executable is in `desktop/folder1/home/github/csv_files/main`, and you want to create or edit a csv file called `csv2.csv` in `desktop/folder1/home/` then you need to specify the file name or file path as `../../../csv2`.



