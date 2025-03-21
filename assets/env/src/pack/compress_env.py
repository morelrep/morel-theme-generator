import os
import zipfile

def zip_directory(directory, zip_path):
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                rel_path = os.path.relpath(file_path, directory)
                zipf.write(file_path, rel_path)

directory_to_compress = '/run/media/febres/TOSHIBA EXT/Dev/MOREL 2.1/morel-theme/assets/env'
zip_path = '/run/media/febres/TOSHIBA EXT/Dev/MOREL 2.1/morel-theme/assets/source/assets/python-env.zip'

zip_directory(directory_to_compress, zip_path)
print(f'Contents of {directory_to_compress} compressed to {zip_path}.')
