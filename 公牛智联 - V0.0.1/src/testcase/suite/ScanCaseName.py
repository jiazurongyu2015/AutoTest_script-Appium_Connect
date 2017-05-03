# coding=utf-8
import os
import re
from collections import Counter


def scan_case_name():
    len_case = {0: [], 1: []}
    case_attr = []
    list_case_id = {}
    rootdir = r"./src/testcase/case"  # 指明被遍历的文件夹
    if os.path.exists(r"./report/") is False:
        os.makedirs(r"./report/")
    with open(u"./report/自动化测试用例对照表.log", "w") as cast_title:
        cast_title.write(u"自动化测试用例对照表:\n".encode("utf-8"))
        for parent, dirnames, filenames in os.walk(rootdir):  # 三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
            for filename in filenames:
                if "GNAPP" in filename and "pyc" not in filename:
                    with open(os.path.join(parent, filename), "r") as files:
                        file = files.read()
                        case_module = re.findall(r'self.case_module = u"(.+)"', file)[0]
                        case_name = re.findall(r"self.case_title = u'(.+)'", file)[0]
                        ZenTao_id = re.findall(r'self.ZenTao_id = (\d+)', file)[0]
                        case_id = re.findall(r"class (.+)\(", file)[0]
                        list_case_id[filename] = case_id
                        case_attr.append([case_module, ZenTao_id, case_id, case_name])
                        len_case[0].append(len(case_module))
                        len_case[1].append(len(case_id))
        len_case_module = tuple(len_case[0])
        len_case_id = tuple(len_case[1])
        max_case_module = max(len_case_module)
        max_case_len = max(len_case_id)
        repetition = Counter(list_case_id.values())  # 计算list内部参数个数
        if len(set(repetition.values())) == 1:
            for i in case_attr:
                module_zen = max_case_module - len(i[0]) - 1 * (max_case_module - len(i[0])) / 3
                case_zen = max_case_len - len(i[2])
                cast_title.write("[CASE_MODULE='%s',%s  ZenTao_ID=%s,  CODE_ID=%s,%s  CASE_NAME='%s']\n"
                                 % (i[0], " " * module_zen, i[1], i[2], " " * case_zen, i[3]))
        else:
            tmp = ""
            dump = ""
            for k, v in repetition.items():
                if v != 1:
                    tmp = k
            for k, v in list_case_id.items():
                if v == tmp:
                    dump = dump + "%s:%s," % (k, v)
            raise ValueError(u"%s重复" % dump[:-1])
