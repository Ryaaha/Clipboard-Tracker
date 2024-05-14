from datetime import datetime
import pyperclip
import time


class UrlTracker:

    def __init__(self):
        self.filename = "tracked_urls.txt"
        self.ensure_file_exists()

    # Check if URL already exists in the file
    def is_url_in_file(self, url, filepath):
        with open(filepath, "r") as file:
            return url in file.read()

    # Append new URL to the file
    def append_url_to_file(self, url, filepath):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(filepath, "a") as file:
            file.write(f"{url} - timestamp : {timestamp} \n")
            print(f"URL saved : {url}")

    # Check for URLs in clipboard every 2 seconds
    def check_clipboard(self, isTestMode):
        while True:
            clipboard_data = pyperclip.paste()
            words = clipboard_data.split()
            for word in words:
                if word.startswith("http://") or word.startswith("https://"):
                    url = word

                    if not self.is_url_in_file(url, "tracked_urls.txt"):
                        self.append_url_to_file(url, "tracked_urls.txt")
            if isTestMode:
                return

            time.sleep(2)

    # Check if file to store URLs exist, if not create it
    def ensure_file_exists(self):
        with open(self.filename, "a"):
            pass  # Create the file if it doesn't exist

    # Start monitoring
    def run(self):
        try:
            self.welcome()
            self.check_clipboard(False)
        except KeyboardInterrupt:
            pass

    # For running checks and tests (Developer Option)
    def run_check(self):
        try:
            self.check_clipboard(True)
        except KeyboardInterrupt:
            pass

    # Introductory Information
    def welcome(self):
        print("Welcome to the URL tracker app.")
        print(
            "The app currently only runs in a terminal, you can press Crtl+C to terminate the app, or just close the window"
        )
        print("The logged urls are saved at tracked_urls.txt")
