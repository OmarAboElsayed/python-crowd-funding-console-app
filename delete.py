import json
from view_projects import view_projects
def delete_project(user_mail):
    view_projects(user_mail)
    project_name = input('\n Please Enter Name Project Deleted : ')
    list = []
    json_file = open('projects_data.json')
    for line in json_file:
        Dict = json.loads(line)
        list.append(Dict)

    for dict in list:
        if dict['Title'] == project_name:
            list.remove(dict)
            projects = open("projects_data.json", "w")
            for add_dict in list:
                json.dump(add_dict, projects)
                projects.write("\n")
            projects.close()

            print("delete project successfully")
            break
    else:
        print("NO Project")
        delete_project(user_mail)