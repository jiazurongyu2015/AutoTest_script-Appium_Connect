# coding=utf-8
from src.testcase.case.LaunchApp import *


class GNAppAccountSettings5(LaunchApp):
    def run(self):
        self.case_module = u"账户设置"  # 用例所属模块
        self.case_title = u'密码修改页面，旧密码输入错误，提示信息检查'  # 用例名称
        self.zentao_id = 1970  # 禅道ID
        self.basename = os.path.basename(__file__).split(".")[0]  # 获取用例的文件名称:GNAPP_ACCOUNT_SETTINGS_005
        self.logger.info('[GN_INF] <current case> [CASE_ID="%s", CASE_NAME="%s", 禅道ID="%s", CASE_MODULE="%s"]'
                         % (self.basename, self.case_title, self.zentao_id, self.case_module))  # 记录log

        try:
            self.launch_app(False)  # 启动APP
            self.case()
        except BaseException:
            self.debug.error(traceback.format_exc())  # Message: ***
            self.case_over("unknown")

    # 用例动作
    def case(self):
        try:
            self.widget_click(self.page["device_page"]["title"],
                              self.page["device_page"]["user_image"],
                              self.page["personal_settings_page"]["title"],
                              1, 1, 1, 10, 0.5)

            self.widget_click(self.page["personal_settings_page"]["title"],
                              self.page["personal_settings_page"]["account_setting"],
                              self.page["account_setting_page"]["title"],
                              1, 1, 1, 10, 0.5)

            self.widget_click(self.page["account_setting_page"]["title"],
                              self.page["account_setting_page"]["change_pwd"],
                              self.page["change_pwd_page"]["title"],
                              1, 1, 1, 10, 0.5)

            old_pwd = self.widget_click(self.page["change_pwd_page"]["title"],
                                        self.page["change_pwd_page"]["old_pwd"],
                                        self.page["change_pwd_page"]["title"],
                                        1, 1, 1, 10, 0.5)

            # 发送数据
            data = "1234567890"
            old_pwd.clear()
            self.ac.send_keys(old_pwd, data)
            self.logger.info(u'[APP_INPUT] ["错误旧密码"] input success')
            time.sleep(0.5)

            new_pwd = self.widget_click(self.page["change_pwd_page"]["title"],
                                        self.page["change_pwd_page"]["new_pwd"],
                                        self.page["change_pwd_page"]["title"],
                                        1, 1, 1, 10, 0.5)

            # 发送数据
            data = conf["user_and_pwd"][self.user]["login_pwd"]
            data = str(data).decode('hex').replace(" ", "")
            new_pwd.clear()
            self.ac.send_keys(new_pwd, data)
            self.logger.info(u'[APP_INPUT] ["新密码"] input success')
            time.sleep(0.5)

            conform_new_pwd = self.widget_click(self.page["change_pwd_page"]["title"],
                                                self.page["change_pwd_page"]["conform_pwd"],
                                                self.page["change_pwd_page"]["title"],
                                                1, 1, 1, 10, 0.5)

            # 发送数据
            data = conf["user_and_pwd"][self.user]["login_pwd"]
            data = str(data).decode('hex').replace(" ", "")
            conform_new_pwd.clear()
            self.ac.send_keys(conform_new_pwd, data)
            self.logger.info(u'[APP_INPUT] ["新密码"] input success')
            time.sleep(0.5)

            widget_px = self.page["change_pwd_page"]["commit"]
            width = int(int(self.device_info["dpi"]["width"]) * widget_px[3]["px"]["width"])
            height = int(int(self.device_info["dpi"]["height"]) * widget_px[3]["px"]["height"])
            self.driver.tap([(width, height)], )
            self.logger.info(u'[APP_CLICK] operate_widget ["%s"] success' % widget_px[2])

            while True:
                try:
                    self.wait_widget(self.page["loading_popup"]["title"], 0.5, 0.1)
                except TimeoutException:
                    break

                # 截屏获取设备toast消息
                ScreenShot(self.device_info, self.zentao_id, self.basename, self.logger)

            self.case_over("screen")
        except TimeoutException:
            self.case_over(False)

    def output(self):
        self.run()
        return self.result()
