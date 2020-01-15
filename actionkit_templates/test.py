import datetime
import os
import re
from sys import platform
import time
try:
    from urlparse import urlparse
except ImportError:
    # python3
    from urllib.parse import urlparse

from pyvirtualdisplay import Display

from django.test import Client, TestCase, override_settings
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.support.ui import Select

TESTSETTINGS = {
    'AK_TEST': True,
}

@override_settings(**TESTSETTINGS)
class TemplateTest(LiveServerTestCase):

    mobile_size = (1024, 1000)  # mobile w/ scroll
    desktop_size = (1920, 1024)

    @classmethod
    def setUpClass(cls):
        super(TemplateTest, cls).setUpClass()
        if platform.startswith('linux'):
            size = cls.mobile_size
            if os.environ.get('SCREENSIZE') == 'desktop':
                size = cls.desktop_size
            cls.display = Display(visible=os.environ.get('VISIBLE',0),
                                  size=size)
            cls.display.start()
        cls.wd = webdriver.Firefox()

    @classmethod
    def tearDownClass(cls):
        if platform.startswith('linux'):
            cls.display.stop()
        super(TemplateTest, cls).tearDownClass()

    def _databases_names(*args, **kwargs):
        #make things database-less
        return []

    def open(self, url):
        self.wd.get("%s%s" % (self.live_server_url, url))

    def test_screenshots(self):
        if os.environ.get('SCREENSHOTS'):
            dirname = 'screenshots_{}'.format(os.environ.get('SCREENSIZE', 'mobile'))
            try:
                os.mkdir(dirname)
            except OSError:
                pass  # we'll overwrite existing screenshots
            self.open('/')
            links = has_header = self.wd.find_elements_by_xpath('//div[@role="main"]//a')
            hrefs = [urlparse(e.get_attribute('href')).path for e in links]
            for href in hrefs:
                filename = href.replace('/', '_')
                self.open(href)
                self.wd.save_screenshot('{}/{}.png'.format(dirname, filename))

    # def test_donate(self, query=''):
    #     self.open('/donations/donate.1?amounts=17-39-51-other&' + query)
    #     # test whether 'donation_type' text is present likely for choosing/setting the donation_type
    #     self.assertTrue(re.search(r'donation_type', self.wd.page_source))

