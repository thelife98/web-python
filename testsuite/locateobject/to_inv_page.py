from testsuite.pagework.base_page import BasePage
import os
from testsuite.pagework.logger import Logger

logger = Logger(logger='ToInvPage').get_log()


# 入区核注清单定位类
class ToInvPage(BasePage):
    # 物流菜单
    def click_assembly(self):
        self.click("xpath=>.//*[@id='BLS-BWS']/span")
        self.sleep(3)

    # 报关出入区
    def menu_2(self):
        self.click("xpath=>.//*[@id='side-menu']/div[3]/ul/li[2]/a/span[1]")
        self.sleep(3)

    # 入区核注清单
    def submenu_2(self):
        self.click("xpath=>.//*[@id='side-menu']/div[3]/ul/li[2]/ul/li[1]/a")
        self.sleep(2)

    # 进入一级frame
    def frame_2_1(self):
        self.get_frame('selector_selector=>iframe[style="width:100%;height:100%;z-index:1;"]')
        self.sleep(2)

    # 新增按钮
    def bill_add(self):
        self.click("xpath=>.//*[@id='add']")
        self.sleep(2)

    # 进入二级frame
    def frame_2(self):
        self.get_frame_1_1("editIframe")
        self.sleep(2)

    # 新增区域场所类别
    def head_1(self, text):
        self.select_value("id=>bwlTypecd", text)
        self.sleep(2)

    # 新增企业类型
    def head_2(self, text):
        self.select_value("id=>houseTypecd", text)
        self.sleep(2)

    # 新增记账模式
    def head_3(self, text):
        self.select_value("id=>appendTypecd", text)
        self.sleep(2)

    # 新增仓库地址
    def head_4(self, text):
        self.type("xpath=>.//*[@id='houseAddress']", text)

    # 新增仓库面积(m²)
    def head_5(self, text):
        self.type("xpath=>.//*[@id='houseArea']", text)

    # 新增仓库容积(m³)
    def head_6(self, text):
        self.type("xpath=>.//*[@id='houseVolume']", text)

    # 新增结束有效日期
    def head_7(self, text):
        self.type("xpath=>.//*[@id='finishValidDate']", text)

    # 新增备注
    def head_8(self, text):
        self.type("xpath=>.//*[@id='rmk']", text)

    # 暂存
    def save_btn(self):
        self.click("xpath=>.//*[@id='save']")
        self.sleep(3)

    # 拉滚动
    def scroll(self):
        self.get_scroll("xpath=>html/body/div/div[3]/div[1]/h4")
        self.sleep(3)

    # 点击随附单证下拉
    def flie_btn(self):
        self.click("xpath=>html/body/div/div[3]/div[1]/div/a/i")
        self.sleep(3)

    # 点击新增
    def file_Add(self):
        self.click("xpath=>.//*[@id='fileAdd']")
        self.sleep(2)

    # 进入二级frame
    def frame_3(self):
        self.get_frame("selector_selector=>.layui-layer-iframe iframe")
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