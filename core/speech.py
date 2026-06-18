import speech_recognition as sr

def listen():

    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:

            print("🎤 Listening...")

            recognizer.adjust_for_ambient_noise(
                source,
                duration=1
            )

            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=10
            )

        text = recognizer.recognize_google(audio)

        print("You:", text)

        return text.lower()

    except sr.WaitTimeoutError:
        print("⏳ No speech detected")
        return ""

    except sr.UnknownValueError:
        print("🤔 Could not understand audio")
        return ""

    except Exception as e:
        print(f"❌ Error: {e}")
        return ""