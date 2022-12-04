import utils
from flask import Flask

app = Flask(__name__)


# главная страница
@app.route("/")
def page_main():
    candidates = utils.load_candidates()
    result = '<pre>'
    for candidate in candidates:
        result += f'''
            {candidate["name"]}\n
            {candidate["position"]}\n
            {candidate["skills"]}\n
        '''
    result += '</pre>'
    return result


# страница с кандидатом по id
@app.route("/candidate/<int:uid>")
def page_candidate(uid):
    candidate = utils.get_by_pk(uid)
    url = candidate["picture"]
    result = f"<img src='({url})'>\n"
    result += '<pre>'
    result += f'''
        {candidate["name"]}\n
        {candidate["position"]}\n
        {candidate["skills"]}\n
    '''
    result += '</pre>'
    return result


# страница с кандидатом по skill
@app.route("/skills/<skill>")
def page_skills(skill):
    candidates = utils.get_by_skill(skill)
    result = '<pre>'
    for candidate in candidates:
        result += f'''
            {candidate["name"]}\n
            {candidate["position"]}\n
            {candidate["skills"]}\n
        '''
    result += '</pre>'
    return result


app.run()
