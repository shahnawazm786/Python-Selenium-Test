import time
from plyer import notification

while True:
    notification.notify(
        title="Alert",
        message="Take a break! It has been an hour",
        timeout=10
    )
    time.sleep(3600)