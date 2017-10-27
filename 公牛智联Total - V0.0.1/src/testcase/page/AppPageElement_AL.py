# coding=utf-8
from AppPageElement_AL_Android import *
from AppPageElement_AL_iOS import *


class MainPageWidgetAL(object):
    def __init__(self, phone_os):
        self.phone_os = phone_os
        self.mpwa = MainPageWidgetAndroidAL()
        self.mpwi = MainPageWidgetIosAL()
        self.pwa = PopupWidgetAndroidAL()
        self.pwi = PopupWidgetIosAL()
    def wrapper(self, func1, func2):
        if self.phone_os == "Android":
            return func1
        elif self.phone_os == "iOS":
            return func2
        else:
            raise KeyError("The OS is wrong!")

    def add_cycle_timer_page(self):
        return self.wrapper(self.mpwa.add_cycle_timer_page(), self.mpwi.add_cycle_timer_page())

    def add_delay_timer_page(self):
        return self.wrapper(self.mpwa.add_delay_timer_page(), self.mpwi.add_delay_timer_page())

    def add_device_class_page(self):
        return self.wrapper(self.mpwa.add_device_class_page(), self.mpwi.add_device_class_page())

    def add_device_method_page(self):
        return self.wrapper(self.mpwa.add_device_method_page(), self.mpwi.add_device_method_page())

    def add_history_list_page(self):
        return self.wrapper(self.mpwa.add_history_list_page(), self.mpwi.add_history_list_page())

    def add_normal_timer_page(self):
        return self.wrapper(self.mpwa.add_normal_timer_page(), self.mpwi.add_normal_timer_page())

    def add_specification_page(self):
        return self.wrapper(self.mpwa.add_specification_page(), self.mpwi.add_specification_page())

    def app_home_page(self):
        return self.wrapper(self.mpwa.app_home_page(), self.mpwi.app_home_page())

    def bind_device_page(self):
        return self.wrapper(self.mpwa.bind_device_page(), self.mpwi.bind_device_page())

    def change_nickname_page(self):
        return self.wrapper(self.mpwa.change_nickname_page(), self.mpwi.change_nickname_page())

    def control_device_page(self):
        return self.wrapper(self.mpwa.control_device_page(), self.mpwi.control_device_page())

    def device_info_page(self):
        return self.wrapper(self.mpwa.device_info_page(), self.mpwi.device_info_page())

    def fish_mode_timer_page(self):
        return self.wrapper(self.mpwa.fish_mode_timer_page(), self.mpwi.fish_mode_timer_page())

    def god_page(self):
        return self.wrapper(self.mpwa.god_page(), self.mpwi.god_page())

    def input_wifi_password_page(self):
        return self.wrapper(self.mpwa.input_wifi_password_page(), self.mpwi.input_wifi_password_page())

    def mosquito_mode_timer_page(self):
        return self.wrapper(self.mpwa.mosquito_mode_timer_page(), self.mpwi.mosquito_mode_timer_page())

    def my_page(self):
        return self.wrapper(self.mpwa.my_page(), self.mpwi.my_page())

    def night_mode_timer_page(self):
        return self.wrapper(self.mpwa.night_mode_timer_page(), self.mpwi.night_mode_timer_page())

    def normal_timer_page(self):
        return self.wrapper(self.mpwa.normal_timer_page(), self.mpwi.normal_timer_page())

    def piocc_mode_timer_page(self):
        return self.wrapper(self.mpwa.piocc_mode_timer_page(), self.mpwi.piocc_mode_timer_page())

    def search_device_fail_page(self):
        return self.wrapper(self.mpwa.search_device_fail_page(), self.mpwi.search_device_fail_page())

    def search_device_loading_page(self):
        return self.wrapper(self.mpwa.search_device_loading_page(), self.mpwi.search_device_loading_page())

    def setting_page(self):
        return self.wrapper(self.mpwa.setting_page(), self.mpwi.setting_page())

    def timer_repeat_page(self):
        return self.wrapper(self.mpwa.timer_repeat_page(), self.mpwi.timer_repeat_page())

    def warmer_mode_timer_page(self):
        return self.wrapper(self.mpwa.warmer_mode_timer_page(), self.mpwi.warmer_mode_timer_page())

    def water_mode_timer_page(self):
        return self.wrapper(self.mpwa.water_mode_timer_page(), self.mpwi.water_mode_timer_page())

    def add_device_popup(self):
        return self.wrapper(self.pwa.add_device_popup(), self.pwi.add_device_popup())

    def loading_popup(self):
        return self.wrapper(self.pwa.loading_popup(), self.pwi.loading_popup())

    def logout_popup(self):
        return self.wrapper(self.pwa.logout_popup(), self.pwi.logout_popup())

    def mode_timer_conflict_popup(self):
        return self.wrapper(self.pwa.mode_timer_conflict_popup(), self.pwi.mode_timer_conflict_popup())

    def timer_roll_popup(self):
        return self.wrapper(self.pwa.timer_roll_popup(), self.pwi.timer_roll_popup())
