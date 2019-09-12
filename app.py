'''
Author: Zack Uno
'''

##############################################
# Importing libraries coz cool peopledo that #
##############################################

import urllib
from urllib.request import urlopen
import threading
import time


#defining the infinity variable


def pinger_urllib(host):
  """
  helper function timing the retrival of / route
  TODO: should there be a 1MB bogus file?
  """
  t1 = time.time()
  urlopen(host + '/').read()
  return (time.time() - t1) * 1000.0

"""
  the actual task
"""
def task(m):
    i = 0 
    #k=0
    while i==0:
        k=0
        while k<4:
            delay = float(pinger_urllib(m))
            print ('%-30s %5.0f [ms]' % (m, delay))
            k = k + 1
  

# parallelization
tasks = []
URLs = [ 'https://nehandaradio.com/', 'https://www.myzimbabwe.co.zw',
for site in URLs:
    t = threading.Thread(target=task, args=(site,))
    t.start()
    tasks.append(t)

    # synchronization point
    for t in tasks:
        t.join()
