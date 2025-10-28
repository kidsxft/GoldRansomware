# GoldMalware
Malware for fun.

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

# GoldRansomware.py

When the program is ran, it will send the IP of the user and the Username of the user to a discord channel. It will also send the key used to encrypt/ decrypted the files and will also send the phrase needed to decrypt. It is possible to change the webhook URL (line 15).

The `key.key` (file that contains the encryption key) and the `phrase.key` (file that contains the phrase to decrypt) file will be made hidden. These files can be viewed in file explorer > view > hidden items (turned on). These files are made when the main program (`GoldRansomware.py`) is ran, and if the phrase is given/ decrpyted, these 2 files will be deleted. 

When encrypted, files cannot be read anymore. Do not worry, as it is easy to restore. This program has no malicious code.

`GoldDecrypt.py` is not necessary, but can be used if unable to decrypt (for example not knowing the phrase). It can also be used to quickly decrypt the files, if you don't want to go through the "phrase" part. The main program is `GoldRansomware.py`. The main program is able to encrypt and decrypt by itself, which is why the second program is not as important.

If the program is closed, keys and phrases will not change, meaning files will not be lost forever. Files that are in the same directory as the program will be affected, so it is easy to control. It cannot affect other files outside unless edited.
