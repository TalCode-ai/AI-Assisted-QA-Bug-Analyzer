from datetime import datetime
from pathlib import Path


def save_screenshot(driver, test_name, folder_path="reports/screenshots"):
    screenshots_folder = Path(folder_path)
    screenshots_folder.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    file_name = f"{test_name}_{timestamp}.png"
    file_path = screenshots_folder / file_name

    driver.save_screenshot(str(file_path))

    return str(file_path)