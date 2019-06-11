from testsuite.pagework.browser_engine import BrowserEngine
from testsuite.locateobject.home_page import HomePage
from testsuite.locateobject.machin_declare_page import MachinDeclare
import unittest
import time
import os
from utx import *
from selenium.webdriver.support.select import Select
# from testsuite.pagework.logger import Logger

# logger = Logger(logger='TestMachinList').get_log()
file_import_dir=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))+ "\\file_import\\" #定位到项目文件夹路径 如我这个项目文件Demo是放在E盘,路径就是:E:\Demo

# 加工 - 加工账册申报
class TestMachinList(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 开始录屏
        # screenCapture.start()
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)
        public = HomePage(cls.driver)
        print("=========登录===========")
        public.user_1("zhengsi")
        public.password_1("1")
        public.send_submit_btn()
        time.sleep(2)

    @classmethod
    # @unittest.skip("结束语句，暂时不执行")
    def tearDownClass(cls):
        cls.driver.quit()

    @tag(Tag.SMOKE,Tag.V8_3_7)
    def test_login_user(self):
        """
        登录测试
        """
        print("=========菜单==========")
        log.debug("=========菜单==========") #在控制台输出，以直观观察测试进度
        public = MachinDeclare(self.driver)
        public.side_menu()
        time.sleep(1)
        public.side_menu_1()
        time.sleep(1)
        public.side_menu_1_1()
        time.sleep(1)

    @tag(Tag.SMOKE)
    def test_bill_add_user(self):
        """
        加工账册新增
        """
        print("=========新增==========")
        log.debug("=========新增==========")
        public = MachinDeclare(self.driver)
        public.frame_1()
        public.bill_add()
        time.sleep(1)

    @tag(Tag.SMOKE)
    def test_bill_biaotou_user(self):
        """
        加工账册表头
        """
        print("=========表头==========")
        log.debug("=========表头==========")
        public = MachinDeclare(self.driver)
        public.frame_2()
        time.sleep(2)
        public.head_1("200")
        public.head_2("2019-12-31")
        public.head_3("无")
        public.save_btn()
        time.sleep(2)

    def test_liaojian_xinzeng_user(self):
        """
        账册表体料件新增
        """
        print("=======表体，料件新增=======")
        log.debug("=========表体，料件新增==========")
        public = MachinDeclare(self.driver)
        public.scroll()
        time.sleep(2)
        public.imgAdd()
        public.frame_3()
        public.body_1_1("z-001")
        public.body_1_2("1001")
        public.body_1_2_1()
        public.frame_4()
        time.sleep(1)
        public.body_1_2_3()
        public.body_1_2_2()
        public.exit_frame_public()
        public.body_1_3("zs")
        public.body_1_4("人民币")
        public.body_1_5("10")
        public.body_1_6("5000")
        public.body_1_7("全免")
        public.body_1_8("无")
        public.body_1_9() #点击“暂存”
        time.sleep(2)
        public.body_1_10() #点击“返回”
        public.exit_frame_public()
        time.sleep(1)

    def test_liaojian_daoru_user(self):
        """
        账册表体料件导入
        """
        print("=========表体，料件导入==========")
        log.debug("=========表体，料件导入==========")
        public = MachinDeclare(self.driver)
        public.scroll()
        public.imgImport()
        time.sleep(2)
        public.frame_5()
        time.sleep(1)
        #定位到选择按钮，直接给出导入文档的路径
        self.driver.find_element_by_name("import").send_keys(file_import_dir+"账册_料件导入格式.xlsx")
        time.sleep(2)
        public.img_import_2()
        time.sleep(2)
        public.exit_frame_public()
        time.sleep(1)

    def test_chengpin_xinzeng_user(self):
        """
        账册表体成品新增
        """
        print("=========表体，成品新增==========")
        log.debug("=========表体，成品新增==========")
        public = MachinDeclare(self.driver)
        public.scroll()
        public.body_2()
        time.sleep(1)
        public.exgAdd()
        time.sleep(1)
        public.frame_3()
        public.body_1_1("c-001")
        public.body_1_2("1001")
        public.body_1_2_1()
        public.frame_4()
        time.sleep(1)
        public.body_1_2_2()
        public.exit_frame_public()
        public.body_1_3("zs")
        public.body_1_4("人民币")
        public.body_1_5("10")
        public.body_1_6("5000")
        public.body_1_7("全免")
        public.body_1_8("无")
        public.body_1_9() #点击暂存
        time.sleep(2)
        public.body_1_10() #点击返回
        public.exit_frame_public()
        time.sleep(1)

    def test_chengpin_daoru_user(self):
        """
        账册表体成品导入
        """
        print("=========表体，成品导入==========")
        log.debug("=========表体，成品导入==========")
        public = MachinDeclare(self.driver)
        public.scroll()
        public.body_2()
        time.sleep(2)
        public.exgImport()
        time.sleep(1)
        public.frame_5()
        # public.exg_import_1()
        # public.exg_import_2()
        time.sleep(1)
        #定位到选择按钮，直接给出导入文档的路径
        self.driver.find_element_by_name("import").send_keys(file_import_dir+"账册_成品导入格式.xlsx")
        time.sleep(2)
        public.img_import_2()
        time.sleep(2)
        public.exit_frame_public()
        time.sleep(1)

    def test_danhao_xinzeng_user(self):
        """
        账册表体单损耗新增
        """
        print("=========表体，单耗新增==========")
        log.debug("=========表体，单耗新增==========")
        public = MachinDeclare(self.driver)
        public.scroll()
        public.body_3()
        time.sleep(1)
        public.bomAdd()
        time.sleep(1)
        public.frame_3()
        public.body_3_1("1")
        public.body_3_1_1()
        public.body_3_2("1")
        public.body_3_2_1()
        public.body_3_3("1.0")
        public.body_3_4("2")
        public.body_3_5("20")
        public.body_3_6("30")
        public.body_3_7()
        public.body_3_7_1("2019-01-01")
        public.body_3_8("无")
        public.body_1_9() #点击暂存
        time.sleep(2)
        public.body_1_10() #点击返回
        public.exit_frame_public()
        time.sleep(1)

    def test_danhao_daoru_user(self):
        """
        账册表体单损耗导入
        """
        print("=========表体，单耗导入==========")
        log.debug("=========表体，单耗导入==========")
        public = MachinDeclare(self.driver)
        public.scroll()
        public.body_3()
        time.sleep(2)
        public.bomImport()
        time.sleep(1)
        public.frame_5()
        # public.bom_import_1()
        # public.bom_import_2()
        time.sleep(1)
        #定位到选择按钮，直接给出导入文档的路径
        self.driver.find_element_by_name("import").send_keys(file_import_dir+"账册_单损耗导入格式.xlsx")
        time.sleep(2)
        public.img_import_2()
        time.sleep(2)
        public.exit_frame_public()
        time.sleep(1)

    # def test_SuiFuDanZheng_user(self):
    #     """
    #     随附单证
    #     """
    #     print("=========随附单证==========")
    #     log.debug("=========随附单证==========")
    #     public = MachinDeclare(self.driver)
    #     public.scroll_file()
    #     public.flie_btn() # 点击随附单证下拉【v】
    #     public.file_Add() # 点击新增
    #     time.sleep(1)
    #     public.frame_3()
    #     time.sleep(1)
    #     public.file_2("文件")
    #     public.file_3("1.1")
    #     public.file_4("1.2")
    #     public.file_5("无")
    #     # public.file_6() # 导入附件
    #     # public.file_7() # 点击上传
    #     self.driver.find_element_by_name("file").send_keys(file_import_dir+"随附单证.pdf")
    #     time.sleep(1)
    #     public.file_7() # 点击上传
    #     time.sleep(1)
    #     public.fil_save()
    #     time.sleep(1)
    #     public.exit_frame_public()
    #     time.sleep(1)
    # #     public.declare()
    # #     time.sleep(3)

    @data({"str1":"文件","str2":1.1,"str3":1.2,"str4":"无"},{"str1":"减免税证明","str2":1,"str3":2,"str4":"有"},unpack=False)
    def test_SuiFuDanZheng_user(self,dict):
        """
        随附单证
        """
        print("=========随附单证==========")
        log.debug("=========随附单证==========")
        public = MachinDeclare(self.driver)
        public.scroll_file()
        if "{}".format(dict["str1"]) == "文件":
            public.flie_btn() # 点击随附单证下拉【v】
        public.file_Add() # 点击新增
        time.sleep(1)
        public.frame_3()
        time.sleep(1)
        # public.file_2("文件")
        Select(self.driver.find_element_by_id("acmpFormTypecd")).select_by_visible_text("{}".format(dict['str1']))
        # public.file_3("1.1")
        self.driver.find_element_by_xpath(".//*[@id='acmpFormNo']").send_keys("{}".format(dict['str2']))
        # public.file_4("1.2")
        self.driver.find_element_by_xpath(".//*[@id='fixdNo']").send_keys("{}".format(dict['str3']))
        # public.file_5("无")
        self.driver.find_element_by_xpath(".//*[@id='rmk']").send_keys("{}".format(dict['str4']))
        self.driver.find_element_by_name("file").send_keys(file_import_dir+"随附单证.pdf")
        time.sleep(1)
        public.file_7() # 点击上传
        time.sleep(1)
        public.fil_save()
        time.sleep(1)
        public.exit_frame_public()
        time.sleep(1)
        if "{}".format(dict["str1"]) == "减免税证明":
            public.declare()
            time.sleep(3)

if __name__ == '__main__':
    #unittest.main(verbosity=2)
    suite = unittest.TestSuite()
    suite.addTest(TestMachinList("test_SuiFuDanZheng_user"))

    runer=unittest.TextTestRunner()
    runer.run(suite)

