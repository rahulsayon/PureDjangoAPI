import json
import requests

BASE_URL = "http://127.0.0.1:8000/"
ENDPOINT = "api/update/"

def get_list():
    r = requests.get(BASE_URL + ENDPOINT)
    print(r.status_code)
    status_code = r.status_code
    if status_code != 200:
        print("probably not good sign?")
    data = r.json()
    for obj in data:
        if obj['id'] == 1:
            r2 = requests.get(BASE_URL + ENDPOINT + str(obj['id']))
            print(r2.json())
    return data

def create_update_list():
    new_data = {
        'user' : 1,
        "content" : "Another new cool update"
    }
    # r = requests.delete(BASE_URL + ENDPOINT,data=new_data)
    r = requests.post(BASE_URL + ENDPOINT,data=new_data)
    print(r.headers)
    if r.status_code == requests.codes.ok:
        return r.json()
    return r.text


def create_get():
    r = requests.get(BASE_URL + ENDPOINT + "1/")
    print(r.headers)
    if r.status_code == requests.codes.ok:
        return r.json()
    return r.text

# print(create_get())

def create_post():
    new_data = {
        'user' : 1,
        "content" : "Rahul new cool update"
    }
    r = requests.post(BASE_URL + ENDPOINT + "1/",data=new_data)
    print(r.headers)
    if r.status_code == requests.codes.ok:
        return r.json()
    return r.text

def update():
    new_data = {
        'user' : 1,
        "content" : "Rahul new cool update"
    }
    r = requests.put(BASE_URL + ENDPOINT + "1/",data=json.dumps(new_data))
    print(r.headers)
    if r.status_code == requests.codes.ok:
        return r.json()
    return r.text


def delete():
    new_data = {
        'user' : 1,
        "content" : "Rahul new cool update"
    }
    r = requests.delete(BASE_URL + ENDPOINT + "1/",data=new_data)
    print(r.headers)
    if r.status_code == requests.codes.ok:
        return r.json()
    return r.text


print(delete())
# print(create_post())




# get_list()
        



