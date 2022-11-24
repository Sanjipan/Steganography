# IMAGE STEGANOGRAPHY OPERATIONS
# 1. Encode the Text message
# 2. Decode the Text message
# 3. Exit

def image_Stegonography():
    def Encode():
        pass

    def Decode():
        pass

    while True:
        print("1. Encode the Text message")
        print("2. Decode the Text message")
        print("3. Exit")
        n = int(input("Enter Your Choice:"))
        if n == 1:
            Encode()
        elif n == 2:
            Decode()
        elif n == 3:
            break
        else:
            print("Invalid")

