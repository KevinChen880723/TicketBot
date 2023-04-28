from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


# Facebook logging information
fb_account = ''
fb_password = ''

options = Options()
options.add_argument("--start-maximized")

options.add_experimental_option("prefs", { 
    "profile.default_content_setting_values.notifications": 1 
})

#goto facebook login
chrome = webdriver.Chrome('./chromedriver', chrome_options=options)
fb_web = 'https://tixcraft.com/login/facebook'
chrome.get(fb_web)

#Enter facebook account
exe = chrome.find_element("xpath", '//*[@id="email"]').send_keys(fb_account)
exe = chrome.find_element("xpath", '//*[@id="pass"]').send_keys(fb_password)
time.sleep(2)
exe = chrome.find_element("xpath", '//*[@id="loginbutton"]').click()
time.sleep(1)
chrome.get("https://tixcraft.com/activity/detail/23_fujirock")
# chrome.get("https://tixcraft.com/activity/detail/23_caodong?fbclid=IwAR1X64RTDbbLO_iEDXy7-3EyARXcce6HsuT1z3MfKdSHLDxgySZfajZwAkI")	# 草東
time.sleep(1)
exe = chrome.find_element("xpath", '//*[@id="onetrust-accept-btn-handler"]').click()	# 接受cookie
time.sleep(1)
chrome.execute_script("window.scrollBy(0, 500)")
time.sleep(1)
chrome.execute_script("window.scrollBy(0, 500)")
exe = chrome.find_element("xpath", '//*[@id="tab-func"]/li[1]/a/div').click()	
time.sleep(2)

startsell = False
while startsell==False:	
	try:
		exe = chrome.find_element("xpath", '//*[@id="gameList"]/table/tbody/tr[1]/td[4]/button').click()						# 點擊第一個場次	
		exe = chrome.find_element("xpath", '//*[@id="TicketForm_ticketPrice_06"]').click()						# 點及下拉式清單
		exe = chrome.find_element("xpath", '//*[@id="TicketForm_ticketPrice_06"]/option[2]').click()						# 選擇一個人
		chrome.execute_script("window.scrollBy(0, 500)")	# 往下滑找同意按鈕
		time.sleep(0.1)
		checkbox = chrome.find_element("id", 'TicketForm_agree').click()	# 點及同意
		startsell = True
	except:
		time.sleep(0.123)
		# 如果按鈕還沒跳出來就重新整理再按一次搶票按鈕，頁面就會更新
		exe = chrome.find_element("xpath", '//*[@id="tab-func"]/li[1]/a/div').click()
		continue
while True:
	pass