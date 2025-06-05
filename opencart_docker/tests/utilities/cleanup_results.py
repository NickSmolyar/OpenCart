import pytest
from pathlib import Path
import time

def delete_old_files():
    script_dir = Path(__file__).parent
    dirs_to_clean = [
        script_dir.parent / 'allure-results',
        script_dir.parent / 'screenshots'
    ]
    days_old = 2
    cutoff = time.time() - (days_old * 86400)

    for directory in dirs_to_clean:
        if not directory.exists():
            continue
        for file in directory.glob('*'):
            if file.is_file() and file.stat().st_mtime < cutoff:
                file.unlink(missing_ok=True)

@pytest.fixture(scope="session", autouse=True)
def cleanup_before_tests():
    delete_old_files()