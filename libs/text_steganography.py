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
        def txt_encode(text):
            pass

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
