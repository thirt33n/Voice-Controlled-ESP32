import serial
import time
import speech_recognition as sr 
import pyaudio
esp = serial.Serial(port='COM8', baudrate=115200, timeout=.1)

def swap(command):
    on = 'on'
    off = 'off'
    if on in command:
        return '5'
    if off in command:
        return '6'
    
    return 0

#Writes the inout onto the board
def write_read(x):
    x_bytes = bytes(x,'utf-8') # converting the bytes to string
    print(x_bytes)
    esp.write(x_bytes)
    time.sleep(0.05)
    data = esp.read_all()
    return data



# initialize the recognizer
def main():
    r = sr.Recognizer()
    while(True):
        with sr.Microphone() as source:
            # read the audio data from the default microphone
            print('Listening...')
            audio_data = r.record(source, duration=5)
            print("Recognizing...")

            # convert speech to text
            try:
                text = r.recognize_google(audio_data)
              
                print(text)
                num = swap(text)
                print(num)
                info = write_read(num)
                print(info)
                
            except:
                print('Couldnt Recognize command')

main()