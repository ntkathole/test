#!/usr/bin/env python

#Search running machine in network 172.22.24.0
import os

for i in range(2,5):
  os.system("ping -c 2 172.22.24."+ str(i))
