import asyncio

import pyperclip


class UrlTracker:
  def __init__(self):
    self.tracked_urls = set() # Store tracked URLs to avoid duplicates
    self.filename = "tracked_urls.txt"
    self.ensure_file_exists()
    self.clipboard_timer = asyncio.ensure_future(self.check_clipboard())

#  async def check_clipboard(self):
#    while True:
#      clipboard_data = pyperclip.paste()
#      if clipboard_data.startswith('http://') or clipboard_data.startswith('https://'):
#        url = clipboard_data.strip()
#        if url not in self.tracked_urls:
#          self.log_url(url)
#          self.tracked_urls.add(url)
#      await asyncio.sleep(2)
#
#    def log_url(self, url):
#     with open(self.filename, "a") as f:
#       f.write(f"{url}\n")
#       print(f"URL logged to file: {url}")
#

    
  def is_url_in_file(self, url, filepath):
            with open(filepath, 'r') as file:
                return url in file.read()
    
  def append_url_to_file(self, url, filepath):
        with open(filepath, 'a') as file:
                file.write(f'{url}\n')
                print(f"URL saved : {url}")

  async def check_clipboard(self):
        while True:
                clipboard_data = pyperclip.paste()
                words = clipboard_data.split()
                for word in words:
                    if word.startswith('http://') or word.startswith('https://'):
                        url=word

                        if not self.is_url_in_file(url, 'tracked_urls.txt'):
                            self.append_url_to_file(url, 'tracked_urls.txt')
        await asyncio.sleep(2)

  def ensure_file_exists(self):
    with open(self.filename, "a"):
      pass # Create the file if it doesn't exist

  def run(self):
    try:
      asyncio.run(self.check_clipboard())
    except KeyboardInterrupt:
      pass
    except asyncio.CancelledError:
        pass  # Ignore CancelledError when the task is cancelled

  def welcome(self):
    print("Welcome to the URL tracker app.")
    print("The app currently only runs in a terminal, you can press Crtl+C to terminate the app, or just close the window")
    print("The logged urls are saved at tracked_urls.txt")

if __name__ == '__main__':
  url_tracker = UrlTracker()
  url_tracker.welcome()
  url_tracker.run()
