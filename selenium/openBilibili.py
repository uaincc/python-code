#!/usr/bin/env/ python3

"""
Python Selenium是一个用于测试网站的自动化测试工具，支持各种浏览器包括Chrome、Firefox、Safari等主流界面浏览器，同时也支持phantomJS无界面浏览器。
msedgedriver.exe 需要对应 Windows Edge版本
同理Chrome版本也需要对应chromedriver.eve

依赖模块
pip install selenium
"""

from selenium.webdriver.edge.service import Service
from selenium import webdriver
import time

while True:
    edgedriver_path = "./msedgedriver.exe"  # 此外为EdgeDriver驱动路径
    edge_options = webdriver.EdgeOptions()
    # edge_options.headless = True
    # edge_options.add_argument('--headless')
    browser = webdriver.Edge(service=Service(edgedriver_path), options=edge_options)
    browser.delete_all_cookies()  # 删除cookie
    browser.get("https://www.bilibili.com/video/BV1CQ4y1L7Az/?spm_id_from=333.999.0.0")  # 视频地址
    # element = WebDriverWait(browser, 15).until(  # 等待播放按钮能够被加载并且能够被点击，15s后如果还没加载完成并且不满足被点击的条件，就抛出异常
    #     EC.element_to_be_clickable((By.XPATH, '//*[@id="bilibiliPlayer"]/div[1]/div[1]/div[8]/video'))
    # )
    # element.click()
    print(browser.get_cookies())
    time.sleep(100)  # 等待时常
    browser.quit()
