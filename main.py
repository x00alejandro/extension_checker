import os
import subprocess

# Check and install required dependencies
def check_and_install_dependencies():
    try:
        import magic
        from PIL import Image
    except ImportError:
        print("Installing required dependencies...")
        subprocess.run(["pip", "install", "-r", "requirements.txt"], check=True)
        print("Dependencies installed.")

class GetExtension:
    def __init__(self, file_path):
        self.file_path = file_path

    def get_file_extension(self):
        import magic
        mime = magic.Magic()
        file_type = mime.from_file(self.file_path)
        return file_type.split()[0]

class IsValid:
    def __init__(self, file_path):
        self.file_path = file_path

    def is_valid_jpg(self):
        try:
            from PIL import Image
            with Image.open(self.file_path) as img:
                return img.format == 'JPEG'
        except:
            return False

def graceful_exit(signum, frame):
    print("\nGoodbye!")
    sys.exit(0)

import signal
signal.signal(signal.SIGINT, graceful_exit)

if __name__ == "__main__":
    check_and_install_dependencies()

    folder_path = input("Enter the relative folder path: ")

    # Convert the relative path to an absolute path
    folder_path = os.path.abspath(folder_path)

    file_extension_groups = {}
    valid_files = []
    invalid_files = []

    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            if os.path.isfile(file_path):
                get_extension = GetExtension(file_path)
                file_extension = get_extension.get_file_extension()

                is_valid = IsValid(file_path)
                if is_valid.is_valid_jpg():
                    valid_files.append(file_name)
                else:
                    invalid_files.append(file_name)

                if file_extension not in file_extension_groups:
                    file_extension_groups[file_extension] = [file_name]
                else:
                    file_extension_groups[file_extension].append(file_name)

    print("Extensions of all files with names:")
    for ext, file_list in file_extension_groups.items():
        print(f"{ext}: {', '.join(file_list)}")

    print("\nValid JPG files:")
    for file_name in valid_files:
        print(file_name)

    print("\nInvalid JPG files:")
    for file_name in invalid_files:
        print(file_name)
