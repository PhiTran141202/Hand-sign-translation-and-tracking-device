# **hand-tracking and ASL translation prototype device**



\############################# **INTRODUCTION ##############################**



This is my project for my bachelor's thesis. The project's foundation is based on the mediapipe(https://mediapipe.dev/)

Hands recognition repo by Kazuhito Takahashi (https://github.com/Kazuhito00/hand-gesture-recognition-using-mediapipe) and translated into English by Nikita Kiselov (https://github.com/kinivi). For the handtracking part, it is based on the repo by Rizky Dermawan (Rishttps://github.com/rizkydermawan1992/handtracking)



My version of the repo is trained to read 24 letters of the ASL alphabet (minus J and K), integrated the hand tracking function performed by pan and tilt servos, and controlled by an Arduino nano, with added photosensor and LCD screen.



All of these are controlled by a Raspberry Pi 4, which is the main CPU that will be processing the captured images with a Picamera attached to the servos. This required more modifications so that the program can work properly in the Raspbian OS and in conjunction with the Picamera.



The Arduino is powered by a 9V battery, and the Pi is powered by a portable power bank (Output: 5V - 2A, Capacity: 5000mAh)



**Notes: Mediapipe doesn't work on Raspbian Bullseye -> download the bookworm version**



**HERE ARE THE RECOMMENDED STEPS TO MAKE SURE THE MAIN PROGRAM RUNS SMOOTHLY WHEN IMPORTED INTO THE RASPBERRY PI:**



\####################### **Image Processing part** ############################



**STEP 1: setting up the Pi**

* Raspbian OS: Raspberry Pi OS (64bit), Debian Bookworm with desktop
* Python 3.11.2
* Packages: update + upgrade



**STEP 2: using pip3, run these commands**

* sudo rm/usr/lib/python3.11/EXTERNALLY-MANAGED
* sudo pip3 install mediapipe
* sudo pip3 install cvzone (optional)
* sudo pip3 install opencv-python
* sudo apt install python3-dev libhdf5-dev
* sudo apt install libatlas-base-dev
* pip3 install tensorflow
* sudo pip3 install gtts
* sudo apt install mpg321
* sudo pip3 install pyfirmata2 (the normal pyfirmata will not work, trust me i tried)



**STEP 3: Run the prototype.py**



\*CONSULT THE ORIGINAL MEDIAPIPE REPO TO TRAIN YOUR OWN DATA\*





\####################### **Hand tracking part** ############################



**Python packages required for hand tracking:**

* opencv-python 4.5.5.64
* mediapipe 0.8.10
* pyfirmata2

**Arduino Configuration**

* Open IDE Arduino
* Select File -> Example -> Firmata -> StandardFirmata
* Select Tools -> Board -> Arduino/Genuino Uno
* Select Tools -> Port -> *choose your port COM*
* Upload the Arduino codes





\######################### **REFERENCES ###################################**



\*\[MediaPipe](https://mediapipe.dev/)



\# Author

Kazuhito Takahashi(https://twitter.com/KzhtTkhs)



\# Translation and other improvements

Nikita Kiselov(https://github.com/kinivi)

 

\# License

hand-gesture-recognition-using-mediapipe is under \[Apache v2 license](LICENSE).

