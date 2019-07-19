# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest
from contact import Contact


class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.contact_creation(wd)
        self.create_contact(wd, Contact(firstname="John", middlename="Patrick", lastname="Dow", nickname="JohnDow",
                                        title="someTitle", company="someCompany", adress="someAdress",
                                        phone_home="+1(123)456-78-90", phone_mobile="+1(123)456-78-90",
                                        phone_work="+1(123)456-78-90", fax="+1(123)456-78-90",
                                        email="someEmai.@mail.com", emal2="someEmai.@mail.com",
                                        email3="someEmai.@mail.com", homepage="http://someUrl.com",
                                        bday="1", bmonth="January", byear="1950", aday="1", amonth="January",
                                        ayear="1960", group="[none]", adresess2="someAdress", phone2="+1(123)456-78-90",
                                        notes="someNotes"))
        self.return_home_page(wd)
        self.logout(wd)

    def test_add_empty_contact(self):
            wd = self.wd
            self.open_home_page(wd)
            self.login(wd, username="admin", password="secret")
            self.contact_creation(wd)
            self.create_contact(wd, Contact(firstname="", middlename="", lastname="", nickname="",
                                            title="", company="", adress="",
                                            phone_home="", phone_mobile="",
                                            phone_work="", fax="",
                                            email="", emal2="",
                                            email3="", homepage="",
                                            bday="", bmonth="-", byear="", aday="", amonth="-",
                                            ayear="", group="[none]", adresess2="",
                                            phone2="",
                                            notes=""))
            self.return_home_page(wd)
            self.logout(wd)

    def create_contact(self, wd, contact):
        # fill contact form
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.adress)
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.phone_home)
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.phone_mobile)
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.phone_work)
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(contact.fax)
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contact.emal2)
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(contact.email3)
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(contact.homepage)
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.bday)
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.bmonth)
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.byear)
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text(contact.aday)
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(contact.amonth)
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(contact.ayear)
        wd.find_element_by_name("new_group").click()
        Select(wd.find_element_by_name("new_group")).select_by_visible_text(contact.group)
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contact.adresess2)
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contact.phone2)
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contact.notes)
        # submit contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])").click()

    def return_home_page(self, wd):
        wd.find_element_by_link_text("home").click()

    def contact_creation(self, wd):
        # init contact creation
        wd.find_element_by_link_text("add new").click()

    def login(self, wd, username, password):
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
