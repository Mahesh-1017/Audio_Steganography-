# Audio_Steganography-
# Project Overview: Audio Steganography with Kali Linux

This project demonstrates how to use Kali Linux to encrypt and decrypt messages embedded within .wav audio files using audio steganography.

## Requirements

1. **Audio Format**: The audio file must be in .wav format. If it is in .mp3 format, convert it to .wav using an appropriate converter.
2. **Audio Properties**: The .wav file must meet the following specifications:
   - **Channels**: Mono (1 channel)
   - **Sample Width**: 16-bit (2 bytes)
   - **Sample Rate**: 44100 Hz

If the audio file does not meet these properties, the provided code includes functionality to convert it to the required format for encryption.

## Steps

### 1. Convert to .wav (if necessary)
   - If your audio file is not already in .wav format, use a converter to change it from .mp3 to .wav.

### 2. Verify Properties
   - Ensure the .wav file has the following properties:
     - **Channels**: Mono (1 channel)
     - **Sample Width**: 16-bit (2 bytes)
     - **Sample Rate**: 44100 Hz

### 3. Encryption
   - Run the encryption script provided.
   - When prompted with “Your file is ready for Encryption,” proceed to encrypt your audio file.

### 4. Confirmation
   - After successful encryption, you will receive a prompt stating: “Data hidden successfully…”

### 5. Decryption
   - Use the Decryption.ipynb script to decrypt the file.
   - Retrieve the hidden text within the audio file using the provided passcode.

## Additional Notes
- The project includes scripts for both encryption and decryption processes.
- Ensure you have the required dependencies and libraries installed on Kali Linux to run the scripts successfully.

By following these steps, you can effectively embed and retrieve hidden messages within .wav audio files using audio steganography techniques on Kali Linux.
