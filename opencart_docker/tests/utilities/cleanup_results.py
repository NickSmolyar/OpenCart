import pytest
from pathlib import Path
import time
import logging
from typing import List, Optional

# Configure basic logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def delete_old_files(
        directories: List[Path],
        days_old: int = 2,
        dry_run: bool = False,
        file_pattern: str = "*"
) -> None:
    """
    Delete files older than specified days in given directories.

    Args:
        directories: List of directory paths to clean
        days_old: Delete files older than this many days (default: 2)
        dry_run: If True, only log what would be deleted (default: False)
        file_pattern: File pattern to match (default: all files)
    """
    cutoff = time.time() - (days_old * 86400)

    for directory in directories:
        if not directory.exists():
            logger.warning(f"Directory not found: {directory}")
            continue

        logger.info(f"Checking directory: {directory}")

        for file in directory.glob(file_pattern):
            if file.is_file() and file.stat().st_mtime < cutoff:
                try:
                    logger.info(f"Deleting {file}")
                    if not dry_run:
                        file.unlink(missing_ok=True)
                except Exception as e:
                    logger.error(f"Failed to delete {file}: {e}")


@pytest.fixture(scope="session", autouse=True)
def cleanup_before_tests(request):
    """
    Pytest fixture to automatically clean old test artifacts before test session.
    Configure with pytest markers:
    @pytest.mark.cleanup_days(3)
    @pytest.mark.cleanup_dry_run(True)
    """
    # Get configuration from pytest markers
    marker_days = request.node.get_closest_marker("cleanup_days")
    marker_dry_run = request.node.get_closest_marker("cleanup_dry_run")

    days_old = marker_days.args[0] if marker_days else 2
    dry_run = marker_dry_run.args[0] if marker_dry_run else False

    script_dir = Path(__file__).parent
    dirs_to_clean = [
        script_dir.parent / 'allure-results',
        script_dir.parent / 'screenshots'
    ]

    logger.info(f"Starting test cleanup (days_old={days_old}, dry_run={dry_run})")
    delete_old_files(
        directories=dirs_to_clean,
        days_old=days_old,
        dry_run=dry_run
    )

# Example usage in test file:
# @pytest.mark.cleanup_days(3)
# @pytest.mark.cleanup_dry_run(True)
# def test_example():
#     ...