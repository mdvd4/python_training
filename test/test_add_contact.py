# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app):
    app.contact.create(
        Contact(firstname="John", middlename="Patrick", lastname="Dow", nickname="JohnDow", title="someTitle",
                company="someCompany", adress="someAdress", phone_home="+1(123)456-78-90",
                phone_mobile="+1(123)456-78-90", phone_work="+1(123)456-78-90", fax="+1(123)456-78-90",
                email="someEmai.@mail.com", emal2="someEmai.@mail.com", email3="someEmai.@mail.com",
                homepage="http://someUrl.com", bday="1", bmonth="January", byear="1950", aday="1", amonth="January",
                ayear="1960", adresess2="someAdress", phone2="+1(123)456-78-90", notes="someNotes"), )


def test_add_empty_contact(app):
    app.contact.create(
        Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", adress="", phone_home="",
                phone_mobile="", phone_work="", fax="", email="", emal2="", email3="", homepage="", bday="", bmonth="-",
                byear="", aday="", amonth="-", ayear="", adresess2="", phone2="", notes=""))


def test_add_contact_only_name(app):
    app.contact.create(
        Contact(firstname="Jonatan",  bday="", bmonth="-", aday="", amonth="-"))
