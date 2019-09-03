from model.contact import Contact
from random import randrange


def test_delete_some_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(lastname="Smith", firstname="Mike"))
    old_contacts = app.contact.get_contacts_list()
    index = randrange(len(old_contacts))
    app.contact.delete_by_index(index)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts


# def test_delete_all_contact(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(lastname="Smith", firstname="Mike"))
#     app.contact.all_delete()
#     assert app.contact.count() == 0


