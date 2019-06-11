from framework.base_page import BasePage
import random
import datetime
from selenium.webdriver.common.keys import Keys

date = datetime.datetime.now()+datetime.timedelta(days=20)  # 获取系统日期+20天
manual_type = ("来料加工", "进料加工", "设备手册")  # 手册类型

"""
    def add_start(self):
        try:
            tr_number = (2, 4, 6)
            for s in tr_number:
                if s == 2:
                    # 第一列必须项字段非空校对
                    tr_numbers = (6, 7, 9)  # 表头第一列必须项字段可以编辑的位置
                    for i in tr_numbers:
                        driver.find_element_by_xpath(".//*[@id='dataForm']/table/tbody/tr[" + str(i) + "]/td["
                                                     + str(s) + "]/div/span/span[1]/span").click()
                        driver.find_element_by_xpath("html/body/span/span/span[1]/input").send_keys(random.randint(1, 10))
                        driver.find_element_by_xpath("html/body/span/span/span[1]/input").send_keys(Keys.ENTER)
                    driver.find_element_by_xpath(".//*[@id='validDate']").send_keys(date.strftime('%Y-%m-%d'))
                    driver.find_element_by_xpath(".//*[@id='validDate']").send_keys(Keys.ENTER)  # 有效期
                    driver.find_element_by_xpath(".//*[@id='etpsContactEr']").send_keys("李四")
                    driver.find_element_by_xpath(".//*[@id='validDate']").send_keys(Keys.ENTER)  # 企业联系人
                if s == 4:
                    # 第二列必须项字段非空校对
                    tr_numbers = (2, 8, 9)  # 表头第二列必须项字段可以编辑的位置
                    for i in tr_numbers:
                        driver.find_element_by_xpath(".//*[@id='dataForm']/table/tbody/tr[" + str(i) + "]/td["
                                                     + str(s) + "]/div/span/span[1]/span").click()
                        if tr_numbers ==2:
                            driver.find_element_by_xpath("html/body/span/span/span[1]/input").send_keys(
                                random.choice(manual_type))
                        else:
                            driver.find_element_by_xpath("html/body/span/span/span[1]/input").send_keys(
                                random.randint(1, 10))
                        driver.find_element_by_xpath("html/body/span/span/span[1]/input").send_keys(Keys.ENTER)
                    driver.find_element_by_xpath(".//*[@id='linkmanTel']").send_keys("155000000")
                    driver.find_element_by_xpath(".//*[@id='validDate']").send_keys(Keys.ENTER)  # 联系人手机号
                if s == 6:
                    # 第三列必须项字段非空校对
                    tr_numbers = (8, 9)  # 表头第三列必须项字段可以编辑的位置
                    for i in tr_numbers:
                        driver.find_element_by_xpath(".//*[@id='dataForm']/table/tbody/tr[" + str(i) + "]/td["
                                                     + str(s) + "]/div/span/span[1]/span").click()
                        if tr_numbers ==2:
                            driver.find_element_by_xpath("html/body/span/span/span[1]/input").send_keys(
                                random.choice(manual_type))
                        else:
                            driver.find_element_by_xpath("html/body/span/span/span[1]/input").send_keys(
                                random.randint(1, 10))
                        driver.find_element_by_xpath("html/body/span/span/span[1]/input").send_keys(Keys.ENTER)
        except Exception as e:
            logger.info(format(e))
"""