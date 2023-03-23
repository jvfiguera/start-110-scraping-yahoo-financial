from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class Browser():
    service, webbrowser= None, None
    def __init__(self, p_driver_path:str):
        self.service= Service(executable_path=p_driver_path)
        self.webbrowser= webdriver.Chrome(service=self.service)

    def mth_open_browser(self, url_page : str):
        '''Method that let us to open a particular URL on the browser'''
        self.webbrowser.get(url=url_page)
        self.webbrowser.maximize_window()
    def mth_close_browser(self):
        '''Method that let us to close browser'''
        self.webbrowser.close()