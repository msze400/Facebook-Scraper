
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


url = 'https://www.facebook.com/search/posts?q=math%20tutor%20&filters=eyJyZWNlbnRfcG9zdHM6MCI6IntcIm5hbWVcIjpcInJlY2VudF9wb3N0c1wiLFwiYXJnc1wiOlwiXCJ9IiwicnBfY3JlYXRpb25fdGltZTowIjoie1wibmFtZVwiOlwiY3JlYXRpb25fdGltZVwiLFwiYXJnc1wiOlwie1xcXCJzdGFydF95ZWFyXFxcIjpcXFwiMjAyMlxcXCIsXFxcInN0YXJ0X21vbnRoXFxcIjpcXFwiMjAyMi0xXFxcIixcXFwiZW5kX3llYXJcXFwiOlxcXCIyMDIyXFxcIixcXFwiZW5kX21vbnRoXFxcIjpcXFwiMjAyMi0xMlxcXCIsXFxcInN0YXJ0X2RheVxcXCI6XFxcIjIwMjItMS0xXFxcIixcXFwiZW5kX2RheVxcXCI6XFxcIjIwMjItMTItMzFcXFwifVwifSJ9'

driver = webdriver.Chrome('/Users/msze/Desktop/chromedriver')


# driver.get("http://selenium.dev")
driver.get(url);

driver.implicitly_wait(10)

driver.find_element_by_xpath('//*[@id="email"]').send_keys('matthew.t.sze@gmail.com')
driver.find_element_by_xpath('//*[@id="pass"]').send_keys('facebookscraper3389')
driver.find_element_by_xpath('//*[@id="loginbutton"]').click();

driver.implicitly_wait(10)

driver.get(url);


driver.implicitly_wait(15)

elements = driver.find_elements_by_xpath("//div[contains(@class, 'kvgmc6g5') and contains (@class, 'cxmmr5t8') and contains (@class, 'oygrvhab') and contains (@class, 'hcukyx3x') and contains (@class, 'c1et5uql')]")

for ele in elements:
        print(ele.get_attribute('textContent'))



# driver.quit()