#s-1: import flask from Flask object
from flask import Flask,request      #flask=module,Flask=class

#s2:   create a object with parameter name __name__
app = Flask(__name__)

##############################################################
#S-3: important step which we write logic for our web app and res other steps are common for alll web app
#Creating a route and binding with functionality
@app.route('/')
def home_page():
    return "This is home page"

@app.route('/search')
def search_page():
    return "This is search page"

@app.route('/add')
def adding():
    a=request.args.get('a')
    b=request.args.get('b')
    return str(int(a)+int(b))

@app.route('/upper')
def upper_case():
    c=request.args.get('c')
    upper=c.upper()
    return 'Uppercase is: ' + upper

#s-4: Run the app
if __name__ =='__main__':
    app.run(debug=True)