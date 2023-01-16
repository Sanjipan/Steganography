import os


def Text_steganography(file, n):
    def EncodeTheText(text):
        i = 0
        add = ''
        while i < len(text):
            t = ord(text[i])
            if 32 <= t <= 64:
                t1 = t + 48
                t2 = t1 ^ 170
                res = bin(t2)[2:].zfill(8)
                add = add + "0011" + res
            else:
                t1 = t - 48
                t2 = t1 ^ 170
                res = bin(t2)[2:].zfill(8)
                add = add + "0110" + res
            i = i + 1
        res1 = add + "111111111111"
        print("[INFO] The String after binary conversion:-{}".format(res1))
        print("[INFO] Length of binary after conversion:-{}".format(len(res1)))
        ZWC = {"00": u'\u200C', "01": u'\u202C', "11": u'\u202D', "10": u'\u200E'}
        file1 = open(file, 'r+')
        f = file.split("/")
        f[len(f)-1] = "/temp.txt"
        aa = file.split("/")
        a = ''
        for i in range(1, len(aa) - 1):
            a = a + "/" + aa[i]
        a = a + "/" + "temp.txt"
        file3 = open(a, 'w+', encoding='utf-8')
        word = []
        for line in file1:
            word = word + line.split()
        ii = 0
        while ii < len(res1):
            s = word[int(ii/12)]
            j = 0
            w = ""
            while j < 12:
                x = res1[j+ii] + res1[ii+j+1]
                w = w + ZWC[x]
                j = j + 2
            s1 = s + w
            file3.write(s1)
            file3.write(" ")
            ii = ii + 12
        t = int(len(res1)/12)
        while t < len(word):
            file3.write(word[t])
            file3.write(" ")
            t = t + 1
        file3.close()
        file1.close()
        os.remove(file)
        os.rename(a, file)
        print("[INFO] ENCODING DATA Successful")
        print("[INFO] LOCATION:{}".format(file))
        print("=" * 100)

    def Encode():
        print("[INFO] Text Steganography ENCODING")
        print("")
        count2 = 0
        file1 = open(file, 'r')
        for line in file1:
            for word in line.split():
                count2 = count2 + 1
        file1.close()
        bt = int(count2)
        print("Maximum number of words that can be inserted:- {}".format(int(bt/6)))
        text1 = input("[*] Enter the secret message:-")
        if len(text1) > bt:
            print("[!] String is too big please reduce string size")
            Encode()
        else:
            EncodeTheText(text1)

    def BinaryToDecimal(binary):
        string = int(binary, 2)
        return string

    def Decode():
        print("[INFO] Text Steganography DECODING")
        ZWC_reverse = {u"\u200C": "00", u'\u202C': "01", u'\u202D': "11", u'\u200E': "10"}
        file4 = open(file, 'r', encoding="utf-8")
        temp = ''
        for line in file4:
            for word in line.split():
                T1 = word
                binary_extract = ""
                for letters in T1:
                    if letters in ZWC_reverse:
                        binary_extract = binary_extract + ZWC_reverse[letters]
                    if letters == "111111111111":
                        break
                    else:
                        if len(binary_extract) == 12:
                            temp = temp + binary_extract
        print("[INFO] Encrypted message present in code bits: {}".format(temp))
        print("[INFO] Length of encoded bits:- {}".format(len(temp)))
        i = 0
        a = 0
        b = 4
        c = 4
        d = 12
        final = ''
        while i < len(temp):
            t3 = temp[a:b]
            a = a + 12
            b = b + 12
            i = i + 12
            t4 = temp[c:d]
            c = c + 12
            d = d + 12
            if t3 == "0110":
                for i in range(0, len(t4), 8):
                    temp_data = t4[i:i + 8]
                    decimal_data = BinaryToDecimal(temp_data)
                    final = final + chr((decimal_data ^ 170) + 48)
            elif t3 == "0011":
                for i in range(0, len(t4), 8):
                    temp_data = t4[i:i + 8]
                    decimal_data = BinaryToDecimal(temp_data)
                    final = final + chr((decimal_data ^ 170) - 48)
        print("[*] The Encoded data was:- {}".format(final))
        print("=" * 100)

    if n == 0:
        Encode()
    else:
        Decode()
