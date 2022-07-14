from app import app

from flask import render_template
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