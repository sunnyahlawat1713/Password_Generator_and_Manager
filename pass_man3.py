import pickle
import random
from cryptography.fernet import Fernet
max_len = 12
user_dict = {}
def password_generator():    
    digits = ['0','1','2','3','4','5','6','7','8','9']
    lowercase_characters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v',
                           'w','x','y','z']
    uppercase_characters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V',
                           'W','X','Y','Z']
    special_characters = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',  
               '*', '(', ')', '!', '^', '&', '_', '-', '<', ',', ';', '+', '[', ']', '{', '}', "'"]
    combined_characters = digits + lowercase_characters + uppercase_characters + special_characters
    random_digit = random.choice(digits)
    random_lowercase = random.choice(digits)
    random_uppercase = random.choice(digits)
    random_special = random.choice(digits)

    temp_password = random_digit + random_lowercase + random_uppercase + random_special
    for x in range(max_len - 4):
        temp_password = temp_password + random.choice(combined_characters)
        temp_password_list = list(temp_password)
        random.shuffle(temp_password_list)

    password = ""
    for x in temp_password_list:
        password = password + x
    return password


user_id = input("Enter your User ID(Press 1 to create account) : ")

with open("pass_man_dict2.pickle", 'rb') as filewrite:
    user_dict = pickle.load(filewrite)

if '1' in user_id:
    email = input("Enter your User ID: ")

    with open("email2.txt", 'w+') as f:
        store_email = f.write(email)

    password = password_generator()
    print("Here is your password: ", password)
    file_en = open('key.key', 'rb')
    key = file_en.read()
    file_en.close()
    encoded = password.encode()
    f = Fernet(key)
    encrypted = f.encrypt(encoded)

    file_open = open('password2.txt', 'wb')
    file_open.write(encrypted)
    file_open.close()

with open("email2.txt", 'r') as fr:
    store_email = fr.read()

if user_id == store_email:
    password2 = input("Enter your password: ")
    with open('password2.txt', 'rb') as ar:
        store_pass = ar.read()
        store_pass = store_pass.decode('utf-8')
        store_pass = bytes(store_pass, 'utf-8')
    file_en = open('key.key', 'rb')
    key = file_en.read()
    file_en.close()
    f2 = Fernet(key)
    #print(store_pass)
    decrypted = f2.decrypt(store_pass)
    decoded = decrypted.decode()
    print(decoded)
    if password2 == decoded:
        conf = input("To know your password press 1, to save your password press 2 :")
        if '2' in conf:
            account = input("Enter your account name : ")
            acc_pass = password_generator()
            print(acc_pass)
            confirmation = input("Would you like to save it (Y/N): ")

            if 'Y' in confirmation:
                file_en = open('key.key', 'rb')
                key = file_en.read()
                file_en.close()
                encoded = acc_pass.encode()
                f = Fernet(key)
                encrypted = f.encrypt(encoded)
                user_dict[account] = encrypted
                pickle_out = open('pass_man_dict2.pickle', 'wb')
                pickle.dump(user_dict, pickle_out)
                pickle_out.close()

                print("Done! : Your password has been saved")
            else:
                print("Your data has not been saved")
        elif '1' in conf:
            pickle_in = open('pass_man_dict2.pickle', 'rb')
            pickle.load(pickle_in)
            pickle_in.close()
            print(user_dict)
            account_find = input("Enter the username which the desired password belongs to: ")
            if account_find in user_dict:
                file_en = open('key.key', 'rb')
                key = file_en.read()
                file_en.close()
                f2 = Fernet(key)
                decrypted = f2.decrypt(user_dict[account_find])
                decoded = decrypted.decode()
                print("The requested password is: ", decoded)
            else:
                print("This Password is not saved")


