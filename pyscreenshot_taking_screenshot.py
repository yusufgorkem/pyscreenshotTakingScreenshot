import time
import pyscreenshot as image_grab
import schedule
from datetime import datetime


def take_screenshot():
    print("Screenshot is being taken...")

    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d_%H-%M-%S-%f")
    image_name = f"screenshot-{timestamp}"
    screenshot = image_grab.grab()

    filepath = f"./screenshots/{image_name}.png"
    screenshot.save(filepath)

    print("Screenshot has been taken")

    return filepath


def main():
    try:
        schedule.every(5).seconds.do(take_screenshot)

        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        print("The program is ended")


if __name__ == "__main__":
    main()
