from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def lambda_handler(event=None, context=None):
    
    return 'hello!'

@app.route('/<name>', methods=['GET', 'POST'])
def hello_name(name):
    
    return 'hello ' + name

if __name__ == '__main__':
    app.run()