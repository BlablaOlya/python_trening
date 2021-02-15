from model.group import Group


def test_modify_group_name(app):
    if app.gpoup.count() == 0:
        app.gpoup.create(Group(name="Modify test group"))
    app.gpoup.modify_first_group(Group(name="New group"))


def test_modify_group_header(app):
    if app.gpoup.count() == 0:
        app.gpoup.create(Group(header="Modify test header"))
    app.gpoup.modify_first_group(Group(header="New header"))
