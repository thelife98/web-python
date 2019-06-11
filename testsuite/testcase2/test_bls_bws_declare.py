from testsuite.pagework.browser_engine import BrowserEngine
# from castro import Castro
import unittest
import time
from testsuite.locateobject.home_page import HomePage
from testsuite.pagework.logger import Logger
logger = Logger(logger='TestBrowserEngine').get_log()
# 创建一个Castro对象并且使用录象文件的路径和名称作为参数初始值实例
# screenCapture = Castro(filename="TestBrowserEngine.swf")


# 物流 - 物流账册申报
class TestBrowserEngine(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 开始录屏
        # screenCapture.start()
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)
        public = HomePage(cls.driver)
        print("=========登录===========")
        public.user_1("wgh123")
        public.password_1("1")
        public.send_submit_btn()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        # 开始录屏
        # screenCapture.stop()

    def test_1_login_user(self):
        """
        登录测试
        :return:
        """
        public = HomePage(self.driver)
        print("=========菜单==========")
        public.click_assembly()
        time.sleep(2)
        public.menu_1()
        time.sleep(2)
        public.submenu_1()
        time.sleep(2)

    def test_2_login_user(self):
        print("=========新增==========")
        public = HomePage(self.driver)
        public.frame_1()
        public.bill_add()
        time.sleep(2)

    def test_3_login_user(self):
        print("=========表头==========")
        public = HomePage(self.driver)
        public.frame_2()
        time.sleep(2)
        public.head_1("保税物流中心A")
        public.head_2("保税物流中心A")
        public.head_3("可累计")
        public.head_4("珠海香洲")
        public.head_5("10")
        public.head_6("10")
        public.head_7("2019-1-1")
        public.head_8("无")
        public.save_btn()

    def test_4_login_user(self):
        print("=========随附单证==========")
        public = HomePage(self.driver)
        public.scroll()
        public.flie_btn()
        public.file_Add()
        public.frame_3()
        public.file_1("1")
        public.file_2("文件")
        public.file_3("1.1")
        public.file_4("1.2")
        public.file_5("无")
        public.file_6()
        public.file_7()
        public.fil_save()
        public.exit_frame_1()
        public.declare()


if __name__ == '__main__':
    unittest.main(verbosity=2)