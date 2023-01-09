
# STEGANOGRAPHY TOOL

***A Advance Steganography Tool made with Python*** 
######
*The Program Supports **Hiding Secret Text data** into an innocent looking cover file **like : .mp4, .wav, .png, .jpeg, .txt** through the use of **Steganography Theory***

### *Supported OS:*
    LINUX
This program is made and designed for **Linux Opearing System** ***only***.

## How To Use?

**To *Use the Code*** :
```bash
$ git clone https://github.com/Sanjipan/Steganography
$ cd Steganography
$ Sudo python3 ./Steganography.py <File Type> <Encode/Decode> <File Location>
```

**-> For *Audio Cover* File** :
```bash
# Encoding
    $ Sudo python3 ./Steganography.py -a -e <location of file>
    $ Sudo python3 ./Steganography.py --audio --encode <location of file>
# Decoding
    $ Sudo python3 ./Steganography.py -a -d <location of file>
    $ Sudo python3 ./Steganography.py --audio --decode <location of file>
```

**-> For *Video Cover* File** :
```bash
# Encoding
    $ Sudo python3 ./Steganography.py -v -e <location of file>
    $ Sudo python3 ./Steganography.py --video --encode <location of file>
# Decoding
    $ Sudo python3 ./Steganography.py -v -d <location of file>
    $ Sudo python3 ./Steganography.py --video --decode <location of file>
```

**-> For *Image Cover* File** :
```bash
# Encoding
    $ Sudo python3 ./Steganography.py -i -e <location of file>
    $ Sudo python3 ./Steganography.py --image --encode <location of file>
# Decoding
    $ Sudo python3 ./Steganography.py -i -d <location of file>
    $ Sudo python3 ./Steganography.py --image --decode <location of file>
```

**-> For *Text Cover* File** :
```bash
# Encoding
    $ Sudo python3 ./Steganography.py -t -e <location of file>
    $ Sudo python3 ./Steganography.py --text --encode <location of file>
# Decoding
    $ Sudo python3 ./Steganography.py -t -d <location of file>
    $ Sudo python3 ./Steganography.py --text --decode <location of file>
```
**For HELP** :
```bash
    $ Sudo python3 ./Steganography.py -h
    $ Sudo python3 ./Steganography.py -help
```
