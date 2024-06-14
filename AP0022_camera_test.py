# npm i --location=global appium
# appium
# appium driver install uiautomator2
# pip install Appium-Python-Client
# pip install
import time
import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName="Pixel 7a",  # Pixel 8 Pro # Galaxy A51 5G
    platformVersion="13.0",  # 14.0


)
appium_server_url = 'http://localhost:4723/wd/hub'


class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))

    def tearDown(self) -> None:
        if self.driver:
            time.sleep(5)
            self.driver.quit()

    def test_camera(self) -> None:  # AP0022
        photo_button = self.driver.find_element(AppiumBy.XPATH,
                                                value='//android.widget.TextView[@content-desc="Camera"]')

        photo_button.click()
        time.sleep(2)
        cap_photo_btn = self.driver.find_element(AppiumBy.XPATH, value='//android.widget.ImageButton['
                                                                       '@content-desc="Take photo"]')
        cap_photo_btn.click()
        display_photo_btn = self.driver.find_element(AppiumBy.XPATH, value='//android.widget.ImageButton['

                                                                           '@content-desc="Photo gallery"]')
        time.sleep(2)
        display_photo_btn.click()
        delete_button = self.driver.find_element(AppiumBy.XPATH, value='//android.widget.TextView['
                                                                       '@resource-id="com.google.android.apps.photos'
                                                                       ':id/button_label" and @text="Delete"]')
        delete_button.click()
        time.sleep(5)
        mv_trash_btn = self.driver.find_element(AppiumBy.XPATH, value='//android.widget.TextView['
                                                                      '@resource-id="com.google.android.apps.photos'
                                                                      ':id/move_to_trash"]')
        mv_trash_btn.click()
        time.sleep(1)

