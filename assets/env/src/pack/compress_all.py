import os
import zipfile

def zip_directory(directory, zip_path):
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                rel_path = os.path.relpath(file_path, directory)
                zipf.write(file_path, rel_path)

directory_to_compress = '../../../../assets/source'
zip_path = '../../../../assets/unpack-and-copy-content-to-main-folder.zip'

zip_directory(directory_to_compress, zip_path)
print(f'Contents of {directory_to_compress} compressed to {zip_path}.')
