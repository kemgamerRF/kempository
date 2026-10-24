from flask import Flask
import random
app = Flask(__name__)

list_facts = [
    "хаммам",
    "круто",
]
@app.route("/")
def hello_world():
    return 'Привет! Меня зовут Илья, и я создал свой первый сайт на Flask! <br> (Тут будет какая нибудь инфа)<br><br> Flask юзаю первый раз, выглядит интересно и относительно удобно!<br><br> С прошлого урока в Kodland мне больше всего запомнилось собственно само создание сайтов!'
@app.route("/blep")
def blep1_world():
    return f'''
    <h1> уйди отсюда <h1>
    <h2> h2tst <h2>
    <p> {random.choice(list_facts)} <p>
    '''
@app.route("/facts")
def blep2_world():
    return f'''
    <p> {random.choice(list_facts)} <p>
    '''
app.run(debug=True)
