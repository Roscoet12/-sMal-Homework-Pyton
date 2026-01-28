import requests
import os
from dotenv import load_dotenv
load_dotenv()


class Yougile:
    def __init__(self, url):
        self.url = url

        login = os.getenv("LOGIN")
        self.login = login

        password = os.getenv("PASSWORD")
        self.password = password

        name = os.getenv("COMPANY_NAME")
        self.name = name

        self.company_id = self.get_id_company(login, password, name)

        self.token = self.get_token(login, password, self.company_id)

    def get_id_company(self, login, password, name):
        creds = {
            'login': login,
            'password': password,
            'name': name
        }
        resp = requests.post(self.url + '/auth/companies', json=creds)
        return resp.json()['content'][0]['id']

    def get_token(self, login, password, companyId):
        creds = {
            'login': login,
            'password': password,
            'companyId': companyId
        }
        resp = requests.post(self.url + '/auth/keys', json=creds)
        return resp.json()['key']

    def get_id_employee(self):
        headers = {
            'Authorization': f'Bearer {self.token}'
        }

        resp = requests.get(self.url + '/users', headers=headers)
        return resp.json()['content'][0]['id']

    def get_new_project(self, title, users):
        headers = {
            'Authorization': f'Bearer {self.token}'
        }
        project = {
            'title': title,
            'users': users
        }
        resp = requests.post(self.url + '/projects',
                             json=project, headers=headers)
        return resp

    def get_project(self):
        headers = {
            'Authorization': f'Bearer {self.token}'
        }
        resp = requests.get(self.url + "/projects", headers=headers)
        return resp.json()

    def get_project_id(self, id_project):
        headers = {
            'Authorization': f'Bearer {self.token}'
        }
        resp = requests.get(self.url + '/projects/' + id_project,
                            headers=headers)
        return resp

    def put_project(self, id_project, name_project):
        headers = {
            'Authorization': f'Bearer {self.token}'
        }
        project = {
            'deleted': True,
            'title': name_project
        }
        resp = requests.put(self.url + '/projects/' + id_project,
                            json=project, headers=headers)
        return resp
