from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="Group name", header="Group header", footer="Group footer"))


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))
