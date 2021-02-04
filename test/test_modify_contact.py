from model.contact import Contact


def test_contact_contact_mobile(app):
    app.contact.modify_first_contact(Contact(firstname="Updated"))
