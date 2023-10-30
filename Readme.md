File Analysis Tool
This is a Python script that analyzes files in a specified folder, categorizes them based on their extensions, and checks if they are valid JPG images. The script is designed to work with relative folder paths, and it can be used to efficiently manage and inspect your files.

Prerequisites
Before running the script, make sure you have the required Python libraries installed. You can install them by running the following command:

bash
Copy code
pip install -r requirements.txt
The requirements.txt file lists the necessary dependencies for the script.

Usage
Run the script by executing main.py in your terminal.

When prompted, enter the relative path to the folder you want to analyze. For example, if your folder is named my_folder and it's located in the same directory as the script, you can enter my_folder.

The script will perform the following tasks:

Check and install required dependencies.
Analyze all files in the specified folder.
Group files based on their extensions.
Check if files are valid JPG images.
The script will display the following information:

Extensions of all files with their names.
Valid JPG files.
Invalid JPG files.
To exit the script gracefully, press Ctrl+C. The script will display a "Goodbye!" message before termination.

Example
Let's say you have a folder named my_files with various files, including images with different extensions. By running this script with the folder path my_files, you can get a summary of all the files in the folder and identify valid and invalid JPG images.

bash
Copy code
python main.py
Enter the relative folder path: my_files
Dependencies
The script relies on two main libraries:

python-magic: Used for determining file types based on content.
Pillow: Used for checking if a file is a valid JPG image.
These dependencies are listed in the requirements.txt file.

Author
Alejandro Sol