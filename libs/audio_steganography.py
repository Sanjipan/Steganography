# AUDIO STEGANOGRAPHY OPERATIONS
# 1. Encode the Text message
# 2. Decode the Text message
# 3. Exit

import wave


def audio_steganography(file):
    def Encode():
        song = wave.open(file, mode='rb')
        nframes = song.getnframes()
        frames = song.readframes(nframes)
        frame_list = list(frames)
        frame_byte = bytearray(frame_list)

        data = input("Enter the secret message:-")

        res = ''.join(format(i, '08b') for i in bytearray(data, encoding='utf-8'))
        print("The String after binary conversion:-{}".format(res))
        length = len(res)
        print("Length of binary after conversion:-{}".format(length))

        data = data + '*^*^*'

        results = []
        for j in data:
            bits = bin(ord(j))[2:].zfill(8)
            results.extend([int(b) for b in bits])

        k = 0
        for i in range(0, len(results), 1):
            res = bin(frame_byte[k])[2:].zfill(8)
            if res[len(res) - 4] == results[i]:
                frame_byte[k] = (frame_byte[k] & 253)
            else:
                frame_byte[k] = (frame_byte[k] & 253) | 2
                frame_byte[k] = (frame_byte[k] & 254) | results[i]
            k = k + 1
        frame_modified = bytes(frame_byte)

        stegofile = input("ENTER STIGO FILE NAME(With Extension):")
        with wave.open(stegofile, 'wb') as fd:
            fd.setparams(song.getparams())
            fd.writeframes(frame_modified)
        print("ENCODING DATA Sucessfull")
        print("LOCATION:{}".format(stegofile))
        song.close()

    def Decode():
        song = wave.open(file, mode='rb')
        nframes = song.getnframes()
        frames = song.readframes(nframes)
        frame_list = list(frames)
        frame_bytes = bytearray(frame_list)

        extracted = ""
        p = 0
        for i in range(len(frame_bytes)):
            if p == 1:
                break
            res = bin(frame_bytes[i])[2:].zfill(8)
            if res[len(res) - 2] == 0:
                extracted += res[len(res) - 4]
            else:
                extracted += res[len(res) - 1]

            all_bytes = [extracted[i: i + 8] for i in range(0, len(extracted), 8)]
            decode_data = ""
            for byte in all_bytes:
                decode_data += chr(int(byte, 2))
                if decode_data[-5:] == '*^*^*':
                    print("The Encoded data was:", decode_data[:-5])
                    p = 1
                    break

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
