# coding=utf-8
from src.testcase.GN_F1331.WidgetOperation import *


class GNF1331Timer11(WidgetOperation):
    @case_run(False)
    def run(self):
        self.case_module = u"定时器(#9)"  # 用例所属模块
        self.case_title = u'设备当前状态和普通定时输出状态相同，定时执行状态检查'  # 用例名称
        self.zentao_id = "111"  # 禅道ID

    # 用例动作
    def case(self):
        self.choose_home_device(conf["MAC"][self.app][self.device_mac])

        self.delete_out_date_timer()
        self.delete_normal_timer_all()

        self.set_power("main_button_off")

        self.input_serial_command("power", "set_normal_timer", "launch_normal_timer_once")

        self.widget_click(self.page["control_device_page"]["up_timer"],
                          self.page["up_timer_page"]["title"])

        now = time.strftime("%H:%M")

        time_1, time_2 = 5, 10
        start_time_1, set_time_1 = self.create_normal_timer("up_timer_page", now, time_1, "power_on")
        start_time_2, set_time_2 = self.create_normal_timer("up_timer_page", now, time_2, "power_off")

        self.widget_click(self.page["up_timer_page"]["to_return"],
                          self.page["control_device_page"]["title"])

        time.sleep(120)

        self.widget_click(self.page["control_device_page"]["up_button"])
        self.wait_widget(self.page["control_device_page"]["up_button_on"])

        control_time_1 = time.time()

        max_time = max(set_time_1, set_time_2)
        while True:
            if time.time() > max_time + 10:
                break
            print(time.time())
            time.sleep(1)

        #####
        # 开关
        btn_dict = self.check_button_state(control_time_1, set_time_1, set_time_2)
        # 定时设置
        set_normal_dict = self.check_set_normal_timer(start_time_1, start_time_2)
        # 定时执行
        launch_normal_once_dict = self.check_launch_normal_timer_once(set_normal_dict, set_time_1, set_time_2)

        # 上层
        # 定时1
        # 设置
        set_timer = set_normal_dict[start_time_1]
        s_time, s_id, s_week = set_timer[0], set_timer[1], set_timer[3]
        result = [s_time is not None,
                  s_week == "0000000"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (s_time, result))
        # 执行
        launch_timer = launch_normal_once_dict[set_time_1]
        l_time, l_id = launch_timer[s_id][0], launch_timer[s_id][1]
        result = [l_time is not None,
                  l_id == s_id]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (launch_timer, result))

        # 定时2
        # 设置
        set_timer = set_normal_dict[start_time_2]
        s_time, s_id, s_week = set_timer[0], set_timer[1], set_timer[3]
        result = [s_time is not None,
                  s_week == "0000000"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (s_time, result))
        # 执行
        launch_timer = launch_normal_once_dict[set_time_2]
        l_time, l_id = launch_timer[s_id][0], launch_timer[s_id][1]
        result = [l_time is not None,
                  l_id == s_id]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (launch_timer, result))

        # 开关
        # 上层手动关→开
        btn = btn_dict[control_time_1]
        btn_up = btn[1][0]
        result = [btn_up == "1"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn, result))
        # 上层开→开
        btn = btn_dict[set_time_1]
        btn_up = btn[1][0]
        result = [btn_up == "1"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn, result))
        # 上层开→关
        btn = btn_dict[set_time_2]
        btn_up = btn[1][0]
        result = [btn_up == "0"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn, result))
