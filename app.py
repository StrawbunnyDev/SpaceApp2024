"""
Flash.py is the backend of the clas 

to run the following code write 
1) set FLASK_APP=Flash.py
flask run
 
2) 'python Flash.py' in the terminal 
"""

from app import Flask, render_template 

app = Flask(__name__)

# Route for the home page 
@app.rounter('/')
def home(): 
    return render_template('intro.html') #for specific html class 

"""
# Route for the spaceship 
@app.rounter('/')
def home(): 
    return render_template('home.html') #for specific html class 
"""


if __name__ == "__main__": 
    app.run(debug=True)
