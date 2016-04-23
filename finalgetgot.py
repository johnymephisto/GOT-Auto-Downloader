from selenium import webdriver
import time
import schedule
import sys


#Change webdriver.Firefox to webdriver.Chrome if you use Chrome browser
#Additionally chromedriver.exe to be placed in python/Scripts folder for running Chrome
#install PhantomJS to python/Scripts folder for prefect running
#install additional modules selenium and schedule using pip instaler

#Don't freak out by seeing random windows popping up :P
#This Script requires the system to have : Python3, Torrent Client, PhantomJS , Firefox/Chrome :)

#Enjoy - johny :)

print("GOT Auto Downloader")
print("For all the GOT fans out there!! Enter the Season and Episode required, eg:-S01E01")
print("It will automatically wait for any future episodes")

url1="http://www.1377x.to/srch?search=game+of+thrones+"
url2=input("S0?E?")
print("Please wait :) :)")
url=url1+url2
flag=0



def mozil():
    try:
        global flag
        flag=1
        browser = webdriver.Firefox()
        main_window = browser.current_window_handle
        browser.get(url)
        
        el=browser.find_element_by_partial_link_text(url2).click();
        
        time.sleep(1)
        el2=browser.find_element_by_id('magnetdl').click();
            
        st1=browser.title
            
            
            
    except:
            
        sys.exit("Done")
        
def job():
    try:
        browser = webdriver.PhantomJS()
        browser.get(url)
        el=browser.find_element_by_partial_link_text(url2).click();
            
        browser.quit()
        mozil()
    except:
        print('I will wait more!')
        browser.quit()

job()
schedule.every(1800).seconds.do(job)

while flag==0:
    schedule.run_pending()
    time.sleep(1)
    
