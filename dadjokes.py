import flask
from flask import request
import random
import json
from random import randint

app = flask.Flask(__name__)


global alreadyReturned
alreadyReturned = []

@app.route('/', methods=['GET'])
def home():
    ret = {'success': True, 'message': 'This is the home page'}
    return json.dumps(ret),200,{'Content-Type': 'application/json'}

@app.route('/random',methods=['GET'])
def random():
    with open('dadjokes.json',encoding='UTF-8') as json_file:
        data = json.load(json_file)
        hasReturned = False
        while(not hasReturned):
            rand = randint(0,len(data)-1)
            currJoke = data[rand]
            if(currJoke not in alreadyReturned):
                alreadyReturned.append(currJoke)
                print(len(alreadyReturned))
                hasReturned = True
                return json.dumps(currJoke) ,200 , {'Content-Type':'application/json'}
        

@app.route('/joke',methods=['GET'])
def joke():
    if 'id' in request.args:
        id = request.args['id']
        with open('dadjokes.json',encoding='UTF-8') as json_file:
            data = json.load(json_file)
            for joke in data:
                if(joke['id']==id):
                    return json.dumps(joke), 200, {"Content-Type":'application/json'}
            return "Couldn't find page", 404
    else:
        return "Couldn't find page", 404

@app.errorhandler(404)
def err_404(e):
    return "Couldn't find page",404

app.run(host='127.0.0.1', port=3001)
