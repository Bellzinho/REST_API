from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Hello(Resource):

  def get(self):
    return {'hello':'Hello World! Esta é minha primeira API REST'}


api.add_resource(Hello, '/hello')

if __name__ == '__main__':
    app.run(debug=True)