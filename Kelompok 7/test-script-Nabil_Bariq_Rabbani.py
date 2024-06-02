from selenium import webdriver
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome()
driver.get("https://seleniumbase.io/demo_page")

def myTextInput():
    driver.find_element(by="id", value="myTextInput").send_keys("Nabil Bariq Rabbani")

def myTextInput2():
    driver.find_element(by="id", value="myTextInput2").send_keys("Mr. ")
    
def placeholderText():
    driver.find_element(by="id", value="placeholderText").send_keys("Enter your name here..")

def myTextArea():
    driver.find_element(by="id", value="myTextarea").send_keys("Tugas TUT GitHub Kelompok")

def myButton():
    driver.find_element(by="id", value="myButton").click()

def mySelect():
    dropdown = driver.find_element(by="id", value="mySelect")
    select = Select(dropdown)
    select.select_by_value("25%")

def mySlider():
    slider = driver.find_element(by="id", value="mySlider")
    driver.execute_script("arguments[0].value = arguments[1];", slider, 47)
    driver.execute_script("arguments[0].dispatchEvent(new Event('change'));", slider)

myTextInput()
myTextInput2()
myTextArea()
myButton()
mySelect()
mySlider()
placeholderText()

input("")
driver.quit()