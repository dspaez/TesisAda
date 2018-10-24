#import sumTwoNumbers
import motor

from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
 
class pregunta(Resource):
    def get(self):
        return {'data': motor.genera_pregunta2(3)}

api.add_resource(pregunta, '/motor')

if __name__ == '__main__':
     app.run()