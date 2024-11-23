from flask import Flask


HOST = '0.0.0.0'
PORT = 5000

def create_app():
    app = Flask(__name__)

if __name__ == '__main__':
    app = create_app()

    from server.routes import api
    app.register_blueprint(api)

    app.run(host=HOST, port=PORT)