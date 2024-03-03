import random
import re
import string



class Scroll(object):

    def __init__(self, driver):
        self.driver = driver
        self.dimensions = driver.get_window_rect()
        self.height = self.dimensions["height"]
        self.width = self.dimensions["width"]

    def swipeUp(self, swipes, duration, driver):
        for _ in range(swipes):
            driver.swipe(self.width * 0.5, self.height * 0.5, self.width * 0.5, self.height * 0.8, duration)

    def swipeDown(self, swipes, duration, driver):
        for _ in range(swipes):
            driver.swipe(self.width * 0.5, self.height * 0.5, self.width * 0.5, self.height * 0.2, duration)

    def swipeLeft(self, swipes, duration, driver):
        for _ in range(swipes):
            driver.swipe(self.width * 0.5, self.height * 0.5, self.width * 0.8, self.height * 0.5, duration)

    def swipeRight(self, swipes, duration, driver):
        for _ in range(swipes):
            driver.swipe(self.width * 0.5, self.height * 0.5, self.width * 0.3, self.height * 0.5, duration)


def remove_text_and_convert_to_int(text):
    numbers = re.findall(r"\b\d+\b", text)
    if numbers:
        return int(numbers[-1])
    else:
        return None

def generate_random_email():
    with open("email.txt", 'a') as file:
        while True:
            username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
            domains = ['gmail.com', 'onet.pl', 'hotmail.com']
            domain = random.choice(domains)
            email = f"{username}@{domain}"            
            if email not in get_email_from_file("email.txt"):
                file.write(email + '\n')
                return email

def get_email_from_file(filename):
    emails = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                emails.append(line.strip())
    except FileNotFoundError:
        print(f"File not found '{filename}'.")
    return emails