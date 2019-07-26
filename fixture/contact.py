# -*- coding: utf-8 -*-
from selenium.webdriver.support.ui import Select


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        self.add_new()
        # select contact group
        wd.find_element_by_name("new_group").click()
        Select(wd.find_element_by_name("new_group")).select_by_visible_text("[none]")
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])").click()
        self.return_home_page()

    def first_edit(self, contact):
        wd = self.app.wd
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        # fill contact form
        self.fill_contact_form(contact)
        # submit contact update
        wd.find_element_by_xpath("(//input[@name='update'])").click()
        self.return_home_page()

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
        # wd.find_element_by_name("bmonth").click()
        # Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.bmonth)
        # self.change_field_value("byear", contact.byear)
        # select пока не трогаем
        self.change_select_value("aday", contact.aday)
        self.change_select_value("amonth", contact.amonth)
        # wd.find_element_by_name("aday").click()
        # Select(wd.find_element_by_name("aday")).select_by_visible_text(contact.aday)
        # wd.find_element_by_name("amonth").click()
        # Select(wd.find_element_by_name("amonth")).select_by_visible_text(contact.amonth)
        self.change_field_value("ayear", contact.ayear)
        self.change_field_value("address2", contact.adresess2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)

    def return_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def add_new(self):
        wd = self.app.wd
        # init contact creation
        wd.find_element_by_link_text("add new").click()

    def first_delete(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        # select_first_contact
        wd.find_element_by_name("selected[]").click()
        # submit delete
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # submit OK on alert
        wd.switch_to_alert().accept()
        self.return_home_page()

    def all_delete(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        # select_all_contact
        wd.find_element_by_id("MassCB").click()
        # submit delete
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # submit OK on alert
        wd.switch_to_alert().accept()
        self.return_home_page()

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
