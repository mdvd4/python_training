from model.group import Group


def test_modify_group_name(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(name="New group"))
    app.session.logout()


def test_modify_group_footer(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(footer="New footer"))
    app.session.logout()


def test_modify_group_header(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(header="New header"))
    app.session.logout()


def test_modify_first_group_all(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="Group name", header="Group header", footer="Group footer"))
    app.group.modify_first_group(
        (Group(name="Edit group name", header="Edit group header", footer="Edit group footer")))
    app.session.logout()
