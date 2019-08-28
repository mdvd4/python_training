from selenium.webdriver.support.ui import Select

from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        self.add_new()
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])").click()
        self.return_home_page()
        self.contacts_cache = None

    def first_edit(self, contact):
        wd = self.app.wd
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        # fill contact form
        self.fill_contact_form(contact)
        # submit contact update
        wd.find_element_by_xpath("(//input[@name='update'])").click()
        self.return_home_page()
        self.contacts_cache = None

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.adress)
        self.change_field_value("home", contact.phone_home)
        self.change_field_value("mobile", contact.phone_mobile)
        self.change_field_value("work", contact.phone_work)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.emal2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        self.change_select_value("bday", contact.bday)
        self.change_select_value("bmonth", contact.bmonth)
        self.change_select_value("aday", contact.aday)
        self.change_select_value("amonth", contact.amonth)
        self.change_field_value("ayear", contact.ayear)
        self.change_select_value("new_group", contact.group)
        self.change_field_value("address2", contact.adresess2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)

    def return_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/index.php") and len(wd.find_elements_by_id("MassCB")) > 0):
            wd.find_element_by_link_text("home").click()

    def add_new(self):
        wd = self.app.wd
        # init contact creation
        wd.find_element_by_link_text("add new").click()

    def first_delete(self):
        wd = self.app.wd
        self.return_home_page()
        # select_first_contact
        wd.find_element_by_name("selected[]").click()
        # submit delete
        self.submit_delete()
        # submit OK on alert
        wd.switch_to_alert().accept()
        self.return_home_page()
        self.contacts_cache = None

    def all_delete(self):
        wd = self.app.wd
        self.return_home_page()
        # select_all_contact
        wd.find_element_by_id("MassCB").click()
        self.submit_delete()
        # submit OK on alert
        wd.switch_to_alert().accept()
        self.return_home_page()
        self.contacts_cache = None

    def submit_delete(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@value='Delete']").click()

    # Метод абсолютно идентичен методу в group возможно нужно отрефакторить и вынести?
    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def change_select_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)

    def count(self):
        wd = self.app.wd
        self.return_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contacts_cache = None

    def get_contacts_list(self):
        wd = self.app.wd
        if self.contacts_cache is None:
            self.return_home_page()
            self.contacts_cache = []
            for element in wd.find_elements_by_name('entry'):
                cells = []
                for cell in element.find_elements_by_tag_name('td'):
                    cells.append(cell.text)
                contact_id = element.find_element_by_name("selected[]").get_attribute('value')
                contact_lastname = cells[1]
                contact_firstname = cells[2]
                self.contacts_cache.append(Contact(id=contact_id, lastname=contact_lastname, firstname=contact_firstname))
        return list(self.contacts_cache)
