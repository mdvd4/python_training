from model.group import Group


def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="Group name", header="Group header", footer="Group footer"))
    app.group.edit_first_group((Group(name="Edit group name", header="Edit group header", footer="Edit roup footer")))
    app.session.logout()
