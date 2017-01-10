#!/usr/bin/env python3

import pymysql
import time
#配置
config = {
    'host':'127.0.0.1',
    'port':3306,
    'user':'root',
    'password':'123456',
    'db':'admaster',
    'charset':'utf8mb4',
    'cursorclass':pymysql.cursors.DictCursor
}

# config = {
#     'host':'114.212.82.189',
#     'port':3306,
#     'user':'root',
#     'password':'root',
#     'db':'ADMASTER',
#     'charset':'utf8mb4',
#     'cursorclass':pymysql.cursors.DictCursor
# }


mysql_batch_num = 10000
batch_list = []
counts = 0
cost_time = 0
try:
    readFile = open('new_AdMaster_train_dataset', 'r', encoding='utf-8')
    connection = pymysql.connect(**config)#连接数据库

    with connection.cursor() as cursor:
        start_time = time.time()
        for eachLine in readFile:
            slice = eachLine.strip().split('\x01')
            if len(slice[17]) > 128:
                slice[17] = slice[17][:128]

            if len(slice[13]) > 50:
                slice[13] = slice[13][:50]

            if len(slice[12]) > 20:
                slice[12] = slice[12][:20]

            if len(slice[19]) > 20:
                slice[19] = slice[19][:20]

            batch_list.append('('+','.join('"'+x+'"' for x in slice) + ')')

            if len(batch_list) == mysql_batch_num:
                sql = "INSERT INTO `RAWTRAINDATA`(`rank`, `dt`, `Cookie`,`Ip`,`mobile_idfa`,`mobile_imei`,`mobile_android_id`,`mobile_openudid`,`mobile_mac`,`timestamps` ,`camp_id` ,`creativeid`,`mobile_os` ,`mobile_type`,`mobile_app_key` ,`mobile_app_name`,`placement_id`,`user_agent`,`media id`,`os`,`born_time`,`media_category`,`media_firstType`,`media_secondType`,`media_tag`,`flag`) VALUES %s" % ','.join(batch_list)
                cursor.execute(sql)
                connection.commit()
                counts += len(batch_list)
                batch_list = []
                period = time.time() - start_time
                cost_time += period
                print('insert %d items costing %d, averagely %f per sec, %d already insert, %fs remain' % (mysql_batch_num, period, counts/cost_time, counts, (42459762-counts)/(mysql_batch_num/period)))
                start_time = time.time()
        cursor.executemany(sql, batch_list)
        connection.commit()
        counts += len(batch_list)
        print('finish all : %d' % counts)
finally:
    connection.close()
    readFile.close()

#3200条/s 太慢了，传完全部需要21229s