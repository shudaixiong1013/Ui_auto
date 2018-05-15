from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import time
import os

# chrome路径
chromedriver = 'chromedriver.exe'
# 判断是否存在
isexists = os.path.exists(chromedriver)
if isexists is False:
    print('chromedriver.exe 不存在')

os.environ['webdriver.chrome.driver'] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.maximize_window()


# 所选元素高亮dfs
def highlight(element):
    driver = element._parent

    def apply_style(s):
        driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element, s)

    original_style = element.get_attribute('style')
    apply_style("background: yellow; border: 2px solid red;")
    time.sleep(3)
    apply_style(original_style)


driver.get('http://passport-test.zring.sz/login.html')
print(driver.title)
sleep(2)

highlight(driver.find_element_by_xpath("//input[@placeholder='请输入账号']"))
driver.find_element_by_xpath("//input[@placeholder='请输入账号']").send_keys('test01')
driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/input').send_keys('12345678')
driver.find_element_by_xpath('//*[@id="app"]/div[2]/a').click()
sleep(1)
loginXpath = driver.find_element_by_xpath('/html/body/div[2]/div/a[4]')
ActionChains(driver).move_to_element(loginXpath).perform()

sleep(3)
driver.quit()
