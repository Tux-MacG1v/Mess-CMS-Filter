import requests
import urllib3
from multiprocessing.dummy import Pool as ThreadPool
import colorama
import os
import random
import requests
import sys
import time
from multiprocessing.dummy import Pool as ThreadPool
from colorama import *
colorama.init()
urllib3.disable_warnings()

# Now regular ANSI codes should work, even in Windows
CLEAR_SCREEN = "\033[2J"
RED = "\033[31m"   # mode 31 = red forground
RESET = "\033[0m"  # mode 0  = reset
BLUE  = "\033[34m"
YELLOW = "\033[1;33m"
CYAN  = "\033[36m"
GREEN = "\033[32m"
RESET = "\033[0m"
BOLD    = "\033[m"
REVERSE = "\033[m"
WHITE = "\033[1;37m"

reload(sys)
sys.setdefaultencoding('utf8')
os.system('cls' if os.name == 'nt' else 'clear')

def print_logo():
    clear = "\x1b[0m"
    colors = [31, 32, 33, 34, 35, 36, 37, 38, 39]

    x = """

           _____               _____       _    _______         
SIMPLE    / ____|             |  __ \     | |  |__   __|        
          | |     _ __ ___  ___| |  | | ___| |_ ___| | ___  _ __ 
          | |    | '_ ` _ \/ __| | 0| |/ _ \ __/ __| |/ _ \| '__|
          | |____| | | | | \__ \ |__| |  __/ || (__| | (_) | |   
          \_____|_| |_| |_|___/_____/ \___|\__\___|_|\___/|_| v3 
                            

           TG:https://t.me/I_am_a_silent_killer
         ICQ:https://icq.im/I_am_a_silent_killer
                          
                                                        
                                            
"""
    for N, line in enumerate(x.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
        time.sleep(0.02)
print_logo()

if not os.path.exists("Cms"):
    os.mkdir("Cms", 0755)



header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


def lightxcms(site):
    site = site.replace('\n', '').replace('\r', '')
    if site.startswith('https://'):
        site = site.replace('https://', 'http://')
    elif site.startswith('http://'):
        pass
    else:
        site = 'http://'+site
    try:
        payload = requests.get(site, headers=header, verify=False, timeout=20, allow_redirects=True)
        if payload.status_code==200:
            if 'content="PrestaShop"' in payload.text:
                print("[+] PRESTASHOP :: "+site)
                open('Preatshop.txt','a').write(site+'\n')
                pass
            elif 'catalog/view/' in payload.text:
                print("[+] OpenCart :: "+site)
                open('OpenCart.txt','a').write(site+'\n')
                pass
            elif 'meta name="generator" content="vBulletin' in payload.text:
                print("[+] vBulletin :: "+site)
                open('vBulletin.txt','a').write(site+'\n')
                pass
            elif '/sites/default/' in payload.text:
                print("[+] Drupal :: "+site)
                open('Drupal.txt','a').write(site+'\n')
                pass
            elif 'laravel_session' in payload.text:
                print("[+] Laravel :: "+site)
                open('Laravel.txt','a').write(site+'\n')
                pass
            else:
                for dirx in ['/media/system/js/core.js', '/wp-includes/js/jquery/jquery.js']:
                    payload2 = requests.get(site+dirx, headers=header, verify=False, timeout=20, allow_redirects=True)
                    if 'jQuery' in payload2.text:
                        print("[+] Wordpress :: "+site)
                        open('Wordpress.txt','a').write(site+'\n')
                        break
                    elif 'window.Joomla' in payload2.text:
                        print("[+] Joomla :: "+site)
                        open('Joomla.txt','a').write(site+'\n')
                        break
                    else:
                        print("[+] UNKNOWN :: "+site)
                        open('Unknown.txt','a').write(site+'\n')
        else:
            print("[+] UNKNOWN :: "+site)
            open('Unknown.txt','a').write(site+'\n')
    except:
        print(RED + "[+] DEAD SITE :: "+site)

def multixcms():
    sitex = open(raw_input(RED + 'site list: ' + WHITE), 'r').readlines()
    td = raw_input("THREADS : ")  
    pool = ThreadPool(int(td))
    pool.map(lightxcms, sitex)
    pool.close()
    pool.join()

multixcms()
