import time
import requests
import re
import itertools
import threading
import random
import base64
import os
import json
import sys
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from os import system, name
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from colorama import Fore, Back, Style
import logging;
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from urllib3 import disable_warnings
from re import search
from json import loads
import ctypes

ctypes.windll.kernel32.SetConsoleTitleW("XBOX AUTO PURCHASER   MADE BY - GALAXY")
green = Fore.GREEN
red = Fore.RED
white = Fore.WHITE
blue = Fore.BLUE
magenta = Fore.MAGENTA
lblue = Fore.LIGHTBLUE_EX
lgreen = Fore.LIGHTGREEN_EX


logging. getLogger("urllib3"). setLevel(logging. WARNING)



def screen_clear():
	if name == 'nt':
		_ = system('cls')
	else:
		_ = system('clear')
screen_clear()
text = green + f"""
$$\   $$\ $$$$$$$\   $$$$$$\  $$\   $$\ 
$$ |  $$ |$$  __$$\ $$  __$$\ $$ |  $$ |
\$$\ $$  |$$ |  $$ |$$ /  $$ |\$$\ $$  |
 \$$$$  / $$$$$$$\ |$$ |  $$ | \$$$$  / 
 $$  $$<  $$  __$$\ $$ |  $$ | $$  $$<  
$$  /\$$\ $$ |  $$ |$$ |  $$ |$$  /\$$\ 
$$ /  $$ |$$$$$$$  | $$$$$$  |$$ /  $$ |
\__|  \__|\_______/  \______/ \__|  \__|
"""
print(text)

 

print(magenta+f"""[+] Made By Galaxy
""")

country_name = input(lblue + f"[+] Enter Code: ")
if country_name=="en-au": 
    address1 = "43 Cassinia Street"
    city = "Adelong"
    state = "New South Wales"
    post_code = "2729"
elif country_name=="en-sg":
    address1 = " LOR 5 TELOK KWAN"
    city = "Singapore"
    state = "Singapore"
    post_code = "425792"
elif country_name=="ar-ae":
    address1 = "Po Box 80619"
    city = "Al Ain"
    state = "دبي"
    post_code = "80619"
elif country_name=="en-za":
    address1 = "1619 Dorp St"
    city = "Athlone"
    state = "Western Cape"
    post_code = "7764"
elif country_name=="es-co":
    address1 = "autop surS/NUM, 16"
    city = "Medellín"
    state = "Medellín"
    post_code = "050006"
elif country_name=="es-cl":
    address1 = "autop surS/NUM, 16"
    city = "Medellín"
    state = "Medellín"
    post_code = "050006"
elif country_name=="en-nz":
    address1 = "14 Gambia Grove"
    city = "Rototuna"
    state = "Hamilton"
    post_code = "3210"
elif country_name=="en-gb":
    address1 = "65 Fulford Road"
    city = "Pentraeth"
    state = "United Kingdom"
    post_code = "LL75 8ZW"
elif country_name=="ar-sa":
    address1 = "Head Office Abdullah Al Suliman Street Al Halees Group Building, Al Faiha'a Dist."
    city = "Jeddah"
    state = "Jeddah"
    post_code = "22233"

elif country_name=='es-ES':
    address1 = "Avendaño 23"
    city = "Almudaina"
    state = "Alicante"
    post_code = "37209"
elif country_name=='ja-JP':
    address1 = "365-1243, Yatsuomachi Ashitani,-shi"
    city = "Toyama-shi"
    state = "Toyama"
    post_code = "321-1661"
elif country_name=='zh-TW':
    address1 = "No.121, Deshou St."
    city = "Taoyuan City"
    state = "Taoyuan"
    post_code = "893"
elif country_name=='nl-NL':
    address1 = "K.P. van der Mandelelaan 150."
    city = "Rotterdam"
    state = "South Holland"
    post_code = "3062 MB"



else: 
	print("wrong country") 

disable_warnings()


options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
driver.get("https://www.xbox.com/"+country_name+"/games/store/xbox-game-pass-ultimate/cfq7ttc0khs0/0007")


join_now_button = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[3]/div/div[1]/div[5]/div/div[1]/button'))).click()
email_input_box = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, '//*[@id="i0116"]')))
with open('./data/accounts.txt', 'r+', encoding='utf-8') as file:
    data = file.readline()
    email = data.split('|', 1)[0]
    password = data.rsplit('|', 1)[-1]
     

email_input_box.send_keys(email)
email_nxt_btn = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, '//*[@id="idSIButton9"]'))).click()

print(Fore.GREEN + f'logging in to email :{email}')
print(Style.RESET_ALL)
password_input_box = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, '//*[@id="i0118"]')))
password_input_box.send_keys(password)
pass_next_btn = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, '//*[@id="idSIButton9"]')))
pass_next_btn.click()
try:
    stay_sign_no_btn = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, '//*[@id="idBtn_Back"]')))
    stay_sign_no_btn.click()
except:
    print(Fore.GREEN + f'please wait.......')

try:
    WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, '//*[@id="Accept"]'))).click()
except:
    print(Fore.GREEN + f'[+] Logged Into Account :{email}|{password}')
    print(Style.RESET_ALL)


next_btn_gp = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[3]/div/div[1]/div[5]/div/div[1]/button'))).click()




iframe = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, "body > reach-portal > div:nth-child(3) > div > div > div > div > div > div > div > div > div > iframe")))

driver.switch_to.frame(iframe)
WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, '//*[@id="store-cart-root"]/div/div/div[2]/div/div[1]/div[4]/button'))).click()
WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, '//*[@id="id_credit_card_visa_amex_mc"]'))).click()

with open('./data/cards.txt', 'r+', encoding='utf-8') as ccs:
    cc1 = ccs.readline()
    cc_num = cc1.split('|', 1)[0]
    exp_mth = cc1.split('|')[1]
    exp_yer = cc1.split('|')[2][-2:]
    cvv = cc1.split('|')[3]

print(Fore.GREEN + f"CHECKING CARDS PLS WAIT")
print(Style.RESET_ALL)
WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, '//*[@id="accountToken"]'))).send_keys(f'{cc_num}')
WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, '//*[@id="accountHolderName"]'))).send_keys("promos hehe")

month = Select(WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, '//*[@id="input_expiryMonth"]'))))

month.select_by_visible_text(f'{exp_mth}')

year = Select(WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, '//*[@id="input_expiryYear"]'))))
year.select_by_visible_text(f'{exp_yer}')

WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, '//*[@id="cvvToken"]'))).send_keys(f'{cvv}')

WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, '//*[@id="address_line1"]'))).send_keys(f'{address1}')

WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, '//*[@id="city"]'))).send_keys(f'{city}')
state_sel = Select(driver.find_element(By.XPATH, '//*[@id="input_region"]'))
state_sel.select_by_visible_text(state)
WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, '//*[@id="postal_code"]'))).send_keys(f'{post_code}')

WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, '//*[@id="pidlddc-button-saveButton"]'))).click()
WebDriverWait(driver, 15).until(ec.visibility_of_element_located((By.XPATH, '/html/body/section/div[1]/div/div/div/div/div[2]/div/div[2]/button[2]'))).click()
WebDriverWait(driver, 15).until(ec.visibility_of_element_located((By.XPATH, '/html/body/reach-portal/div[3]/div/div/div/div/div/div/div/div/div/div/div[2]/button'))).click()
print(Fore.GREEN + f"SUCCESSFULLY BOUGHT XBOX GAMEPASS IN {email}:{password}")

try:
    WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, '//*[@id="store-cart-root"]/div/div/div[2]/div/div[2]/button[2]'))).click()
    WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, '/html/body/reach-portal/div[3]/div/div/div/div/div/div/div/div/div/div/div[2]/button'))).click()
    print(Fore.GREEN + f"SUCCESSFULLY BOUGHT XBOX GAMEPASS IN {email}:{password}")
    print(Style.RESET_ALL)
    with open('./data/accounts.txt', 'r+', encoding='utf-8') as file:
        def remove_line(bruh1,lineToSkip):
            with open(bruh1,'r') as read_file:
                lines = read_file.readlines()
                currentLine = 1
                with open(bruh1,'w') as write_file:
                    for line in lines:
                        if currentLine == lineToSkip:
                            pass
                        else:
                            write_file.write(line)
                            currentLine += 1
                            remove_line("./data/accounts.txt",1)
                            with open('./data/accounts_with_gp.txt', 'w') as accounts_with_gp:
                                accounts_with_gp.write(f'{email}:{password}')
except:
    print(Fore.RED + "THE CC DOESN'T WORK DELETING NON WORKING CC PLEASE RUN THIS FILE AGAIN")
    print(Style.RESET_ALL)
    with open('./data/cards.txt', 'r+', encoding='utf-8') as file:
        def remove_line(bruh2,lineToSkip):
            with open(bruh2,'r') as read_file:
                lines = read_file.readlines()
                currentLine = 1
                with open(bruh2,'w') as write_file:
                    for line in lines:
                        if currentLine == lineToSkip:
                            pass
                        else:
                            write_file.write(line)
                            currentLine += 1
                            remove_line("./data/cards.txt",1)
    time.sleep(10)
    driver.quit()





account = open("./data/accounts_with_gp.txt",'r').read().splitlines()
for i in account:
    email = i.split("|")[0]
    password = i.split("|")[1]
    getlink(email,password)
    removeaccount(i)

    
