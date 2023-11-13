# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 08:42:05 2023

@author: tiwashima
"""

import re

importList='C:\\users\\tiwashima\\downloads\\IPs.txt'
file=open(importList)
data=file.read()
print('Opened: ' + importList + '.')
file.close()
print('Closed: ' + importList + '.\n')

#If you need a list of the data
#dataList=list(data.split(';'))

#Test that only IP addresses will be pulled from a text file
#testString='Internet communication detected between reported malicious IP address 192.42.116.20 and 1 device'
#dataIPAddresses=re.search(r'[\d]+.[\d]+.[\d]+.[\d]+', testString)
#print(dataIPAddresses)

outputFile=('C:\\users\\tiwashima\\downloads\\ipAddresses.txt')
ipList=open(outputFile,'a')
dataIPAddresses=re.findall(r'[\d]+.[\d]+.[\d]+.[\d]+', data)
for ipAddress in dataIPAddresses:
    ipList.write(ipAddress + '\n')
    print(ipAddress)
ipList.close()
print('\nSaved: ' + outputFile + '.')
ipList.close()