import os
import cv2
import numpy as np
from PIL import Image


def Image_steganography(file, n):
    # it converts data in binary format

    def data2binary(data):
        p = ''
        if type(data) == str:
            p = p.join([format(ord(i), '08b') for i in data])
        elif type(data) == bytes or type(data) == np.ndarray:
            p = [format(i, '08b') for i in data]
        return p

    # hide data in given img

    def hide_data(img, data):
        data += "$$"  # '$$'--> secrete key
        d_index = 0
        b_data = data2binary(data)
        len_data = len(b_data)

        # iterate pixels from image and update pixel values

        for value in img:
            for pix in value:
                r, g, b = data2binary(pix)
                if d_index < len_data:
                    pix[0] = int(r[:-1] + b_data[d_index])
                    d_index += 1
                if d_index < len_data:
                    pix[1] = int(g[:-1] + b_data[d_index])
                    d_index += 1
                if d_index < len_data:
                    pix[2] = int(b[:-1] + b_data[d_index])
                    d_index += 1
                if d_index >= len_data:
                    break
        return img

    def Encode():

        print("[INFO] Image Steganography ENCODING")
        print("")
        image = cv2.imread(file)
        img = Image.open(file, 'r')
        w, h = img.size
        data = input("[*] Enter the secret message:- ")
        if len(data) == 0:
            raise ValueError("[INFO] Empty data")
        enc_img = 'temp.png'
        enc_data = hide_data(image, data)
        cv2.imwrite(enc_img, enc_data)
        img1 = Image.open(enc_img, 'r')
        img1 = img1.resize((w, h), Image.Resampling.LANCZOS)
        # optimize with 65% quality
        if w != h:
            img1.save(enc_img, optimize=True, quality=65)
        else:
            img1.save(enc_img)
        img.close()
        img1.close()
        os.remove(file)
        os.rename(enc_img, file)
        print("[INFO] ENCODING DATA Successful")
        print("[INFO] LOCATION:{}".format(file))
        print("=" * 100)

    # decoding

    def find_data(img):
        bin_data = ""
        for value in img:
            for pix in value:
                r, g, b = data2binary(pix)
                bin_data += r[-1]
                bin_data += g[-1]
                bin_data += b[-1]

        all_bytes = [bin_data[i: i + 8] for i in range(0, len(bin_data), 8)]

        readable_data = ""
        for i in all_bytes:
            readable_data += chr(int(i, 2))
            if readable_data[-2:] == "$$":
                break
        return readable_data[:-2]

    def Decode():

        print("[INFO] Image Steganography DECODING")
        print("")
        image = cv2.imread(file)
        img = Image.open(file, 'r')
        msg = find_data(image)
        img.close()
        print("[*] The Encoded data was: {}".format(msg))
        print("=" * 100)

    if n == 0:
        Encode()
    else:
        Decode()
