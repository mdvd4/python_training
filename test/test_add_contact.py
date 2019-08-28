# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contacts_list()
    contact = Contact(firstname="John", middlename="Patrick", lastname="Dow", nickname="JohnDow", title="someTitle",
                      company="someCompany", adress="someAdress", phone_home="+1(123)456-78-90",
                      phone_mobile="+1(123)456-78-90", phone_work="+1(123)456-78-90", fax="+1(123)456-78-90",
                      email="someEmai.@mail.com", emal2="someEmai.@mail.com", email3="someEmai.@mail.com",
                      homepage="http://someUrl.com", bday="1", bmonth="January", byear="1950", aday="1",
                      amonth="January",
                      ayear="1960", adresess2="someAdress", phone2="+1(123)456-78-90", notes="someNotes",
                      group="[none]")
    app.contact.create(contact)
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


# def test_add_empty_contact(app):
#     old_contacts = app.contact.get_contacts_list()
#     contact = Contact()
#     app.contact.create(contact)
#     new_contacts = app.contact.get_contacts_list()
#     assert len(old_contacts) + 1 == len(new_contacts)
#     old_contacts.append(contact)
#     assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
#
#
# def test_add_contact_only_name(app):
#     old_contacts = app.contact.get_contacts_list()
#     contact = Contact(firstname="Jonatan")
#     app.contact.create(contact)
#     new_contacts = app.contact.get_contacts_list()
#     assert len(old_contacts) + 1 == len(new_contacts)
#     old_contacts.append(contact)
#     assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
