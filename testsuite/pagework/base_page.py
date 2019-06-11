# coding=utf-8
from testsuite.pagework.logger import Logger
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import os.path
import time
import xlrd

# 创建日志实例
logger = Logger(logger='BasePage').get_log()


class BasePage(object):
    """
    定义一个页面基类，让所有页面都继承这个类，封装一些常用的页面操作方法到这个类
    """
    def __init__(self, driver):
        self.driver = driver

    def quit_browser(self):
        self.driver.quit()

    def forward(self):
        self.driver.forward()
        logger.info("浏览器前进操作")

    def back(self):
        self.driver.back()
        logger.info("浏览器后退操作")

    # 隐式等待
    def wait(self, seconds):
        self.driver.implicitly_wait(seconds)
        logger.info("隐式等待 %d 秒." % seconds)

    # 关闭当前窗口
    def close(self):
        try:
            self.driver.close()
            logger.info("关闭和退出浏览器.")
        except NameError as e:
            logger.error("退出浏览器失败: %s" % e)

    # 截图
    def get_windows_img(self):
        file_path = os.path.dirname(os.getcwd()) + '/screenshot/'
        rq = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        try:
            time.sleep(1)
            self.driver.get_screenshot_as_file(screen_name)
            logger.info("开始截图并保存")
        except Exception as e:
            logger.error("出现异常", format(e))
            self.get_windows_img()

    # 六大元素定位(单个元素)
    def find_element(self, selector):
        element = ' '
        # 如果没有=>符号，就进行id的定位元素
        if '=>' not in selector:
            return self.driver.find_element_by_id(selector)
        selector_by = selector.split('=>')[0]  # 定义selector_by变量，获取=>符号左边的内容
        selector_value = selector.split('=>')[1]  # 定义selector_value变量，获取=>符号右边的内容

        if selector_by == "i" or selector_by == "id":
            try:
                element = self.driver.find_element_by_id(selector_value)
                # logger.info("已找到元素 \' %s \' 成功, 通过 %s 找到值: %s " % (element.text, selector_by, selector_value))
                logger.info("已找到元素成功, 通过 %s 找到值: %s " % (selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error("未找到元素异常: %s" % e)
                self.get_windows_img()  # 开始截图
        elif selector_by == "n" or selector_by == "name":
                element = self.driver.find_element_by_name(selector_value)
        elif selector_by == "c" or selector_by == "class_name":
            element = self.driver.find_element_by_class_name(selector_value)
        elif selector_by == "l" or selector_by == "link_text":
            element = self.driver.find_element_by_link_text(selector_value)
        elif selector_by == "p" or selector_by == 'partial_link_text':
            element = self.driver.find_element_by_partial_link_text(selector_value)
        elif selector_by == "t" or selector_by == 'tag_name':
            element = self.driver.find_element_by_tag_name(selector_value)
        elif selector_by == "x" or selector_by == 'xpath':
            try:
                element = self.driver.find_element_by_xpath(selector_value)
                # logger.info("已找到元素 \' %s \' 成功, 通过 %s 找到值: %s " % (element.text, selector_by, selector_value))
                logger.info("已找到元素成功, 通过 %s 找到值: %s " % (selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error("未找到元素异常: %s" % e)
                self.get_windows_img()
        elif selector_by == "s" or selector_by == 'selector_selector':
            try:
                element = self.driver.find_element_by_css_selector(selector_value)
                print(element)
                logger.info("已找到元素 \' %s \' 成功, 通过 %s 找到值: %s " % (element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error("未找到元素异常: %s" % e)
                self.get_windows_img()
        else:
            raise NameError("请输入有效类型的目标元素.")
        return element

    # 六大元素定位(多个元素)

    # 进入frame框架
    def get_frame(self, selector):
        el = self.find_element(selector)
        try:
            self.driver.switch_to.frame(el)
        except NameError as e:
            logger.info("找不到该i_frame框架 %s" % e)
            self.driver.switch_to.frame(el)

    # 进入frame框架
    def get_frame_1_1(self, x):
        try:
            self.driver.switch_to.frame(x)
        except NameError as e:
            logger.info("找不到该i_frame框架 %s" % e)
            self.driver.switch_to.frame(e)

    # 退出frame框架
    def exit_frame(self):
        self.driver.switch_to.parent_frame()
        logger.info("退回父iframe")

    #  输入文本
    def type(self, selector, text):
        el = self.find_element(selector)
        try:
            el.send_keys(text)
            logger.info("已输入 \' %s \' 在输入框" % text)
        except NameError as e:
            logger.error("在输入框中键入 %s 失败" % e)
            self.get_windows_img()

    # 回车
    def enter(self, selector):
        el = self.find_element(selector)
        try:
            el.send_keys(Keys.ENTER)
            logger.info("回车操作成功")
        except NameError as e:
            logger.error("回车操作失败")
            self.get_windows_img()

    # 清除文本框
    def clear(self, selector):
        el = self.find_element(selector)
        try:
            el.clear()
            logger.info("Clear text in input box before typing.")
        except NameError as e:
            logger.error("Failed to clear in input box with %s" % e)
            self.get_windows_img()

    # 点击元素
    def click(self, selector):
        el = self.find_element(selector)
        try:
            el.click()
            logger.info("The element \' %s \' was clicked." % el.text)
        except NameError as e:
            logger.error("Failed to click the element with %s" % e)

    # 获得网页标题
    def get_page_title(self):
        logger.info("Current page title is %s" % self.driver.title)
        return self.driver.title

    # 获得弹窗信息
    def get_alert_text(self):
        logger.info("这个弹窗的信息为 %s" % self.driver.switch_to_alert().text())
        return self.driver.title

    # 通过元素定位拉滚动
    def get_scroll(self, selector):
        el = self.find_element(selector)
        try:
            self.driver.execute_script("arguments[0].scrollIntoView();", el)
        except NameError as e:
            logger.info("找不到该元素 %s" % e)
            self.driver.switch_to.frame(el)

    # 刷新
    def refresh(self):
        self.driver.refresh()

    # 下拉框赋值
    def select_value(self, selector, text):
        el = Select(self.find_element(selector))
        try:
            el.select_by_visible_text(text)
            logger.info("已输入 \' %s \' 在输入框" % el.select_by_visible_text(text))
        except NameError as e:
            logger.error("在输入框中键入 %s 失败" % e)
            self.get_windows_img()


    # 根据索引获取元素列表中的元素

    # 获取列表中的记录数

    # 断言数据库查询

    # 断言新增记录的数据库查询

    # 断言提示语与预期的一致

    # 断言两个字符串是否一致

    # 根据关键字获取UiLibrary中封装的元素位置信息

    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)
        logger.info("Sleep for %d seconds" % seconds)


class OfferPage(object):
    # 根据索引获取Excel表格中的数据 参数:file：Excel文件路径 colnameindex：表头列名所在行的所以 ，by_index：表的索引
    def excel_table_byindex(self, file='file.xls', colnameindex=0, by_index=0):
        data = xlrd.open_workbook(file)
        table = data.sheets()[by_index]
        nrows = table.nrows  # 行数
        colnames = table.row_values(colnameindex)  # 某一行数据
        list = []
        for rownum in range(1, nrows):
            row = table.row_values(rownum)
            if row:
                app = {}
                for i in range(len(colnames)):
                    app[colnames[i]] = row[i]
                    list.append(app)
        return list

