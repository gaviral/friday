import speech_recognition as sr


if __name__ == '__main__':

    # initialize
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    # stt
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        transcript = recognizer.recognize_google(audio)

    # log
    print(f"USER: {transcript}")
