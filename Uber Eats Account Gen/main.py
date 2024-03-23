from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium_stealth import stealth
from sel_safe_click import sel_safe_click
from sel_safe_entry import sel_safe_entry
from fake_info_kit import rand_email_gen, first_name_gen, last_name_gen
import time
from random import randint


CATCHALL = "(CHANGE THIS)"

# service = Service("C:/Users/imdoe/OneDrive/Desktop/Uber Eats Account Gen/chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled") 
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_experimental_option("detach", True)
options.add_argument("--window-size=1600,900")
# service = Service()
driver = webdriver.Chrome(options=options)

stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        user_agent= "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.00.0.0 Safari/537.36",
        fix_hairline=True,
        )

driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

driver.get("https://www.ubereats.com/")


actions = ActionChains(driver)
wait = WebDriverWait(driver, 60)

print("Clicking sign up button....")
sign_up = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='wrapper']/header/div/div/div/div/a[3]")))
time.sleep(randint(10, 100)/ 100)
sel_safe_click(sign_up, actions)

# time.sleep(randint(10, 100)/ 100)

email_input = wait.until(EC.presence_of_element_located((By.ID, "PHONE_NUMBER_or_EMAIL_ADDRESS")))

rand_first_name = first_name_gen()
rand_last_name = last_name_gen()

# rand_email = f"{rand_first_name}{rand_last_name}{"".join(choices(alphabet, k=10))}{randint(0, 100)}@axbconcepts.com"

rand_email = rand_email_gen(rand_first_name, rand_last_name, CATCHALL)

print("Entering random email.....")

sel_safe_entry(email_input, actions, rand_email)
email_input.send_keys(Keys.ENTER)

code = input("What's the code you received from the email? ")

time.sleep(randint(10, 100)/ 100)

# code_input = driver.find_element(By.ID, value='EMAIL_OTP_CODE-2')
code_input = wait.until(EC.presence_of_element_located((By.ID, 'EMAIL_OTP_CODE-2')))

print("Entering code...")

sel_safe_entry(element=code_input, sel_actions=actions, input_var=code)


time.sleep(randint(10, 100)/ 100)

# skip_button = driver.find_element(By.XPATH, value='//*[@id="alt-SKIP"]')
skip_button = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="alt-SKIP"]')))

print("Clicking skip button...")

sel_safe_click(element=skip_button, sel_actions=actions)

time.sleep(randint(10, 100)/ 100)

# fname_input = driver.find_element(By.ID, value="FIRST_NAME")
# lname_input = driver.find_element(By.ID, value="LAST_NAME")

fname_input = wait.until(EC.presence_of_element_located((By.ID, "FIRST_NAME")))
lname_input = wait.until(EC.presence_of_element_located((By.ID, "LAST_NAME")))

print("Entering name...")

sel_safe_entry(element=fname_input, sel_actions=actions, input_var=rand_first_name)

sel_safe_entry(element=lname_input, sel_actions=actions, input_var=rand_last_name)

# first_next_button = driver.find_element(By.ID, value="forward-button")
first_next_button = wait.until(EC.presence_of_element_located((By.ID, "forward-button")))

print("Clicking next...")

sel_safe_click(first_next_button, actions)

time.sleep(randint(10, 100)/ 100)

# accept_terms = driver.find_element(By.ID, value="LEGAL_ACCEPT_TERMS")
accept_terms = wait.until(EC.presence_of_element_located((By.ID, "LEGAL_ACCEPT_TERMS")))

print("Clicking checkbox....")
sel_safe_click(element=accept_terms, sel_actions=actions)


# second_next_button = driver.find_element(By.ID, value="forward-button")
second_next_button = wait.until(EC.presence_of_element_located((By.ID, "forward-button")))

print("Clicking next....")
sel_safe_click(element=second_next_button, sel_actions=actions)

print("Waiting for success....")

time.sleep(3)

# driver.quit()



with open("./uber_eats_catchalls (Only need email).txt", "a") as file:
    file.write(f"{rand_email}\n")

print("Script finished!!!")

