from time import sleep
from selenium import webdriver


class TestCase(object):

    def test(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.baidu.com')
        self.driver.find_element_by_id('kw').send_keys('selenuim')
        sleep(2)
        self.driver.find_element_by_id('su').click()
        sleep(2)
        self.driver.quit()


if __name__ == '__main__':
    case = TestCase()
    case.test()
