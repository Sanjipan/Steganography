# STEGANOGRAPHY TOOL
## **Project** : ***Ch@meleon***

***A Advance Steganography Tool made with Python*** 
######
*The Program Supports **Hiding Secret Text data** into an innocent looking cover file **like : .mp4, .wav, .png, .jpeg, .txt** through the use of **Steganography Theory***

### *Supported OS:*
    LINUX
This program is made and designed for **Linux Opearing System** ***only***.

## How To Use?

**To *Use the Code*** :
```console
kali@kali:~$ git clone https://github.com/Sanjipan/Steganography
kali@kali:~$ cd Steganography
kali@kali:~$ Sudo python3 ./Steganography.py <File Type> <Encode/Decode> <File Location>
```

**-> For *Audio Cover* File** :
```console
# Encoding
    kali@kali:~$ Sudo python3 ./Steganography.py -a -e <location of file>
    kali@kali:~$ Sudo python3 ./Steganography.py --audio --encode <location of file>
# Decoding
    kali@kali:~$ Sudo python3 ./Steganography.py -a -d <location of file>
    kali@kali:~$ Sudo python3 ./Steganography.py --audio --decode <location of file>
```

**-> For *Video Cover* File** :
```console
# Encoding
    kali@kali:~$ Sudo python3 ./Steganography.py -v -e <location of file>
    kali@kali:~$ Sudo python3 ./Steganography.py --video --encode <location of file>
# Decoding
    kali@kali:~$ Sudo python3 ./Steganography.py -v -d <location of file>
    kali@kali:~$ Sudo python3 ./Steganography.py --video --decode <location of file>
```

**-> For *Image Cover* File** :
```console
# Encoding
    kali@kali:~$ Sudo python3 ./Steganography.py -i -e <location of file>
    kali@kali:~$ Sudo python3 ./Steganography.py --image --encode <location of file>
# Decoding
    kali@kali:~$ Sudo python3 ./Steganography.py -i -d <location of file>
    kali@kali:~$ Sudo python3 ./Steganography.py --image --decode <location of file>
```

**-> For *Text Cover* File** :
```console
# Encoding
    kali@kali:~$ Sudo python3 ./Steganography.py -t -e <location of file>
    kali@kali:~$ Sudo python3 ./Steganography.py --text --encode <location of file>
# Decoding
    kali@kali:~$ Sudo python3 ./Steganography.py -t -d <location of file>
    kali@kali:~$ Sudo python3 ./Steganography.py --text --decode <location of file>
```
**For HELP** :
```console
kali@kali:~$ Sudo python3 ./Steganography.py -h
kali@kali:~$ Sudo python3 ./Steganography.py -help
```
## Demo
```console
┌──(kali㉿kali)-[~/Desktop]
└─$ cd Steganography
                                                                                                        
┌──(kali㉿kali)-[~/Desktop/Steganography]
└─$ ls      
libs  Steganography.py
                                                                                                        
┌──(kali㉿kali)-[~/Desktop/Steganography]
└─$ sudo python3 ./Steganography.py -v -e /home/kali/Desktop/Test/test.mp4
[sudo] password for kali: 
====================================================================================================
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣴⣿⣿⣾⣿⣿⣷⣄⣀⣯⣯⣳⣄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠑⠲⢦⣤⣈⡛⠿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠛⣿⣿⣧⠀⠀
⠀⠀⠀⠀⠀⠐⠢⣤⣄⣈⠙⠿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣷⣶⣿⣿⣿⡆⠀_⠀                             _
⠀⠀⠀⠀⠐⠠⢤⣄⣉⣛⠿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿(⠀)        _                   (_ )
⠀⠀⠀⠀⠲⢤⣤⣈⡙⠻⢿⣿⣿⠿⠿⠛⠛⠉⠉⠀⠀⠀⠀⠉___|⠀|__    /'_`\   ___ ___    __  | |   __    _    ___
⠀⠀⠀⠢⢤⣀⣈⠙⠿⣿⣷⠋⠀⠀⣀⣀⣀⣀⠀⠀⠀⠀/'___|⠀⠀_ `\/'/'_` )/' _ ` _ `\/'__`\| | /'__`\/'_`\/' _ `\ 
⠀⠀⠀⢤⣀⡉⠛⠿⣷⣶⠃⢠⣶⣿⣿⠿⠿⣿⣿⣷⣄(⠀(___|⠀| | ( ( (_| || ( ) ( ) (  ___/| |(  ___( (_) | ( ) |
⠀⠀⠀⢀⣈⠙⠻⢶⣾⡅⠀⣾⣿⠋⠀⠀⢤⣄⠉⢿⣿`\____(_) (_)\ `\__,_(_) (_) (_`\____(___`\____`\___/(_) (_)
⠀⠀⠀⠈⠙⠻⣿⣶⣾⡅⠀⣿⣿⡀⠀⠀⠀⣻⡇⢸⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀     `\_____)
⠀⠀⠀⠀⠻⣷⣶⣯⣿⣷⡀⠘⢿⣿⣶⣶⣾⣿⠇⣸⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣦⣀⠉⠙⠛⠉⢁⣴⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠛⠿⣿⣿⣿⣿⣷⣶⣿⣿⣿⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
====================================================================================================
Ch@meleon STARTED
====================================================================================================
[INFO] Video Steganography ENCODING

[*] Enter the message :hii
[INFO] temp directory is created
[INFO] frame ./temp/0.png holds h
[INFO] frame ./temp/1.png holds i                                                                                                                                                                                                           
[INFO] frame ./temp/2.png holds i                                                                                                                                                                                                           
[INFO] The message is stored in the Embedded_Video.mp4 file                                                                                                                                                                                 
[INFO] temp files are cleaned up                                                                                                                                                                                                            
[INFO] FILE LOCATION:/home/kali/Desktop/Test/test.mp4                                                                                                                                                                                       
====================================================================================================                                                                                                                                        
                                                                                                                                                                                                                                            
┌──(kali㉿kali)-[~/Desktop/Steganography]
└─$ sudo python3 ./Steganography.py -v -d /home/kali/Desktop/Test/test.mp4
====================================================================================================
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣴⣿⣿⣾⣿⣿⣷⣄⣀⣯⣯⣳⣄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠑⠲⢦⣤⣈⡛⠿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠛⣿⣿⣧⠀⠀
⠀⠀⠀⠀⠀⠐⠢⣤⣄⣈⠙⠿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣷⣶⣿⣿⣿⡆⠀_⠀                             _
⠀⠀⠀⠀⠐⠠⢤⣄⣉⣛⠿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿(⠀)        _                   (_ )
⠀⠀⠀⠀⠲⢤⣤⣈⡙⠻⢿⣿⣿⠿⠿⠛⠛⠉⠉⠀⠀⠀⠀⠉___|⠀|__    /'_`\   ___ ___    __  | |   __    _    ___
⠀⠀⠀⠢⢤⣀⣈⠙⠿⣿⣷⠋⠀⠀⣀⣀⣀⣀⠀⠀⠀⠀/'___|⠀⠀_ `\/'/'_` )/' _ ` _ `\/'__`\| | /'__`\/'_`\/' _ `\ 
⠀⠀⠀⢤⣀⡉⠛⠿⣷⣶⠃⢠⣶⣿⣿⠿⠿⣿⣿⣷⣄(⠀(___|⠀| | ( ( (_| || ( ) ( ) (  ___/| |(  ___( (_) | ( ) |
⠀⠀⠀⢀⣈⠙⠻⢶⣾⡅⠀⣾⣿⠋⠀⠀⢤⣄⠉⢿⣿`\____(_) (_)\ `\__,_(_) (_) (_`\____(___`\____`\___/(_) (_)
⠀⠀⠀⠈⠙⠻⣿⣶⣾⡅⠀⣿⣿⡀⠀⠀⠀⣻⡇⢸⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀     `\_____)
⠀⠀⠀⠀⠻⣷⣶⣯⣿⣷⡀⠘⢿⣿⣶⣶⣾⣿⠇⣸⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣦⣀⠉⠙⠛⠉⢁⣴⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠛⠿⣿⣿⣿⣿⣷⣶⣿⣿⣿⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
====================================================================================================
Ch@meleon STARTED
====================================================================================================
[INFO] Video Steganography DECODING

[INFO] temp directory is created

[*] The Encoded data was:hii

[INFO] temp files are cleaned up
====================================================================================================
```


## Authors :

- [@Sanjipan Deb](https://github.com/Sanjipan)
- [@Abanteeka Acharya](https://github.com/Abanteeka)
- [@Priyanshi Panchal](https://github.com/sketchmaxion108)


## **Disclaimer**
**"EDUCATIONAL PURPOSES ONLY"**
######
## Legal Disclaimer
The use of code contained in this repository, either in part or in its totality,
for engaging targets without prior mutual consent is illegal. **It is
the end user's responsibility to obey all applicable local, state and
federal laws.**

Developers assume **no liability** and are not
responsible for misuses or damages caused by any code contained
in this repository in any event that, accidentally or otherwise, it comes to
be utilized by a threat agent or unauthorized entity as a means to compromise
the security, privacy, confidentiality, integrity, and/or availability of
systems and their associated resources. In this context the term "compromise" is
henceforth understood as the leverage of exploitation of known or unknown vulnerabilities
present in said systems, including, but not limited to, the implementation of
security controls, human- or electronically-enabled.

The use of this code is **only** endorsed by the developers in those
circumstances directly related to **educational environments** or
**authorized penetration testing engagements** whose declared purpose is that
of finding and mitigating vulnerabilities in systems, limiting their exposure
to compromises and exploits employed by malicious agents as defined in their
respective threat models.
######
The application must be used for **"EDUCATIONAL PURPOSES ONLY"**


### *Contect Us On:*
###### **SANJIPAN DEB** :
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/sanjipan-deb-834601220/)
###### **ABANTEEKA ACHARYA** :
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/abanteeka-acharya-1867ab225/)
###### **PRIYANSHI PANCHAL** :
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/priyanshi-panchal-25069022a/)


