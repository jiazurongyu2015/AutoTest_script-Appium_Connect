# coding=utf-8
from src.testcase.common.WidgetCheckUnit import *


class ToDevicePage(object):
    def __init__(self):
        self.driver = database["driver"]
        widget_check_unit = WidgetCheckUnit(self.driver)
        self.widget_click = widget_check_unit.widget_click
        self.wait_widget = widget_check_unit.wait_widget
        self.case()

    def case(self):
        # 用例动作
        while True:
            if self.driver.current_activity == login_popup["activity"][0]:
                if self.wait_widget(login_popup["title"], 3, 1):
                    logger.info(u"[APP_INF] 设备需要重新登陆")
                    self.widget_click(login_popup["title"],
                                      login_popup["confirm"],
                                      login_page["title"],
                                      1, 1, 1, 10, 0.5, 0)

            if self.driver.current_activity == device_page["activity"][0]:
                logger.info(u"[APP_INF] APP当前页面为设备主页面")
                break

            if self.driver.current_activity == login_page["activity"][0]:
                logger.info(u"[APP_INF] APP当前页面为登录页面")
                self.widget_click(login_page["title"],
                                  login_page["login_button"],
                                  device_page["title"],
                                  1, 1, 1, 10, 0.5, 0)
            return True
