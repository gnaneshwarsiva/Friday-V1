from core.speech import listen
from core.speaker import speak
from core.wakeword import is_wake_word
from commands import execute

speak("Friday is online")

try:

    while True:

        print("\n🎤 Waiting for wake word...")

        text = listen()

        print(f"📝 Heard: {text}")

        if not text:
            continue

        # Exit anytime
        if any(word in text for word in [
            "exit",
            "quit",
            "goodbye",
            "shutdown friday"
        ]):
            speak("Goodbye Gnaneshwar")
            break

        # Check wake word
        if not is_wake_word(text):
            continue

        speak("Yes Gnaneshwar")

        print("🎧 Listening for command...")

        command = listen()

        print(f"📝 Command: {command}")

        if not command:
            continue

        # Exit after wake word
        if any(word in command for word in [
            "exit",
            "quit",
            "goodbye",
            "shutdown friday"
        ]):
            speak("Goodbye Gnaneshwar")
            break

        response = execute(command)

        if response:
            speak(response)

except KeyboardInterrupt:

    print("\n🛑 Shutting down...")

    speak("Goodbye Gnaneshwar")