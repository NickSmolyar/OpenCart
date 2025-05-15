import os
from datetime import time
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from playwright.sync_api import BrowserContext, Page
    import pytest


class BaseComponent:
    def __init__(
            self,
            context: 'BrowserContext',
            page: 'Page',
            request: Optional['pytest.FixtureRequest'] = None
    ):
        self.context: 'BrowserContext' = context
        self.page: 'Page' = page
        self.request: Optional['pytest.FixtureRequest'] = request

    def make_screenshot(self, name: str = "screenshot", full_page: bool = True):
        """Take and return screenshot path for current page."""
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        file_name = f"{name}_{timestamp}.png"
        screenshot_dir = "screenshots"
        os.makedirs(screenshot_dir, exist_ok=True)
        path = os.path.join(screenshot_dir, file_name)
        self.page.screenshot(path=path, full_page=full_page)
        return path