import re

import requests

import json

from data import *


class Player(object):
    def __init__(self, account, password):
        self.account = account
        self.password = password
        self.spider_init()
        self.spider_login()

    def spider_init(self):
        self.main_session = requests.session()
        login_page_object = self.main_session.get(url=login_page_url)
        # print(login_page_object.content.decode())
        login_page_html_string = login_page_object.content.decode()
        # print(login_page_object.url)
        csrftoken_html = re.search(r'name="csrftoken" value="([a-z]|[0-9]|-)*"', login_page_html_string).group()
        sessionTimeout_html = re.search(r'name="sessionTimeout" value="([0-9])*"', login_page_html_string).group()
        self.csrftoken = re.search(r'([0-9]|[a-z]|-){36}', csrftoken_html).group()
        self.sessionTimeout = re.search(r'\d{13}', sessionTimeout_html).group()

    def spider_login(self):
        login_form = {
            "accountName": self.account,
            "password": self.password,
            "srpEnabled": "false",
            "upgradeVerifier": "",
            "useSrp": "false",
            "publicA": "",
            "clientEvidenceM1": "",
            "persistLogin": "on",
            "csrftoken": self.csrftoken,
            "sessionTimeout": self.sessionTimeout
        }
        self.main_session.post(url=login_data_url,data=login_form)

    def getprofile(self):
        profile_json = self.main_session.get(url='https://ow.blizzard.cn/action/career/profile').content.decode()
        return json.loads(profile_json)

