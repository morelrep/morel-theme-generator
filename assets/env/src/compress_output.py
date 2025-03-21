import shutil
import os

ZIP_FILE = "output.zip"
FOLDERS_TO_ZIP = ["_authors", "_books", "_cities", "_publishers", "_repositories", "assets/img", "_data", "assets/data"]

def create_zip():
    """Compresses output folders into a zip file."""
    if os.path.exists(ZIP_FILE):
        os.remove(ZIP_FILE)
    shutil.make_archive("output", "zip", root_dir=".", base_dir=".")
    print("Zip file created:", ZIP_FILE)

if __name__ == "__main__":
    create_zip()
