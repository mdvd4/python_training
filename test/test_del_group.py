from model.group import Group


def test_delete_first_group(app):
    app.group.create(Group(name="Group name", header="Group header", footer="Group footer"))
    app.group.delete_first_group()
