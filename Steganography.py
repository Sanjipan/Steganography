import sys
import argparse

from libs import audio_steganography
from libs import image_steganography
from libs import text_steganography
from libs import video_steganography

use_text_encode = "python3 ./Steganography.py -t -e <location of file>"
use_text_decode = "python3 ./Steganography.py -t -d <location of file>"

use_audio_encode = "python3 ./Steganography.py -a -e <location of file>"
use_audio_decode = "python3 ./Steganography.py -a -d <location of file>"

use_vedio_encode = "python3 ./Steganography.py -v -e <location of file>"
use_vedio_decode = "python3 ./Steganography.py -v -d <location of file>"

use_image_encode = "python3 ./Steganography.py -i -e <location of file>"
use_image_decode = "python3 ./Steganography.py -i -d <location of file>"

use_help = "python3 ./Steganography.py -h -----> help"


def symbols():
    print("=" * 100)
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣴⣿⣿⣾⣿⣿⣷⣄⣀⣯⣯⣳⣄⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠑⠲⢦⣤⣈⡛⠿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠛⣿⣿⣧⠀⠀")
    print("⠀⠀⠀⠀⠀⠐⠢⣤⣄⣈⠙⠿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣷⣶⣿⣿⣿⡆⠀_⠀                             _")
    print("⠀⠀⠀⠀⠐⠠⢤⣄⣉⣛⠿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿(⠀)        _                   (_ )")
    print("⠀⠀⠀⠀⠲⢤⣤⣈⡙⠻⢿⣿⣿⠿⠿⠛⠛⠉⠉⠀⠀⠀⠀⠉___|⠀|__    /'_`\   ___ ___    __  | |   __    _    ___")
    print("⠀⠀⠀⠢⢤⣀⣈⠙⠿⣿⣷⠋⠀⠀⣀⣀⣀⣀⠀⠀⠀⠀/'___|⠀⠀_ `\/'/'_` )/' _ ` _ `\/'__`\| | /'__`\/'_`\/' _ `\ ")
    print("⠀⠀⠀⢤⣀⡉⠛⠿⣷⣶⠃⢠⣶⣿⣿⠿⠿⣿⣿⣷⣄(⠀(___|⠀| | ( ( (_| || ( ) ( ) (  ___/| |(  ___( (_) | ( ) |")
    print("⠀⠀⠀⢀⣈⠙⠻⢶⣾⡅⠀⣾⣿⠋⠀⠀⢤⣄⠉⢿⣿`\____(_) (_)\ `\__,_(_) (_) (_`\____(___`\____`\___/(_) (_)")
    print("⠀⠀⠀⠈⠙⠻⣿⣶⣾⡅⠀⣿⣿⡀⠀⠀⠀⣻⡇⢸⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀     `\_____)")
    print("⠀⠀⠀⠀⠻⣷⣶⣯⣿⣷⡀⠘⢿⣿⣶⣶⣾⣿⠇⣸⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣦⣀⠉⠙⠛⠉⢁⣴⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠈⠛⠿⣿⣿⣿⣿⣷⣶⣿⣿⣿⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("=" * 100)
    print("Ch@meleon STARTED")
    print("=" * 100)


def main():
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
        symbols()
        if args.audio and args.encode and t:
            audio_steganography.Audio_steganography(args.filename, 0)
            t = False
        elif args.audio and args.decode and t:
            audio_steganography.Audio_steganography(args.filename, 1)
            t = False
        elif args.text and args.encode and t:
            text_steganography.Text_steganography(args.filename, 0)
            t = False
        elif args.text and args.decode and t:
            text_steganography.Text_steganography(args.filename, 1)
            t = False
        elif args.vedio and args.encode and t:
            video_steganography.Video_Steganography(args.filename, 0)
            t = False
        elif args.vedio and args.decode and t:
            video_steganography.Video_Steganography(args.filename, 1)
            t = False
        elif args.image and args.encode and t:
            image_steganography.Image_steganography(args.filename, 0)
            t = False
        elif args.image and args.decode and t:
            image_steganography.Image_steganography(args.filename, 1)
            t = False
        else:
            c = 1
    else:
        symbols()
        parser.print_help()
        sys.exit(0)
    if c == 1:
        symbols()
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
