import mysql.connector
import pandas as pd
import streamlit as st
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="pes1ug20cs250",
    database="hostel_management"
)
c = mydb.cursor()


def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS `STUDENT` ( `Student_id` varchar(255) NOT NULL,`Fname` varchar(255) NOT NULL,`Lname` varchar(255) NOT NULL,`Mob_no` varchar(255) NOT NULL,`Dept` varchar(255) NOT NULL,`Year_of_study` varchar(255) NOT NULL,`Hostel_id` int(10) DEFAULT NULL,`Room_id` int(10) DEFAULT NULL, PRIMARY KEY (`Student_id`),KEY `Hostel_id` (`Hostel_id`), KEY `Room_id` (`Room_id`),FOREIGN KEY (`Hostel_id`) REFERENCES `Hostel` (`Hostel_id`) on delete cascade on  update cascade,FOREIGN KEY (`Room_id`) REFERENCES `Room` (`Room_id`) on  delete cascade on  update cascade);')
    c.execute("CREATE TABLE IF NOT EXISTS `hostel_manager` ( `Hostel_man_id` int(10) NOT NULL AUTO_INCREMENT,`Username` varchar(255) NOT NULL,`Fname` varchar(255) NOT NULL,`Lname` varchar(255) NOT NULL,`Mob_no` varchar(255) NOT NULL,`Hostel_id` int(10) NOT NULL,`Pwd` LONGTEXT NOT NULL,`Isadmin` tinyint(1) DEFAULT '0',PRIMARY KEY (`Hostel_man_id`),UNIQUE (`Username`),KEY `Hostel_id` (`Hostel_id`),FOREIGN KEY (`Hostel_id`) REFERENCES `Hostel` (`Hostel_id`) on delete cascade on  update cascade);")
    c.execute('CREATE TABLE IF NOT EXISTS `visitor` ( VISITOR_ID INT NOT NULL,IN_TIME DATETIME,OUT_TIME DATETIME,NAME VARCHAR(20),Student_id VARCHAR(20),PRIMARY KEY  (VISITOR_ID),FOREIGN KEY (Student_id) REFERENCES STUDENT(Student_id) on  delete  cascade on  update cascade );')
    

def add_data(STUD_ID,NAME1,NAME2,PH_NO,DEPARTMENT,YEAR,H_ID,R_ID):
    c.execute('INSERT INTO STUDENT (`Student_id`,`Fname`,`Lname`,`Mob_no`,`Dept` ,`Year_of_study` ,`Hostel_id`,`Room_id`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s);',
              (STUD_ID,NAME1,NAME2,PH_NO,DEPARTMENT,YEAR,H_ID,R_ID))
    mydb.commit()
def add_data_VISITOR(VISITOR_ID,IN_TIME,OUT_TIME,NAME,STUDENT_ID):
    c.execute('INSERT INTO visitor (VISITOR_ID,IN_TIME,OUT_TIME,NAME,STUDENT_ID) VALUES (%s,%s,%s,%s,%s);',
              (VISITOR_ID,IN_TIME,OUT_TIME,NAME,STUDENT_ID))
    mydb.commit()
def add_data_HOSTELMANAGER(HOSTEL_MAN_ID,USERNAME,FNAME,LNAME,MOB_NO,HOSTEL_ID,PWD,ISADMIN):
    c.execute('INSERT INTO hostel_manager (HOSTEL_MAN_ID,USERNAME,FNAME,LNAME,MOB_NO,HOSTEL_ID,PWD,ISADMIN) VALUES (%s,%s,%s,%s,%s,%s,%s,%s);',
              (HOSTEL_MAN_ID,USERNAME,FNAME,LNAME,MOB_NO,HOSTEL_ID,PWD,ISADMIN))
    mydb.commit()

def view_all_data():
    c.execute('SELECT * FROM STUDENT')
    data = c.fetchall()
    return data

def view_all_manager():
    c.execute('SELECT * FROM hostel_manager')
    data = c.fetchall()
    return data
def view_all_visitor():
    c.execute('SELECT * FROM visitor')
    data = c.fetchall()
    return data

def view_only_student_names():
    c.execute('SELECT fName FROM STUDENT')
    data = c.fetchall()
    return data
def view_only_manager():
    c.execute('SELECT HOSTEL_MAN_ID FROM hostel_manager')
    data = c.fetchall()
    return data
def view_only_visitor():
    c.execute('SELECT VISITOR_ID FROM visitor')
    data = c.fetchall()
    return data

def get_details(STUD_ID):
    c.execute('SELECT * FROM STUDENT WHERE FName="{}"'.format(STUD_ID))
    data = c.fetchall()
    return data



def edit_details(new_STUD_ID,new_NAME1,new_NAME2,new_PH_NO,new_DEPARTMENT,new_YEAR , new_H_ID,  new_R_ID,STUD_ID,NAME1,NAME2,PH_NO,DEPARTMENT,YEAR,H_ID,R_ID):
    c.execute("UPDATE student SET Student_id=%s, Fname=%s, Lname=%s, Mob_no=%s, Dept=%s, Year_of_study=%s,Hostel_id=%s,Room_id=%s WHERE "
              "Student_id=%s and Fname=%s and Lname=%s and Mob_no=%s and Dept=%s and Year_of_study=%s and Hostel_id=%s and Room_id=%s" , (new_STUD_ID,new_NAME1,new_NAME2,new_PH_NO,new_DEPARTMENT,new_YEAR , new_H_ID,  new_R_ID,STUD_ID,NAME1,NAME2,PH_NO,DEPARTMENT,YEAR,H_ID,R_ID))
    mydb.commit()
    data = c.fetchall()
    return data


def delete_data(STUD_ID):
    c.execute('DELETE FROM student WHERE FName="{}"'.format(STUD_ID))
    mydb.commit()
def delete_data_hostel_manager(Hostel_man_id):
    c.execute('DELETE FROM customer_details WHERE hostel_man_id="{}"'.format(Hostel_man_id))
    mydb.commit()

def delete_visitor(VISITOR_ID):
    c.execute('DELETE FROM car_category WHERE VISITOR_ID="{}"'.format(VISITOR_ID))
    mydb.commit()
    
def quer():  
    with st.form(key="form1"):
        str1=st.text_area("Enter the query here:")
        submit=st.form_submit_button("Submit")
        if(submit):
            try:
                c.execute(str1)
                df=pd.DataFrame(c.fetchall())
                st.table(df)
            except mysql.connector.Error as e:
                st.warning(e)