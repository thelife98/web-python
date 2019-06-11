from testsuite.pagework.base_page import BasePage
import os
from testsuite.pagework.logger import Logger
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

logger = Logger(logger='TemsToInvPage').get_log()


# 加工，报告出入区的入区核注清单定位类
class TemsToInvPage(BasePage):
    """"-------- 以下是菜单的界面定位 --------"""
    # 报关出入区
    def menu_declare_customs(self):
        self.click("xpath=>.//*[@id='side-menu']/div[3]/ul/li[3]/a/span[1]")
        self.sleep(3)

    # 入区核注清单
    def menu_to_inv(self):
        self.click("xpath=>.//*[@id='side-menu']/div[3]/ul/li[3]/ul/li[1]/a")
        self.sleep(3)

    """-------- 以下是frame框架的界面定位 --------"""

    # 进入一级frame
    def frame_1(self):
        self.get_frame('selector_selector=>iframe[style="width:100%;height:100%;z-index:1;"]')
        self.sleep(2)

    # 进入二级frame
    def frame_2(self):
        self.get_frame_1_1("editIframe")
        self.sleep(2)

    # 进三级frame
    def frame_3(self):
        self.get_frame("selector_selector=>.layui-layer-iframe iframe")
        self.sleep(2)

    # 点击新增按钮
    def add(self):
        self.click("xpath=>.//*[@id='add']")
        self.sleep(2)

    """-------- 以下是单据表头的界面定位 --------"""

    # 新增手(账)册编号
    def sno(self, text):
        self.select_value("id=>putrecNo", text)
        self.sleep(2)

    # 新增料件、成品标志
    def material_goods_marking (self, text):
        self.select_value("id=>mtpckEndprdMarkcd", text)
        self.sleep(2)

    # 新增监管方式
    def supervise(self, text):
        self.select_value("id=>supvModecd", text)
        self.sleep(2)

    # 新增运输方式
    def transport(self, text):
        self.select_value("id=>trspModecd", text)
        self.sleep(2)

    # 新增进（出）口口岸
    def head_5(self, text):
        self.select_value("id=>impexpPortcd", text)
        self.sleep(2)

    # 新增起运运抵国别
    def head_6(self, text):
        self.select_value("id=>natcd", text)
        self.sleep(2)

    # 新增毛重
    def head_7(self, text):
        self.type("xpath=>.//*[@id='grossWt']", text)
        self.sleep(2)

    # 新增净重
    def head_8(self, text):
        self.type("xpath=>.//*[@id='netWt']", text)
        self.sleep(2)

    # 新增包装种类
    def head_9(self, text):
        self.select_value("id=>packType", text)
        self.sleep(2)

    # 新增报关标志
    def head_10(self, text):
        self.select_value("id=>dclcusFlag", text)
        self.sleep(2)

    # 新增备注
    def head_11(self, text):
        self.type("xpath=>.//*[@id='rmk']", text)

    # 暂存
    def save_btn(self):
        self.click("xpath=>.//*[@id='save']")
        self.sleep(3)

    # 拉滚动
    def scroll(self):
        self.get_scroll("xpath=>.//*[@id='imgHead']/a")
        self.sleep(3)

    """ --- 表体清单商品操作 ---"""
    # 新增按钮
    def img_add(self):
        self.click("xpath=>.//*[@id='imgadd']")
        self.sleep(2)

    # 进入三级frame
    def frame_3(self):
        self.get_frame("selector_selector=>.layui-layer-iframe iframe")
        self.sleep(2)

    # 新增确认
    def from_1(self):
        self.click("xpath=>.//*[@id='ok']")
        self.sleep(2)

    # 进入四级frame
    def frame_4(self):
        self.get_frame('selector_selector=>iframe[style="height: 458px;"]')
        self.sleep(2)

    # 清空申报数量
    def body_1(self):
        self.clear("xpath=>.//*[@id='dclQty']")
        self.sleep(2)

    # 新增申报数量
    def body_1_1(self, text):
        self.type("xpath=>.//*[@id='dclQty']", text)
        self.sleep(2)

    def body_1_2(self):
        self.enter("xpath=>.//*[@id='dclQty']")

    # 新增原产国/目的国
    def body_2(self, text):
        self.select_value("id=>natcd", text)
        self.sleep(2)

    # 新增净重
    def body_3(self, text):
        self.type("xpath=>.//*[@id='netWt']", text)
        self.sleep(2)

    # 最终目的国(地区)
    def body_4(self, text):
        self.select_value("id=>destinationNatcd", text)
        self.sleep(2)

    # 征减免方式
    def body_5(self, text):
        self.select_value("id=>lvyrlfModecd", text)
        self.sleep(2)

    # 退出frame框架
    def exit_frame_public(self):
        self.exit_frame()
        self.sleep(3)

    # 点击返回
    def from_2(self):
        print("11111111")
        try:
            self.click("xpath=>.//*[@id='cancel']")
        except Exception as e:
            WebDriverWait(self.driver, 20).until(
                expected_conditions.presence_of_element_located((By.XPATH, ".//*[@id='cancel']")))
            self.click("xpath=>.//*[@id='cancel']")
            self.sleep(10)
            print("11111111")
        print("11111111")

    """ --- 表体清单商导入 ---"""

    # 点击清单商品导入
    def imgImport(self):
        self.click("xpath=>.//*[@id='imgImport']")
        self.sleep(5)

    # 点击清单商品选择
    def img_import_1(self):
        self.click("class_name=>input-group-btn")
        self.sleep(2)
        try:
            os.system("F:\\bls_file_import\\machin_to_inv_img.exe")
            logger.info("文件导入成功")
        except Exception as e:
            logger.error(format(e))
        self.sleep(3)

    # 点击清单商品上传
    def img_import_2(self):
        self.click("xpath=>html/body/div[1]/div/div[3]/div[2]/a/i")
        self.sleep(3)

    # 点击随附单证下拉
    def flie_btn(self):
        self.click("xpath=>html/body/div/div[3]/div[1]/div/a/i")
        self.sleep(3)

    # 点击新增
    def file_Add(self):
        self.click("xpath=>.//*[@id='fileAdd']")
        self.sleep(2)

    # 新增随附单证序号
    def file_1(self, text):
        self.type("xpath=>.//*[@id='acmpFormSeqno']", text)
        self.sleep(2)

    # 新增随附单证类型
    def file_2(self, text):
        self.select_value("id=>acmpFormTypecd", text)
        self.sleep(2)

    # 新增随附单证编号
    def file_3(self, text):
        self.type("xpath=>.//*[@id='acmpFormNo']", text)
        self.sleep(2)

    # 新增固定编号
    def file_4(self, text):
        self.type("xpath=>.//*[@id='fixdNo']", text)

    # 新增备注
    def file_5(self, text):
        self.type("xpath=>.//*[@id='rmk']", text)

    # 导入附件
    def file_6(self):
        self.click("class_name=>input-group-btn")
        self.sleep(2)
        try:
            os.system("F:\\bls_file_import\\documents_import.exe")
            logger.info("文件导入成功")
        except Exception as e:
            logger.error(format(e))
        self.sleep(3)

    # 点击上传
    def file_7(self):
        self.click("xpath=>.//*[@id='head']/div[4]/div/div[3]/div[2]/a/span")
        self.sleep(3)

    # 点击暂存
    def fil_save(self):
        self.click("xpath=>.//*[@id='save']")
        self.sleep(4)

    # 退出二级frame框架
    def exit_frame_1(self):
        self.exit_frame()
        self.sleep(2)

    # 点击申报
    def declare(self):
        self.click("xpath=>.//*[@id='declare']")
        self.sleep(2)





