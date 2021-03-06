#!/user/bin/env python
# encoding: utf-8
"""
@author: zwnong
@project: HogwartsSDE17
@file: appo.py
@time: 2021/3/4 0:49
"""
import sys

sys.path.append('..')
from appium import webdriver
from app.appo.utli.get_file import GetFile
from ui_framework.base.base_page import BasePage
from app.appo.page.main_page import MainPage

get_datas = GetFile(r'../datas\caps.yaml')
desirecaps = get_datas.get_yaml_data('desirecaps')
IP = get_datas.get_yaml_data('server')['IP']
port = get_datas.get_yaml_data('server')['port']


class App(BasePage):

    # 复用driver 判断driver是否为None
    def start_android_driver(self):
        if self.driver is None:
            self.driver = webdriver.Remote(f"http://{IP}:{port}/wd/hub", desirecaps)
            self.driver.implicitly_wait(10)
        else:
            self.driver.launch_app()
        return self

    def restart_android_driver(self):
        """
        # 重启
        :return:
        """
        self.driver.close()
        self.driver.launch_app()

    def stop_android_driver(self):
        self.driver.quit()

    def start_ios_driver(self):
        pass

    def goto_main_page(self):
        return MainPage(self.driver)

    def page_source(self):
        return self.driver.page_source

    def implicitly_wait(self, time):
        return self.driver.implicitly_wait(time)
