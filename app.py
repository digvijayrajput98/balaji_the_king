
from flask import Flask,render_template,jsonify
app = Flask(__name__)
RESULT = [{'match':' ',
        'Balaji Team':" ",
        'Script':' '}]
@app.route('/')

def hello_world():
   return render_template('home.html',result=RESULT)
@app.route("/api/result")
def list_result():
  return jsonify(RESULT)


if __name__ == '__main__':
   app.run(host = '0.0.0.0',debug = True)