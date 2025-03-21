import os

# Adjust paths to work from the src folder
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
FOLDERS_TO_CLEAN = [
    os.path.join(BASE_DIR, "_authors"),
    os.path.join(BASE_DIR, "_books"),
    os.path.join(BASE_DIR, "_cities"),
    os.path.join(BASE_DIR, "_publishers"),
    os.path.join(BASE_DIR, "_repositories"),
    os.path.join(BASE_DIR, "assets/img"),
    os.path.join(BASE_DIR, "_data"),
    os.path.join(BASE_DIR, "assets/data"),
]
ZIP_FILE = os.path.join(BASE_DIR, "output.zip")

def delete_generated_files():
    """Deletes generated files but keeps .keep files. Only prints if files were actually deleted."""
    files_deleted = False

    for folder in FOLDERS_TO_CLEAN:
        if os.path.exists(folder):
            for root, dirs, files in os.walk(folder):
                for file in files:
                    if file != ".keep":  # Keep .keep files
                        os.remove(os.path.join(root, file))
                        files_deleted = True

    # Remove the zip file after processing
    if os.path.exists(ZIP_FILE):
        os.remove(ZIP_FILE)
        files_deleted = True

    if files_deleted:
        print("Generated files deleted successfully.")

if __name__ == "__main__":
    delete_generated_files()
