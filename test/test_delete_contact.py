def test_delete_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.first_delete()
    app.session.logout()

def test_delete_all_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.all_delete()
    app.session.logout()