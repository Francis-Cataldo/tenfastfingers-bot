from selenium import webdriver
import time
import pytesseract
from PIL import Image
import requests
import urllib

driver = webdriver.Chrome()

driver.get('https://10fastfingers.com/')

def anticheat_pass():
    driver.get('https://10fastfingers.com/anticheat')

    driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[4]/div/div/div[1]/table/tbody/tr[1]/td[1]/a').click()
    driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[4]/div/div/div[3]/div[1]/button').click()

    url = driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[4]/div/div/div[3]/div[1]/img').get_attribute("src")
    print(url)
    time.sleep(2)
    with open('cheat.png', 'wb') as file:
        file.write(driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[4]/div/div/div[3]/div[1]').screenshot_as_png)

    img = Image.open('cheat.png')
    # img.show()
    text = pytesseract.image_to_string(img)
    print(text)

    driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[4]/div/div/div[3]/textarea').send_keys(text)
    driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[4]/div/div/div[3]/button').click()
    # img =  Image()
    # img.show()


def typing_test():
    print('running')
    time.sleep(3)
    words = []
    # print(driver.find_element_by_xpath('/html/body/div[5]/div/div[4]/div/div[1]/div[7]/div[1]/div/span[1]').text)
    # for i in range(200):
    #     words.append(driver.find_element_by_xpath('/html/body/div[5]/div/div[4]/div/div[1]/div[7]/div[1]/div/span[' + str(i+1) + ']').text)
    #
    # print(len(words))\
    # print('word = ' + words[150])
    # print('word = ' + driver.find_element_by_xpath('/html/body/div[5]/div/div[4]/div/div[1]/div[7]/div[1]/div/span[100]').text)

    # ending = 0
    # for _ in range(7):
    #     for i in range(15):
    #         words.append(driver.find_element_by_xpath('/html/body/div[5]/div/div[4]/div/div[1]/div[7]/div[1]/div/span[' + str(i+1+ending) + ']').text)
    #         ending = i
    #     for i in range(15):
    #         driver.find_element_by_xpath('/html/body/div[5]/div/div[4]/div/div[1]/div[7]/div[2]/div/div[1]/input').send_keys(words[i+ending] + ' ')
    #         time.sleep(.1)
    #         # /html/body/div[5]/div/div[4]/div/div[1]/div[7]/div[1]/div/span[21]
    for i in range(250):
        driver.find_element_by_xpath('/html/body/div[5]/div/div[4]/div/div[1]/div[7]/div[2]/div/div[1]/input').send_keys(driver.find_element_by_xpath('/html/body/div[5]/div/div[4]/div/div[1]/div[7]/div[1]/div/span[' + str(i+1) + ']').text + ' ')
        # time.sleep(.21) 141
    time.sleep(15)
    # anticheat_pass()

def login():
    driver.get('https://10fastfingers.com/login')

    driver.find_element_by_xpath('/html/body/div[4]/div/div[4]/div/div[1]/div/div[2]/div/div[2]/form/div[3]/input').send_keys(email)
    driver.find_element_by_xpath('/html/body/div[4]/div/div[4]/div/div[1]/div/div[2]/div/div[2]/form/div[4]/input').send_keys(password)


    # typing_test()

def get_login_creds():
    global email, password
    path = "./creds.txt"
    info = open(path, 'r')
    email = info.readline()
    password = info.readline()


get_login_creds()
login()
typing_test()
# anticheat_pass()
time.sleep(10)

# driver.quit()
