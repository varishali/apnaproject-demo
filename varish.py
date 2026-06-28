class Encryptor:
    def __init__(self,filename):
        self.filename = filename

    def encrypt_file(self):
        with open(self.filename,"r") as file:
            data = file.read() 

        encrypted = ""

        for ch in data:
            encrypted += chr(ord(ch) + 3) 

        with open ("encrypted.txt","w") as file:
            file.write(encrypted)

        print("File Encrypted Successfully !")

encrypt = Encryptor("log.txt")

encrypt.encrypt_file()