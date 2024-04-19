# npm i --location=global appium
# appium
# appium driver install uiautomator2
# pip install Appium-Python-Client
# pip install
# Failed to create session. The session identified by 820c42fb-7367-4c2c-8dbb-9b13cce1f6c3 is not known
# adb uninstall io.appium.uiautomator2.server
import time
import unittest
from selenium.webdriver.common.action_chains import ActionChains

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName="Galaxy A51 5G",  # Pixel 8 Pro
    platformVersion="11.0",  # 14.0
    # appPackage='com.android.settings',
    # appActivity='.Settings',
    # appPackage="com.android.camera",  # Package name of the camera app
    # appActivity="com.android.camera.CameraActivity",
    # app=r"C:\Users\sael\PycharmProjects\AS0780Automation\apps\calculator-lock-video-lock-and-photo-vault-hidex-3-5-17"
    #   "-4.apk"

)
appium_server_url = 'http://localhost:4723/wd/hub'


class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))

    def tearDown(self) -> None:
        if self.driver:
            time.sleep(5)
            self.driver.quit()

    def test_Display(self) -> None:
        display_button = self.driver.find_element(AppiumBy.XPATH, value='//androidx.recyclerview.widget.RecyclerView['
                                                                        '@resource-id="com.android.settings:id'
                                                                        '/recycler_view'
                                                                        '"]/android.widget.LinearLayout['
                                                                        '5]/android.widget.RelativeLayout')
        display_button.click()

    def test_camera(self) -> None:
        photo_button = self.driver.find_element(AppiumBy.XPATH, value='//android.view.View['
                                                                      '@resource-id="com.sec.android.app.camera:id'
                                                                      '/bottom_background"]')
        photo_button.click()
        # failed

    def test_calculator_installed(self) -> None:  # succeed
        time.sleep(5)
        number9 = self.driver.find_element(AppiumBy.XPATH,
                                           value='//android.widget.Button[@resource-id="com.flatfish.cal.privacy:id'
                                                 '/cal_9"]')
        number9.click()
        time.sleep(2)
        multi_sign = self.driver.find_element(AppiumBy.XPATH, value='//android.widget.Button['
                                                                    '@resource-id="com.flatfish.cal.privacy:id'
                                                                    '/cal_multiply"]')
        multi_sign.click()
        time.sleep(1)
        number9.click()
        screen = self.driver.find_element(AppiumBy.XPATH, value='//android.widget.EditText['
                                                                '@resource-id="com.flatfish.cal.privacy:id/cal_result"]')
        result = screen.text
        print("Result will be", result)

    def test_brute_force(self) -> None:
        time.sleep(5)
        pin1 = self.driver.find_element(AppiumBy.XPATH, value='//android.view.ViewGroup[@content-desc="1"]')
        pin2 = self.driver.find_element(AppiumBy.XPATH, value='//android.view.ViewGroup[@content-desc="2"]')
        pin3 = self.driver.find_element(AppiumBy.XPATH, value='//android.view.ViewGroup[@content-desc="3"]')
        pin4 = self.driver.find_element(AppiumBy.XPATH, value='//android.view.ViewGroup[@content-desc="4"]')
        ok_button = self.driver.find_element(AppiumBy.XPATH, value='//android.widget.TextView[@content-desc="OK"]')

        pin1.click()
        time.sleep(1)
        pin2.click()
        time.sleep(1)
        pin3.click()
        time.sleep(1)
        pin4.click()
        time.sleep(1)
        ok_button.click()


if __name__ == '__main__':
    unittest.main()
