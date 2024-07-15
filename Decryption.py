
import wave
import base64
from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import os
import getpass

SALT = b'fixed_salt_here'  # Use the same fixed salt as in the encryption code

def generate_key(password):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=SALT,
        iterations=100000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    return key

def extract_data(audio_file, password):
    try:
        key = generate_key(password)
        f = Fernet(key)
        wav_file = wave.open(audio_file, 'rb')
        if wav_file.getnchannels() != 1 or wav_file.getsampwidth() != 2 or wav_file.getframerate() != 44100:
            raise ValueError('Invalid audio file format')
        frames = wav_file.readframes(wav_file.getnframes())
        binary_data = ''.join(format(frame & 0b00000001, '01b') for frame in frames)
        data_bytes = bytes(int(binary_data[i:i+8], 2) for i in range(0, len(binary_data), 8))
        try:
            decrypted_data = f.decrypt(data_bytes).decode()
            print(f'Decrypted data: {decrypted_data}')  # Debug print
            return decrypted_data
        except InvalidToken:
            raise ValueError('Invalid data')
    except wave.Error as e:
        print(f'Error: {e}')
    except ValueError as e:
        print(f'Error: {e}')
    except Exception as e:
        print(f'Error: {e}')
    return None

def main():
    audio_file = input("Enter the path of the Encrypted File:")
    if audio_file[0] == "\"":
        audio_file = audio_file[1:-1]
    password = getpass.getpass('Enter the password: ')
    data = extract_data(audio_file, password)
    if data:
        print('Extracted data:', data)

if __name__ == '__main__':
    main()
Decrypted data: Luffy
Extracted data: Luffy
 
