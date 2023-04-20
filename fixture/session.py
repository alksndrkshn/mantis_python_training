class SessionHelper:
    def __init__(self, app):
        self.app = app
        self.manage_project_page = "/mantisbt-1.2.20/manage_proj_page.php"
        self.manage_page = "/mantisbt-1.2.20/manage_overview_page.php"
    def login(self, username, password):
        wd = self.app.wd
        self.app.open_view_page()
        wd.find_element_by_name("username").click()
        wd.find_element_by_name("username").clear()
        wd.find_element_by_name("username").send_keys(username)
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()
    def ensure_login(self, username, password):
        wd = self.app.wd
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)
    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()
    def ensure_logout(self):
        wd = self.app.wd
        if self.is_logged_in() > 0:
            self.logout()
    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_link_text("Logout")) > 0
    def is_logged_in_as(self, username):
        wd = self.app.wd
        return self.get_logged_user() == username
    def get_logged_user(self):
        wd = self.app.wd
        return wd.find_element_by_css_selector("td.login-info-left "
                                               "span").text
    def is_on_page(self, url):
        wd = self.app.wd
        return wd.current_url.endswith(url)
    def open_manage_page(self):
        wd = self.app.wd
        if self.is_on_page(self.manage_page) is False:
            wd.find_element_by_css_selector("a["
                                            "href='/mantisbt-1.2.20/manage_overview_page.php']").click()

    def open_manage_project_page(self):
        wd = self.app.wd
        self.open_manage_page()
        if self.is_on_page(self.manage_project_page) is False:
            wd.find_element_by_css_selector("a["
                                            "href='/mantisbt-1.2.20/manage_proj_page.php']").click()