import sys
import threading

from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QWidget
from PyQt6.QtWidgets import QLabel
from PyQt6.QtWidgets import QVBoxLayout

from core.speech import listen
from core.speaker import speak
from core.wakeword import is_wake_word
from commands import execute


class FridayWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setStyleSheet("""
        background-color: #111;
        color: white;
        font-size: 24px;
        """)

        self.setWindowTitle("F.R.I.D.A.Y")
        self.resize(500, 300)

        self.status_label = QLabel(
            "Waiting for wake word..."
        )

        layout = QVBoxLayout()
        layout.addWidget(self.status_label)

        self.setLayout(layout)

        # Start assistant thread
        threading.Thread(
            target=self.run_assistant,
            daemon=True
        ).start()

    def update_status(self, text):

        self.status_label.setText(text)

    def run_assistant(self):

        speak("Friday is online")

        while True:

            self.update_status(
                "Waiting for wake word..."
            )

            text = listen()

            if not text:
                continue

            print("Heard:", text)

            if "exit" in text:
                speak("Goodbye Gnaneshwar")
                break

            if not is_wake_word(text):
                continue

            self.update_status(
                "Listening..."
            )

            speak("Yes Gnaneshwar")

            command = listen()

            if not command:
                continue

            self.update_status(
                f"Command: {command}"
            )

            response = execute(command)

            if response:
                speak(response)

            self.update_status(
                "Waiting for wake word..."
            )


app = QApplication(sys.argv)

window = FridayWindow()

window.show()

sys.exit(app.exec())