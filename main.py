import subprocess

import speech_recognition as sr


def say(text):
    print(text)
    subprocess.call(['say', text])


def listen():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        return recognizer.recognize_google(audio)


if __name__ == '__main__':
    transcript = listen()
    say(f"You said: {transcript}")
