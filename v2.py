import colorama
import os
import random
import requests
import sys
import time
from multiprocessing.dummy import Pool as ThreadPool
from colorama import *
colorama.init()


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
          \_____|_| |_| |_|___/_____/ \___|\__\___|_|\___/|_| v2  
                            
                     CODED BY TuxMacG1v
           TG:https://t.me/I_am_a_silent_killer
         ICQ:https://icq.im/I_am_a_silent_killer
                          
                                                        
                                            
"""
    for N, line in enumerate(x.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
        time.sleep(0.02)
print_logo()

if not os.path.exists("Cms"):
    os.mkdir("Cms", 0755)



def cms(url):
    try:
        url = url.replace('\n', '').replace('\r', '')
        if url.startswith('http://'):
            url = url.replace('http://', '')
        elif url.startswith("https://"):
            url = url.replace('https://', '')
        else:
            pass

        r = requests.get('http://'+url,timeout=10)
        p = requests.get('http://'+url,timeout=5, allow_redirects = False)
        
        
        # 1. CMS WORDPRESS
        if "/wp-login.php" in r.text or "/wp-admin" in r.text or "/wp-config.php" in r.text:
            print "[+] Wordpress CMS http://"+url + GREEN + '\n'
            open("Cms/wordpress.txt", "a").write('http://'+url + '\n')
        elif "/license.txt" in p.text:
            print "[+] Wordpress CMS http://"+url + GREEN + '\n'
            open("Cms/wordpress", "a").write('http://'+url + '\n')
            
        # 2. CMS LARAVEL
        elif "/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php" in r.text:
            print  "[+] Laravel CMS http://"+url + CYAN + '\n'
            open("Cms/Laravel.txt", "a").write('http://'+url + '\n')
        elif "/.env'" in p.text:
            print  "[+] Laravel CMS http://"+url + CYAN + '\n'
            open("Cms/Laravel Env.txt", "a").write('http://'+url + '\n')
        elif "/.env'" in r.text:
            print  "[+] Laravel CMS http://"+url + CYAN + '\n'
            open("Cms/Laravel Env.txt", "a").write('http://'+url + '\n')
            
        # 3. CMS OPENCART
        elif "/index.php?route=common/home" in r.text:
            print  "[+] Opencart CMS http://"+url + YELLOW + '\n'
            open("Cms/Opencart.txt", "a").write('http://'+url + '\n')
        elif "/config.php" in r.text:
            print  "[+] Opencart CMS http://"+url + YELLOW + '\n'
            open("Cms/Opencart.txt", "a").write('http://'+url + '\n')
            
        #4. CMS JOOMLA
        elif "/Joomla!" in r.text or "/index.php?option=com_" in r.text or "/administrator/index.php" in r.text or "/administrator/" in r.text or "/administrator/manifests/files/joomla.xml" in r.text or "/<version>(.*?)<\/version>" in r.text or "/language/en-GB/en-GB.xml" in r.text or "<version>(.*?)<\/version>" in r.text:
            print  "[+] JOOMLA CMS http://"+url + BLUE + '\n'
            open("Cms/Joomla.txt", "a").write('http://'+url + '\n')

        #4. CMS Drupal
        elif "/drupal/" in r.text:
            print  "[+] DRUPAL CMS http://"+url + WHITE + '\n'
            open("Cms/Drupal.txt", "a").write('http://'+url + '\n')

        else:
            print '[-]< Cms Not Found >[-] http://'+url + BOLD + '\n'
            open("Cms/Unknown.txt", "a").write('http://'+url + '\n')

    except:	
	    print ('[*x*] DEAD SITE [*x*] http://'+url + RED + '\n')
	    open("Cms/Dead.txt", "a").write('http://'+url + '\n')
            pass

List = open(raw_input(RED + "GIVE ME SITE LIST:" + WHITE), 'r').readlines()
pool = ThreadPool(100)
pool.map(cms, List)
pool.close()
pool.join()

if __name__ == '__main__':
    print("Finished, success , Thank you for using.")
