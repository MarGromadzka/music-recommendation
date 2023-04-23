from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os

gauth = GoogleAuth()
drive = GoogleDrive(gauth)

upload_file_list = os.listdir('.')
for upload_file in upload_file_list:
    gfile = drive.CreateFile({'parents': [{'id': '1zDtRMmkQE1r_1vRuntX8vP6Qs77XFZtY'}]})
    # Read file and set it as the content of this instance.
    gfile.SetContentFile(upload_file)
    os.chdir('../../../src/data')
    gfile.Upload()  # Upload the file.
    os.chdir('../../data/processed/spectrograms')
