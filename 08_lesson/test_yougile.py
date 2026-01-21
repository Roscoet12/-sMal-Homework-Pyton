from Yougile import Yougile
api = Yougile('https://ru.yougile.com/api-v2')

def test_new_project_positiv():

    users_id  = api.get_id_employee()
    users = {
         users_id: 'admin',
    }
    result = api.get_new_project('Сладкоежка', users)

    assert result.status_code == 201

    project_list = api.get_project()

    assert project_list['content'][0]['title'] == 'Сладкоежка'

    api.delete_key()

def test_new_project_negativ():

    users = {
        12345: 'admin',
    }
    result = api.get_new_project('Горькоежка', users)

    assert result.status_code == 400

    api.delete_key()

def test_get_project_id_positiv():

    result = api.get_project()
    id_project = result['content'][0]['id']

    result2 = api.get_project_id(id_project)

    assert result2.status_code == 200
    assert result['content'][0]['title'] == 'Сладкоежка'

    api.delete_key()

def test_get_project_id_negativ():

    id_project = '12345'
    result = api.get_project_id(id_project)

    assert result.status_code == 404

    api.delete_key()

def test_change_positiv():

    result = api.get_project()
    id_project = result['content'][0]['id']
    name_project = result['content'][0]['title']

    change_project = api.put_project(id_project, name_project)

    projects = api.get_project()
    assert projects['content'] == []
    assert change_project.status_code == 200

    api.delete_key()

def test_change_project_negativ():
    id_project = '234'
    name_project = 'Горькоежка'
    change_project = api.put_project(id_project, name_project)

    assert change_project.status_code == 404

    api.delete_key()
