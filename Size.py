# coding: utf8
import os
import time
import ruamel.yaml as yaml
from os.path import getsize, join

# 设置查询命令
command = '!!getsize'


def locate_world_file_path():
    """定位存档文件位置"""
    # 好吧我承认这个地址我写的很烂但至少能用
    MCDRPath = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    with open(MCDRPath + '/config.yml') as Config_File:
        global exc
        try:
            Settings = yaml.safe_load(Config_File)
            world_path = '{}/{}/world'.format(MCDRPath, Settings['working_directory'])
            return world_path
        except yaml.YAMLError as exc:
            return False


def get_world_size(world_path):
    """获取存档大小"""
    Size = 0
    # 遍历文件夹内的文件并加和大小
    for root, dirs, files in os.walk(world_path):
        Size += sum([getsize(join(root, name)) for name in files])
    return Size


def Byte_to_Gigabyte(Size):
    """将字节转换为GB并保留三位小数"""
    Final_Size = round(Size / 1073741824, 3)
    return Final_Size


def on_user_info(server, info):
    """这是一个无意义的注释，因为这个函数的意思不需要我解释"""
    if info.content == command:
        server.execute('/save-all')
        time.sleep(0.1)
        if locate_world_file_path() is not False:
            Size = Byte_to_Gigabyte(get_world_size(locate_world_file_path()))
            server.reply(info, '本服务器存档的大小是§l§6{}§7GB'.format(Size))
        else:
            server.reply(info, '§c{}'.format(exc))