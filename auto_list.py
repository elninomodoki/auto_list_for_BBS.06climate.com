import os  
import time
from selenium import webdriver
#测试网络连通性
ping_value=os.system('ping www.baidu.com')
#如果网络通畅自动登陆气象家园
if ping_value == 0:
    browser = webdriver.Chrome()
    browser.get('http://bbs.06climate.com/forum.php')
    #用户名
    username="xxxxxxxx"
    #密码
    passwd="xxxxxxxx"
    #自动登陆
    browser.implicitly_wait(10)
    elem=browser.find_element_by_id("ls_username")
    elem.send_keys(username)
    elem=browser.find_element_by_id("ls_password")
    elem.send_keys(passwd)
    elem=browser.find_element_by_xpath('//*[@id="lsform"]/div/div[1]/table/tbody/tr[2]/td[3]/button')
    elem.click()
    elem=browser.find_element_by_xpath('//*[@id="pper_a"]')
    elem.click()
    browser.implicitly_wait(10)
    browser.quit()  
    elem=browser.find_element_by_xpath('//*[@id="myprompt_check"]')
    elem.click()
