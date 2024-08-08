from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class ChromeDriver:
    def __enter__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--user-agent=selenium')
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--no-zygote')
        options.add_argument('--single-process')
        self.driver = webdriver.Chrome(options=options)
        self.driver.set_window_size(1920, 1080)
        return self.driver

    def __exit__(self, exc_type, exc_value, tb):
        self.driver.quit()


def main():
    with ChromeDriver() as driver:
        driver.get('https://www.google.com/')
        print(driver.title)

main()
