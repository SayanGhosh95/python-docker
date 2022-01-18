from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def index():
  return '''<h1 style='color: blue;'>Grettings from Suroj!!</h1>'''

@app.route("/about")
def about():
  return '''<h1 style='color: green;'>This is about us</h1>'''

if __name__ == "__main__":
  port =  int(os.environ.get("PORT",8081))
  app.run(debug=True,host='0.0.0.0',port=port)
  
