from flask import Flask
from flask import render_template
import os

app = Flask(__name__)

@app.route("/")
def index():
  return '''<h1 style='color: blue;'>Grettings from Suroj!! Welcome you all!!</h1>'''

@app.route("/dashboard")
def about():
  #return '''<h1 style='color: green;'>This is about us</h1>'''
  return render_template("about.html")
  
if __name__ == "__main__":
  port =  int(os.environ.get("PORT",8081))
  app.run(debug=True,host='0.0.0.0',port=port)
  
