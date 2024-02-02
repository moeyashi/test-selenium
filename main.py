import time
from datetime import datetime
import psutil
import chromedriver_binary
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
        self.driver = webdriver.Chrome(executable_path='chromedriver', options=options)
        self.driver.set_window_size(1920, 1080)
        return self.driver

    def __exit__(self, exc_type, exc_value, tb):
        self.driver.quit()


def print_all_processes():
    for proc in psutil.process_iter(['pid', 'name']):
        print(proc.info)


def main():
    started_at = datetime.now()
    print(started_at)
    with ChromeDriver() as driver:
        driver.get('https://www.google.com/')
        print(driver.title)
        loop_count = 1
        while True:
            driver.execute_script("window.open('https://example.com/');")
            driver.switch_to.window(driver.window_handles[-1])
            print(loop_count)
            loop_count += 1
            print(f"{datetime.now() - started_at}秒経過")
            print(driver.title)
            print_all_processes()
            time.sleep(3)
            driver.close()
            driver.switch_to.window(driver.window_handles[0])


main()
