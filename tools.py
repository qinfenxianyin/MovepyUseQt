#!/usr/bin
# -*- coding: utf-8 -*-

import os

#文件名加字符
def move_fileto_out(infile, initstr):

    dir, suffix = os.path.splitext(infile)
    outfile = str('{}-'+str(initstr)+'{}').format(dir, suffix)
    return outfile

if __name__=='__main__':
    out=move_fileto_out('/Users/xiwenkai/1100/mycode/1598080495180776.mp4','aaa')
    print(out)