from playwright.sync_api import Page

class NavigationMenu:
    def __init__(self, page: Page):
        self.page = page

        self.desktops_menu = page.get_by_role("link", name="Desktops")
        self.laptops_menu = page.get_by_role("link", name="Laptops & Notebooks")
        self.components_menu = page.get_by_role("link", name="Components")
        self.tablets_menu = page.get_by_role("link", name="Tablets")
        self.software_menu = page.get_by_role("link", name="Software")
        self.phones_menu = page.get_by_role("link", name="Phones & PDAs")
        self.cameras_menu = page.get_by_role("link", name="Cameras")
        self.mp3_players_menu = page.get_by_role("link", name="MP3 Players")
        self.dropdown_menu = page.locator(".nav-item.dropdown")

    def click_desktops(self):
        self.desktops_menu.click()

    def hover_over_menu(self, menu_name: str):
        menu_item = self.page.get_by_role("link", name=menu_name)
        menu_item.hover()

    def select_dropdown_option(self, main_menu: str, sub_option: str):
        self.hover_over_menu(main_menu)
        dropdown_option = self.page.locator(f"li.nav-item >> text={sub_option}")
        dropdown_option.click()