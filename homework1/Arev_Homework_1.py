from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Edge(executable_path="C:\\Windows\\msedgedriver.exe")
driver.get('https://www.demoblaze.com/')

def task_1():
    print(driver.title)
    print(driver.current_url)
    driver.save_screenshot("screenshot.png")

# task_1()

# TASK2.   Locate header elements using different XPaths(not absolute),Print “Element is located” if element is found”,
# Print  “No Such Element” if element is not found”  You can use “Try Except”
def task_2():
    try:
        el_1 = driver.find_element(By.XPATH, "//*[contains(text(),'Home')]")
        print(el_1.text, 'Element is located')
    except:
        print("No Such ELement")
    try:
        el_2 = driver.find_element(By.XPATH,"//*[@id = 'cartur']")
        print(el_2.text, 'Element is located')
    except:
        print("No Such Element")

    try:
        el_3 = driver.find_element(By.XPATH,"//*[@id = 'signout']")
        print(el_3.text, 'Element is located')
    except:
        print("No Such Element")

    try:
        el_4 = driver.find_element(By.XPATH, "//a[contains(text(),'Cont')]")
        print(el_4.text, 'Element is located')
    except:
        print("No Such Element")
    try:
        el_5 = driver.find_element(By.XPATH, "//*[@data-target='#videoModal']")
        print(el_5.text, 'Element is located')
    except:
        print("No Such Element")
    try:
        el_6 = driver.find_element(By.XPATH, "//*[@id='login2']")
        print(el_6.text, 'Element is located')
    except:
        print("No Such Element")
    try:
        el_7 = driver.find_element(By.XPATH, "//*[@id='signin2']")
        print(el_7.text, 'Element is located')
    except:
        print("No Such Element")

# task_2()



# TASK3...Locate Categories Elements using different CSS selectors, Print “Element is located” if element is found”
# Print  “No Such Element” if element is not found”, You can use “Try Except”
def task3_version1():
    categories_list =[]
    items = driver.find_elements(By.CSS_SELECTOR, "a[id= 'itemc']")
    for el in items:
        categories_list.append(el.text)
    if 'Phones' in categories_list:
        print( '"Phones" element is located')
    else:
        print("No Such Element")
    if 'Laptops' in categories_list:
        print( '"Laptops" element is located')
    else:
        print("No Such Element")
    if 'Monitors' in categories_list:
        print( '"Monitors" element is located')
    else:
        print("No Such Element")
    if 'iPads' in categories_list:
        print( '"iPads" element is located')
    else:
        print("No Such Element")
#task3_version1()

def task3_version2():
    try:
        el_1 = driver.find_element(By.CSS_SELECTOR, "a[onclick=\"byCat('phone')\"]")
        print(el_1.text, 'Element is located')
    except:
        print("No Such ELement")
    try:
        el_2 = driver.find_element(By.CSS_SELECTOR, 'a[onclick="byCat(\'notebook\')"]')
        print(el_2.text, 'Element is located')
    except:
        print("No Such Element")

    try:
        el_3 = driver.find_element(By.CSS_SELECTOR,'a[onclick="byCat(\'monitor\')"]')
        print(el_3.text, 'Element is located')
    except:
        print("No Such Element")

    try:
        el_4 = driver.find_element(By.CSS_SELECTOR, "div[id='Barev')]")
        print(el_4.text, 'Element is located')
    except:
        print("No Such Element")
    try:
        el_5 = driver.find_element(By.CSS_SELECTOR, "a[class='no such el']")
        print(el_5.text, 'Element is located')
    except:
        print("No Such Element")

#task3_version2()


#TASK4... Find Highest Price item in first page and print it’s name and price
def task_4():
    driver.implicitly_wait(10)
    elements = driver.find_elements(By.CSS_SELECTOR, "a[class='hrefch']")
    prices = driver.find_elements(By.CSS_SELECTOR,'div[class="card-block"] >h5')
    items_list = []
    prices_list = []
    for item in elements:
        items_list.append(item.text)
    for price in prices:
        elem = price.text[1:]
        prices_list.append(int(elem))
    max_price = max(prices_list)
    max_price_index = prices_list.index(max_price)
    print(f'The most expensive item is {items_list[max_price_index]} - {max_price}$ ')

# task_4()


# TEST5...Add a simple test case for this site(E.G. verify that phones, laptops and monitor pages are loaded correctly)
def task_5():
    global driver
    driver.implicitly_wait(10)
    driver.find_element(By.CSS_SELECTOR, "a[onclick=\"byCat('phone')\"]").click()
    assert driver.find_element(By.XPATH, "//*[text()='HTC One M9']").is_displayed()

    driver.find_element(By.CSS_SELECTOR, "a[onclick=\"byCat('notebook')\"]").click()
    assert driver.find_element(By.XPATH, "//*[text()='MacBook Pro']").is_displayed()
    # or this version
    # laptops_group = driver.find_element(By.XPATH, "//*[text()='MacBook Pro']")
    # print(laptops_group.text)

    driver.find_element(By.CSS_SELECTOR, "a[onclick=\"byCat('monitor')\"]").click()
    driver.find_element(By.XPATH, '//*[@id = "next2"]').click()
    assert driver.find_element(By.XPATH, "//*[text()='ASUS Full HD']").is_displayed()


task_5()


# driver.quit()