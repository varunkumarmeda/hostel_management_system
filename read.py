import pandas as pd
import streamlit as st
from database import view_all_data,view_all_manager,view_all_visitor


def read(table):
    if table=='student':
        result = view_all_data()
        # st.write(result)
        df = pd.DataFrame(result, columns=['Student_id','Fname','Lname','Mob_no','Dept' ,'Year_of_study' ,'Hostel_id','Room_id'])
        with st.expander("View all student"):
            st.dataframe(df)
    
    elif table=='hostel_manager':
        result = view_all_manager()
        # st.write(result)
        df = pd.DataFrame(result, columns=['HOSTEL_MAN_ID','USERNAME','FNAME','LNAME','MOB_NO','HOSTEL_ID','PWD','ISADMIN'])
        with st.expander("View all managers"):
            st.dataframe(df)
    elif table=='visitor':
        result = view_all_visitor()
        # st.write(result)
        df = pd.DataFrame(result, columns=['VISITOR_ID','IN_TIME','OUT_TIME','NAME','STUDENT_ID'])
        with st.expander("View visitors"):
            st.dataframe(df)