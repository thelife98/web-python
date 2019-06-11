from testsuite.pagework.base_page import BasePage
import os
from testsuite.pagework.logger import Logger
logger = Logger(logger='TempAppFormPage').get_log()

"""
此文件为临时出入区申请表定位类
类名注释：Temp为临时英文缩写，ApplForm为申请表英文缩写，Page为界面
"""


class TempAppFormPage(BasePage):
    # 临时出入区
    def menu_temp(self):
        self.click("xpath=>.//*[@id='side-menu']/div[3]/ul/li[4]/a/span[1]")
        self.sleep(3)

    # 临时出入区申请表
    def menu_app(self):
        self.click("xpath=>.//*[@id='side-menu']/div[3]/ul/li[4]/ul/li[1]/a")
        self.sleep(2)

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

    # 点击表体新增
    def add(self):
        self.click("xpath=>.//*[@id='add']")
        self.sleep(2)

    # 点击确认
    def affirm(self):
        self.click("xpath=>.//*[@id='affirm']")
        self.sleep(2)

    # 点击暂存
    def save(self):
        self.click("xpath=>.//*[@id='save']")
        self.sleep(2)

    # 新增备注
    def rmk(self, text):
        self.type("xpath=>.//*[@id='rmk']", text)

    # 新增商品备注
    def gds_rmk(self, text):
        self.type("xpath=>.//*[@id='gdsRmk']", text)

    # 点击申报
    def declare(self):
        self.click("xpath=>.//*[@id='declare']")
        self.sleep(2)

    # 区内账册编号
    def select_no(self, text):
        self.select_value("id=>areainOriactNo", text)
        self.sleep(2)

    # 业务类型选择
    def business_type_cd(self, text):
        self.select_value("id=>businessTypecd", text)
        self.sleep(2)

    # 区内企业编号
    def area_out_etp_sno(self, text):
        self.type("xpath=>.//*[@id='areaoutEtpsno']", text)

    # 有效日期
    def valid_time(self, text):
        self.type("xpath=>.//*[@id='validTime']", text)

    # 展示地
    def exhibition_place(self, text):
        self.type("xpath=>.//*[@id='exhibitionPlace']", text)

    # 拉滚动
    def scroll(self):
        self.get_scroll("xpath=>html/body/header/div/div[2]/div[1]/h4")
        self.sleep(3)

    # 数量
    def dcl_qty(self, text):
        self.type("xpath=>.//*[@id='dclQty']", text)

    # 申报单价
    def dcl_uprc_amt(self, text):
        self.type("xpath=>.//*[@id='dclUprcAmt']", text)

    # 商品标记
    def gds_mark_cd(self, text):
        self.select_value("id=>gdsMarkcd", text)
        self.sleep(2)