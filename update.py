import datetime
import pandas as pd
import streamlit as st
from database import view_all_data, view_only_student_names, get_details, edit_details


def update(table):
    if table=='student':
        result = view_all_data()
        st.table(result)
        # st.write(result)
        df = pd.DataFrame(result, columns=['Student_id','Fname','Lname','Mob_no','Dept' ,'Year_of_study' ,'Hostel_id','Room_id'])
        with st.expander("Current students"):
            st.dataframe(df)
        list_of_students = [i[0] for i in view_only_student_names()]
        selected_student = st.selectbox("student to Edit", list_of_students)
        selected_result = get_details(selected_student)
        # st.write(selected_result)
        if selected_result:
            STUD_ID = selected_result[0][0]
            NAME1 = selected_result[0][1]
            NAME2 = selected_result[0][2]
            PH_NO= selected_result[0][3]
            DEPARTMENT = selected_result[0][4]
            YEAR = selected_result[0][5]
            H_ID = selected_result[0][5]
            R_ID = selected_result[0][5]

            # Layout of Create

            col1, col2 ,col3= st.columns(3)
            with col1:
                new_STUD_ID = st.text_input(" STUD_ID:",STUD_ID)
                new_NAME1 = st.text_input("NAME1:",NAME1)
                new_NAME2= st.text_input("NAME2:",NAME2)
            with col2:
                new_PH_NO = st.text_input("PH_NO:",PH_NO)
                new_DEPARTMENT = st.text_input("DEPARTMENT:",DEPARTMENT)
                new_YEAR = st.text_input("YEAR:",YEAR)
            with col3:
                new_H_ID = st.text_input("H_ID:",H_ID)
                
                new_R_ID= st.text_input("R_ID:",R_ID) 
        

            if st.button("Update student"):
                edit_details(new_STUD_ID,new_NAME1,new_NAME2,new_PH_NO,new_DEPARTMENT,new_YEAR , new_H_ID,  new_R_ID,STUD_ID,NAME1,NAME2,PH_NO,DEPARTMENT,YEAR,H_ID,R_ID)
                st.success("Successfully updated:: {} to ::{}".format(NAME1, new_NAME1))

        result2 = view_all_data()
        df2 = pd.DataFrame(result2, columns=['Student_id','Fname','Lname','Mob_no','Dept' ,'Year_of_study' ,'Hostel_id','Room_id'])
        with st.expander("Updated data"):
            st.dataframe(df2)
