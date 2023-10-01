"""
Backend API
Copyright (c) 2023 - adrianbotteon@gmail.com
"""

from model import User, Project, init, engine, session

# db init
init()

#test pullrequest
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/api/v1/project/create', methods=['POST'])
def create_project():
    try:
        new_project = Project(user_id=1)
        session.add(new_project)
        session.commit()
        
        return {"id":new_project.id, 'message':"Project has been created"}
    except:
        return "Failed"
    
if __name__ == '__main__':
    app.run(debug=True)