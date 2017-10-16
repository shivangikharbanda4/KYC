from flask import Flask, render_template, request
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map
import sqlite3 as sql
app = Flask(__name__)

app.config['GOOGLEMAPS_KEY'] = "AIzaSyCDVDHiJIjCT7MuzDO0uNv6gknHDRx7V-I"

GoogleMaps(app, key="AIzaSyCDVDHiJIjCT7MuzDO0uNv6gknHDRx7V-I")

@app.route('/')
def homepage():
   return render_template('homepage.html')

@app.route('/vision')
def vision():
   return render_template('vision.html')


@app.route('/mission')
def mission():
   return render_template('mission.html')


@app.route('/addpass')
def addpass():
   return render_template('Passengerreg.html')


@app.route('/addcoolie')
def addcoolie():
   return render_template('cooliereg.html')


@app.route("/doublemarkermap")
def doublemarkermap():
    return render_template('doublemarkermap.html')


@app.route('/alldata')
def alldata():
   return render_template('list.html')


@app.route('/passlogin')
def passlogin():
   return render_template('Passengerlogin.html')

@app.route('/arrtime')
def arrtime():
   return render_template('times.html')


@app.route('/coolielogin')
def coolielogin():
   return render_template('coolielogin.html')


@app.route('/feedback')
def feedback():
   return render_template('feedback.html')

@app.route('/logout')
def logout():
   return render_template('homepage.html')


@app.route('/calculate')
def calculate():
   return render_template('calc.html')


@app.route('/passe',methods = ['POST','GET'])
def passe():
   if request.method == 'POST':
      try:
         fname = request.form['passfname']
         mname = request.form['passmname']
         lname = request.form['passlname']
         mobile = request.form['passmobile']
         email = request.form['passemail']
         username = request.form['passusername']
         password = request.form['passpassword']
         
         with sql.connect("proj.db") as con:
            cur = con.cursor()
            
            cur.execute("INSERT INTO passenger (fname,mname,lname,mobile,email,username,password)VALUES (?,?,?,?,?,?,?)",(fname,mname,lname,mobile,email,username,password) )
            
            con.commit()
            msg = "Record successfully added"
      except:
         con.rollback()
         msg = "error in insert operation"
      
      finally:
         return render_template("regfinal.html",msg = msg)
         con.close()


@app.route('/coolie',methods = ['POST','GET'])
def coolie():
   if request.method == 'POST':
      try:
         firstname = request.form['cooliefirstname']
         middlename = request.form['cooliemiddlename']
         lastname = request.form['coolielastname']
         username = request.form['coolieusername']
         mobile_1 = request.form['cooliemobile_1']
         mobile_2 = request.form['cooliemobile_2']
         batch_no = request.form['cooliebatch_no']
         street = request.form['cooliestreet']
         city = request.form['cooliecity']
         state = request.form['cooliestate']
         country = request.form['cooliecountry']
         pin = request.form['cooliepin']
         aadhar_no = request.form['coolieaadhar_no']
         fmcontact_no = request.form['cooliefmcontact_no']
         passw = request.form['cooliepassw']
         
         with sql.connect("proj.db") as con:
            cur = con.cursor()
            
            cur.execute("INSERT INTO coolie (firstname,middlename,lastname,username,mobile_1,mobile_2,batch_no,street,city,state,country,pin,aadhar_no,fmcontact_no,passw)VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(firstname,middlename,lastname,username,mobile_1,mobile_2,batch_no,street,city,state,country,pin,aadhar_no,fmcontact_no,passw) )
            
            con.commit()
            msg = "Record successfully added"
      except:
         con.rollback()
         msg = "error in insert operation"
      
      finally:
         return render_template("regfinal.html",msg = msg)
         con.close()
         

@app.route('/printlist')
def printlist():
    con = sql.connect("proj.db")
    con.row_factory = sql.Row
   
    cur = con.cursor()
    cur.execute("select firstname,middlename,lastname,mobile_1,mobile_2,batch_no from coolie")
   
    rows = cur.fetchall();
    return render_template("list.html",rows = rows)



@app.route('/simplesearch')
def simplesearch():
   return render_template('Search.html')

@app.route('/simple', methods = ['POST'])
def simple():
    if request.method == 'POST':
        con = sql.connect("proj.db")
        myvar= request.form['cooliefirstname']
        #con.row_factory = sql.Row
        cur = con.cursor()
        
        query = ("Select firstname,middlename,lastname,mobile_1,mobile_2,batch_no from coolie where firstname = '{myvar}'"). format(myvar=myvar)
        cur.execute(query)
        row = cur.fetchone();
        print (row)
        return render_template("result.html", row = row)



@app.route('/advancesearch')
def advancesearch():
   return render_template('adv.html')

@app.route('/advance', methods = ['POST'])
def advance():
    if request.method == 'POST':
        con = sql.connect("proj.db")
        myvar= request.form['cooliefirstname']
        myvar2= request.form['cooliebatch_no']
        #con.row_factory = sql.Row
        cur = con.cursor()
        
        query = ("Select firstname,middlename,lastname,mobile_1,mobile_2,batch_no from coolie where firstname = '{myvar}' and batch_no = '{myvar2}'"). format(myvar=myvar,myvar2=myvar2)
        cur.execute(query)
        row = cur.fetchone();
        print (row)
        return render_template("Advanced.html", row = row)


   
@app.route('/coolielog', methods = ['POST'])
def coolielog():
    if request.method == 'POST':
        myvar= request.form['cooliebatch_no']
        myvar2 = request.form['cooliepassw']
        con = sql.connect("proj.db")
        
        #con.row_factory = sql.Row
        cur = con.cursor()
        
        query = ("Select passw from coolie where batch_no = '{myvar}'"). format(myvar=myvar)
        cur.execute(query)
        row = cur.fetchone();
        print (row)
        a = str(row)
        result1=a[2:-3]
        if myvar2 == result1 :
           ta = "login successful"
        else :
           ta = "login failed"

    return render_template("dashboard.html", result = ta)


@app.route('/passlog', methods = ['POST'])
def passlog():
    if request.method == 'POST':
        myvar= request.form['passemail']
        myvar2= request.form['passpassword']
        con = sql.connect("proj.db")
        
        #con.row_factory = sql.Row
        cur = con.cursor()
        
        query = ("Select password from passenger where email = '{myvar}'"). format(myvar=myvar)
        cur.execute(query)
        row = cur.fetchone();
        print (row)
        a = str(row)
        q1= ("select fname from passenger where email = '{myvar}'"). format(myvar=myvar)
        cur.execute(query)
        ro = cur.fetchone();
        print (ro)
        b = str(ro)
        result1=a[2:-3]
        res=b[2:-3]
        if myvar2 == result1 :
           ta = "login successful"
        else :
           ta = "login failed"

    return render_template("dashboard.html", result = ta, re = res)


@app.route('/locsearch', methods = ['POST'])
def locsearch():
    '''lat1 = None
    lat2 = None
    long1 = None
    long2 = None'''
    con = sql.connect("proj.db")
    start= request.form['start']
    stop= request.form['stop']
    cur = con.cursor()
    
    #Lat1 = ("select Lat from maps where Location = ?",(start,))
    cur.execute("select Lat from coolie where street = ?",(start,))
    a = cur.fetchone();
    ta=str(a)
    startlat=ta[1:-3]

    cur.execute("select Long from coolie where street = ?",(start,))
    b = cur.fetchone();
    ca=str(b)
    startlong=ca[1:-3]

    cur.execute("select Lat from coolie where street = ?",(stop,))
    w = cur.fetchone();   
    wa=str(w)
    stoplat=wa[1:-3]

    cur.execute("select Long from coolie where street = ?",(stop,))
    e = cur.fetchone();
    ea=str(e)
    startlong=ea[1:-3]  



    #return render_template("doublemarkermap.html",result = qa)
    #return render_template("doublemarkermap.html",result = xa)
    #return render_template("doublemarkermap.html",result = cda)
    return render_template("abc.html",result = startlat,result1 = startlong, result2 = stoplat, result3 = startlong) 
    con.close()   
   



@app.route('/addfb',methods = ['POST','GET'])
def addfb():
   if request.method == 'POST':
      try:
         rating = request.form['passfeedback']
         
         with sql.connect("proj.db") as con:
            cur = con.cursor()
            
            cur.execute("INSERT INTO passenger (rating)VALUES (?)",(rating) )
            
            con.commit()
            msg = "Record successfully added"
      except:
         con.rollback()
         msg = "error in insert operation"
      
      finally:
         return render_template("feed.html",msg = msg)
         con.close()


@app.route('/fblogin', methods = ['POST'])
def fblogin():
    if request.method == 'POST':
        myvar= request.form['passfname']
        myvar2 = request.form['passemail']
        con = sql.connect("proj.db")
        
        #con.row_factory = sql.Row
        cur = con.cursor()
        query = ("Select email from passenger where fname = '{myvar}'"). format(myvar=myvar)
        cur.execute(query)
        row = cur.fetchone();
        print (row)
        a = str(row)
        result1=a[2:-3]
        if myvar2 == result1 :
           ta = "login successful"
        else :
           ta = "login failed"

    return render_template("feed.html", msg = ta)


   
@app.route('/time',methods = ['POST','GET'])
def time():
   if request.method == 'POST':
         var = request.form['arrival']
         var2 = int(var)
         con = sql.connect("proj.db")
         cur = con.cursor()
         query1 = ("select firstname,middlename,lastname,mobile_1 from coolie where '{var2}'- stop_time >30") . format(var2=var2)
         cur.execute(query1)
         row1 = cur.fetchall();

         return render_template("listdisplay.html", msg = row1)


@app.route('/calcu', methods = ['POST'])
def calcu():
    if request.method == 'POST':
        myvar = request.form['firstname']
        myvar2= request.form['no_of_bag']
        var2 = int(myvar2)
        '''con = sql.connect("mydata.db")
        cur = con.cursor()
        query = ("Select bag from bags where fname = '{myvar}'"). format(myvar=myvar)
        cur.execute(query)
        row = cur.fetchone();'''
        print (var2)
        '''a = str(row)
        var = a[1:-2]
        print(var)
        print(myvar)'''
        '''myvar.strip(")");
        myvar.strip("'");'''
        if var2<=3 :
           var1 = var2*25
        elif var2>3 :
           var1 = var2*30
           
        print (var1)
        '''a = str(var)'''
        '''result1= a.strip("(",")","'")'''
        
    return render_template("resultfare.html", result = var1)      


if __name__ == '__main__':
   app.run(debug = True)
