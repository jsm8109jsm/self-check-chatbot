import pyautogui
import time
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

username = input('이름을 입력하세요(예시 : 정승민) : ')
birthday = input('생일을 입력하세요(예시 : 050203) : ')

city = {
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

driver = webdriver.Chrome()
url = 'https://hcs.eduro.go.kr/#/loginHome'
driver.get(url)

time.sleep(1)

# go = pyautogui.locateCenterOnScreen('images/go.png', confidence=0.8)
# pyautogui.click(go)

driver.find_element(By.ID, 'btnConfirm2').click()

# driver.find_element(By.ID, 'user_name_input').click()
driver.find_element(By.ID, 'schul_name_input').click()
pyautogui.typewrite(['enter'])
driver.find_element(By.ID, 'user_name_input').send_keys(username)
driver.find_element(By.ID, 'birthday_input').send_keys(birthday)

# time.sleep(0.5)
# name = pyautogui.locateCenterOnScreen('images/name.png', confidence=0.8)
# pyautogui.click(name)
# time.sleep(1)
# print(a)
# pyautogui.typewrite(a)
