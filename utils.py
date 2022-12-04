import json


# загрузка и возврат json файла
def load_candidates():
    with open("candidates.json", 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


# возвращение всех кандидатов по имени, позиции и навыкам
def get_all():
    users = []
    user = {}
    data = load_candidates()
    for i in data:
        user["name"] = i["name"]
        user["position"] = i["position"]
        user["skills"] = i["skills"]
        users.append(user)
        user = {}
    return users


# возвращение кандидата по id
def get_by_pk(pk):
    data = load_candidates()
    for i in data:
        if i["pk"] == pk:
            return i


# возвращение кандидата по навыку
def get_by_skill(skill_name):
    data = load_candidates()
    candidates_list = []
    for i in data:
        if skill_name.lower() in i["skills"].lower():
            candidates_list.append(i)
    return candidates_list
