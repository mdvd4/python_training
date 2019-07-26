from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(lastname="Smith", firstname="Mike"))
    app.contact.first_delete()


def test_delete_all_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(lastname="Smith", firstname="Mike"))
    app.contact.all_delete()
