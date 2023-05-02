from model.project import Project
import string
import random


def random_project(prefix, maxlen):
    symbols = string.ascii_letters
    return prefix + "".join([random.choice(symbols) for i in range(
        random.randrange(maxlen))])

def test_add_project(app):
    old_projects = app.soap.get_project_list()
    project = Project(name=random_project("name", 5), status="stable",
                      view_state="private",
                      description="descp")
    app.project.create(project)
    new_projects = app.soap.get_project_list()
    old_projects.append(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(
        new_projects, key=Project.id_or_max)
