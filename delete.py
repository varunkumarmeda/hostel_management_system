import pandas as pd
import streamlit as st
from database import view_all_data, view_only_student_names, delete_data,view_all_manager,view_all_visitor,view_only_manager,delete_data_hostel_manager,view_only_visitor,delete_visitor


def delete(table):
    if table=='student':
        result = view_all_data()
        df = pd.DataFrame(result, columns=['Student_id','Fname','Lname','Mob_no','Dept' ,'Year_of_study' ,'Hostel_id','Room_id'])
        with st.expander("Current data"):
            st.dataframe(df)

        list_of_student = [i[0] for i in view_only_student_names()]
        selected_student = st.selectbox("student to Delete", list_of_student)
        st.warning("Do you want to delete ::{}".format(selected_student))
        if st.button("Delete student"):
            delete_data(selected_student)
            st.success("student has been deleted successfully")
        new_result = view_all_data()
        df2 = pd.DataFrame(new_result, columns=['Student_id','Fname','Lname','Mob_no','Dept' ,'Year_of_study' ,'Hostel_id','Room_id'])
        with st.expander("Updated data"):
            st.dataframe(df2)
    elif table=='hostel_manager':
        result = view_all_manager()
        df = pd.DataFrame(result, columns=['HOSTEL_MAN_ID','USERNAME','FNAME','LNAME','MOB_NO','HOSTEL_ID','PWD','ISADMIN'])
        with st.expander("Current data"):
            st.dataframe(df)

        list_of_admin = [i[0] for i in view_only_manager()]
        selected_admin = st.selectbox("admin to Delete", list_of_admin)
        st.warning("Do you want to delete ::{}".format(selected_admin))
        if st.button("Delete manager"):
            delete_data_hostel_manager(selected_admin)
            st.success("manager has been deleted successfully")
        new_result = view_all_manager()
        df2 = pd.DataFrame(new_result, columns=['HOSTEL_MAN_ID','USERNAME','FNAME','LNAME','MOB_NO','HOSTEL_ID','PWD','ISADMIN'])
        with st.expander("Updated data"):
            st.dataframe(df2)

    elif table=='visitor':
        result = view_all_visitor()
        df = pd.DataFrame(result, columns=['Category','No_of_persons','Cost_per_day','LateFee_charges'])
        with st.expander("Current data"):
            st.dataframe(df)

        list_of_dealer = [i[0] for i in view_only_visitor()]
        selected_dealer = st.selectbox("visitor to Delete", list_of_dealer)
        st.warning("Do you want to delete ::{}".format(selected_dealer))
        if st.button("Delete visitor"):
            delete_visitor(selected_dealer)
            st.success("visitor has been deleted successfully")
        new_result = view_all_visitor()
        df2 = pd.DataFrame(new_result, columns=['VISITOR_ID','IN_TIME','OUT_TIME','NAME','STUDENT_ID'])
        with st.expander("Updated data"):
            st.dataframe(df2)
