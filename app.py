from flask import Flask
from flask import render_template
import os

app = Flask(__name__)

@app.route("/")
def index():
  return '''<html>
<head>
<style>
h1 {text-align: center; color:blue; margin-top:100px;}
h2 {text-align: center;color:green;}
div {text-align: center;}
</style>
</head>
<body>
<h1>Grettings from Suroj!!</h1>
<h2>Welcome you all to Dockerized Python application!!</h2>
</body>
</html>'''

@app.route("/admin")
def admin():
  return '''<h1 style='color: green;'>This is about us</h1>'''
  
if __name__ == "__main__":
  port =  int(os.environ.get("PORT",8081))
  app.run(debug=True,host='0.0.0.0',port=port)
  
