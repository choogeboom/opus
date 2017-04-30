from flask import url_for


def test_home_page(client):
    response = client.get(url_for('page.home'))
    assert response.status_code == 200
