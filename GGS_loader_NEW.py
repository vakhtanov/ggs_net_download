"""
comment
"""
# @wahha  @HomeD
# скрипт для скачки ГГС с сайта http://pbprog.ru, скачка по областям
#import fetch_data
# 123456
import requests
import base64

REGIONS_CODE=[str(i).rjust(2,'0') for i in range(1,92)]
#region_code='89'
rayon_count=100


def download_GGS_by_Region(region_code,rayon_count):
	filename='region'+region_code+'.txt'
	link='http://pbprog.ru/webservices/oms/ajax_oms.php?type=fs&cn='+region_code+'%3A'
	headers = {'X-Requested-With':'XMLHttpRequest','Cookie':'_ym_uid=1508829202456486828; BX_USER_ID=345f53efb749c88b92c3744f1042df14; BITRIX_SM_LOGIN=wahha; BITRIX_SM_SOUND_LOGIN_PLAYED=Y; last_visit=1508902955787::1508913755787; __utma=16333431.2118996432.1508829202.1508846067.1508913757.5; __utmc=16333431; __utmz=16333431.1508832650.2.2.utmcsr=yandex|utmccn=(organic)|utmcmd=organic; _ym_isad=2; BITRIX_CONVERSION_CONTEXT_s1=%7B%22ID%22%3A1%2C%22EXPIRE%22%3A1508965140%2C%22UNIQUE%22%3A%5B%22conversion_visit_day%22%5D%7D; tmr_detect=0%7C1508913765891; PHPSESSID=5cc9cbedfac835b4bc9ae15acecc368e; BITRIX_SM_UIDH=c4c748dc20c1a16b16209a430e30a080; BITRIX_SM_UIDL=wahha; BITRIX_SM_SALE_UID=1937074'}
	# построение списка текстов из 2х символов на всякий случай
	# i=[str(i).rjust(2,'0') for i in range(1,16)]
	
	kvartal_spisok=[str(i).rjust(2,'0') for i in range(1,rayon_count+1)]
	# цикл по кварталам
	with open(filename,'w') as fd:
		for kvartal in kvartal_spisok:
			print('kvartal: '+kvartal)
			req_link=link+kvartal
			print('link:',req_link)
			print('ZAPROS!!!')
			#Запрос к сайту с пунктами
			req=requests.get(req_link,headers=headers)
			#Декодировка из бейза64
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
			# запись в файл
			fd.write(req_out)
			print('ZAPISAN')
			
def main():
	for region in REGIONS_CODE:
		print('Start DOUNLOAD',region,'code')
		download_GGS_by_Region(region,rayon_count)
	
if __name__ == '__main__':
	main()