#!/bin/python
# -*- coding:utf8 -*-
# Describe:  统计命令行历史键入次数最多的前十条命令
# Auther: 肓己


import os
from collections import Counter
c = Counter()
with open(os.path.expanduser('/root/.bash_history')) as f:
    for line in f:
        cmd = line.strip().split()
        if cmd:
            c[cmd[0]]+=1

print(c.most_common(10))
