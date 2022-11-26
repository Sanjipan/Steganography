import sys
import argparse

from libs import audio_steganography
# from libs import image_steganography
# from libs import text_steganography
# from libs import vedio_steganography

use_text_encode = "python3 ./Steganography.py -t -e <location of file>"
use_text_decode = "python3 ./Steganography.py -t -d <location of file>"

use_audio_encode = "python3 ./Steganography.py -a -e <location of file>"
use_audio_decode = "python3 ./Steganography.py -a -d <location of file>"

use_vedio_encode = "python3 ./Steganography.py -v -e <location of file>"
use_vedio_decode = "python3 ./Steganography.py -v -d <location of file>"

use_image_encode = "python3 ./Steganography.py -i -e <location of file>"
use_image_decode = "python3 ./Steganography.py -i -d <location of file>"

use_help = "python3 ./Steganography.py -h -----> help"


def main():
    # file = input("ENTER FILE NAME")
    # while True:
    #     print("MAIN MENU")
    #     print("1. IMAGE STEGANOGRAPHY {Hiding Text in Image cover file}")
    #     print("2. TEXT STEGANOGRAPHY {Hiding Text in Text cover file}")
    #     print("3. AUDIO STEGANOGRAPHY {Hiding Text in Audio cover file}")
    #     print("4. VIDEO STEGANOGRAPHY {Hiding Text in Video cover file}")
    #     print("5. Exit")
    #     n = int(input("Enter Your Choice:"))
    #     if n == 1:
    #         image_steganography.image_Stegonography(file)
    #     elif n == 2:
    #         text_steganography.text_steganography()
    #     elif n == 3:
    #         audio_steganography.audio_steganography()
    #     elif n == 4:
    #         vedio_steganography.vedio_steganography(file)
    #     elif n == 5:
    #         break
    #     else:
    #         print("Invalid Input")
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--audio', action='store_true', help="For audio file")
    parser.add_argument('-t', '--text', action='store_true', help="For text file")
    parser.add_argument('-v', '--vedio', action='store_true', help="For vedio file")
    parser.add_argument('-i', '--image', action='store_true', help="For image file")
    parser.add_argument('-e', '--encode', action='store_true', help="For encoding")
    parser.add_argument('-d', '--decode', action='store_true', help="For decoding")
    parser.add_argument('filename')
    args = parser.parse_args()
    c = 0
    t = True
    if args.filename:
        if args.audio and args.encode and t:
            audio_steganography.audio_steganography(args.filename, 0)
            t = False
        elif args.audio and args.decode and t:
            audio_steganography.audio_steganography(args.filename, 1)
            t = False
        elif args.text and args.encode and t:
            print("Encode text")
            t = False
        elif args.text and args.decode and t:
            print("Decode text")
            t = False
        elif args.vedio and args.encode and t:
            print("Encode vedio")
            t = False
        elif args.vedio and args.decode and t:
            print("Decode vedio")
            t = False
        elif args.image and args.encode and t:
            print("Encode image")
            t = False
        elif args.image and args.decode and t:
            print("Decode image")
            t = False
        else:
            c = 1
    else:
        parser.print_help()
        sys.exit(0)
    if c == 1:
        parser.print_help()
        sys.exit()


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

# python3 ./<filename.py> /t /e <location of file>#########################
# python3 ./<filename.py> /t /d <location of file>
#
# python3 ./<filename.py> /a /e <location of file>
# python3 ./<filename.py> /a /d <location of file>
#
# python3 ./<filename.py> /v /e <location of file>
# python3 ./<filename.py> /v /d <location of file>
#
# python3 ./<filename.py> /i /e <location of file>
# python3 ./<filename.py> /i /d <location of file>
#
# python3 ./<filename.py> /h -----> help
