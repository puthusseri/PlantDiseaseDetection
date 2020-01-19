from flask import Flask, render_template, request      
import sys
import script as maincode
app = Flask(__name__)

@app.route("/")
def home():
	return render_template("upload.html")


@app.route("/home")
def result():
	return render_template("upload.html")
   
@app.route('/success', methods = ['POST'])  
def success():   
	f = request.files['file']
	name = f.filename  
	res = maincode.analysis(name)
	return render_template("home.html",fname=name,status=res)
if __name__ == "__main__":
	app.run(debug=True)
