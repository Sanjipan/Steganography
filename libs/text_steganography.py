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
        string = int(binary, 2)
        return string

    def Decode():
        ZWC_reverse = {u'\u200C': "00", u'\u202C': "01", u'\u202D': "11", u'\u200E': "10"}
        stego = input("Please enter the stego file name(with extension) to decode the message: ")
        file_4 = open(stego, "r", encoding="utf=8")
        temp = ''
        for Line in file_4:
            for words in Line.split():
                T1 = words
                binary_extract = ""
                for letter in T1:
                    if letter in ZWC_reverse:
                        binary_extract += ZWC_reverse[letter]
                if binary_extract == "111111111111":
                    break
                else:
                    temp += binary_extract
        print("Encrypted message presented in code bits: ", temp)
        length = len(temp)
        print("length of encoded bits: ", length)
        i = 0
        a = 0
        b = 4
        c = 4
        d = 12
        final = ""
        while i < len(temp):
            t3 = temp[a:b]
            a += 12
            b += 12
            i += 12
            t4 = temp[c:d]
            c += 12
            d += 12
            if t3 == '0110':
                decimal_data = BinaryToDecimal(t4)
                final += str((decimal_data ^ 170) + 48)
            elif t3 == '0011':
                decimal_data = BinaryToDecimal(t4)
                final += str((decimal_data ^ 170) - 48)
        print("Message after decoding from the stego file: ", final)

    while True:
        print("TEXT STEGANOGRAPHY OPERATIONS")
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


text_steganography()
