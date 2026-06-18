import subprocess
import webbrowser
import platform
from datetime import datetime


SYSTEM = platform.system()


def open_chrome():

    if SYSTEM == "Darwin":  # macOS
        subprocess.Popen([
            "open",
            "-a",
            "Google Chrome"
        ])

    elif SYSTEM == "Windows":
        subprocess.Popen(
            "start chrome",
            shell=True
        )

    elif SYSTEM == "Linux":
        subprocess.Popen([
            "google-chrome"
        ])


def open_vscode():

    if SYSTEM == "Darwin":  # macOS
        subprocess.Popen([
            "open",
            "-a",
            "Visual Studio Code"
        ])

    elif SYSTEM == "Windows":
        subprocess.Popen(
            "code",
            shell=True
        )

    elif SYSTEM == "Linux":
        subprocess.Popen([
            "code"
        ])


def execute(command):

    command = command.lower()

    print(f"Received command: {command}")

    # Open Chrome
    if "open chrome" in command:

        print("Launching Chrome...")

        open_chrome()

        return "Opening Chrome"

    # Open VS Code
    elif (
        "open vs code" in command
        or "open vscode" in command
        or "open visual studio code" in command
    ):

        open_vscode()

        return "Opening Visual Studio Code"

    # Tell Time
    elif "time" in command:

        current_time = datetime.now().strftime(
            "%I:%M %p"
        )

        return f"The current time is {current_time}"

    # Tell Date
    elif "date" in command:

        current_date = datetime.now().strftime(
            "%d %B %Y"
        )

        return f"Today's date is {current_date}"

    # Google Search
    elif "search" in command:

        query = command.replace(
            "search",
            ""
        ).strip()

        if query:

            webbrowser.open(
                f"https://www.google.com/search?q={query}"
            )

            return f"Searching for {query}"

        return "Please tell me what to search"

    # Help
    elif "help" in command:

        return (
            "You can ask me to open Chrome, "
            "open VS Code, tell the time, "
            "tell the date, or search Google."
        )

    return "Command not recognized"