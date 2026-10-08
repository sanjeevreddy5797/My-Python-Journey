print("----------Welcome to Caesar Cipher----------")
condition = True
while condition:
    en_or_de = input("Type 'encrypt' for encryption, type 'decrypt' for decryption:")

    
    if(en_or_de == "encrypt"):
        message = input("Type your message:")
        shift_number = int(input("Type the shift number:")) 
        encrypted_message = ""
        for ch in message:
          if ch == " ":
            encrypted_message += ch
          else:
            new_char = chr((ord(ch) - 97 + shift_number) % 26 + 97)
            encrypted_message += new_char
        print(f"Here is the text after encryption:{encrypted_message}")


    elif(en_or_de == "decrypt"):
        message = input("Type your message:")
        shift_number = int(input("Type the shift number:")) 
        decrypted_message = ""
        for ch in message:
          if ch == " ":
            decrypted_message += ch
          else:
            new_char = chr((ord(ch) - 97 - shift_number) % 26 + 97)
            decrypted_message += new_char
        print(f"Here is the text after decrypted message:{decrypted_message}")


    condition1 = input("Type 'yes' is you want to go again. Otherwise type 'no'.")
    if (condition1 == "yes"):
        condition = True
    else:
        condition = False
        print("Good Bye.")    