# coding:utf-8
'makeTextFile.py -- create text file'

def fun_3_6():
    import os
    ls = os.linesep     #行终止符

    'get filename'
    while True:
        fname = raw_input("please input name")
        if os.path.exists(fname):
            print "Error:'%s' already exists" % fname
        else:
            break

    'get file content lines'
    all = []

    while True:
        entry = raw_input('> ')
        if entry == '.':
            break
        else:
            all.append(entry)

    fobj = open(fname, 'w')
    fobj.writelines(['%s%s'%(x,ls) for x in all])
    fobj.close()
    print 'Done'

if __name__ == '__main__':
    fun_3_6()