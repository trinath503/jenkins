from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

class PYDRIVE(object):
    def __init__(self):
       self.set_gdrive_credentials
    def set_gdrive_credentials(self):
        self.g_login = GoogleAuth()
        try:
            if self.g_login.access_token_expired:
                # Refresh them if expired
                self.g_login.Refresh()
            self.g_login.LoadCredentialsFile("PyDrive.txt")
        except:
            self.g_login.LocalWebserverAuth()
        #Finally save the credentials 
        self.g_login.SaveCredentialsFile("PyDrive.txt")

        self.drive = GoogleDrive(self.g_login)


    def gdrive_upload_file(self,file_name):
        try:
            gdrive_upload_file = self.drive.CreateFile()
            gdrive_upload_file.SetContentFile(file_name)
            gdrive_upload_file.Upload()
        except:
            print("Problem while uploading file")

    def gdrive_download_file(self,file_id,upload_path, download_path):
        gdrive_dwnload_file = self.drive.CreateFile({'id': file_id})
        gdrive_dwnload_file.GetContentFile(gdrive_dwnload_file['title'])






