import re


class TemplateTest:
    def test_donate(self):
        self.open("/donations/donate.1?amounts=17-39-51-other")
        # test whether 'donation_type' text is present likely for choosing/setting the donation_type
        self.assertTrue(re.search(r"donation_type", self.wd.page_source))
