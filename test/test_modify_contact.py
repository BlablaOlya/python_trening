from model.contact import Contact


def test_contact_contact_mobile(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Updated test contact"))
    app.contact.modify_first_contact(Contact(firstname="Updated"))
