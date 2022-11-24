from libs import audio_steganography
from libs import image_steganography
from libs import text_steganography
from libs import vedio_steganography


def main():
    file = input("ENTER FILE NAME")
    while True:
        print("MAIN MENU")
        print("1. IMAGE STEGANOGRAPHY {Hiding Text in Image cover file}")
        print("2. TEXT STEGANOGRAPHY {Hiding Text in Text cover file}")
        print("3. AUDIO STEGANOGRAPHY {Hiding Text in Audio cover file}")
        print("4. VIDEO STEGANOGRAPHY {Hiding Text in Video cover file}")
        print("5. Exit")
        n = int(input("Enter Your Choice:"))
        if n == 1:
            image_steganography.image_Stegonography(file)
        elif n == 2:
            text_steganography.text_steganography(file)
        elif n == 3:
            audio_steganography.audio_steganography(file)
        elif n == 4:
            vedio_steganography.vedio_steganography(file)
        elif n == 5:
            break
        else:
            print("Invalid Input")


if __name__ == "__main__":
    main()

# MAIN MENU
#
# 1. IMAGE STEGANOGRAPHY {Hiding Text in Image cover file}
# 2. TEXT STEGANOGRAPHY {Hiding Text in Text cover file}
# 3. AUDIO STEGANOGRAPHY {Hiding Text in Audio cover file}
# 4. VIDEO STEGANOGRAPHY {Hiding Text in Video cover file}
# 5. Exit


# SYS
# python Steganography.py -<e-->encode> <file location>
# python Steganography.py -<d-->decode> <file location>


