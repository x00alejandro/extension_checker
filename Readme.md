# File Analysis Tool

## Overview

This Python script provides a convenient way to analyze and manage files in a specified folder. It categorizes files based on their extensions and checks if they are valid JPG images. The tool is designed to work with relative folder paths, making it easy to inspect and organize your files.

## Prerequisites

Before running the script, ensure you have the required Python libraries installed. You can install them by running the following command:

```bash
pip install -r requirements.txt
```
The requirements.txt file lists the necessary dependencies for the script.

## Usage
Run the script by executing main.py in your terminal.

When prompted, enter the relative path to the folder you want to analyze. For example, if your folder is named my_folder and it's located in the same directory as the script, you can enter my_folder.

The script performs the following tasks:

Checks and installs required dependencies.
Analyzes all files in the specified folder.
Groups files based on their extensions.
Checks if files are valid JPG images.
The script displays the following information:

Extensions of all files with their names.
Valid JPG files.
Invalid JPG files.
To exit the script gracefully, press Ctrl+C. The script will display a "Goodbye!" message before termination.

## Example
Suppose you have a folder named my_files with various files, including images with different extensions. Running this script with the folder path my_files provides a summary of all the files in the folder and identifies valid and invalid JPG images.

```bash
Copy code
python main.py
```
Enter the relative folder path: my_files

## Dependencies
The script relies on two primary libraries:

python-magic: Used for determining file types based on content.
Pillow: Used for checking if a file is a valid JPG image.
These dependencies are listed in the requirements.txt file.

## Author
Alejandro Sol