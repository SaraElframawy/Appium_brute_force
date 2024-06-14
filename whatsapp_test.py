import time
import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Desired Capabilities
capabilities = {
    'platformName': 'Android',
    'automationName': 'UiAutomator2',
    'deviceName': 'Pixel 7a',
    'platformVersion': '13.0',
    'appPackage': 'com.whatsapp',
    'appActivity': 'com.whatsapp.Main',
    'noReset': True,
    'fullReset': False
}

appium_server_url = 'http://localhost:4723/wd/hub'


class TestAppium(unittest.TestCase):
    def setUp(self):
        options = UiAutomator2Options()
        options.load_capabilities(capabilities)
        self.driver = webdriver.Remote(appium_server_url, options=options)
        self.wait = WebDriverWait(self.driver, 30)  # Set explicit wait

    def tearDown(self):
        if self.driver:
            self.driver.quit()

    def test_start(self):
        time.sleep(2)

    def test_send_message(self):
        try:

            contact = self.wait.until(
                EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView['
                                                                '@resource-id="com.whatsapp:id'
                                                                '/conversations_row_contact_name" and @text="Me"]'))
            )
            contact.click()

            message_input = self.wait.until(
                EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.EditText['
                                                                '@resource-id="com.whatsapp:id/entry"]'))
            )
            message_input.click()
            message_input.send_keys("Hello, this is a test message from Sara ! ")

            send_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Send')
            send_button.click()

        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == '__main__':
    unittest.main()