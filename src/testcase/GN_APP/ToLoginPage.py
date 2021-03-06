# coding=utf-8
import os

from src.common.WidgetCheckUnit import *


class ToLoginPage(object):
    def __init__(self, driver, device_info):
        self.driver = driver
        self.page = device_info["page"]  # 页面元素库
        self.debug = device_info["debug"]  # debug日志
        self.ac = device_info["ac"]  # appium command
        self.basename = os.path.basename(__file__).split(".")[0]
        widget_check_unit = WidgetCheckUnit(driver, device_info)
        self.widget_click = widget_check_unit.widget_click
        self.wait_widget = widget_check_unit.wait_widget
        self.case()

    # 检查APP是否升级，取消
    def check_update(self):
        try:
            self.wait_widget(self.page["update_popup"]["title"])
            self.debug.info(u"[APP_INF] APP有最新版本，可以更新")
            self.widget_click(self.page["update_popup"]["cancel"],
                              log_record=0)
            self.debug.info(u"[APP_INF] 取消更新")
        except TimeoutException:
            pass

    # 账户异地登录弹窗，确定跳过
    def login_abnormal(self):
        try:
            self.wait_widget(self.page["login_popup"]["title"])
            self.debug.info(u"[APP_INF] APP需要重新登陆，等待重新登录")
            self.widget_click(self.page["login_popup"]["confirm"],
                              self.page["login_page"]["title"],
                              log_record=0)
        except TimeoutException:
            pass

    # 退出登录至登录界面
    def device_to_login(self):
        self.wait_widget(self.page["device_page"]["title"])
        self.debug.info(u"[APP_INF] APP当前页面为主页面,等待退出")
        try:
            self.widget_click(self.page["device_page"]["user_image"],
                              self.page["personal_settings_page"]["title"],
                              log_record=0)

            self.widget_click(self.page["personal_settings_page"]["account_setting"],
                              self.page["account_setting_page"]["title"],
                              log_record=0)

            self.widget_click(self.page["account_setting_page"]["logout"],
                              self.page["logout_popup"]["title"],
                              log_record=0)

            self.widget_click(self.page["logout_popup"]["confirm"],
                              self.page["login_page"]["title"],
                              log_record=0)
        except TimeoutException:
            self.debug.info(u"[APP_INF] APP进入登录页面失败")
            self.driver.close_app()
            self.debug.warn("(%s)self.driver.close_app() App closed" % self.basename)
            raise TimeoutException("ToLoginPage Error!")

    # 用例动作
    def case(self):
        self.check_update()
        self.login_abnormal()
        self.device_to_login()
        self.wait_widget(self.page["login_page"]["title"])
        self.debug.info(u"[APP_INF] APP当前页面为登录页面")
