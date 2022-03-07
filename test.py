import pytest
import json
import sqlite3
import random

from main import app

def test_listwishlist_route():
    response = app.test_client().get('/wishlist')
    res = json.loads(response.data)
    
    conn = sqlite3.connect('database.sqlite')
    rows = conn.execute('SELECT * FROM WISHLIST')
    rows = rows.fetchall()

    assert response.status_code == 200
    assert type(res) is dict
    assert type(res['wishlist']) is list
    assert len(res['wishlist']) == len(rows)


def test_addwishlist_route():
    ranint = random.randint(1,100)
    data = {
        'isbn':f'pytestisbn{ranint}',
        'user_id': 1,
        'date_of_publication': f'pytestdate{ranint}',
        'title': f'pytesttitle{ranint}'
    }
    response = app.test_client().post('/wishlist', data=data)
    res = json.loads(response.data)
    
    assert response.status_code == 200
    assert type(res) is dict

    response = app.test_client().get('/wishlist')
    getres = json.loads(response.data)
    titles = [i['title'] for i in getres['wishlist']]
    assert data['title'] in titles
    

def test_updatelist_route():
    response = app.test_client().get('/wishlist')
    getres = json.loads(response.data)
    id1 = getres['wishlist'][0]

    ranint = random.randint(1,100)
    data = {
        'id':1,
        'isbn':f'pytestisbn{ranint}',
        'user_id': 1,
        'date_of_publication': f'pytestdate{ranint}',
        'title': f'pytesttitle{ranint}'
    }

    response = app.test_client().post('/updatewishlist', data=data)
    res = json.loads(response.data)
    print('====== data ======')
    print(data)
    print(res)
    return
    assert response.status_code == 200
    assert type(res) is dict
    
    response = app.test_client().get('/wishlist')
    getres = json.loads(response.data)
    id1new = getres['wishlist'][0]

    print(id1new['isbn'])
    print(id1['isbn'])
    assert id1new['isbn'] != id1['isbn'] and id1new['isbn'] == data['isbn']
    assert id1new['date_of_publication'] != id1['date_of_publication'] and id1new['date_of_publication'] == data['date_of_publication']
    assert id1new['title'] != id1['title'] and id1new['title'] == data['title']


def test_deletelist_route():
    response = app.test_client().get('/wishlist')
    getres = json.loads(response.data)
    ids = [i['id'] for i in getres['wishlist']]
    # choose random id to delete
    deleteid = random.choice(ids)
    data = {'id': int(deleteid)}
    response = app.test_client().post('/deletewishlist', data=data)
    response = app.test_client().get('/wishlist')
    getres = json.loads(response.data)
    newids = [i['id'] for i in getres['wishlist']]

    assert deleteid in ids and deleteid not in newids

test_listwishlist_route()
test_addwishlist_route()
test_updatelist_route()
test_deletelist_route()