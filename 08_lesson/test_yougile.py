from Yougile import Yougile
api = Yougile('https://ru.yougile.com/api-v2')


def test_new_project_positive():
    users_id = api.get_id_employee()

    users = {
         users_id: 'admin',
    }
    result = api.get_new_project('Сладкоежка', users)

    assert result.status_code == 201

    project_list = api.get_project()
    projects = project_list.get('content', [])
    my_project = [proj for proj in projects
                  if proj.get('title') == 'Сладкоежка']

    assert my_project, 'Проект "Сладкоежка" не найден в списке'


def test_new_project_negativ():
    users = {
        12345: 'admin',
    }
    result = api.get_new_project('Горькоежка', users)

    assert result.status_code == 400


def test_get_project_id_positive():
    users_id = api.get_id_employee()
    users = {
        users_id: 'admin',
    }
    api.get_new_project('Сладкоежка', users)

    project_list = api.get_project()
    assert ('content' in project_list
            and len(project_list['content']) > 0), 'Нет проектов в ответе'
    projects = project_list['content']
    my_project = None
    for proj in projects:
        if proj['title'] == 'Сладкоежка':
            my_project = proj
            break

    assert my_project is not None, 'Проект "Сладкоежка" не найден в списке'

    id_project = my_project['id']

    result = api.get_project_id(id_project)

    assert result.status_code == 200


def test_get_project_id_negativ():
    id_project = '12345'
    result = api.get_project_id(id_project)

    assert result.status_code == 404


def test_change_positive():
    users_id = api.get_id_employee()
    users = {
        users_id: 'admin',
    }
    api.get_new_project('Сладкоежка', users)

    project_list = api.get_project()
    projects = project_list['content']
    my_project = None
    for proj in projects:
        if proj['title'] == 'Сладкоежка':
            my_project = proj
            break

    id_project = my_project['id']
    name_project = my_project['title']

    change_project = api.put_project(id_project, name_project)

    assert change_project.status_code == 200

    project_list_change = api.get_project()
    projects_change = project_list_change['content']
    no_project = None
    for proj in projects_change:
        if proj['title'] == 'Сладкоежка':
            no_project = proj
            break

    assert no_project is None, 'Проект "Сладкоежка" не удален'


def test_change_project_negativ():
    id_project = '234'
    name_project = 'Горькоежка'
    change_project = api.put_project(id_project, name_project)

    assert change_project.status_code == 404
