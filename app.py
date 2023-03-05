from flask import Flask
# from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

# csrf = CSRFProtect(app)


@app.route('/')
def hello_world():
    return 'Laboratório Pipeline DevOps - v1'


if __name__ == '__main__':
    app.run()