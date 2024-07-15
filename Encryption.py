
import wave
import struct
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import scipy.io.wavfile as wav
import os
import base64
import getpass

SALT = b'fixed_salt_here'  # Use a fixed salt

def check_wav_prop(audio_file):
    try:
        wav_file = wave.open(audio_file, 'rb')
        # Check properties (channels, sample width, sample rate)
        channels = wav_file.getnchannels()
        sample_width = wav_file.getsampwidth()
        sample_rate = wav_file.getframerate()

        print(f"\tChannels: {channels}")
        print(f"\tSample Width (bytes): {sample_width}")
        print(f"\tSample Rate (Hz): {sample_rate}")        

        if(channels > 1 or sample_width != 2 or sample_rate != 44100):
            print(" \nNOTE : The audio file is in INVALID FORMAT ")
            reply = input(" \nTo convert the audio file into valid format press (y/n)")
            if(reply.lower() == "y"):
                convert_to_mono(audio_file)
        print("Your file is ready for Encryption")
        wav_file.close()
    except wave.Error as e:
        print(f"Error: {e}")

def convert_to_mono(input_file):
    try:
        wav_file = wave.open(input_file, 'rb')
        num_channels = wav_file.getnchannels()
        desired_sample_rate = 44100
        
        frames = wav_file.readframes(wav_file.getnframes())
        mono_frames = bytearray()

        for i in range(0, len(frames), num_channels * 2):
            # Calculate the average of all channels
            sample_sum = 0
            for j in range(num_channels):
                sample = struct.unpack('<h', frames[i + j * 2:i + (j + 1) * 2])[0]
                sample_sum += sample

            mono_sample = sample_sum // num_channels
            mono_frames.extend(struct.pack('<h', mono_sample))
        wav_file.close()

        # Write mono frames to a new WAV file
        with wave.open(input_file, 'wb') as output_wav:
            output_wav.setnchannels(1)
            output_wav.setsampwidth(2)
            output_wav.setframerate(desired_sample_rate)  # Set the desired frame rate
            output_wav.writeframes(mono_frames)

        print(f"Converted to a valid file and saved as {input_file}")
    except wave.Error as e:
        print(f"Error: {e}")

def generate_key(password, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    return key

def encrypt_data(data, key):
    f = Fernet(key)
    return f.encrypt(data.encode())

def hide_data(audio_file, output_file, data, password):
    try:
        wav_file = wave.open(audio_file, 'rb')
        if wav_file.getnchannels()!= 1 or wav_file.getsampwidth()!= 2 or wav_file.getframerate()!= 44100:
            raise ValueError('Invalid audio file format')
        frames = wav_file.readframes(wav_file.getnframes())
        key = generate_key(password, SALT)
        data_bytes = encrypt_data(data, key)
        binary_data = ''.join(format(byte, '08b') for byte in data_bytes)
        data_size = len(binary_data)
        max_data_size = len(frames) * 8
        if data_size > max_data_size:
            raise ValueError('Data too large for audio file.')
        data_index = 0
        new_frames = bytearray(frames)
        for i in range(len(frames)):
            if data_index < data_size:
                bit = binary_data[data_index]
                new_frames[i] = (new_frames[i] & 0b11111110) | int(bit)
                data_index += 1
        wav_file.close()
        wav_file = wave.open(output_file, 'wb')
        wav_file.setnchannels(1)
        wav_file.setsampwidth(2)
        wav_file.setframerate(44100)
        wav_file.writeframes(new_frames)
        wav_file.close()
        print('Data hidden successfully...')
    except wave.Error as e:
        print(f'Error: {e}')
    except ValueError as e:
        print(f'Error: {e}')
    except Exception as e:
        print(f'Error: {e}')

def main():
    while True:
        print("\n\nEnter \t1.To Check .wav file\n\t2.To hide text in .wav file\n\t3.Exit\n\n")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            audio_file = input("Enter the path of your .wav file:")
            if audio_file[0] == "\"":
                audio_file = audio_file[1:-1]
            check_wav_prop(audio_file)
        elif choice == 2:
            audio_file = input("Enter the path of your .wav file:")
            if audio_file[0] == "\"":
                audio_file = audio_file[1:-1]
            output_file = input("Enter the name of the file to be saved (make sure to provide extension .wav): ")
            if output_file[0] == "\"":
                output_file = output_file[1:-1]
            data = input("Enter the text to hide:")
            password = getpass.getpass('Enter password: ')
            hide_data(audio_file, output_file, data, password)
        elif choice == 3:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()

Enter 	1.To Check .wav file
	2.To hide text in .wav file
	3.Exit


	Channels: 2
	Sample Width (bytes): 2
	Sample Rate (Hz): 48000
 
NOTE : The audio file is in INVALID FORMAT 
Converted to a valid file and saved as D:/Sample Audio.wav
Your file is ready for Encryption


Enter 	1.To Check .wav file
	2.To hide text in .wav file
	3.Exit


 
