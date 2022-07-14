from app import app

from flask import render_template, request, redirect, jsonify, make_response
from datetime import datetime

@app.template_filter("clean_date")
def clean_date(dt):
    return dt.strftime("%d %b %Y")

@app.route('/')
def index():
    return render_template("public/index.html")

@app.route('/jinja')
def jinja():
    
    my_name = "Praveen"
    age = 25
    langs = ['Python','R','Bash','HTML']
    friends = {"Nina":29,"Somesh":25,"Daniela":29}
    
    colors = ('Red','Blue')
    
    cool = True
    
    class GitRemote:
        
        def __init__(self,name,description, url):
            self.name = name
            self.description = description
            self.url = url
            
        def pull(self):
            return f'pulling repo {self.name}'
        
        def clone(self):
            return f'cloning into {self.url}'
        
    my_remote = GitRemote(name='Flask Jinja',description='Template Design Tutorial',url='http://github.com/srpraveen97/jinja.git')
        
    def repeat(x,qty):
        return x*qty
    
    date = datetime.utcnow()
    
    my_html = '<h1>This is some HTML</h1>'
    
    suspicious = "<script>alert('You got Hacked')</script>"
    
    return render_template("public/jinja.html", my_name=my_name, age = age,
                           langs = langs, friends = friends, colors = colors,
                           cool = cool, GitRemote=GitRemote, repeat=repeat, my_remote=my_remote, date = date,
                           my_html = my_html, suspicious=suspicious)

@app.route('/about')
def about():
    return "<h1 style='color:red'>About!!!</h1>"

@app.route('/sign-up', methods=["GET","POST"])
def sign_up():
    
    if request.method == "POST":
        
        req = request.form
        
        username = req["username"]
        email = req.get("email")
        password = request.form["password"]
        
        print(username, email, password)

        
        return redirect(request.url)
    
    return render_template('public/sign_up.html')

users = {
    "elonmusk" : {"name":"Elon Musk", "bio":"Technology Enterpreneur, Investor, and Engineer","twitter_handle":"@elonmusk"},
    "gvanrossum" : {"name":"Guido Van Rossum", "bio":"Creator of Python programming language","twitter_handle":"@gvanrossum"},
    "mitsuhiko" : {"name":"Armin Ronacher", "bio":"Creator of the Flask Framework","twitter_handle":"@mitsuhiko"}
}

@app.route("/profile/<username>")
def profile(username):
    
    user = None
    
    if username in users:
        user = users[username]
    
    return render_template("public/profile.html",user=user,username=username)

@app.route("/multiple/<foo>/<bar>/<baz>")
def multi(foo, bar, baz):
          return f'foo is {foo}, bar is {bar}, baz is {baz}'
      
      
@app.route('/json',methods=['POST'])
def json():
    
    if request.is_json:
        req = request.get_json()
        
        response = {
            "message":"JSON received",
            "name": req.get("name")
        }
        
        res = make_response(jsonify(response), 200)
        
        return res
    
    res = make_response(jsonify({"message":"No JSON received"}), 400)
    return res


