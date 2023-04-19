import random
from model.project import Project


def test_del_project(app):
    old_project = app.soap.get_project_list()
    if not old_project:
        app.project.create(name="test_test")
    old_project = app.soap.get_project_list()
    project = random.choice(old_project)
    app.project.delete_project_by_name(project.name)
    new_project = app.soap.get_project_list()
    assert len(old_project) - 1 == len(new_project)
    old_project.remove(project)
    assert sorted(old_project, key=Project.id_or_max) == sorted(
        new_project, key=Project.id_or_max)