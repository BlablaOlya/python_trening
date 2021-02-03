from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper


class Application:

    def __init__(self):
        # self.wd = webdriver.Chrome(ChromeDriverManager().install())
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.gpoup = GroupHelper(self)
        self.contact = ContactHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()