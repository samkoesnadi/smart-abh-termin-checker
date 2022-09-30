import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from pysine import sine


sine(frequency=440.0, duration=0.5)  # plays a 1s sine wave at 440 Hz
driver = webdriver.Chrome()

n = 0
while True:
    print(f"------------------{n}------------------")
    n += 1
    driver.get("https://otv.verwalt-berlin.de/ams/TerminBuchen")
    driver.implicitly_wait(60)

    # page 1
    driver.find_element(By.LINK_TEXT, "Termin buchen").click()

    # page 2
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, ".label-right > p").click()
    driver.find_element(By.CSS_SELECTOR, "#applicationForm\:managedForm\:proceed > .ui-button-text").click()

    # page 3
    time.sleep(2)
    select = Select(driver.find_element(By.ID, 'xi-sel-400'))
    select.select_by_visible_text("Indonesien")
    select = Select(driver.find_element(By.ID, 'xi-sel-422'))
    select.select_by_visible_text("eine Person")
    select = Select(driver.find_element(By.ID, 'xi-sel-427'))
    select.select_by_visible_text("nein")

    time.sleep(4)

    driver.find_element(By.CSS_SELECTOR, ".kachel-437-0-1 p").click()

    time.sleep(1)

    driver.find_element(By.CSS_SELECTOR, ".accordion-437-0-1-1 p").click()

    time.sleep(3)

    driver.find_element(By.CSS_SELECTOR, ".level3:nth-child(11) > label").click()

    time.sleep(4)

    driver.find_element(By.CSS_SELECTOR, "#applicationForm\:managedForm\:proceed").click()

    # page 4

    time.sleep(15)

    successful = "Dienstleistung sind aktuell keine Termine frei" not in driver.page_source

    if successful:
        while True:
            sine(frequency=440.0, duration=0.5)
            time.sleep(0.1)

    driver.delete_all_cookies()

driver.close()
