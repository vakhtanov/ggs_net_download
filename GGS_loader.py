﻿"""
comment
"""

#import fetch_data
import requests
import base64


region_code='69'
rayon_count=50
filename='Tverskaya.txt'

link='http://pbprog.ru/webservices/oms/ajax_oms.php?type=fs&cn='+region_code+'%3A'
#link_full='http://pbprog.ru/webservices/oms/ajax_oms.php?type=fs&cn=66%3A01' 

headers = {'X-Requested-With':'XMLHttpRequest','Cookie':'_ym_uid=1508829202456486828; BX_USER_ID=345f53efb749c88b92c3744f1042df14; BITRIX_SM_LOGIN=wahha; BITRIX_SM_SOUND_LOGIN_PLAYED=Y; last_visit=1508902955787::1508913755787; __utma=16333431.2118996432.1508829202.1508846067.1508913757.5; __utmc=16333431; __utmz=16333431.1508832650.2.2.utmcsr=yandex|utmccn=(organic)|utmcmd=organic; _ym_isad=2; BITRIX_CONVERSION_CONTEXT_s1=%7B%22ID%22%3A1%2C%22EXPIRE%22%3A1508965140%2C%22UNIQUE%22%3A%5B%22conversion_visit_day%22%5D%7D; tmr_detect=0%7C1508913765891; PHPSESSID=5cc9cbedfac835b4bc9ae15acecc368e; BITRIX_SM_UIDH=c4c748dc20c1a16b16209a430e30a080; BITRIX_SM_UIDL=wahha; BITRIX_SM_SALE_UID=1937074'}
# построение списка текстов из 2х символов на всякий случай
# i=[str(i).rjust(2,'0') for i in range(1,16)]


i=1
# цикл по кварталам
with open(filename, 'wb') as fd:
	while i<=rayon_count:
		#_______________________________
		if i<10:
			kvartal='0'+str(i)
		else:
			kvartal=str(i)
		print('kvartal: '+kvartal)
		req_link=link+kvartal
		print('link:',req_link)
		print('ZAPROS!!!')
			#req = requests.Request('GET',req_link, auth=('user', 'pass'))
		#Запрос к сайту с пунктами
		req=requests.get(req_link,headers=headers)
		#Декодировка из бейза
		try:
			req_out=base64.b64decode(req.text)
		except:
			req_out='____________\n'
		req_out=req_out.replace('"omss": [','"omss": [\n')
		req_out=req_out.replace('}, {','},\n{')
		req_out=req_out.replace('"}]}','"}\n')
		req_out=req_out.replace('", "','*')
		req_out=req_out.replace('": "','*')
		print('ZAMENA')
#    for chunk in r.iter_content(chunk_size=128):
# запись в файл
		fd.write(req_out)
		print('ZAPISAN')
		i=i+1





#print out_text.decode('utf-8')
#print out_text_j.decode('utf-8')