from testsuite.pagework.base_page import BasePage
import os
from testsuite.pagework.logger import Logger

logger = Logger(logger='FilePage').get_log()


# 此文件为随附单证操作定位界面
class FilePage(BasePage):
    # 点击随附单证下拉
    def file_btn(self):
        self.click("xpath=>html/body/div/div[3]/div[1]/div/a/i")
        self.sleep(3)

    # 点击随附单证新增
    def file_add(self):
        self.click("xpath=>.//*[@id='fileAdd']")
        self.sleep(2)

    # 随附单证序号
    def seq_no(self, text):
        self.type("xpath=>.//*[@id='acmpFormSeqno']", text)
        self.sleep(2)

    # 随附单证类型
    def type_cd(self, text):
        self.select_value("id=>acmpFormTypecd", text)
        self.sleep(2)

    # 随附单证编号
    def form_no(self, text):
        self.type("xpath=>.//*[@id='acmpFormNo']", text)
        self.sleep(2)

    # 固定编号
    def fix_dno(self, text):
        self.type("xpath=>.//*[@id='fixdNo']", text)

    # 备注
    def rmk(self, text):
        self.type("xpath=>.//*[@id='rmk']", text)

    # 导入附件
    def documents_import(self):
        self.click("class_name=>input-group-btn")
        self.sleep(2)
        try:
            os.system("F:\\bls_file_import\\documents_import.exe")
            logger.info("文件导入成功")
        except Exception as e:
            logger.error(format(e))
        self.sleep(3)

    # 点击上传
    def upload(self):
        self.click("xpath=>.//*[@id='head']/div[4]/div/div[3]/div[2]/a/span")
        self.sleep(3)

    # 点击随附单证暂存
    def fil_save(self):
        self.click("xpath=>.//*[@id='save']")
        self.sleep(4)

    # 退出二级frame框架
    def exit_frame_1(self):
        self.exit_frame()
        self.sleep(2)