from flask import Flask, render_template
import config
from exts import db


app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)


@app.route('/')
def HomePage():
    return render_template("HomePage.html")


if __name__ == '__main__':
    app.run(debug=True, port=8080)
