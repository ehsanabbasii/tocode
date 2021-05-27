# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 02:44:42 2021

@author: EHSAN
"""

from selenium import webdriver
from time import sleep
import time
import pandas as pd
from datetime import datetime




options = webdriver.ChromeOptions()

#Change this to your default downloading folder
preferences = {"download.default_directory": r"E:\py", "safebrowsing.enabled": "false"}

options.add_experimental_option("prefs", preferences)

browser = webdriver.Chrome(options=options)


def get_mofid():
    try:
        browser.get("https://d.easytrader.emofid.com/")
        browser.implicitly_wait(5)
    except :
        print("couldn't load the page!")

def login(username,password):
    login_code_username=browser.find_element_by_name(name='Username')
    login_code_username.send_keys(username)
    login_code_pw=browser.find_element_by_name(name='Password')
    login_code_pw.send_keys(password)
    
    
    
    try :
        login_char=browser.find_element_by_id("Captcha")
        login_char.click()
        
    
    except:
        print("rechapta wasn't in the field!")
        
        
    def login_click_func():
        login_click=browser.find_element_by_id("submit_btn")
        login_click.click()
        try :
            login_click()

        except:
            print("You were slow to enter rechapta! ===> 3 seconds again!")
            return 1
    sleep(4)        
    login_click_func()
    
    
    
    



def download_excel():
    
    browser.implicitly_wait(30)
    try :
        extra_elm=browser.find_element_by_class_name("btn.btn-lg.btn-block.btn-success.mt-auto.text-light")
        extra_elm.click()
    except :
        print("no extra btn!")
        
    excel_btn=browser.find_element_by_class_name("icon.mdi.mdi-file-excel-outline.mdi-18px.text-success")    
    excel_btn.click()     
    
    
    sleep(2)
    


def search_stock(name):
    search_btn=browser.find_element_by_class_name("mdi.mdi-24px.mdi-magnify")
    search_btn.click()
    search_box=browser.find_element_by_class_name("form-control.pl-5.ng-pristine.ng-valid.ng-touched")
    search_box.click()
    search_box.send_keys(name)
    
    sleep(0.5)
    browser.implicitly_wait(0.5)
    stock_click=browser.find_element_by_xpath("//a[text()='{}']".format(name))
    stock_click.click()
    
    
def close():
    browser.close()    

'''      
import test 
login(a,b)
download_excel()
'''