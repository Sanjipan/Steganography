# VIDEO STEGANOGRAPHY OPERATIONS
# 1. Encode the Text message
# 2. Decode the Text message
# 3. Exit
import cv2
import numpy as np


def video_steganography():

    def PRGA(s, num):
        i = 0
        j = 0
        key = []
        while num > 0:
            num = num - 1
            i = (i + 1) % 256
            j = (j + s[i]) % 256
            s[i], s[j] = s[j], s[i]
            K = s[(s[i] + s[j]) % 256]
            key.append(K)
        return key

    def KSA(key):
        key_length = len(key)
        S = list(range(256))
        j = 0
        for i in range(256):
            j = (j + S[i] + key[i % key_length]) % 256
            S[i], S[j] = S[j], S[i]
        return S

    def preparing_key_array(s):
        return [ord(c) for c in s]

    def encryption(plaintext):
        key = input("Enter the Key:")
        key = preparing_key_array(key)

        S = KSA(key)

        keystream = np.arry(PRGA(S, len(plaintext)))
        plaintext = np.array([ord(i)] for i in plaintext)

        cipher = keystream ^ plaintext
        ctext = ''
        for c in cipher:
            ctext = ctext + chr(c)
        return ctext

    def msgtobinary(msg):
        if type(msg) == str:
            result = ''.join([format(ord(i), "08b") for i in msg])

        elif type(msg) == bytes or type(msg) == np.ndarray:
            result = [format(i, "08b") for i in msg]

        elif type(msg) == int or type(msg) == np.uint8:
            result = format(msg, "08b")

        else:
            raise TypeError("Input type is not supported in this function")

        return result

    def embed(frame):
        data = input("Enter the data to be Encoded in Video :")
        data = encryption(data)
        print("The Encrypted data is:", data)
        if len(data) == 0:
            raise ValueError("Data entered to be encoded is empty")
        data = data + '*^*^*'

        binary_data = msgtobinary(data)
        length_data = len(binary_data)

        index_data = 0

        for i in frame:
            for pixel in i:
                r, g, b = msgtobinary(pixel)
                if index_data < length_data:
                    pixel[0] = int(r[:-1] + binary_data[index_data], 2)
                    index_data = index_data + 1
                if index_data < length_data:
                    pixel[1] = int(g[:1] + binary_data[index_data], 2)
                    index_data = index_data + 1
                if index_data < length_data:
                    pixel[2] = int(b[:-1] + binary_data[index_data], 2)
                    index_data = index_data + 1
                if index_data >= length_data:
                    break
        return frame

    def Encode():
        cap = cv2.VideoCapture("video.mp4")
        vidcap = cv2.VideoCapture("video.mp4")
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        frame_width = int(vidcap.get(3))
        frame_height = int(vidcap.get(4))

        size = (frame_width, frame_height)
        out = cv2.VideoWriter('stego.mp4', fourcc, 25.0, size)
        max_frame = 0
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            max_frame = max_frame + 1
        cap.release()
        print("Total Number of Frame in Selected Video:", max_frame)

        num = int(input("Enter the frame number where you want to embed data:"))
        frame_number = 0
        while vidcap.isOpened():
            frame_number = frame_number + 1
            ret, frame = vidcap.read()
            if not ret:
                break
            if frame_number == num:
                change_frame_with = embed(frame)
                frame_ = change_frame_with
                frame = change_frame_with
            out.write(frame)
        print("Encoded the data successfully in the video file")
        return frame_

    def decryption(ciphertext):
        key = input("Enter the key:")
        key = preparing_key_array(key)

        S = KSA(key)

        keystream = np.array(PRGA(S, len(ciphertext)))
        ciphertext = np.array([ord(i) for i in ciphertext])

        decoded = keystream ^ ciphertext
        dtext = ''
        for c in decoded:
            dtext = dtext + chr(c)
        return dtext

    def extract(frame):
        data_binary = ""
        final_decode_msg = ""
        for i in frame:
            for pixel in i:
                r, g, b = msgtobinary(pixel)
                data_binary = data_binary + r[-1]
                data_binary = data_binary + g[-1]
                data_binary = data_binary + b[-1]
                total_bytes = [data_binary[i: i+8] for i in range(0, len(data_binary), 8)]
                decoded_data = ""
                for byte in total_bytes:
                    decoded_data = decoded_data + chr(int(byte, 2))
                    if decoded_data[-5:] == "*^*^*":
                        for j in range(0, len(decoded_data)-5, 1):
                            final_decode_msg = final_decode_msg + decoded_data[j]
                        final_decode_msg = decryption(final_decode_msg)
                        print("The encoded data which was hidden in the video was :--{}".format(final_decode_msg))
                        return

    def Decode(frame_):
        cap = cv2.VideoCapture('stego.mp4')
        max_frame = 0
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                max_frame = max_frame + 1
                break

        print("Total number of Frame in selected Video: ", max_frame)
        num = int(input("Enter the secret frame number from from where you want to extract data"))
        vidcap = cv2.VideoCapture('stego.mp4')
        frame_number = 0
        while vidcap.isOpened():
            frame_number += 1
            ret, frame = vidcap.read()
            if not ret:
                break
            if frame_number == num:
                extract(frame_)
                return

    while True:
        print("1.Encode")
        print("2.Decode")
        print("3.Exit")
        n = int(input("Enter Your choice:"))
        if n == 1:
            a = Encode()
        elif n == 2:
            Decode(a)
        elif n == 3:
            break
        else:
            print("invalid Choice")
