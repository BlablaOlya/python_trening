from model.group import Group


def test_add_group(app):
    app.gpoup.create(Group(name="test", header="123", footer="123"))


def test_add_empty_group(app):
    app.gpoup.create(Group(name="", header="", footer=""))
