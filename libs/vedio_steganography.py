# VIDEO STEGANOGRAPHY OPERATIONS
# 1. Encode the Text message
# 2. Decode the Text message
# 3. Exit
import cv2


def vedio_steganography(file):

    def encryption(data):
        return data

    def msgtobinary(data):
        return data

    def embed(frame):
        data = input("Enter the data to be Encoded in Video :")
        data = encryption(data)
        print("The Encrypted data is:", data)
        if len(data) == 0:
            raise ValueError("Data entered to be encoded is empty")
        data = data + '*^*^*'

        binary_data = msgtobinary(data)
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

        n = int(input("Enter the frame number where you want to embed data:"))
        frame_number = 0
        while vidcap.isOpened():
            frame_number = frame_number + 1
            ret, frame = vidcap.read()
            if not ret:
                break
            if frame_number == n:
                change_frame_with = embed(frame)
                frame_ = change_frame_with
                frame = change_frame_with
            out.write(frame)
        print("Encoded the data successfully in the video file")
        return frame_



    def Decode():
        pass

    while True:
        print("1.Encode")
        print("2.Decode")
        print("3.Exit")
        n = int(input("Enter Your choice:"))
        if n == 1:
            Encode()
        elif n == 2:
            Decode()
        elif n == 3:
            break
        else:
            print("invalid Choice")