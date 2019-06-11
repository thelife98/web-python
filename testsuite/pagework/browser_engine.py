# coding = utf-8
from selenium import webdriver
from testsuite.pagework.logger import Logger
import configparser
import os.path

logger=Logger(logger='BrowserEngine').get_log()


class BrowserEngine(object):
    """
    浏览器引擎类,根据browser_type的值去，控制启动不同的浏览器，浏览器主要是IE，Firefox, Chrome
    """
    dir = os.path.dirname(os.path.abspath('.'))  # 定义dir变量,获取当前项目的根目录的相对路径方法
    chrome_driver_path = dir + '/drivers/chromedriver.exe'  # 定义chrome_driver_path变量,获取谷歌驱动的路径
    ie_driver_path = dir + '/drivers/IEDriverServer.exe'  # 定义ie_driver_path变量,获取IE驱动的路径

    def __init__(self, driver):
        self.driver = driver

    def open_browser(self, driver):
        config = configparser.ConfigParser()
        # file_path = os.path.dirname(os.getcwd()) + '/config/config.ini'
        file_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
        config.read(file_path)
        # config.read(file_path,encoding='UTF-8'), 如果代码有中文注释，用这个，不然报解码错误

        browser = config.get("browserType", "browserName")
        logger.info("你已经选择了 %s 浏览器." %browser)
        url = config.get("testServer", "URL")
        logger.info("测试套件服务器URL是 : %s" %url)

        if browser == "Firefox":
            driver = webdriver.Firefox()
            logger.info("启动Firefox浏览器.")
        elif browser == "Chrome":
            driver = webdriver.Chrome(self.chrome_driver_path)
            logger.info("启动Chrome浏览器.")
        elif browser == "IE":
            driver = webdriver.Ie(self.ie_driver_path)
            logger.info("启动IE浏览器.")
        driver.get(url)
        logger.info("打开地址: %s" % url)
        driver.maximize_window()
        logger.info("最大化当前窗口.")
        driver.implicitly_wait(10)
        logger.info("隐式等待10秒,正在处理.......")
        return driver

    def quit_browser(self):
        logger.info("现在，关闭并退出浏览器 .")
        self.driver.quit()



