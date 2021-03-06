# coding=utf-8
from src.testcase.GN_Y201J.WidgetOperation import *


class GNY201JElectricityMeter5(WidgetOperation):
    @case_run(False)
    def run(self):
        self.case_module = u"电量计量"  # 用例所属模块
        self.case_title = u'用电图表显示周期设置'  # 用例名称
        self.zentao_id = "1149"  # 禅道ID

    # 用例动作
    def case(self):
        self.choose_home_device(conf["MAC"]["JD"][0])

        self.set_power("power_on")

        self.widget_click(self.page["control_device_page"]["elec"],
                          self.page["elec_page"]["title"])

        elec_elements = self.wait_widget(self.page["elec_page"]["elec_time"])[0]
        if not re.findall("\d+:\d+", self.ac.get_attribute(elec_elements, "name")):
            raise TimeoutException("elec time is wrong, current is %s" % elec_elements)

        self.widget_click(self.page["elec_page"]["week"],
                          self.page["elec_page"]["title"])

        elec_elements = self.wait_widget(self.page["elec_page"]["elec_time"])[0]
        if not re.findall(u"\d+月\d+日", self.ac.get_attribute(elec_elements, "name")):
            raise TimeoutException("elec time is wrong, current is %s" % elec_elements)

        self.widget_click(self.page["elec_page"]["month"],
                          self.page["elec_page"]["title"])

        elec_elements = self.wait_widget(self.page["elec_page"]["elec_time"])[0]
        if not re.findall("\d+-\d+-\d+", self.ac.get_attribute(elec_elements, "name")):
            raise TimeoutException("elec time is wrong, current is %s" % elec_elements)

        self.widget_click(self.page["elec_page"]["year"],
                          self.page["elec_page"]["title"])

        elec_elements = self.wait_widget(self.page["elec_page"]["elec_time"])[0]
        if not re.findall(u".+月", self.ac.get_attribute(elec_elements, "name")):
            raise TimeoutException("elec time1 is wrong, current is %s" % elec_elements)
        if re.findall(u"月.+", self.ac.get_attribute(elec_elements, "name")):
            raise TimeoutException("elec time2 is wrong, current is %s" % elec_elements)
