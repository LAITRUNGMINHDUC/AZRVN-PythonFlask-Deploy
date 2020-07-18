from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/')
def index():
    my_str = 'Hello Azure Vietnam Community'
    my_str = my_str + '<br> Show Request <br>'
    my_str = my_str + '<pre>{}</pre>'.format(request.headers)
    return my_str

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')