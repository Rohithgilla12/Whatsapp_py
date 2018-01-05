import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from termcolor import colored, cprint
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
def send_msg(name,text):
    elem=driver.find_element_by_xpath('//*[@id="input-chatlist-search"]')
    elem.click()
    elem.send_keys(name)
    elem.send_keys(Keys.ENTER)
    elem3=driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    elem3.click()
    elem3.send_keys(text)
    elem3.send_keys(Keys.ENTER)
chats=[]
def get_chats():
    chats=driver.find_elements_by_class_name('chat-title')
    for i in chats:
        print i.text
    return chats
chromedriver='/home/rohith-gilla/chromedriver'
os.environ["webdriver.chrome.driver"]=chromedriver
driver=webdriver.Chrome(chromedriver)
driver.get('https://web.whatsapp.com')
opt=input(bcolors.BOLD+'Press 1 once you have verified : '+bcolors.ENDC)
if(opt == 1):
    name=raw_input('Name of the person you wish to text : ')
    text=raw_input('Your message body : '+bcolors.OKBLUE)
#    for i in range(1000):
    send_msg(name,text)
    chats=get_chats()
    print bcolors.ENDC
else:
    print bcolors.FAIL+"Verify ASAP"
