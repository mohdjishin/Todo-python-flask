from crypt import methods
from email import message
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
        
        
        
        
@app.route('/update/<id>', methods =['POST','GET'])
def view_update(id):
    ID = int(escape(id))
    
    if request.method == 'GET':
        return show_todo_data(ID)
    else:
        
        
            
        msg = request.form['inputmg']
        sql = '''UPDATE list SET msg=%s  WHERE id =%s'''
        val = (msg,ID)
        mycursor.execute(sql,val)
        mydb.commit()
        if mycursor.rowcount > 0:
            message = 'Updated'
        else:
            message = None
        flash(message)
        return redirect(url_for('index'))
   
    
    
    
    
    
def show_todo_data(ID):
    
    sql = "SELECT * FROM list WHERE id = %s"
    val = (ID,)
    mycursor.execute(sql,val)
    result = mycursor.fetchone()
    return render_template('update_page.html', result=result)
    
    
    
    