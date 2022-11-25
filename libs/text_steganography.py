import numpy as np
import pandas as pd
import os
import cv2
from matplotlib import pyplot as plt


# TEXT STEGANOGRAPHY OPERATIONS
# 1. Encode the Text message
# 2. Decode the Text message
# 3. Exit

def text_steganography():
    def Encode():
        def txt_Encoder(text):
            l = len(text)
            i = 0
            add = ''
            while i < l:
                t = ord(text[i])
                if 32 <= t <= 64:
                    t1 = t + 48
                    t2 = t1 ^ 170
                    res = bin(t2)[2:].zfill(8)
                    add += "0011" + res
                else:
                    t1 = t - 48
                    t2 = t1 ^ 170
                    res = bin(t2)[2:].zfill(8)
                    add += "0110" + res

                i += 1

            res1 = add + "111111111111"
            print("The string after binary conversion applying all the transformation: " + (res1))
            length = len(res1)
            print("Length of binary after conversion: ", length)
            HM_SK = ""
            ZWC = {"00": u'\u200C', "01": u'\u202C', "11": u'\u202D', "10": u'\u200E'}
            file_1 = open("cover_text.txt", "r+")
            name_of_file = input("\nEnter the name of thr stego file after encoding(with extention): ")
            file3 = open(name_of_file, "w+", encoding="utf-8")
            word_list = []
            for Line in file_1:
                word_list += Line.split()
            i = 0
            while i < len(res1):
                s = word_list[int(i / 12)]
                j = 0
                x = ""
                HM_SK = ""
                while j < 12:
                    x = res1[j + 1] + res1[i + j + 1]
                    HM_SK += ZWC[x]
                    j += 2
                s1 = s + HM_SK
                file3.write(s1)
                file3.write(" ")
                i += 12
            t = int(len(res1) / 12)
            while t < len(word_list):
                file3.write(word_list[t])
                file3.write(" ")
                t += 1
            file3.close()
            file_1.close()
            print("Stego file has successfully generated")
        count2 = 0
        file1 = open("cover_text.txt", "r")
        for line in file1:
            for word in line.split():
                count2 = count2 + 1

        file1.close()
        bt = int(count2)
        print("Maximum number of words that can be inserted: ", int(bt / 6))
        text1 = input("Enter data to be encoded: ")
        l = len(text1)

        if l <= bt:
            print(" The text  can be hidden in the cover file")
            txt_Encoder(text1)
        else:
            print("String is too big please reduce string size")
            Encode()

    def BinaryToDecimal(binary):
        pass

    def Decode():
        pass

    while True:
        print("TEXT STEGANOGRAPHY OPERATIONS\n")
        print("1. Encode the Text message")
        print("2. Decode the Text message")
        print("3. Exit")
        n = int(input("Enter Your Choice: "))
        if n == 1:
            Encode()
        elif n == 2:
            Decode()
        elif n == 3:
            break
        else:
            print("INVALID CHOICE")
