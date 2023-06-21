from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

# driver = webdriver.Chrome(service=ChromeService(
#     ChromeDriverManager().install()))


class ChromeAuto:
    def __init__(self):
        self.driver = webdriver.Chrome(service=ChromeService(
            ChromeDriverManager().install()))

    def click_sign_in(self):
        try:
            btn_sign_in = self.driver.find_element(
                By.XPATH, '//button[text()="Sign in"]')
            btn_sign_in.click()
        except Exception as error:
            print('❌❌❌Error on click in sign in:', error)

    def surf_in(self, site):
        self.driver.get(site)

    def quit(self):
        self.driver.quit()


if __name__ == '__main__':
    chome = ChromeAuto()
    chome.surf_in("https://github.com/")
    chome.click_sign_in()
    sleep(10)
    chome.quit()


# driver.maximize_window()
# driver.get("https://g1.globo.com/")
# print("Aplication title is", driver.title)
# print("Current URL:", driver.current_url)
# driver.quit()
