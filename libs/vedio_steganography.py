# Importing requiered modules
import math
import os
import shutil
from subprocess import call, STDOUT
import cv2
from stegano import lsb


def Video_Steganography(file):
    def split_string(split_str, count=10):
        per_c = math.ceil(len(split_str) / count)
        c_cout = 0
        out_str = ''
        split_list = []
        for s in split_str:
            out_str += s
            c_cout += 1
            if c_cout == per_c:
                split_list.append(out_str)
                out_str = ''
                c_cout = 0
        if c_cout != 0:
            split_list.append(out_str)
        return split_list

    def frame_extraction(video):
        if not os.path.exists("./temp"):
            os.makedirs("temp")
        temp_folder = "./temp"
        print("[INFO] temp directory is created")
        vidcap = cv2.VideoCapture(video)
        count = 0
        while True:
            success, image = vidcap.read()
            if not success:
                break
            cv2.imwrite(os.path.join(temp_folder, "{:d}.png".format(count)), image)
            count += 1

    def encode_string(input_string, root="./temp/"):
        split_string_list = split_string(input_string)
        for i in range(0, len(split_string_list)):
            f_name = "{}{}.png".format(root, i)
            secret_enc = lsb.hide(f_name, split_string_list[i])
            secret_enc.save(f_name)
            print("[INFO] frame {} holds {}".format(f_name, lsb.reveal(f_name)))
        print("The message is stored in the Embedded_Video.mp4 file")

    def Decode(video):
        frame_extraction(video)
        secret = []
        root = "./temp/"
        a = ''
        try:
            for i in range(0, len(os.listdir(root)) - 1):
                f_name = "{}{}.png".format(str(root), str(i))
                secret_dec = lsb.reveal(f_name)
                if secret_dec == None:
                    break
                secret.append(secret_dec)
        except IndexError as e:
            print("[Done]")
        a = a.join([i for i in secret])
        print(a)
        clean_temp()

    def clean_temp(path="./temp"):
        if os.path.exists(path):
            shutil.rmtree(path)
            print("[INFO] temp files are cleaned up")

    def Encode(f_name):
        input_string = input("Enter the message :")
        frame_extraction(f_name)
        call(["ffmpeg", "-i", f_name, "-q:a", "0", "-map", "a", "temp/audio.mp3", "-y"], stdout=open(os.devnull, "w"),
             stderr=STDOUT)
        encode_string(input_string)
        call(["ffmpeg", "-i", "temp/%d.png", "-vcodec", "png", "temp/Embedded_Video.mp4", "-y"],
             stdout=open(os.devnull, "w"), stderr=STDOUT)
        call(["ffmpeg", "-i", "temp/Embedded_Video.mp4", "-i", "temp/audio.mp3", "-codec", "copy", "Embedded_Video.mp4",
              "-y"], stdout=open(os.devnull, "w"), stderr=STDOUT)
        clean_temp()

    while True:
        print("1.Hide a message in video\n2.Reveal the secret from the video\n")
        print("Any other value to exit\n")
        choice = input("Enter your choice :")
        if choice == '1':
            f_name = input("Enter the name of video file with extension:")
            Encode(f_name)
        elif choice == '2':
            Decode(input("Enter the name of video with extension :"))
        else:
            break
