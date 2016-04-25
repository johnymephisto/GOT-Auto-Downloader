from selenium import webdriver
import time
import schedule
import sys
import os


#Only works if you have Mozilla Firefox and magnet automatically set for torrent application
#install additional modules selenium and schedule using pip installer

#Don't freak out by seeing random windows popping up :P
#This Script requires the system to have : Python3, Torrent Client, PhantomJS , Firefox/Chrome :)

#Enjoy - johny :)

path=os.path.expanduser('~\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\')
path=path+os.listdir(path)[0]


print("GOT Auto Downloader")
print("For all the GOT fans out there!! Enter the Season and Episode required, eg:-S01E01")
print("It will automatically wait for any future episodes")

url=["http://www.1377x.to/srch?search=game.of.thrones+","http://www.1377x.to/srch?search=game+of+thrones+","http://www.1377x.to/srch?search=thrones+"]
urlx=input("\nS0?E?: ")

print("Please wait :) :)")

flag=0



def mozil(urlf):
    try:
        global flag
        flag=1
        profile = webdriver.FirefoxProfile(path)
        browser = webdriver.Firefox(profile)
        
        browser.get(urlf)
        
        el=browser.find_element_by_partial_link_text(urlx).click();
        
        time.sleep(1)
        el2=browser.find_element_by_id('magnetdl').click();
            
        time.sleep(2)
        browser.quit()
            
    except:
            
        sys.exit("Done")
        
def job():
    try:
        browser = webdriver.PhantomJS()
        for i in url:
            if flag==0:
                try:
                    browser.get(i+urlx)
                    el=browser.find_element_by_partial_link_text(urlx).click();
                    flag=1
                    urlf=i
                    break
                except:
                    flag=0
        if flag==0:
            raise Exception
            
        browser.quit()
        mozil(urlf)
        
    except Exception:
        print('I will wait more!')
        browser.quit()

job()
schedule.every(1800).seconds.do(job)

while flag==0:
    schedule.run_pending()
    time.sleep(1)
    
