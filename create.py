import streamlit as st
from database import add_data,add_data_VISITOR,add_data_HOSTELMANAGER


def create(table):
    if table=='student':
        col1, col2 ,col3= st.columns(3)
        with col1:
            STUD_ID = st.text_input(" STUD_ID:")
            NAME1 = st.text_input("NAME1:")
            NAME2= st.text_input("NAME2:")
        with col2:
            PH_NO = st.text_input("PH_NO:")
            DEPARTMENT = st.text_input("DEPARTMENT:")
            YEAR = st.text_input("YEAR:")
        with col3:
            H_ID = st.text_input("H_ID:")
            
            R_ID= st.text_input("R_ID:") 
        
        if st.button("Add"):
            add_data(STUD_ID,NAME1,NAME2,PH_NO,DEPARTMENT,YEAR,H_ID,R_ID)
            st.success("Successfully added student: {}".format(STUD_ID))


    elif table=='visitor':
        col1, col2 = st.columns(2)
        with col1:
            VISITOR_ID = st.text_input(" VISITOR_ID:")
            IN_TIME = st.text_input("INTIME:")
            OUT_TIME= st.text_input("OUTTIME:")
        with col2:
            NAME = st.text_input("NAME:")
            STUDENT_ID = st.text_input("STUDENT_ID:")
            
        
        if st.button("Add"):
            add_data_VISITOR(VISITOR_ID,IN_TIME,OUT_TIME,NAME,STUDENT_ID)
            st.success("Successfully added VISITOR: {}".format(VISITOR_ID))


    elif table=='hostel_manager':
        col1, col2 ,col3= st.columns(3)
        with col1:
            HOSTEL_MAN_ID = st.text_input(" HOSTEL_MANAGER_ID:")
            USERNAME = st.text_input("USERNAME:")
            FNAME= st.text_input("NAME1:")
        with col2:
            LNAME = st.text_input("NAME2:")
            MOB_NO = st.text_input("MOB_NUMBER:")
            HOSTEL_ID = st.text_input("HOSTEL_ID:")
        with col3:
            PWD = st.text_input("PASSWORD:")
            
            ISADMIN = st.selectbox("ISADMIN 1/0 FOR YES OR NO ", ["1", "0"])
        
        if st.button("Add"):
            add_data_HOSTELMANAGER(HOSTEL_MAN_ID,USERNAME,FNAME,LNAME,MOB_NO,HOSTEL_ID,PWD,ISADMIN)
            st.success("Successfully added MANAGER: {}".format(HOSTEL_MAN_ID))