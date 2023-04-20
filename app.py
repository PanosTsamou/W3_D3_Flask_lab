from flask import Flask

app = Flask(__name__)

from controlers import controler

if __name__ == "__main__":
    app.run(debug=True)