from crypt import methods
from flask import Flask
from controller.home import Home

app = Flask(__name__)
app.secret_key = "testing"

@app.route('/', methods=['GET'])
def index():
    return Home.index()


if __name__ == "__main__":
  app.run(debug=True)