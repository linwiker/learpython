#!/usr/bin/env python
# -*- coding: utf-8 -*-
#汉诺塔,三座塔座A,B,C上各有一个竖棍，需要我们把所有盘子从A借助B移动到C上面,要永远保持大的盘子在下面，盘子的数量需要我们自己输入，
def hanoi(a,b,c,n):
    if n == 1:
        print a,'->',c 
    else:
        hanoi(a,c,b,n-1)
        print a,'->',c
        hanoi(b,a,c,n-1)
