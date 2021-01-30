from selenium import webdriver


driver = webdriver.Chrome(executable_path='chromedriver.exe')


driver.get('https://www.youtube.com/playlist?list=WL')


driver.quit()
