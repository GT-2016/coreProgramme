# coding:utf-8
"""
第5章 数字
"""

def fun_5_6():
    "int floor round区别"
    import math
    for eachNum in (.2, .7,1.2,-.2,-.7,-1.2,-1.7):
        print "int(%.1f)\t%+01f" %(eachNum, float(int(eachNum)))
        print "floor(%.1f)\t%+01f" %(eachNum, math.floor(eachNum))
        print "round(%.1f)\t%+.1f" %(eachNum, round(eachNum))
        print '-' * 20


if __name__ == '__main__':
    fun_5_6()