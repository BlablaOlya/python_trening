from model.contact import Contact


def test_contact_contact_mobile(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(firstname="Updated"))
    app.session.logout()