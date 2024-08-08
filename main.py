from selenium import webdriver


class ChromeDriver:
    def __enter__(self):
        options = webdriver.ChromeOptions()
        # 参考
        # https://qiita.com/kawagoe6884/items/cea239681bdcffe31828
        options.add_argument("--disable-background-networking")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--disable-default-apps")
        # 必須 これがないとメモリ不足になる
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-extensions")
        options.add_argument('--disable-features=DownloadBubbleV2')
        options.add_argument("--disable-features=Translate")
        # 必須 `--headless=new`にはしない。hangしてしまう。
        options.add_argument('--headless')
        options.add_argument("--hide-scrollbars")
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--incognito")
        options.add_argument("--mute-audio")
        options.add_argument("--no-default-browser-check")
        # 必須 「session not created: DevToolsActivePort file doesn't exist」と言われる
        options.add_argument('--no-sandbox')
        # ゾンビプロセスを作らない。プロセスが残るとメモリをくいつぶす
        options.add_argument('--no-zygote')
        options.add_argument("--propagate-iph-for-testing")
        # ゾンビプロセスを作らない。プロセスが残るとメモリをくいつぶす
        options.add_argument('--single-process')
        options.add_argument('--user-agent=selenium')
        options.add_experimental_option(
            "excludeSwitches", ["enable-automation", "enable-logging"]
        )
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
