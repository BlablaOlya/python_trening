from model.group import Group


def test_delete_first_group(app):
    if app.gpoup.count() == 0:
        app.gpoup.create(Group(name="del test"))
    app.gpoup.delete_first_group()
