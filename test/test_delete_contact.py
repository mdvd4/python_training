from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(lastname="Smith", firstname="Mike"))
    old_contacts = app.contact.get_contacts_list()
    app.contact.first_delete()
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[0:1] = []
    assert old_contacts == new_contacts


def test_delete_all_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(lastname="Smith", firstname="Mike"))
    app.contact.all_delete()
    new_contacts = app.contact.get_contacts_list()
    assert len(new_contacts) == 0
