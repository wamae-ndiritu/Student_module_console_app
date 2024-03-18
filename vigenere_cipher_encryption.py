import csv
import os

def vigenere_cipher_encrypt(plaintext, key):
    encrypted_text = ''
    key_length = len(key)
    for i in range(len(plaintext)):
        shift = ord(key[i % key_length]) - ord('a')
        encrypted_char = chr(((ord(plaintext[i]) - ord('a') + shift) % 26) + ord('a'))
        encrypted_text += encrypted_char
    return encrypted_text

def main():
    # Prompt user for input
    first_name = input("Enter your first name: ").lower()
    last_name = input("Enter your last name: ").lower()
    username = input("Enter your username: ")
    password = input("Enter your password: ").lower()

    # Encrypt the password using Vigenère Cipher with a key based on the user's name
    vigenere_key = first_name + last_name
    encrypted_password = vigenere_cipher_encrypt(password, vigenere_key)

    # Write user data to CSV file
    file_exists = os.path.isfile('user_encrypted.csv')
    with open('user_encrypted.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(['First Name', 'Last Name', 'Username', 'Password'])
        writer.writerow([first_name, last_name, username, encrypted_password])

    print("User data encrypted and stored successfully.")

if __name__ == "__main__":
    main()

