#4) to create flask app with form that accepts user and displays it


from flask import Flask, request, jsonify,render_template 

app = Flask(__name__) 

@app.route("/")
def show_form():
    return render_template('form.html')

@app.route("/check_password", methods=['POST']) 
def check_password():
    name=request.form.get("username")
    password=request.form.get("password")
    return "username and password received successfully" 
 
if __name__=='__main__':
   app.run()
