from selenium import webdriver
import time

class Command:
    def Excute(self): pass

class Login(Command): # 로그인 하고 내 강의실까지 눌러보리기
    def __init__(self, id, pw, browser):
        self.id = id
        self.pw = pw
        self.browser = browser

    def Excute(self):
        self.browser.switch_to_window(self.browser.window_handles[1])
        self.browser.close()
        self.browser.switch_to_window(self.browser.window_handles[0])

        inputBox = self.browser.find_element_by_id("id")
        inputBox.send_keys(self.id)
        inputBox = self.browser.find_element_by_id("pw")
        inputBox.send_keys(self.pw)
        inputBox.submit()

        time.sleep(1)

        goMyClass = self.browser.find_element_by_xpath('//*[@id="layer2"]/div/div[2]/div/div[1]/table/tbody/tr[5]/td/a/img')
        goMyClass.click()

        self.browser.switch_to_window(self.browser.window_handles[1])
        self.browser.close()
        self.browser.switch_to_window(self.browser.window_handles[0])

        time.sleep(1)

class CourseList(Command): # 강의 리스트
    def __init__(self, isRead, xpath, browser):
        self.xpath = xpath
        self.browser = browser
        self.count = 4
        self.isRead = isRead

    def IsAlert(self):
        try:
            alert = self.browser.switch_to_alert()
            alert.accept()
            return True;
        except:
            return False;

    def Excute(self):
        course = self.browser.find_element_by_xpath(self.xpath)
        course.click()

        while True:
            try :
                attend = self.browser.find_element_by_xpath(
                    '//*[@id="layer1"]/table/tbody/tr[2]/td[2]/table/tbody/tr[9]/td/table/tbody/tr[%d]/td[7]/a/img' % self.count)
                attend.click()

                time.sleep(0.5)

                if not self.IsAlert():
                    self.browser.switch_to_window(self.browser.window_handles[1])
                    if self.isRead:
                        course = CourseReading(self.browser, self.count)
                    else:
                        course = CourseListening(self.browser)
                    course.Excute()

            except :
                break
            self.count += 2

class CourseReading(Command): #리딩 수업
    def __init__(self, browser, count):
        self.browser = browser
        self.count = (count // 2) + 6

    def Excute(self):
        self.browser.find_element_by_xpath('//*[@id="wrap"]/div/img').click()
        self.browser.find_element_by_xpath('//*[@id="_menu62%02d"]' % self.count).click()
        time.sleep(0.5)
        self.browser.execute_script('send_attendance()')
        self.browser.close()
        self.browser.switch_to_window(self.browser.window_handles[0])

class CourseListening(Command): #리스닝 수업
    count = 82
    def __init__(self, browser):
        self.browser = browser

    def Excute(self):
        self.browser.find_element_by_xpath('//*[@id="wrap"]/div/img').click()
        self.browser.find_element_by_xpath('//*[@id="_menu59%d"]' % CourseListening.count).click()
        time.sleep(0.5)
        self.browser.execute_script('send_attendance()')
        CourseListening.count += 1
        self.browser.close()
        self.browser.switch_to_window(self.browser.window_handles[0])

