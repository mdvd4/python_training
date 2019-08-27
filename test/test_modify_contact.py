# -*- coding: utf-8 -*-

from model.contact import Contact


def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(lastname="Smith", firstname="Mike"))
    old_contacts = app.contact.get_contacts_list()
    contact = Contact(firstname="Joana", middlename="Mari", lastname="Dow")
    contact.id = old_contacts[0].id
    app.contact.first_edit(contact)
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

