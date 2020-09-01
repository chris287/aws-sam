import json
from flask_lambda import FlaskLambda
from flask import request
import boto3

app = FlaskLambda(__name__)
ddb = boto3.resource('dynamodb')
table = ddb.Table('students')

@app.route('/')
def index(): 
    data = {
        "message":"Hello, world!"
    }
    return (
        json.dumps(data),
        200,
        {'Content-Type':'application/json'}
    )

@app.route('/students',methods=['GET','POST'])
def put_or_list_students():
    if request.method == 'GET':
        students = table.scan()['Items']
        return(
            json.dumps(students),
            200,
             {'Content-Type':'application/json'}
        )
    else:
        table.put_item(Item=request.form.to_dict())
        return(
            json.dumps({
                'message':'Student data created',
            }),
            200,
            {'Content-Type':'application/json'}
        )