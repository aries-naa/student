#!/usr/bin/env python

from behave import *

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

timeout = 10


@given("1.1 Заходим на сайт '{site}'")
def step(context, site):
    context.browser.get(site)


@when("1.2 Ищем '{search_string}'")
def step(context, search_string):

    # Там этих id="search" как ...
    id_search = "search"
    new_page = "result-count"

    search_input = WebDriverWait(context.browser, timeout).until(
        EC.visibility_of_element_located((By.TAG_NAME, "input")))
        #EC.presence_of_element_located((By.TAG_NAME, "input")))
    search_input.send_keys(search_string)
    search_input.send_keys(Keys.ENTER)

    # ждём результатов поиска.
    WebDriverWait(context.browser, timeout).until(
        EC.presence_of_element_located((By.ID, new_page)))


@when("1.3 Выводим первые '{count}' ссылок")
def step(context, count):

    id_link = "thumbnail"
    id_desc = "video-title"
    xpath_links = ("//div[@id='contents' and "
                   "@class='style-scope ytd-item-section-renderer']/*")
    link_count = int(count)

    # count {5} результатов.
    WebDriverWait(context.browser, timeout).until(
         EC.presence_of_element_located((By.XPATH, xpath_links)))
    search = context.browser.find_elements(By.XPATH, xpath_links)

    if len(search) < link_count:
        raise Exception("Number of links is less then {}".format(link_count))

    def search_link_desc(element):
        href = element.find_element(By.ID, id_link).get_attribute("href")
        desc = element.find_element(By.ID, id_desc).text
        return (desc, href)

    #info = map(search_link_desc, search)
    info = (search_link_desc(x) for x in search)
    for (desc, href) in list(info)[0:link_count]:
        print('{} ==> {}'.format(desc, href))

    # !!! зачем ?
    print("")

    # Список ссылок.
    def search_link(element):
        href = element.find_element(By.ID, id_link)
        return href.get_attribute("href")

    #context.links = map(search_link, search)
    context.links = (search_link(x) for x in search)


@when("1.4 Открываем '{number}' ссылку")
def step(context, number):

    link_number = int(number)
    link = list(context.links)[link_number - 1]
    new_page = "container"

    context.browser.get(link)

    # Ждём загрузки страницы.
    # На новой есть "container".
    WebDriverWait(context.browser, timeout).until(
        EC.presence_of_element_located((By.ID, new_page)))


@then("1.5 Сохраняем в файл '{file_name}' описание видео")
def step(context, file_name):

    id_description = "description"

    description = WebDriverWait(context.browser, timeout).until(
        EC.presence_of_element_located((By.ID, id_description)))

    # Запись.
    f = open(file_name, 'w')
    f.write(description.text)
    # Удивлён, думал что close сбросит буфер.
    f.flush()
    f.close
