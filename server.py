from flask import Flask,render_template,redirect,request
from mysqlconnection import connectToMySQL    # import the function that will return an instance of a connection

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html") 
    

@app.route('/create_user', methods=["POST"])
def add_user_to_db():
    mysql = connectToMySQL('users')
    query = "INSERT INTO users (first_name,last_name,email) VALUES (%(first_name)s,%(last_name)s,%(email)s)"
    data = {
        "first_name":request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
    }

    mysql = connectToMySQL('users')
    mysql.query_db(query,data)
    return redirect('/read')

@app.route('/read')
def users():
    query = "SELECT * FROM users;"
    users = connectToMySQL('users').query_db(query)
    print(users)
    return render_template("display.html",all_users=users)
            
if __name__ == "__main__":
    app.run(debug=True)