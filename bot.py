from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get('https://10fastfingers.com/')

def typing_test():
    print('running')
    time.sleep(5)
    words = []
    # print(driver.find_element_by_xpath('/html/body/div[5]/div/div[4]/div/div[1]/div[7]/div[1]/div/span[1]').text)
    # for i in range(200):
    #     words.append(driver.find_element_by_xpath('/html/body/div[5]/div/div[4]/div/div[1]/div[7]/div[1]/div/span[' + str(i+1) + ']').text)
    #
    # print(len(words))
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
    for i in range(120):
        driver.find_element_by_xpath('/html/body/div[5]/div/div[4]/div/div[1]/div[7]/div[2]/div/div[1]/input').send_keys(driver.find_element_by_xpath('/html/body/div[5]/div/div[4]/div/div[1]/div[7]/div[1]/div/span[' + str(i+1) + ']').text + ' ')
        time.sleep(.1)

def login():
    driver.get('https://10fastfingers.com/login')

    driver.find_element_by_xpath('/html/body/div[4]/div/div[4]/div/div[1]/div/div[2]/div/div[2]/form/div[3]/input').send_keys(email)
    driver.find_element_by_xpath('/html/body/div[4]/div/div[4]/div/div[1]/div/div[2]/div/div[2]/form/div[4]/input').send_keys(password)


    typing_test()

def get_login_creds():
    global email, password
    path = "./creds.txt"
    info = open(path, 'r')
    email = info.readline()
    password = info.readline()


get_login_creds()
login()
