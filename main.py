from selenium import webdriver


class ChromeDriver:
    def __enter__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-background-networking")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--disable-default-apps")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-extensions")
        options.add_argument('--disable-features=DownloadBubbleV2')
        options.add_argument("--disable-features=Translate")
        options.add_argument('--headless')
        options.add_argument("--hide-scrollbars")
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--incognito")
        options.add_argument("--mute-audio")
        options.add_argument("--no-default-browser-check")
        options.add_argument('--no-sandbox')
        options.add_argument("--propagate-iph-for-testing")
        options.add_experimental_option("excludeSwitches", ["enable-automation", "enable-logging"])
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
