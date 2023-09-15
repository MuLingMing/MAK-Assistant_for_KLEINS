"""
filename:action.py
Author:MuLingMing
包含press(key),wait(t),start(fpath),killgame(fpath)
"""
# coding=utf-8

# conda install pywin32
import os
import time
import shlex
import win32api
import win32con
from keydict import key_dict
# win32api.keybd_event虚拟键码表

# 模拟按键


def press(key):
    if type(key) in [list, tuple, dict]:
        key_names = list(key)  # 组合键
    else:
        key_names = [key]  # 单键
    for key_name in key_names:
        key_list = []
        if key_name.upper() in key_dict:
            key_list.append(key_dict[key_name])
        elif key_name in key_dict.values():  # 数字键值
            key_list.append(key_name)
    # 单键、组合键
    for key_num in key_list:
        try:
            win32api.keybd_event(key_num, 0, 0, 0)  # 按下key_num虚拟键
        except:
            return
    for key_num in key_list:
        try:
            win32api.keybd_event(
                key_num, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放key_num按键
        except:
            return

# time.sleep(sec)


def wait(t):
    time.sleep(t/1000)

# shlex.quote()转义路径
# 打开程序


def start(fpath):
    # 验证文件路径
    if os.path.exists(fpath):
        if os.path.isfile(fpath):
            command = 'start "" {} -popupwindow'.format(shlex.quote(fpath))
            os.system(command)
    # 路径错误
    return 1

# 关闭游戏


def killgame(fpath):
    try:
        command = 'taskkill /f /t /im {}'.format(os.path.split(fpath)[-1])
        os.system(command)
        return 0
    except:
        return 1
