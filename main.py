from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


def main():

    service = Service(r"C:\Users\dough\OneDrive\Documents\chromedriver\chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    driver.get("https://orteil.dashnet.org/cookieclicker/")

    cookie = driver.find_element(By.ID, "bigCookie")

    counter = 0
    timer = time.time() + 10000
    buy_time = time.time() + 2
    while timer > time.time():
        cookie.click()
        if buy_time < time.time():
            upgrades = driver.find_elements(By.CSS_SELECTOR, "#upgrades .enabled")
            for upgrade in upgrades:
                try:
                    upgrade.click()
                except:
                    pass
            tools = driver.find_elements(By.CSS_SELECTOR, ".unlocked")
            quantites = driver.find_elements(By.CSS_SELECTOR, ".unlocked .content .owned")
            # tool_quantity = {}
            # tool_quantity = driver.find_element(By.CSS_SELECTOR, ".content .title.owned").text
            for tool in reversed(tools):
                tool_quantity = quantites[tools.index(tool)].text
                if tool_quantity == "":
                    try:
                        tool.click()
                    except:
                        pass
                else:
                    try:
                        if int(tool_quantity) < 50:
                            tool.click()
                    except:
                        pass
            windows = driver.find_elements(By.CSS_SELECTOR, "#notes .close")
            for window in windows:
                try:
                    window.click()
                except:
                    pass
            counter += 1
            print(counter)
            if counter < 20:
                buy_time = time.time() + 2
            elif counter < 35:
                buy_time = time.time() + 8
            elif counter < 500:
                buy_time = time.time() + 30
            elif counter < 1000:
                buy_time = time.time() + 45
            elif counter < 1500:
                buy_time = time.time() + 60
            elif counter < 2000:
                buy_time = time.time() + 90

    print(driver.find_element(By.CSS_SELECTOR, "#cookies").text.split(":")[1].strip())
    print(driver.find_element(By.CSS_SELECTOR, "#cookies").text.split(" ")[0])


if __name__ == '__main__':
    main()
