from selenium import webdriver
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome()
driver.get("https://seleniumbase.io/demo_page")

# Mengisi Text Input Field menjadi Nabil Bariq Rabbani
def myTextInput():
    driver.find_element(by="id", value="myTextInput").send_keys("Nabil Bariq Rabbani")

# Mengisi Pre-Filled Text Input Field menjadi Mr.
def myTextInput2():
    driver.find_element(by="id", value="myTextInput2").send_keys("Mr. ")
    
# Mengisi Placeholder Text Field menjadi Enter your name here..
def placeholderText():
    driver.find_element(by="id", value="placeholderText").send_keys("Enter your name here..")

# Mengisi Text Area menjadi Tugas TUT GitHub Kelompok
def myTextArea():
    driver.find_element(by="id", value="myTextarea").send_keys("Tugas TUT GitHub Kelompok")

# Melakukan click pada Button sehingga berubah menjadi Purple
def myButton():
    driver.find_element(by="id", value="myButton").click()

# Mengubah value dari Select Dropdown menjadi 25%
def mySelect():
    dropdown = driver.find_element(by="id", value="mySelect")
    select = Select(dropdown)
    select.select_by_value("25%")

# Mengubah value dari Input Slider Control menjadi 47
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

# Meminta input agar program tidak langsung berhenti
input("")
driver.quit()