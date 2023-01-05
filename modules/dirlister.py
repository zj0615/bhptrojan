# coding=utf-8
# ^...^*:詹峻
# 开发时间：2023/1/5 19:25
import os


def run(**args):
    print("[*] In dirlister module.")
    files = os.listdir(".")
    return str(files)