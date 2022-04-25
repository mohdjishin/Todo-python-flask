from crypt import methods
from glob import escape
from flask import Flask, render_template, request,flash, redirect,url_for
import mysql.connector


mydb = mysql.connector.connect(
    
    host= "localhost",
    user = "root",
    password = "",
    database= "todo"
    
)

mycursor = mydb.cursor(dictionary=True)

app = Flask(__name__)
app.secret_key = b'_325523ewvrX?'



@app.route('/')
def index():
    
    mycursor.execute("SELECT * FROM list")
    data = mycursor.fetchall()
    
    
    return render_template('table.html',data = data)


@app.route('/done/<id>', methods=['GET'])
def done(id):
    ID = int(escape(id))
    sql = "DELETE FROM list WHERE id= %s"
    val =(ID,)
    mycursor.execute(sql,val)
    mydb.commit()
    if mycursor.rowcount >0:
        message = "Done"
    else:
        message = None
    flash(message)
    return redirect(url_for('index'))
        
        
    