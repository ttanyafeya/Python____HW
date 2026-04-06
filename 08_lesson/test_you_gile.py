import requests

from user import base_url, token


def test_ceatecompany():
    headers = {'Authorization': f'Bearer {token}',
               'Content-Type': 'application/json'
               }
    body = {"title": "ГосУслуги"}
    r = requests.post(f"{base_url}/projects", headers=headers, json=body)
    assert r.status_code == 201


def test_ceatecompany_negativ():
    headers = {'Authorization': f'Bearer {token}',
               'Content-Type': 'application/json'
               }
    body = {"title": ""}
    r = requests.post(f"{base_url}/projects", headers=headers, json=body)
    assert r.status_code == 400


def test_update__positiv():
    # На этом этапе создаем проект
    headers = {'Authorization': f'Bearer {token}',
               'Content-Type': 'application/json'
               }
    body = {"title": "ГосУслуги"}
    r = requests.post(f"{base_url}/projects", headers=headers, json=body)
    assert r.status_code == 201
    id = r.json()["id"]
    # редактируем проект
    body = {"title": "GOs"}
    r = requests.put(f"{base_url}/projects/{id}", headers=headers, json=body)
    assert r.status_code == 200
    # Получаем по id
    r = requests.get(f"{base_url}/projects/{id}", headers=headers)
    assert r.status_code == 200
    title = r.json()["title"]
    assert title == "GOs"


def test_update_negayiv():
    # создаем проект (без токена авторизации)
    headers = {'Authorization': f'Bearer{""}',
               'Content-Type': 'application/json'
               }
    body = {"title": "ГосУслуги"}
    r = requests.post(f"{base_url}/projects", headers=headers, json=body)
    assert r.status_code == 401


def test_change_negayiv():
    # редактируем проект ( в теле нет названия компании)
    headers = {'Authorization': f'Bearer{token}',
               'Content-Type': 'application/json'
               }
    body = {"title": ""}
    r = requests.put(f"{base_url}/projects/{id}", headers=headers, json=body)
    assert r.status_code == 401


def test_getid_negayiv():
    # Получаем по id (несуществующее id)
    headers = {'Authorization': f'Bearer{token}',
               'Content-Type': 'application/json'
               }
    id = "1cae774c-1606-48aa-b20c-0e9bdc90186"
    r = requests.put(f"{base_url}/projects/{id}", headers=headers)
    assert r.status_code == 401
