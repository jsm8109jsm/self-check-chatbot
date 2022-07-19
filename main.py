from typing import Union, Any

import pyautogui
import time
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

city = input('당신의 학교가 있는 시/도를 입력하세요(예시 : 부산광역시) : ')
schoolLevel = input('당신의 학교의 학교 등급을 입력하세요(예시 : 고등학교) : ')
username = input('이름을 입력하세요(예시 : 정승민) : ')
birthday = input('생일을 입력하세요(예시 : 050203) : ')

cityDict = {
    "서울특별시": 1,
    "부산광역시": 2,
    "대구광역시": 3,
    "인천광역시": 4,
    "광주광역시": 5,
    "대전광역시": 6,
    "울산광역시": 7,
    "세종특별자치시": 8,
    "경기도": 9,
    "강원도": 10,
    "충청북도": 11,
    "충청남도": 12,
    "전라북도": 13,
    "전라남도": 14,
    "경상북도": 15,
    "경상남도": 16,
    "제주특별자치도": 17
}

schoolLevelDict = {
    "유치원": 1,
    "초등학교": 2,
    "중학교": 3,
    "고등학교": 4,
    "특수학교 등": 5
}

for key, value in cityDict.items():
    if key == city:
        cityValue = value

for key, value in schoolLevelDict.items():
    if key == schoolLevel:
        schoolLevelValue = value


driver = webdriver.Chrome()
url = 'https://hcs.eduro.go.kr/#/loginHome'
driver.get(url)

time.sleep(1)
driver.find_element(By.ID, 'btnConfirm2').click()

driver.find_element(By.ID, 'schul_name_input').click()
time.sleep(1)

for i in range(cityValue):
    driver.find_element(By.ID, 'sidolabel').send_keys(Keys.ARROW_DOWN)

for i in range(schoolLevelValue):
    driver.find_element(By.ID, 'crseScCode').send_keys(Keys.ARROW_DOWN)

# driver.find_element(By.CLASS_NAME, "layerFullBtn").click()
# driver.find_element(By.ID, 'user_name_input').send_keys(username)
# driver.find_element(By.ID, 'birthday_input').send_keys(birthday)