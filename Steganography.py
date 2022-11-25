import sys

# from libs import audio_steganography
# from libs import image_steganography
# from libs import text_steganography
# from libs import vedio_steganography

use_text_encode = "python3 ./Steganography.py /t /e <location of file>"
use_text_decode = "python3 ./Steganography.py /t /d <location of file>"

use_audio_encode = "python3 ./Steganography.py /a /e <location of file>"
use_audio_decode = "python3 ./Steganography.py /a /d <location of file>"

use_vedio_encode = "python3 ./Steganography.py /v /e <location of file>"
use_vedio_decode = "python3 ./Steganography.py /v /d <location of file>"

use_image_encode = "python3 ./Steganography.py /i /e <location of file>"
use_image_decode = "python3 ./Steganography.py /i /d <location of file>"

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
    if sys.argv[0] == "./Steganography.py":
        if len(sys.argv) == 2:
            if sys.argv[1] == '/h':
                print("FORMAT : \npython3 ./Steganography.py /<File_Type> /<e(encode)/d(decode)> <location of file>")
                print("File_Types: /t [text], /i [image] , /a [audio], /v [vedio]")
                print("/e [Encode], /d [Decode]")
                print("")
                print("For Help:")
                print("FORMAT : python3 ./Steganography.py /h")
            else:
                print("For Help:")
                print("FORMAT : python3 ./Steganography.py /h")
        elif len(sys.argv) == 4:
            if sys.argv[1] == '/t':
                if sys.argv[2] == '/e':
                    pass
                elif sys.argv[2] == '/d':
                    pass
                else:
                    print("Wrong Parameter:{}".format(sys.argv[2]))
                    print("Formats:")
                    print(use_text_encode)
                    print(use_text_decode)
                    print("/e [Encode], /d [Decode]")
                    print("/h [For Help]")

            elif sys.argv[1] == '/a':
                if sys.argv[2] == '/e':
                    pass
                elif sys.argv[2] == '/d':
                    pass
                else:
                    print("Wrong Parameter:{}".format(sys.argv[2]))
                    print("Formats:")
                    print(use_audio_encode)
                    print(use_audio_decode)
                    print("/e [Encode], /d [Decode]")
                    print("/h [For Help]")

            elif sys.argv[1] == '/v':
                if sys.argv[2] == '/e':
                    pass
                elif sys.argv[2] == '/d':
                    pass
                else:
                    print("Wrong Parameter:{}".format(sys.argv[2]))
                    print("Formats:")
                    print(use_vedio_encode)
                    print(use_vedio_decode)
                    print("/e [Encode], /d [Decode]")
                    print("/h [For Help]")

            elif sys.argv[1] == '/i':
                if sys.argv[2] == '/e':
                    pass
                elif sys.argv[2] == '/d':
                    pass
                else:
                    print("Wrong Parameter:{}".format(sys.argv[2]))
                    print("Formats:")
                    print(use_image_encode)
                    print(use_image_decode)
                    print("/e [Encode], /d [Decode]")
                    print("/h [For Help]")
            else:
                print("Wrong Parameter:{}".format(sys.argv[1]))
                print("FOR: text file")
                print(use_text_encode)
                print(use_text_decode)
                print("FOR: audio file")
                print(use_audio_encode)
                print(use_audio_decode)
                print("FOR: vedio file")
                print(use_vedio_encode)
                print(use_vedio_decode)
                print("FOR: image file")
                print(use_image_encode)
                print(use_image_decode)

        else:
            print("Wrong Input of parameters")
            print("For Help:")
            print("FORMAT : python3 ./Steganography.py /h")
    else:
        print("FORMAT : \npython3 ./Steganography.py /<File_Type> /<e(encode)/d(decode)> <location of file>")
        print("File_Types: /t [text], /i [image] , /a [audio], /v [vedio]")
        print("/e [Encode], /d [Decode]")
        print("")
        print("For Help:")
        print("FORMAT : python3 ./Steganography.py /h")


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
