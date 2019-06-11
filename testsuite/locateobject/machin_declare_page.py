from testsuite.pagework.base_page import BasePage
import os
from testsuite.pagework.logger import Logger
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

logger = Logger(logger='MachinDeclare').get_log()


# 加工账册定位类
class MachinDeclare(BasePage):
    # 加工
    def side_menu(self):
        self.click("xpath=>.//*[@id='app']/div/div/div[1]/div[1]/div/div/ul/div/li[4]/div")
        self.wait(3)

    # 加工账册
    def side_menu_1(self):
        self.click("xpath=>.//*[@id='app']/div/div/div[1]/div[1]/div[1]/div/ul/div/li[4]/ul/div[1]/li/div/span")
        self.wait(3)

    # 加工账册申报
    def side_menu_1_1(self):
        self.click("xpath=>.//*[@id='app']/div/div/div[1]/div[1]/div[1]/div/ul/div/li[4]/ul/div[1]/li/ul/a[1]/li/span")
        self.wait(2)

    # 进入一级frame
    def frame_1(self):
        self.get_frame('selector_selector=>#BLS-TEMS1008100180')
        self.wait(2)

    # 新增按钮
    def bill_add(self):
        self.click("xpath=>.//*[@id='add']")
        self.wait(2)

    # 进入二级frame
    def frame_2(self):
        self.get_frame_1_1("editIframe")
        self.wait(2)

    # 新增最大周转金额（万美元）
    def head_1(self, text):
        self.type("xpath=>.//*[@id='maxTovrAmt']", text)

    # 新增账册结束有效日期
    def head_2(self, text):
        self.type("xpath=>.//*[@id='finishValidDate']", text)

    # 新增备注
    def head_3(self, text):
        self.type("xpath=>.//*[@id='rmk']", text)

    # 暂存
    def save_btn(self):
        self.click("xpath=>.//*[@id='save']")
        self.wait(10)

    """-------- 以下是料件、成品分页卡的界面定位 --------"""

    # 拉滚动
    def scroll(self):
        self.get_scroll("xpath=>.//*[@id='tab']/li[1]/a")
        self.wait(3)

    # 点击新增
    def imgAdd(self):
        self.click("xpath=>.//*[@id='imgAdd']")
        self.wait(3)

    # 进入三级frame--加工账册料件点击"新增"
    def frame_3(self):
        self.get_frame('selector_selector=>iframe[style="height: 478px;"]')
        self.wait(2)

    # 新增料件
    def body_1_1(self, text):
        self.type("xpath=>.//*[@id='gdsMtno']", text)
        self.wait(2)

    # 新增商品编码
    def body_1_2(self, text):
        self.type("xpath=>.//*[@id='gdecd']", text)
        self.wait(3)

    # 新增商品编码回车
    def body_1_2_1(self):
        self.enter("xpath=>.//*[@id='gdecd']")

    # 进入四级frame--进入商品编码回车后的弹出框
    def frame_4(self):
        self.get_frame('selector_selector=>iframe[style="height: 408px;"]')
        self.wait(2)

    #选择商品编码回车后的弹出框的第一个圈
    def body_1_2_3(self):
        self.click("xpath=>.//*[@id='table']/tbody/tr[1]/td[1]/input")

    # 点击商品编码回车后的弹出框的确认按钮
    def body_1_2_2(self):
        self.enter("xpath=>.//*[@id='affirm']")

    # 进入五级frame--点击加工账册料件导入后的弹出框
    def frame_5(self):
        self.get_frame('selector_selector=>iframe[style="height: 408px;"]')
        #self.get_frame('selector_selector=>iframe#editIframe>html>body>div>div>iframe')
        self.wait(2)

    # 退出frame框架
    def exit_frame_public(self):
        self.exit_frame()
        self.wait(3)

    # 新增规格型号
    def body_1_3(self, text):
        self.type("xpath=>.//*[@id='endprdGdsSpcfModelDesc']", text)
        self.wait(3)

    # 新增币制
    def body_1_4(self, text):
        self.select_value("id=>dclCurrcd", text)
        self.wait(2)

    # 新增申报单价
    def body_1_5(self, text):
        self.type("xpath=>.//*[@id='dclUprcAmt']", text)
        self.wait(3)

    # 新增申报数量
    def body_1_6(self, text):
        self.type("xpath=>.//*[@id='dclQty']", text)
        self.wait(3)

    # 新增征免方式
    def body_1_7(self, text):
        self.select_value("id=>lvyrlfModecd", text)
        self.wait(2)

    # 新增备注
    def body_1_8(self, text):
        self.type("xpath=>.//*[@id='rmk']", text)
        self.wait(3)

    # 点击暂存
    def body_1_9(self):
        self.enter("xpath=>.//*[@id='save']")
        self.wait(3)

    # 点击返回
    def body_1_10(self):
        self.enter("xpath=>.//*[@id='reback']")
        self.wait(3)

    # 点击料件导入
    def imgImport(self):
        self.click("xpath=>.//*[@id='imgImport']")
        self.wait(5)

    # 点击料件选择
    def img_import_1(self):
        self.click("class_name=>input-group-btn")
        self.wait(2)
        try:
            rootpath = os.path.abspath('..')
            os.system(rootpath+r"\bls_file_import\machin_img_import.exe")
            logger.info("文件导入成功")
        except Exception as e:
            logger.error(format(e))
        self.wait(3)

    # 点击料件上传
    def img_import_2(self):
        self.click("xpath=>html/body/div[1]/div/div[3]/div[2]/a/span")
        self.wait(10)

    # 点击成品分页卡
    def body_2(self):
        self.click("xpath=>.//*[@id='tab']/li[2]/a")
        self.wait(3)

    # 点击新增成品
    def exgAdd(self):
        self.click("xpath=>.//*[@id='exgAdd']")
        self.wait(3)

    # 点击成品导入
    def exgImport(self):
        self.enter("xpath=>.//*[@id='exgImport']")
        self.wait(3)

    # 点击成品选择
    def exg_import_1(self):
        self.click("class_name=>input-group-btn")
        self.wait(2)
        try:
            os.system("D:\\bls\\bls_file_import\\machin_goods_import.exe")
            logger.info("文件导入成功")
        except Exception as e:
            logger.error(format(e))
        self.wait(3)

    # 点击成品上传
    def exg_import_2(self):
        self.click("xpath=>html/body/div[1]/div/div[3]/div[2]/a")
        self.wait(3)

    """-------- 以下是单耗分页卡的界面定位 --------"""

    # 点击单损耗分页卡
    def body_3(self):
        self.click("xpath=>.//*[@id='liBom']")
        self.wait(3)

    # 点击新增单损耗
    def bomAdd(self):
        self.click("xpath=>.//*[@id='bomAdd']")
        self.wait(3)

    # 新增成品序号
    def body_3_1(self, text):
        self.type("xpath=>.//*[@id='endprdSeqno']", text)
        self.wait(3)

    # 新增成品序号回车
    def body_3_1_1(self):
        self.enter("xpath=>.//*[@id='endprdSeqno']")
        self.wait(3)

    # 新增料件序号
    def body_3_2(self, text):
        self.type("xpath=>.//*[@id='mtpckSeqno']", text)
        self.wait(3)

    # 新增料件序号回车
    def body_3_2_1(self):
        self.enter("xpath=>.//*[@id='mtpckSeqno']")

    # 新增单耗版本号
    def body_3_3(self, text):
        self.type("xpath=>.//*[@id='ucnsVerno']", text)
        self.wait(3)

    # 新增净耗数量
    def body_3_4(self, text):
        self.type("xpath=>.//*[@id='netUseupQty']", text)
        self.wait(3)

    # 新增有形损耗率(%)
    def body_3_5(self, text):
        self.type("xpath=>.//*[@id='tgblLossRate']", text)
        self.wait(3)

    # 新增无形损耗率(%)
    def body_3_6(self, text):
        self.type("xpath=>.//*[@id='intgbLossRate']", text)
        self.wait(3)

    # 新增清空单耗有效日期
    def body_3_7(self):
        self.clear("xpath=>.//*[@id='ucnsValidDate']")
        self.wait(3)

    # 新增单耗有效日期
    def body_3_7_1(self, text):
        self.type("xpath=>.//*[@id='ucnsValidDate']", text)
        self.wait(3)

    # 新增备注
    def body_3_8(self, text):
        self.type("xpath=>.//*[@id='rmk']", text)
        self.wait(3)

    # 点击单耗导入
    def bomImport(self):
        self.click("xpath=>.//*[@id='bomImport']")
        self.wait(3)

    # 点击单耗选择
    def bom_import_1(self):
        self.click("class_name=>input-group-btn")
        self.wait(2)
        try:
            os.system("D:\\bls\\bls_file_import\\machin_bom_import.exe")
            logger.info("文件导入成功")
        except Exception as e:
            logger.error(format(e))
        self.wait(3)

    # 点击单耗上传
    def bom_import_2(self):
        self.click("xpath=>html/body/div[1]/div/div[3]/div[2]/a")
        self.wait(3)

    """-------- 以下是随附单证的界面定位 --------"""

    # 拉滚动到随附单证
    def scroll_file(self):
        self.get_scroll("xpath=>.//*[@id='file_ibox']/div[1]/h4")
        self.wait(3)

    # 点击随附单证下拉【v】
    def flie_btn(self):
        self.click("xpath=>.//*[@id='file_ibox']/div[1]/div/a/i")
        self.wait(3)

    # 点击新增
    def file_Add(self):
        self.click("xpath=>.//*[@id='fileAdd']")
        self.wait(2)

    # 新增随附单证类型
    def file_2(self, text):
        self.select_value("id=>acmpFormTypecd", text)
        self.wait(2)

    # 新增随附单证编号
    def file_3(self, text):
        self.type("xpath=>.//*[@id='acmpFormNo']", text)
        self.wait(2)

    # 新增固定编号
    def file_4(self, text):
        self.type("xpath=>.//*[@id='fixdNo']", text)

    # 新增备注
    def file_5(self, text):
        self.type("xpath=>.//*[@id='rmk']", text)

    # 导入附件
    def file_6(self):
        self.click("class_name=>input-group-btn")
        self.wait(2)
        try:
            os.system("D:\\bls\\bls_file_import\\documents_import.exe")
            logger.info("文件导入成功")
        except Exception as e:
            logger.error(format(e))
        self.wait(3)

    # 点击上传
    def file_7(self):
        self.click("xpath=>.//*[@id='head']/div[4]/div/div[3]/div[2]/a/span")
        self.wait(3)

    # 点击暂存
    def fil_save(self):
        self.click("xpath=>.//*[@id='save']")
        self.wait(4)

    # 退出二级frame框架
    def exit_frame_1(self):
        self.exit_frame()
        self.wait(2)

    # 点击申报
    def declare(self):
        self.click("xpath=>.//*[@id='declare']")
        self.wait(2)