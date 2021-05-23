import requests
from todo_app.flask_config import Config
from flask import Flask
from flask import request
from flask import render_template
from werkzeug.utils import redirect

app = Flask(__name__)
app.config.from_object(Config)

trelloKey = app.config['TRELLO_KEY']
trelloToken = app.config['TRELLO_TOKEN']
toDoListId = app.config['TRELLO_TO_DO_LIST_ID']
doneListId = app.config['TRELLO_DONE_LIST_ID']

def getCards():
    lists = {"To Do": toDoListId, "Done": doneListId}
    cardList = []
    for key in lists:
        headers = {"Accept": "application/json"}
        url = f"https://api.trello.com/1/lists/{lists[key]}/cards?key={trelloKey}&token={trelloToken}"
        resp = requests.request("GET", url, headers=headers)
        cards=resp.json()
        for card in cards:
            card.update({"listName": key})
            cardList.append(card) 
    return cardList


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        toDoCardId = request.form['cardid']
        url = f"https://api.trello.com/1/cards/{toDoCardId}/?key={trelloKey}&token={trelloToken}&idList={doneListId}"
        response = requests.request("PUT", url)
        return redirect('/')
    if request.method == 'GET':
        return render_template('index.html', cards=getCards())
        


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        newCardName = request.form['input']
        url = f"https://api.trello.com/1/cards?key={trelloKey}&token={trelloToken}&idList={toDoListId}&name={newCardName}"
        response = requests.request("POST", url)
        return redirect('/')
    if request.method == 'GET':
        return render_template('add.html')


if __name__ == '__main__':
    app.run()
