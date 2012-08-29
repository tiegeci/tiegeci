# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 23:50:04 2012

@author: Administrator
"""
import math
import urllib
import socket
from multiprocessing import Process,Queue
socket.setdefaulttimeout(10)

def downlrc(lrc_id):
    lrc_dir = lrc_id/100;
    lrc_path = str(lrc_dir) + "/" + str(lrc_id) + ".lrc"
    url = "http://box.zhangmen.baidu.com/bdlrc/" + lrc_path
    try:
        wp = urllib.urlopen(url)
        lrc = wp.read()
        if (lrc =="" or lrc.find("TABLE") > -1):
            err = "get" + url + u"failed\n"
            print err
            return
        fp = open(str(lrc_id)+".lrc","w")
        fp.write(lrc)
        fp.close()
	print url + "is ok!"
    except:
        return
def process_get(q):
    while(not q.empty()):
	ix = q.get()
        downlrc(ix)

istart = 10000
iend = 100000
psum = 200
q = Queue()
while(True):
    q.put(istart)
    if (istart > iend):
	break
    istart = istart + 1
for ix in range(psum):
    p = Process(target=process_get,args=(q,))
    p.start()

print "OK"
