# -*- coding: utf-8 -*-

from model.contact import Contact


def test_edit_first_contact(app):
    app.contact.create(
        Contact(firstname="John", middlename="Patrick", lastname="Dow", nickname="JohnDow", title="someTitle",
                company="someCompany", adress="someAdress", phone_home="+1(123)456-78-90",
                phone_mobile="+1(123)456-78-90", phone_work="+1(123)456-78-90", fax="+1(123)456-78-90",
                email="someEmai.@mail.com", emal2="someEmai.@mail.com", email3="someEmai.@mail.com",
                homepage="http://someUrl.com", bday="1", bmonth="January", byear="1950", aday="1", amonth="January",
                ayear="1960", adresess2="someAdress", phone2="+1(123)456-78-90", notes="someNotes"), )
    app.contact.first_edit(
        Contact(firstname="Joana", middlename="Mari", lastname="Dow", nickname="JoanaDow", title="someTitle2",
                company="someCompany2", adress="someAdress2", phone_home="+1(123)456-78-99",
                phone_mobile="+1(123)456-78-99", phone_work="+1(123)456-78-99", fax="+1(123)456-78-99",
                email="someEmail2.@mail.com", emal2="someEmail2.@mail.com", email3="someEmail2.@mail.com",
                homepage="http://someUrl2.com", bday="10", bmonth="April", byear="1955", aday="10", amonth="April",
                ayear="1965", adresess2="someAdress2", phone2="+1(123)456-78-99", notes="someNotes2"))
