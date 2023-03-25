from flask import Flask, render_template, request, jsonify, url_for, redirect,make_response,Response
import mysql.connector
import json



class handle_data():
    __mydb=mysql.connector.connect(host="localhost",user="root",password="1234",database="blongSchooll")
    __mycursor = __mydb.cursor()
    
    def run(self):
       pass

    def getCatagoryTable(self,mail,mobile):
        query="select * from category where mail= %s && mobile=%s"
        value=(mail,mobile,)
        print(value)
        self.__mycursor.execute(query,value)
        result=self.__mycursor.fetchall()
        return result

    def getCourseTable(self,mail,mobile):
        query="select title,category,price from courses where mail= %s && mobile=%s"
        value=(mail,mobile,)
        print(value)
        self.__mycursor.execute(query,value)
        result=self.__mycursor.fetchall()
        return result

    def ver_id_exists(self,email,mobile):
        query="select * from users where email= %s && mobile=%s"
        value=(email,mobile,)
        self.__mycursor.execute(query,value)
        result=self.__mycursor.fetchall()
        if result==[]:
            return False
        else:
            return True

    def ver_cat_exists(self,cat,email,mobile):
        query="select * from category where mail= %s && mobile=%s && cat=%s"
        value=(email,mobile,cat)
        self.__mycursor.execute(query,value)
        result=self.__mycursor.fetchall()
        if result==[]:
            return False
        else:
            return True

    def save_new_user(self,fname,lname,mailid,mobile,upass,spaciality):
        print("save user")
        query="insert into users values (%s, %s, %s, %s, %s,%s)"
        value=(fname,lname,mailid,mobile,upass,spaciality)
        self.__mycursor.execute(query,value)
        self.__mydb.commit()

    def save_course(self,title,disc,cat,level,req,outcome,price,discount,channel,url,thmb,mkey,mdisc,mail,mobile):
        query="insert into courses values (%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s)"
        values=(title,disc,cat,level,req,outcome,price,discount,channel,url,"done",mkey,mdisc,mail,mobile)
        #print(values)
        self.__mycursor.execute(query,values)
        self.__mydb.commit()

    def add_cat(self,cat,name,mailid,mobile):
        print("catagory added")
        query="insert into category values (%s, %s, %s, %s)"
        value=(name,mailid,mobile,cat)
        self.__mycursor.execute(query,value)
        self.__mydb.commit()

    def login(self,uid,upass):
        query="select * from users where email=%s AND password=%s"
        value=(uid,upass)
        self.__mycursor.execute(query,value)
        result=self.__mycursor.fetchall()
        if result ==[]:
            return False
        else:
            return result

    def del_cat(self,mail,mobile,cat):
        try:
            query="delete from category where mail=%s AND mobile=%s AND cat=%s"
            value=(mail,mobile,cat)
            self.__mycursor.execute(query,value)
            self.__mydb.commit()
            return "done"
        except:
            return "try again"
        
        
    


app=Flask(__name__)
@app.route("/")
def start():
    return render_template("main.html")

@app.route("/Design")
def Design():
    return render_template("Design.html")

@app.route("/home")
def start_home():
    return render_template("home.html")

@app.route("/sign")
def sign():
    return render_template("signup1.html")

@app.route("/login_load")
def login_load():
    return render_template("login1.html")

@app.route("/afterlogin")
def afterlogin():
    print("login success")
    return render_template("admin_dashboard.html")

@app.route("/headerlogin")
def headerlogin():
    return render_template("header.html")

@app.route("/sidebarlogin")
def sidebarlogin():
    return render_template("sidebar.html")

@app.route("/catagory")
def catagory():
    return render_template("catagory.html")

@app.route("/coupens")
def coupens():
    return render_template("coupens.html")




@app.route("/courses")
def courses():
    return render_template("courses.html")

@app.route("/coursesBasic")
def coursB():
    return render_template("sub_courses/courseBasic.html")

@app.route("/coursesReq")
def coursR():
    return render_template("sub_courses/courseReq.html")

@app.route("/coursesOutcome")
def coursO():
    return render_template("sub_courses/courseOutcome.html")

@app.route("/coursesPrice")
def courseP():
    return render_template("sub_courses/coursePrice.html")

@app.route("/coursesMedia")
def courseM():
    return render_template("sub_courses/courseMedia.html")

@app.route("/coursesSeo")
def courseS():
    return render_template("sub_courses/seo.html")

@app.route("/courseFinish")
def courseF():
    return render_template("sub_courses/courseFinish.html")



@app.route("/addcoupen")
def addcoupen():
    return render_template("sub_coupons/addcoupon.html")

@app.route("/event")
def event():
    return render_template("events.html")

@app.route("/addevent")
def addevent():
    return render_template("sub_events/addevent.html")



@app.route("/instructorlist")
def instructorlist():
    return render_template("Instructorlist.html")

@app.route("/instList")
def addinstructorlist():
    return render_template("sub_instructor/addinstructorlist.html")

@app.route("/logincred_instruct")
def logincred_instruct():
    return render_template("Logincredentials.html")

@app.route("/social_instruct")
def social_instruct():
    return render_template("Socialinformation.html")

@app.route("/pay_instruct")
def pay_instruct():
    return render_template("Paymentinfo.html")

@app.route("/finish_instruct")
def finish_instruct():
    return render_template("Finish.html")
#####
@app.route("/instructorPay")
def instructorPay():
    return render_template("sub_instructor/instructorpayout.html")
@app.route("/instructorSet")
def instructorSet():
    return render_template("Instructorsettings.html")



##############################################################################################

@app.route("/add_cat", methods=["POST"])
def add_cat():
    req = request.values
    print(req)
    cat=req['cat']
    name=req['name']
    mail=req['mail']
    mobile=req['mobile']
    db=handle_data()
    ret=db.ver_cat_exists(cat,mail,mobile)
    if(ret==False):
        db.add_cat(cat,name,mail,mobile)
        return "done"
    return "exists"

@app.route("/getCatagoryTable", methods=["POST"])
def getCatagoryTable():
    req = request.values
    mail=req["mail"]
    mobile=req["mobile"]
    ptype=req["func"]
    db=handle_data()
    #print(user)
    ret=db.getCatagoryTable(mail,mobile)
    return {"ret":ret}

@app.route("/getCourseTable", methods=["POST"])
def getCourseTable():
    req = request.values
    mail=req["mail"]
    mobile=req["mobile"]
    ptype=req["func"]
    db=handle_data()
    #print(user)
    ret=db.getCourseTable(mail,mobile)
    print(ret)
    return {"ret":ret}

@app.route("/request_data", methods=["POST"])
def request_data():
    req = request.values
    #print("data: ",(req['fname'],req['lname'],req['email'],req['mob'],req['pass'],req['sp']))
    db=handle_data()
    ret=db.ver_id_exists(req["email"],req["mob"])
    if(ret==False):
        db.save_new_user(req['fname'],req['lname'],req['email'],req['mob'],req['pass'],req['sp'])
        return "done"
    return "exists"

@app.route("/request_login_data", methods=["POST"])
def request_login_data():
    req = request.values
    db=handle_data()
    ret=db.login(req['mail'],req['pass'])
    #print(ret)
    if(ret==False):
        return "not exists"
    ret={"ret":ret}
    return jsonify(ret)

@app.route("/del_cat",methods=["POST"])
def del_cat():
    req=request.values
    print(req)
    db=handle_data()
    ret=db.del_cat(req['mail'],req['mobile'],req['del'])
    return ret

@app.route("/save_courses", methods=["POST"])
def save_courses():
    req=request.values
    #print(req)
    #print(req["courseTitle"],req["courseDisc"],req["spaciality"],req["courseCategory"],req["courseReq"],req["coursePrice"],req["courseDiscount"],req["courseMedia"],req["url"],req["thumbnail"],req["meta"],req["mdisc"])
    #print(req["courseTitle"],req["courseDisc"],req["spaciality"],req["courseCategory"],req["courseReq"],req["courseOutcome"],req["coursePrice"],req["courseDiscount"],req["courseMedia"],req["url"],req["thumbnail"],req["meta"],req["mdisc"])
    #db=handle_data(basic["courseTitle"],basic["courseDisc"],basic["spaciality"],basic["courseCategory"],requ["courseReq"],outcome["courseOutcome"],price["coursePrice"],price["courseDiscount"],media["courseMedia"],media["url"],media["thumbnail"],seo["meta"],seo["mdisc"])
    #db.save_courses()
    db=handle_data()
    db.save_course(req["courseTitle"],req["courseDisc"],req["spaciality"],req["courseCategory"],req["courseReq"],req["courseOut"],req["coursePrice"],req["courseDiscount"],req["courseMedia"],req["url"],req["thumbnail"],req["meta"],req["mdisc"],req["mail"],req["mobile"])
    return ""


@app.route("/get_fonts", methods=["POST"])
def get_fonts():
    req=request.values
    return {"ret":new_cert.get_font("D:\\Projects\\External_downloads\\Fonts\\static")}

@app.route("/preview", methods=["POST"])
def preview():
    req=request.values
    names=["sarvesh","sameer"]
    #new_cert.pre(new_cert.cert_template_path+req["font"],names[0],int(req["size"]),req["col"])
    #print(req[""])
    print(req["col"])
    return new_cert.pre(names[0],int(req["size"]),req["font"],new_cert.cert_template_path,req["col"])

@app.route("/generate", methods=["POST"])
def generate():
    req=request.values
    names=["sarvesh","sameer"]
    for name in names:
        cert.start(cert.path+req["font"],name,int(req["size"]),req["col"])
    return "done"

app.run(port="5001")




