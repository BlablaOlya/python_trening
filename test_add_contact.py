import pytest
from contact import Contact
from application_contact import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(
        Contact(firstname="Olya", middlename="blabla", lastname="Popova", nickname="blablaolya", title="test",
                company="OOO \"test\"", address="ul testovskaya", home="1",
                mobile="+7909090", work="tester", fax="+79898998", email="blabla@mail.ru", email2="blabla2@mail.ru",
                homepage="https://www.youtube.com/", email3="blabla3@mail.ru", bday="1", bmonth="January", byear="1992",
                aday="2", amonth="February",
                ayear="1993", new_group="test", address2="ul energeticheskaya", phone2="2", notes="test test"))
    app.logout()
