
from flask import Flask,render_template,jsonify
app = Flask(__name__)
RESULT = [{'match':'namibia vs usa',
        'Balaji Team':'usa',
        'Script':'lay namibia at every odds, if namibia lambi 280 bet not with 20% limit'}]
@app.route('/')

def hello_world():
   return render_template('home.html',result=RESULT)
@app.route("/api/result")
def list_result():
  return jsonify(RESULT)


if __name__ == '__main__':
   app.run(host = '0.0.0.0',debug = True)