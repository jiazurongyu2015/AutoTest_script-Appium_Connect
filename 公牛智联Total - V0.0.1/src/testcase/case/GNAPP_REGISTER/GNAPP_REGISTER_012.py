# coding=utf-8
from src.testcase.case.LaunchApp import *


class GNAppRegister12(LaunchApp):
    def run(self):
        self.case_module = u"注册"  # 用例所属模块
        self.case_title = u'注册页面-用户名长度大于11位，提示信息检查'  # 用例名称
        self.zentao_id = 1826  # 禅道ID
        self.basename = os.path.basename(__file__).split(".")[0]  # 获取用例的文件名称:GNAPP_REGISTER_012
        self.driver = self.return_driver()
        self.logger.info('[GN_INF] <current case> [CASE_ID="%s", CASE_NAME="%s", 禅道ID="%s", CASE_MODULE="%s"]'
                         % (self.basename, self.case_title, self.zentao_id, self.case_module))  # 记录log

        try:
            self.launch_app(True)  # 启动APP
            self.case()
        except WebDriverException:
            self.debug.error(traceback.format_exc())  # Message: ***

    # 用例动作
    def case(self):
        try:
            self.widget_click(self.page["login_page"]["title"],
                              self.page["login_page"]["to_register"],
                              self.page["register_page"]["title"],
                              1, 1, 1, 10, 0.5)

            user_name = self.widget_click(self.page["register_page"]["title"],
                                          self.page["register_page"]["username"],
                                          self.page["register_page"]["title"],
                                          1, 1, 1, 10, 0.5)

            # 发送数据
            data = "138123412341"
            user_name.clear()
            self.ac.send_keys(user_name, data)
            self.logger.info(u'[APP_INPUT] ["用户名"] input success')
            time.sleep(0.5)

            user_name = self.wait_widget(self.page["register_page"]["username"], 1, 0.5).get_attribute("name")
            if len(user_name) != 11:
                raise TimeoutException()

            self.case_over(True)
        except TimeoutException:
            self.case_over(False)

    def output(self):
        self.run()
        return self.result()
