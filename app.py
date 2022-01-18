from flask import Flask
import os

app = Flask(__name__)
@app.route("/")

def hello():
  return '''<h1 style='color: red;'>I'm a red H1 heading!</h1>'''

if __name__ == "__main__":
  port =  int(os.environ.get("PORT",8081))
  app.run(debug=True,host='0.0.0.0',port=port)
  
