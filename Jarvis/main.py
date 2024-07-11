import speech_recognition as sr
import webbrowser
import pyttsx3
import music_library

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("http://www.google.com")

    elif "open facebook" in c.lower():
        webbrowser.open("https://www.facebook.com/")

    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com/")

    elif "open linkedin" in c.lower():
        webbrowser.open("https://in.linkedin.com/")

    elif "open instagram" in c.lower():
        webbrowser.open("https://www.instagram.com/")

    elif c.lower().startswith("play"):
        try:
            song = c.lower().split(" ")[1]
            link = music_library.music[song]
            webbrowser.open(link)

        except KeyError:
            speak(f"Sorry, I couldn't find {song} in the music library.")

        except Exception as e:
            speak("Sorry, there was an error while playing the song.")


if __name__ == "__main__":
    speak("Initializing Jarvis......")

    while True:
        # listen for the word "Jarvis"
        # "obtain audio from microphone"
        r = sr.Recognizer()
        
        print("recognising.....")
        try:
            with sr.Microphone() as source:
                print("Listening....")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("How may I help you")
                # listen for command
                with sr.Microphone() as source:
                    print("Activating Jarvis")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)

        except sr.UnknownValueError:
            speak("Could not understand audio")
        except sr.RequestError as e:
            speak(f"Could not request results; {e}")
        except Exception as e:
            print(f"Error: {e}")