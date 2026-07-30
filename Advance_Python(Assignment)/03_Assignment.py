from abc import ABC, abstractmethod


# Strategy Interface
class Notification(ABC):

    @abstractmethod
    def send(self, message):
        pass


class Email(Notification):

    def send(self, message):
        print(f"Email Sent: {message}")


class SMS(Notification):

    def send(self, message):
        print(f"SMS Sent: {message}")


class WhatsApp(Notification):

    def send(self, message):
        print(f"WhatsApp Message Sent: {message}")


# Context Class
class NotificationService:

    def __init__(self, notification):
        self.notification = notification

    def notify(self, message):
        self.notification.send(message)


# Main Program
msg = input("Enter Message: ")

print("\nSelect Notification Type")
print("1. Email")
print("2. SMS")
print("3. WhatsApp")

choice = input("Enter Choice: ")

if choice == "1":
    service = NotificationService(Email())
elif choice == "2":
    service = NotificationService(SMS())
elif choice == "3":
    service = NotificationService(WhatsApp())
else:
    print("Invalid Choice")
    exit()

service.notify(msg)

# output:
# Enter Message: "hello APP"

# Select Notification Type
# 1. Email
# 2. SMS
# 3. WhatsApp
# Enter Choice: 3