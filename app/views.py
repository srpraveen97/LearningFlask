
from app import app

from flask import render_template, request, redirect, jsonify, make_response
from datetime import datetime

from werkzeug.utils import secure_filename

import os

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


@app.route('/guestbook')
def guestbook():
    return render_template('public/guestbook.html')

@app.route('/guestbook/create-entry', methods=['POST'])
def create_entry():
    
    req = request.get_json()
    
    print(req)   
    
    res = make_response(jsonify(req), 200) 
    
    return res

@app.route('/query')
def query():
    
    if request.args:
        
        args = request.args
        
        serialized = ", ".join(f"{k}: {v}" for k, v in args.items())
    
        return f"Query: {serialized}", 200
    
    return "No Query received", 200


def allowed_image(filename):
    
    if not "." in filename:
        return False
    
    ext = filename.rsplit(".",1)[1]
    
    if ext.upper() in app.config["ALLOWED_IMAGE_EXTENTIONS"]:
        return True
    
    return False
    


@app.route("/upload-image", methods=['POST','GET'])
def upload_image():
    
    if request.method == "POST":
        
        if request.files:
            
            image = request.files["image"]
            
            if image.filename == "":
                
                print("Image must have a filename")
                
                return redirect(request.url)
            
            if not allowed_image(image.filename):
                
                print("That image extension is not valid!")
                
                return redirect(request.url)
            
            else:
                
                filename = secure_filename(image.filename)
            
            image.save(os.path.join(app.config["IMAGE_UPLOADS"],filename))
            
            print("Image Saved")
            
            return redirect(request.url)
    
    return render_template("public/upload_image.html")
