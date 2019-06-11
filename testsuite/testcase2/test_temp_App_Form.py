from testsuite.pagework.browser_engine import BrowserEngine
import unittest
import time
from testsuite.locateobject.home_page import HomePage
from testsuite.locateobject.Temp_App_Form_page import TempAppFormPage
from testsuite.pagework.logger import Logger
logger = Logger(logger='TestTempAppForm').get_log()


# 临时出入区申请表自动化测试脚本
class TestTempAppForm(unittest.TestCase):
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
        public = TempAppFormPage(self.driver)
        print("=========菜单==========")
        public.menu_temp()
        public.menu_app()

    def test_2_login_user(self):
        print("=========新增==========")
        public = TempAppFormPage(self.driver)
        public.frame_1()
        public.add()
        time.sleep(3)
        public.select_no("H1812280949")
        public.save()

    def test_3_login_user(self):
        print("=========表头==========")
        public = TempAppFormPage(self.driver)
        public.frame_2()
        time.sleep(2)
        public.business_type_cd("其他业务")
        public.area_out_etp_sno("2018HS1228")
        public.valid_time("2018-12-29")
        public.exhibition_place("珠海香洲唐家湾")

    def test_4_login_user(self):
        print("=========表体 新增==========")
        public = TempAppFormPage(self.driver)
        public.frame_3()
        time.sleep(2)
        public.affirm()
        public.dcl_qty("10")
        public.dcl_uprc_amt("5")
        public.gds_mark_cd("重点商品")
        public.gds_rmk("容易破碎，运输请小心")
        public.rmk("无")


if __name__ == '__main__':
    unittest.main(verbosity=2)