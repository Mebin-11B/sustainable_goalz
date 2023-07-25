from flask import *
from sahana.timee import cur_t
app = Flask(__name__)

@app.route('/')
def message():
    t = cur_t()
    return render_template("index.html",t = t)

if __name__ == '__main__':
   app.run(debug = True)