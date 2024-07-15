# Audio_Steganography-
OverviewThis project focuses on audio steganography using Kali Linux to encrypt and decrypt messages within .wav audio files.RequirementsYour audio file must be in .wav format. If it is in .mp3 format, you can convert it to .wav using this converter.After converting to .wav, verify the following properties:Channels: It should be 1 (mono audio).Sample Width: It should be 2 bytes (16-bit audio).Sample Rate: It should be 44100 Hz (standard for audio).Note: If your audio file does not meet these properties, the provided code includes an option to convert the properties to the required format for encryption.StepsConvert to .wav (if necessary): Use the converter if your audio file is not already in .wav format.Verify Properties: Check the Channels, Sample Width, and Sample Rate as mentioned above.Encryption:Run the encryption script.When the program prompts, “Your file is ready for Encryption,” proceed to encrypt your audio file.Confirmation: After successful encryption, you will receive a confirmation prompt: “Data hidden successfully…”Decryption:Use the Decryption.ipynb script to decrypt the file.Retrieve the hidden text within the audio file using the provided passcode.
