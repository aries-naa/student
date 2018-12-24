#!/usr/bin/env python

from selenium import webdriver


def before_scenario(context, scenario):
    context.browser = webdriver.Firefox()


def after_scenario(context, scenario):
    context.browser.quit()
