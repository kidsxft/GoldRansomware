# DISCLAIMER
This project does NOT contain malicious code. This is a project that I decided to make to step foot into cybersecurity. 

# GoldRansomware
Malware for educational purposes.

Modules needed to install:
- cryptography
- urllib3
- discord_webhook
- numpy
- dotenv

How to install modules:
1) Open command prompt
2) Type `pip install [module]`
3) For example: `pip install discord_webhook`

# main.py

This program runs as a ransomware. This python file will only affect files in the same directory, so it is safe. When the program is ran, it will send the user's IP, username, and affected files to a discord channel as part of a webhook. It will also send the key used to encrypt/ decrypt the files and will also send the "phrase" needed to decrypt. The "phrase" is a word randomly generated from a pre-existing list of words on the internet, and is required for users to decrypt their locked files. This is the "ransom" part of the program. It is possible to change the webhook URL to another (line 15).

The `key.key` (file that contains the encryption key) and the `phrase.key` (file that contains the phrase to decrypt) file will be made and will also be hidden. These files can be viewed in file explorer > view > hidden items (turned on). These files are made when the main program (`main.py`) is ran, and if the phrase is given/ decrpyted, these 2 files will be deleted. 

This is a text file.
<img width="883" height="176" alt="image" src="https://github.com/user-attachments/assets/84c499b0-4246-4edd-a37c-a3bb8193ea7f" />

After `main.py` is ran, this is what the text file contains.
<img width="1883" height="147" alt="image" src="https://github.com/user-attachments/assets/82db522c-06e7-4772-999f-cdd33959e380" />

As for the webhook, this is what the bot will send.
<img width="512" height="290" alt="image" src="https://github.com/user-attachments/assets/416627c0-10b9-4e6f-842d-8cc0c13b45f8" />

After the "phrase" is inputted into the terminal, all files and webhooks are reverted.

`GoldDecrypt.py` is not necessary, but can be used if unable to decrypt (for example not knowing the phrase). It can also be used to quickly decrypt the files, if you don't want to go through the "phrase" part. The main program is `main.py`. The main program is able to encrypt and decrypt by itself, which is why the second program is not as important.

If the program is closed, keys and phrases will not change, meaning files will not be lost forever. Files that are in the same directory as the program will be affected, so it is easy to control. It cannot affect other files outside unless edited.
