import os
from datetime import datetime


def take_screenshot(driver, test_name):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    screenshot_dir = "screenshots"

    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)

    file_path = os.path.join(
        screenshot_dir,
        f"{test_name}_{timestamp}.png"
    )

    driver.save_screenshot(file_path)

    return file_path