# AUDIO STEGANOGRAPHY OPERATIONS
# 1. Encode the Text message
# 2. Decode the Text message
# 3. Exit

import wave


def audio_steganography(file):
    def Encode():
        pass

    def Decode():
        pass

    while True:
        print("AUDIO STEGANOGRAPHY OPERATIONS\n")
        print("1.Encode the Text message")
        print("2.Decode the Text message")
        print("3.Exit")
        n = int(input("Enter Your Choice:"))
        if n == 1:
            Encode()
        elif n == 2:
            Decode()
        elif n == 3:
            break
        else:
            print("INVALID CHOICE")
