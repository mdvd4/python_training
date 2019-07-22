class GroupHelper:

    def __init__(self, app):
        self.app = app

    def return_groups_page(self):
        wd = self.app.wd
        # return groups page
        wd.find_element_by_link_text("groups").click()

    def create(self, group):
        wd = self.app.wd
        self.open_group_page()
        # init group creation
        wd.find_element_by_name("new").click()
        self.fill_group_form(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_groups_page()

    def open_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()
        self.return_groups_page()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_group_page()
        # select_first_group
        wd.find_element_by_name("selected[]").click()
        # submit_deletion
        wd.find_element_by_name("delete").click()
        self.return_groups_page()

    def edit_first_group(self, group):
        wd = self.app.wd
        self.open_group_page()
        # select_first_group
        wd.find_element_by_name("selected[]").click()
        # submit edit group
        wd.find_element_by_name("edit").click()
        self.fill_group_form(group)
        # submit_update
        wd.find_element_by_name("update").click()
        self.return_groups_page()

    def fill_group_form(self, group):
        wd = self.app.wd
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
