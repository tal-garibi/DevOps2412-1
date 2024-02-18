from selenium import webdriver
from time import sleep
dr = webdriver.Chrome()
dr.get("file:///Users/talgaribi/Downloads/tip_calc/index.html?")
#dr.get("https://github.com")
billamt = dr.find_element(by="id", value="billamt")
billamt.send_keys("100")
dr.find_element(by="xpath", value="//*[@id=\"serviceQual\"]/option[3]").click()
dr.find_element(by="id", value="peopleamt").send_keys("5")
dr.find_element(by="id", value="calculate").click()
actual = dr.find_element(by="id", value="tip").text
expected = "8.0"
assert  expected == actual
#assert במידה והתנאי מתקיים הכל תקין במידה ולא נקבל שגיאה
