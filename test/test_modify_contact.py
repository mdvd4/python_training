# -*- coding: utf-8 -*-

from model.contact import Contact


def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(lastname="Smith", firstname="Mike"))
    app.contact.first_edit(Contact(firstname="Joana", middlename="Mari", lastname="Dow"))
