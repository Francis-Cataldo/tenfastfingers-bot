from selenium import webdriver
import time
import pytesseract
from PIL import Image


class Bot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.email, self.password = self.get_login_creds()
        self.login()
    def anticheat_pass(self):
        self.driver.get('https://10fastfingers.com/anticheat')

        self.driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[4]/div/div/div[1]/table/tbody/tr[1]/td[1]/a').click()
        self.driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[4]/div/div/div[3]/div[1]/button').click()

        url = self.driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[4]/div/div/div[3]/div[1]/img').get_attribute("src")
        print(url)
        time.sleep(2)
        with open('cheat.png', 'wb') as file:
            file.write(self.driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[4]/div/div/div[3]/div[1]').screenshot_as_png)

        img = Image.open('cheat.png')
        # img.show()
        text = pytesseract.image_to_string(img)
        print(text)

        self.driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[4]/div/div/div[3]/textarea').send_keys(text)
        self.driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[4]/div/div/div[3]/button').click()
        # img =  Image()
        # img.show()


    def typing_test(self):
        print('running')
        time.sleep(3)
        words = []
        # print(self.driver.find_element_by_xpath('/html/body/div[5]/div/div[4]/div/div[1]/div[7]/div[1]/div/span[1]').text)
        # for i in range(200):
        #     words.append(self.driver.find_element_by_xpath('/html/body/div[5]/div/div[4]/div/div[1]/div[7]/div[1]/div/span[' + str(i+1) + ']').text)
        #
        # print(len(words))\
        # print('word = ' + words[150])
        # print('word = ' + self.driver.find_element_by_xpath('/html/body/div[5]/div/div[4]/div/div[1]/div[7]/div[1]/div/span[100]').text)

        # ending = 0
        # for _ in range(7):
        #     for i in range(15):
        #         words.append(self.driver.find_element_by_xpath('/html/body/div[5]/div/div[4]/div/div[1]/div[7]/div[1]/div/span[' + str(i+1+ending) + ']').text)
        #         ending = i
        #     for i in range(15):
        #         self.driver.find_element_by_xpath('/html/body/div[5]/div/div[4]/div/div[1]/div[7]/div[2]/div/div[1]/input').send_keys(words[i+ending] + ' ')
        #         time.sleep(.1)
        #         # /html/body/div[5]/div/div[4]/div/div[1]/div[7]/div[1]/div/span[21]
        for i in range(344):
            self.driver.find_element_by_xpath('/html/body/div[5]/div/div[4]/div/div[1]/div[7]/div[2]/div/div[1]/input').send_keys(self.driver.find_element_by_xpath('/html/body/div[5]/div/div[4]/div/div[1]/div[7]/div[1]/div/span[' + str(i+1) + ']').text + ' ')
            if i > 335:
                time.sleep(.2)
            # time.sleep(.21) 141
        time.sleep(15)
        # anticheat_pass()

    def login(self):


        self.driver.get('https://10fastfingers.com/login')

        self.driver.find_element_by_xpath('/html/body/div[4]/div/div[4]/div/div[1]/div/div[2]/div/div[2]/form/div[3]/input').send_keys(self.email)
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div[4]/div/div[1]/div/div[2]/div/div[2]/form/div[4]/input').send_keys(self.password)


        # typing_test()

    def get_login_creds(self):
        path = "./creds.txt"
        info = open(path, 'r')
        email = info.readline()
        password = info.readline()

        return email, password



    # anticheat_pass()

    # self.driver.quit()
