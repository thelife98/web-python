from testsuite.pagework.browser_engine import BrowserEngine
import unittest
import time
from testsuite.locateobject.home_page import HomePage
from testsuite.locateobject.tems_to_inv_page import TemsToInvPage
from testsuite.pagework.logger import Logger
logger = Logger(logger='TestInvList').get_log()


class TestInvList(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
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

    def test_1_login_user(self):
        """
        登录测试
        :return:
        """
        public = TemsToInvPage(self.driver)
        print("=========菜单==========")
        public.menu_3()
        public.submenu_1()

    def test_2_login_user(self):
        print("=========新增==========")
        public = TemsToInvPage(self.driver)
        public.frame_1()
        public.bill_add()
        time.sleep(3)

    def test_3_login_user(self):
        print("=========表头==========")
        public = TemsToInvPage(self.driver)
        public.frame_2()
        time.sleep(2)
        public.head_1("H1901026413")
        public.head_2("料件")
        public.head_3("一般贸易")
        public.head_4("公路运输")
        public.head_5("北京关区")
        public.head_6("亚洲")
        public.head_7("15")
        public.head_8("10")
        public.head_9("木箱")
        public.head_10("非报关")
        public.head_11("无")
        public.save_btn()

    def test_4_login_user(self):
        print("=========表体 新增==========")
        public = TemsToInvPage(self.driver)
        public.scroll()
        public.img_add()
        public.frame_3()
        public.from_1()
        public.frame_4()
        public.body_1()
        public.body_1_1("100")
        public.body_1_2()
        public.body_2("中国")
        public.body_3("10")
        public.body_4("借用")
        public.exit_frame_public()
        public.frame_3()
        print("111111111")
        public.from_2()
        public.exit_frame_public()

    @unittest.skip("我不想运行这个用例")
    def test_5_login_user(self):
        print("=========表体 导入==========")
        public = TemsToInvPage(self.driver)
        public.scroll()
        public.imgImport()
        public.frame_4()
        public.img_import_1()
        public.img_import_2()

    @unittest.skip("我不想运行这个用例")
    def test_6_login_user(self):
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