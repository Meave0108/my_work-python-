# coding: utf-8
from numpy.random import randint
words='''
我
我的
妳
妳的
心
溫柔
日子
雨
風
天空
雲
等待
哭泣
戀愛
相遇
分離
忘記
心醉
驀然
吹過
思念
靈魂
停止'''
words
ph=words.split('\n')
from numpy.random import choice


l=randint(3,6)

print("文青機器人")
for i in range(l):
    s=randint(1,7)
    egg=choice(ph,s)
    h=" ".join(egg)
    print(h)
