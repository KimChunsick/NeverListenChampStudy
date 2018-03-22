from selenium import webdriver
import time
import os
from Scripts.Command import *

path = os.path.abspath("..") + '/chromedriver'
browser = webdriver.Chrome(os.getcwd())
browser = webdriver.Chrome(path)
browser.get("http://kookmin.champstudy.com/")

id = input("챔프스터디 ID를 입력해주세요: ")
pw = input("챔프스터디 PW를 입력해주세요: ")

program = Login(id, pw, browser)
program.Excute()

subject = input("들을려는 수업 고르기 (리딩: R, 리스닝: L) : ");
read = '//*[@id="layer1"]/table/tbody/tr[2]/td[2]/table/tbody/tr[10]/td/table/tbody/tr[4]/td[7]/a/img'
listening = '//*[@id="layer1"]/table/tbody/tr[2]/td[2]/table/tbody/tr[10]/td/table/tbody/tr[7]/td[7]/a/img'
xpath = read if subject == 'R' else listening
program = CourseList((subject == read), xpath, browser)
program.Excute()

browser.quit()