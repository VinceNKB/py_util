#!/usr/bin/env python3
# coding=utf-8


import os
import time
import requests
from bs4 import BeautifulSoup
import json
from page_parser import CommentParser

proxy_path = 'E:/code/douban/db/'

comment_parser = CommentParser.CommentParser()

#num获取num页 国内高匿ip的网页中代理数据
def fetch_proxy(num = 10, path = proxy_path):
    '''
    :param num: the num of pages
    :param path: the path to save, None if do not save
    :return: the list of proxies
    '''

    api = 'http://www.xicidaili.com/nn/{}'
    header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/'
                  '537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    proxy_list = []

    for i in range(num):
        cur_api = api.format(i+1)
        #print(cur_api)
        respones = requests.get(url=cur_api, headers=header)
        soup = BeautifulSoup(respones.text, 'html.parser')
        container = soup.find_all(name='tr', attrs={'class' : 'odd'})
        for tag in container:
            try:
                con_soup = BeautifulSoup(str(tag), 'html.parser')
                td_list = con_soup.find_all('td')
                ip = td_list[1].text.strip()
                port = td_list[2].text.strip()
                city = td_list[3].text.strip()
                safety = td_list[4].text.strip()
                host_type = td_list[5].text.strip()
                speed = td_list[6].find('div').attrs['title'].strip()[:-1]
                connect_time = td_list[7].find('div').attrs['title'].strip()[:-1]
                survive = td_list[8].text.strip()[:-1]

                proxy = {
                    'ip' : ip,
                    'port' : port,
                    'city' : city,
                    'safety' : safety,
                    'host_type' : host_type,
                    'speed' : speed,
                    'connect_time' : connect_time,
                    'survive' : survive
                }

                proxy_list.append(proxy)

            except Exception as e:
                print('No IP！')
        time.sleep(1)


    if path is not None:
        fp = open(path, 'w')
        json.dump(proxy_list, fp)
        fp.close()

    return proxy_list

def test_proxy(test_proxy_list = None, load_path = None, save_path = None, test_url = 'http://www.baidu.com'):
    '''
    :param test_proxy_list: list of dict
    :param load_path:
    :param save_path: None if do not save
    :param test_url:
    :return: good proxu list
    '''

    if test_proxy_list is None:
        if load_path is not None:
            fp = open(load_path, 'r', encoding='utf-8')
            test_proxy_list = json.load(fp)
            fp.close()
        else:
            raise Exception('Can\'t load proxy list')

    good_proxy_list = []
    url = test_url

    for proxy in test_proxy_list:
        host_type = proxy['host_type']
        ip = proxy['ip']
        port = proxy['port']
        ip_port = '{}:{}'.format(ip, port)
        try:
            s = requests.get(url, proxies={host_type : ip_port})
            print('ip：{} 状态{}'.format(ip_port,s.status_code))
			if s.status_code == 200:
			good_proxy_list.append(proxy)
'''
            s.encoding = 'utf-8'

            comment_parser.set_html_doc(s.text)

            comments, state = comment_parser.extract_comments()

            if state == 'ok':
                good_proxy_list.append(proxy)
                print('  ok')
            else:
                print('  error')
'''
        except Exception as e:
            print(e)

    if save_path is not None:
        fp = open(save_path, 'w', encoding='utf-8')
        json.dump(good_proxy_list, fp)
        fp.close()

    return good_proxy_list


def proxypool(good_proxy_list = None, load_path = None, num = None):
    proxys = []

    if good_proxy_list is None:
        if load_path is not None:
            fp = open(load_path, 'r', encoding='utf-8')
            good_proxy_list = json.load(fp)
            fp.close()
        else:
            raise Exception('Can\'t load proxy list')

    for proxy in good_proxy_list:
        host_type = proxy['host_type']
        ip = proxy['ip']
        port = proxy['port']
        ip_port = '{}:{}'.format(ip, port)
        proxys.append({host_type : ip_port})

    return proxys if num is None else proxys[:min(num, len(proxys))]


if __name__ == '__main__':
    #fetch_proxy(path = 'E:/code/douban/db/host.txt')
    # test_proxy_list = [{'ip' : '111.231.221.32',
    #                 'port' : '8765',
    #                 'host_type' : 'http'}]
    # test_proxy(test_proxy_list)
    #
    # #ps = proxypool()
    # proxies = {'http': 'http://1.2.3.4:808'}
    # s = requests.get('https://www.baidu.com', proxies=proxies)
    # print(s.text)
    # print('ip：{} 状态{}'.format(proxies,s.status_code))
    test_proxy(load_path = 'E:/code/douban/db/host.txt', test_url = 'https://movie.douban.com/subject/1293145/comments?start=60&limit=20&sort=new_score&status=P&percent_type=h')
    # proxy_list = proxypool(load_path = 'E:/code/douban/db/good_proxy.txt')
    # print(proxy_list)




