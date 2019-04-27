#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 이 코드는 음주 후 작성ㅇ되었습ㅂ3ㅈㄴ키다

import random, turtle

t = turtle.Turtle()
t.speed(0)

while True:
    # 20%의 확률로 원을 그립니다.
    if random.random() < 0.2: 
        t.circle(random.randint(0,100))
    else:
        t.forward(random.randint(0,100))
    t.left(random.randint(0,359))