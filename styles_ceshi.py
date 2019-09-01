#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ss = [(['名次'], ['学校名称'], ['星级排名'], ['办学层次'], ['总分']), (['名次'], ['学校名称'], ['星级排名'], ['办学层次'], ['总分'])]
# for i in ss:
#     u_list = []
#     for j in i:
#         ss = ''.join(j)
#         u_list.append(ss)
#     print(u_list)
# print(ss)
# print(u_list)
# '名次', '学校名称', '星级排名', '办学层次', '总分'
fb = [['1', '北京大学', '8星级', '世界一流大学', '100']]

for i in fb:
    ss = {
        "名次": i[0],
        "学校名称": i[1],
        "星级排名": i[2],
        "办学层次": i[3],
        "总分": i[4]
    }

    print(ss)
