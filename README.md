# Password_Generator_and_Manager
Python program to create and store passwords for different online accounts for a single registered user.
Password encryption has been attempted by using the cryptography module(specifically the Fernet object).Both encryption and decryption has been carried out with the same key.
The python pickle module has been used to store the encrypted passwords in a {"Account":"Password"} style dictionary in the pass_man_dict2.pickle file. 
The main username and password credentials are stored in the email2.txt and password2.txt files.
Flaws:
To create a new username, you'll need to clear the email2.txt and password2.txt files maunally first. This issue is currently being worked on. 
