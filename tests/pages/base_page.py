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