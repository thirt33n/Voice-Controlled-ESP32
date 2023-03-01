# Voice-Controlled-ESP32
# Intro
The title is slightly misleading as the voice recognition is not infact done by the ESP32 itself.

Rather the computer connected to the ESP32 does it first and then passes the command over to the ESP32.
# Installation

<li>
The <a href='https://github.com/thirt33n/Voice-Controlled-ESP32/blob/master/flash.ino'>Flash.ino</a> file should be initially flashed onto the ESP32 board using the Arduino IDE or any other software.
</li>
<li>
Then, <a href='https://github.com/thirt33n/Voice-Controlled-ESP32/blob/master/esp32.py'>esp32.py</a> file can be run after installing the requirements and configuring the COM port it uses on your device.The script uses the <a href='https://pypi.org/project/SpeechRecognition/'>SpeechRecognition</a> library to listen and record the voice then recognizes it and returns it as text, this is then sent to the board via the serial interface using the <a href='https://pyserial.readthedocs.io/en/latest/index.html'>pyserial</a> library.
</li>

<h2> It is important to first flash the board using the <a href='https://github.com/thirt33n/Voice-Controlled-ESP32/blob/master/flash.ino'>Flash.ino</a> file, then close the Arduino IDE and then run the python script to prevent errors involving the COM ports </h2>


# Working

Running the <a href='https://github.com/thirt33n/Voice-Controlled-ESP32/blob/master/esp32.py'>esp32.py</a> python script will start your device's microphone and starts listening to your voice, speaking "ON" will turn on the Built-In LED and "OFF" Will switch off the LED. You can stop the program by pressing CTRL+C.

![image](https://user-images.githubusercontent.com/55974622/222079157-ada66d0f-f640-43a0-b992-c5dcdfca04ba.png)


# Author

<a href='https://github.com/thirt33n'>Siddharth Pradeep</a>
