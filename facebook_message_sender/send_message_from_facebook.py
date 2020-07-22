from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from random import randint
from Creed import * #creedential import
import sys
import os

driver = webdriver.Chrome()
driver.maximize_window()
user_name = EMAIL
password = PASSWORD
send_to_name = "Naymul Hasan Fahim"


#login xpaths
fb_url = 'https://www.facebook.com/'
fb_messenger_url = 'https://www.facebook.com/messages'
user_name_xpath = "//input[@name='email']"
password_xpath = "//input[@name='pass']"
login_btn_xpath = "//input[@value='Log In']"

#SENDING MESSAGE FROM FACEBOOK MESSAGE
#finding targed user xpaths
MESSANGER_btn_in_feed_xpath = "//div[contains(@aria-label,'Messenger') and @tabindex='0']"
MESSANGER_search_bar_in_feed_xpath = "//input[@aria-label='Search Messenger']"
MESSANGER_target_user_in_feed_xpath = f"//div[@role='listbox']//div[@aria-label='{send_to_name}']"
search_btn_xpath = "//div[@aria-label='Search by name or group']"
input_search_bar_xpath = "//input[@placeholder='Search by name or group']"
target_user_xpath = f"//span[text()='{send_to_name}']"
#message
title_xpath = "//div[@data-testid='messenger-chat-title-text']"
msg_field_xpath = f"//div[contains(@aria-label,'Chat with')]//child::span[contains(@data-offset-key,'-0-0')]"
send_btn_xpath = f"//div[contains(@aria-label,'Chat with')]//child::div[@aria-label='Press Enter to send' and @role='button']"

#SENDING MESSAGE FROM FACEBOOK MESSANGER
MESSANGER_search_bar_xpath = "//input[@aria-label='Search Messenger']"
MESSANGER_target_user_xpath = f"//div[text()='{send_to_name}']//ancestor::a"
#message
MESSANGER_field_xpath = f"//div[@aria-label='Type a message...']"
MESSANGER_send_btn_xpath = f"//div[@aria-label='Chat with {send_to_name}']//child::div[@aria-label='Press Enter to send' and @role='button']"

def get_title():
    return driver.find_element_by_xpath("//div[@data-testid='messenger-chat-title-text']").text

#waits for a specific element to load for specified time
def wait_for_ele_by_xpath(xpath,time=None,driver=driver,fn=EC.presence_of_element_located):
    if time:
        WebDriverWait(driver,time).until(fn((By.XPATH,xpath)))
    while True:
        try:
            WebDriverWait(driver, .1,.1).until(fn((By.XPATH, xpath)))
            return
        except TimeoutException:
            continue

def wait_for_eles_by_xpath(xpath,element_num=2,time=None,driver=driver):
    if time:
        WebDriverWait(driver,time).until(EC.presence_of_all_elements_located((By.XPATH,xpath)))
        return
    while True:
        try:
            eles = WebDriverWait(driver, .1).until(EC.presence_of_all_elements_located((By.XPATH, xpath)))
            if len(eles)>=element_num:
                return
        except TimeoutException:
            continue

def copy_file_or_text_to_clipbord(text=None,file=None):
    if file==None and text:
        os.system(f"echo {text}| clip")
    elif file:
        os.system(f"clip < {file}")
    else:
        raise ValueError("You haven't passed any parameter")

def paste_keys(xpath,text=None,file=None):
    copy_file_or_text_to_clipbord(text=text,file=file)
    el = driver.find_element_by_xpath(xpath)
    el.send_keys(Keys.CONTROL, 'v',Keys.ENTER)


def _initiate_xpath_getter():
    driver.execute_script("""
    function getElementByXpath(path) {
        return document.evaluate(path, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
    }
    """)


#javascript_funcs
def _js_scroll_to_page_top():
    driver.find_element_by_tag_name('body').send_keys(Keys.HOME)

def _js_scroll_to_page_bottom():
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

def _js_scroll_into_view(element):
    driver.execute_script("arguments[0].scrollIntoView(true);", element)

def _js_click(element):
    driver.execute_script("arguments[0].click();", element)

def _js_select_by_xpath_and_click(xpath):
    driver.execute_script("""xpath = '{}';document.evaluate(xpath, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.click();""".format(xpath))




#page loader
def load_page(url='https://www.google.com',error_element='//div[@class="error-code"]'):
    """"Tries to load the URL. If it finds error element by XPATH then it reloads the page.\nIf it doesn't finds the error element then it returns form the function.\n
    Requited imports:\n
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.common.exceptions import TimeoutException
    """
    driver.get(url)
    while True:
        try:
            WebDriverWait(driver, .1).until(EC.presence_of_element_located((By.XPATH, error_element)))
        except TimeoutException:
            return
        driver.refresh()

#random string generator
def random_jybirsh(characters,assci_table_start=32,assci_table_end=127):
    chars = []
    for _ in range(characters):
        chr_num_on_assci_table = randint(assci_table_start,assci_table_end)
        chars.append(chr(chr_num_on_assci_table))
    return ''.join(chars)

#sequential number generator
def sequential_number(steps=1):
    count = 0
    while True:
        count += steps
        yield count

def dec_to_chr(dec):
    return chr(dec)


def login_to_fb(url,wait_for_ele_xpath=None):
    #LOGIN
    load_page(url)
    wait_for_ele_by_xpath(user_name_xpath)

    user_name_field = driver.find_element_by_xpath(user_name_xpath)
    pass_field = driver.find_element_by_xpath(password_xpath)
    login_btn = driver.find_element_by_xpath(login_btn_xpath)

    user_name_field.send_keys(user_name)
    pass_field.send_keys(password)
    login_btn.click()
    if wait_for_ele_xpath:
        wait_for_ele_by_xpath(wait_for_ele_xpath)


def select_target_user():
    wait_for_ele_by_xpath(MESSANGER_btn_in_feed_xpath)
    search_btn = driver.find_element_by_xpath(MESSANGER_btn_in_feed_xpath)
    wait_for_ele_by_xpath(MESSANGER_btn_in_feed_xpath,fn=EC.element_to_be_clickable)
    _js_click(search_btn)

    wait_for_ele_by_xpath(MESSANGER_search_bar_in_feed_xpath)
    search_field = driver.find_element_by_xpath(MESSANGER_search_bar_in_feed_xpath)
    wait_for_ele_by_xpath(MESSANGER_search_bar_in_feed_xpath,fn=EC.element_to_be_clickable)
    search_field.send_keys(send_to_name)

    wait_for_ele_by_xpath(MESSANGER_target_user_in_feed_xpath)
    target_user = driver.find_element_by_xpath(MESSANGER_target_user_in_feed_xpath)
    wait_for_ele_by_xpath(MESSANGER_target_user_in_feed_xpath,fn=EC.element_to_be_clickable)
    _js_click(target_user)
    wait_for_ele_by_xpath(msg_field_xpath)


def send_message_from_facebook_home_page(message=None,msg_len=5,msg_count=None):
    unlimited_flag = False
    if msg_count==None:
        unlimited_flag = True
        msg_count=-1
    
    login_to_fb(fb_url,MESSANGER_btn_in_feed_xpath)
    
    #selecting target user
    select_target_user()
    global send_to_name
    send_to_name = get_title()
    global msg_field_xpath
    msg_field_xpath = f"//div[@aria-label='Chat with {send_to_name}']//child::span[contains(@data-offset-key,'-0-0')]"

    #sending message
    generator = sequential_number()

    count = 1
    while count<=msg_count or unlimited_flag:
        if message=='sequential_num':
            paste_keys(msg_field_xpath,next(generator))
        elif message=='random_str':
            paste_keys(msg_field_xpath,random_jybirsh(msg_len))
        elif message=='use_file':
            paste_keys(msg_field_xpath,file='msg.text')
        elif message:
            paste_keys(msg_field_xpath,message)
        else:
            print('You haven\'t specified any maessage')
            break
        if msg_count>=count:
            count+=1


#sending message
send_message_from_facebook_home_page('sequential_num')