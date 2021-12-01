import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token
    
    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)
    
def main():
    access_token = 'LD0BjkrJEI4AAAAAAAAAAUgguy1p7NSXGwEdRt0bRtVqhVS755OHMLKlonEzywX5'
    transferData = TransferData(access_token)

    file_from = input("Enter the file you want to upload: ")
    file_to = input("Enter your destination of the file: ")

    transferData.upload_file(file_from, file_to)
    print("FILE UPLOADED")

main()