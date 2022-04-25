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



@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'GET':
        mycursor.execute("SELECT * FROM list")
        data = mycursor.fetchall()
    else:
        msg = request.form['inputmg']
        sql = 'INSERT INTO list (msg) VALUES(%s);'
        val = (msg,)
        
        mycursor.execute(sql,val)
        mydb.commit()
        if mycursor.rowcount > 0:
            message = "Insert Success"
        else:
            message = None
        flash(message)
        return redirect(url_for('index'))
        
        
        
        
        return msg
    
    
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
        
        
    