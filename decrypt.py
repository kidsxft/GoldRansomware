import os
from dotenv import load_dotenv
from cryptography.fernet import Fernet

load_dotenv()

files = []

for file in os.listdir():
    if file.endswith(".py") or file.endswith(".key") or file.endswith(".key"):
        continue
    if os.path.isfile(file):
        files.append(file)

#print(files)

with open("key.key", "rb") as thekey:
    key = thekey.read()

for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    #print(key)
    #print(contents)
    #missing_padding = 4 - len(key) % 4
    #if missing_padding:
    #    key += b'=' * missing_padding
    contents_dec = Fernet(key).decrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_dec)
    os.remove("phrase.key")
    os.remove("key.key")