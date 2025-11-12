import pytest
import time
from pathlib import Path


@pytest.fixture(scope="session", autouse=True)
def cleanup_old_files():
    """Delete screenshots and allure results older than 2 days before tests run"""
    current_dir = Path(__file__).parent
    screenshots_dir = current_dir.parent / 'screenshots'
    allure_dir = current_dir.parent / 'allure-results'

    two_days_ago = time.time() - (2 * 24 * 60 * 60)

    if screenshots_dir.exists():
        for file in screenshots_dir.iterdir():
            if file.is_file() and file.stat().st_mtime < two_days_ago:
                file.unlink()
                print(f"Deleted old screenshot: {file.name}")

    if allure_dir.exists():
        for file in allure_dir.iterdir():
            if file.is_file() and file.stat().st_mtime < two_days_ago:
                file.unlink()
                print(f"Deleted old allure result: {file.name}")