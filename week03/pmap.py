import multiprocessing
import argparse
import os
import subprocess
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time
import socket
"""
网络安全工具中有一个常用软件称作端口扫描器，即通过一台主机发起向另一主机的常用端口发起连接，探测目标主机是否开放了指定端口（1-1024），用于改善目标主机的安全状况。

要求：编写一个基于多进程或多线程模型的主机扫描器。

使用扫描器可以基于 ping 命令快速检测一个 IP 段是否可以 ping 通，如果可以 ping 通返回主机 IP，如果无法 ping 通忽略连接。
使用扫描器可以快速检测一个指定 IP 地址开放了哪些 tcp 端口，并在终端显示该主机全部开放的端口。
IP 地址、使用 ping 或者使用 tcp 检测功能、以及并发数量，由命令行参数传入。
需考虑网络异常、超时等问题，增加必要的异常处理。
因网络情况复杂，避免造成网络拥堵，需支持用户指定并发数量。

命令行参数举例如下：
pmap.py -n 4 -f ping -ip 192.168.0.1-192.168.0.100

pmap.py -n 10 -f tcp -ip 192.168.0.1 -w result.json

说明：

因大家学习的操作系统版本不同，建立 tcp 连接的工具不限，可以使用 telnet、nc 或 Python 自带的 socket 套接字。
-n：指定并发数量。
-f ping：进行 ping 测试
-f tcp：进行 tcp 端口开放、关闭测试。
-ip：连续 IP 地址支持 192.168.0.1-192.168.0.100 写法。
-w：扫描结果进行保存。
"""


def get_user_input():
    parser = argparse.ArgumentParser(description='ping ip port')
    parser.add_argument('-n', help='n 属性，并发数，必要参数', required=True)
    parser.add_argument('-f', choices=['ping', 'tcp'], help='f 属性，类型，非必要参数，但是有默认值', default='ping')
    parser.add_argument('-ip', help='ip 属性，ip地址或地址段，必要参数', required=True)
    parser.add_argument('-w', help='w 属性，写入文件，非必要参数')
    parser.add_argument('-m', choices=['proc', 'thread'], default='proc', help='m 属性，选择线程或者进程', required=False)

    args = parser.parse_args()
    return args


def run():
    args = get_user_input()
    num = int(args.n)
    ip = args.ip
    model = args.m
    form = args.f
    write = args.w

    # ip参数
    list_ip = ip.split('-')

    # 获取最后的数字
    if len(list_ip) > 1:
        start = int(list_ip[0].split('.')[-1])
        end = int(list_ip[1].split('.')[-1])
    else:
        start = end = int(list_ip[0].split('.')[-1])

    tmp = list_ip[0].split('.')
    tmp.pop()
    prefix = '.'.join(tmp)

    if model == "thread":
        pool = ThreadPoolExecutor(num)
    else:
        pool = ProcessPoolExecutor(num)

    future = pool.submit(run_one, prefix, start, end, form, write)
    print(future.result())


def log_file(filename, text):
    localtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(str(localtime) + ': ' + text + '\r\n')


def run_one(prefix, start, end, form, write):
    result = check_ip(form, prefix, start, end)

    if write:
        log_file(write, result)


def check_ip(form, prefix, start, end):
    if form == 'ping':
        result = []
        for i in range(start, end):
            ip = f'{prefix}.{i}'
            try:
                command = f"ping -c 1 -w 1 {ip}"
                res = subprocess.run(command)
                if res.returncode == 0:
                    result.append(i)
            except Exception as e:
                print(e)
        return ' '.join(result)
    elif form == 'tcp':
        result = {}
        for i in range(start, end):
            ip = f'{prefix}.{i}'
            result[ip] = []
            for port in range(0, 1024):
                try:
                    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sk.settimeout(2)
                    res = sk.connect_ex((ip, port))
                    print(res)
                    if res == 0:
                        result[ip].append(port)
                    sk.close()
                except Exception as e:
                    print(e)
        return str(result)


if __name__ == '__main__':
    run()
