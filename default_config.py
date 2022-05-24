from selenium import webdriver

def config():
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('start-maximized')
    options.add_argument('enable-automation')
    options.add_argument('--disable-infobars')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-browser-side-navigation')
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--remote-debugging-port=9222")
    options.add_argument('--disable-gpu')
    options.add_argument("--log-level=3")
    options.add_experimental_option("useAutomationExtension", False)
    options.add_extension("files/3.0.7_0.crx")
    options.add_extension("files/3.12_0.crx")
    return options