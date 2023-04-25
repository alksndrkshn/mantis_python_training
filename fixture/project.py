from selenium.webdriver.support.select import Select

from model.project import Project


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_project_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()

    def create(self, project):
        wd = self.app.wd
        self.open_project_page()
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()
        self.fill_project_form(project)
        wd.find_element_by_xpath("//input[@value='Add Project']").click()
        self.project_cache = None

    def fill_project_form(self, project):
        wd = self.app.wd
        self.change_field_value("name", project.name)
        self.change_list_value("status", project.status)
        self.change_list_value("view_state", project.view_state)
        self.change_field_value("description", project.description)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def change_list_value(self, list_name, value):
        wd = self.app.wd
        if value is not None:
            wd.find_element_by_name(list_name).click()
            Select(wd.find_element_by_name(list_name)).select_by_visible_text(
                value)

    def delete_project_by_name(self, name):
        wd = self.app.wd
        self.open_project_page()
        wd.find_element_by_link_text(name).click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        wd.find_element_by_xpath("//*/text()[normalize-space(.)='']/parent::*").click()
        self.project_cache = None

    def select_first_group(self):
        self.select_group_by_index(0)

    def select_group_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def get_project_list(self):
        if self.project_cache is None:
            wd = self.app.wd
            self.open_project_page()
            self.project_cache = []
            #project_list = []
            for row in wd.find_elements_by_xpath("//table[3]/*/tr[@class='row-1' or @class='row-2']"):
                cells = row.find_elements_by_css_selector("td")
                id = cells[0].find_element_by_css_selector("a").get_attribute("href").split("=")[-1]
                name = cells[0].text
                status = cells[1].text
                enabled = cells[2].text
                view_state = cells[3].text
                description = cells[4].text
                #project_list.append(Project(id=id, name=name,
                # status=status,
                # view_state=view_state,
                # description=description))
                self.project_cache.append(Project(id=id, name=name,
                                                  status=status,
                                                  view_state=view_state,
                                                  description=description))
        return list(self.project_cache)
