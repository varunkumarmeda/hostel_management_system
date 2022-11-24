import streamlit as st
import mysql.connector

from create import create
from database import create_table,quer
from delete import delete
from read import read
from update import update

def main():
    st.title("HOSTEL MANAGEMENT SYSTEM")
    menu = ["Add ", "View ", "Edit", "Remove ","Query"]
    choice = st.sidebar.selectbox("Menu", menu)
    table_names=["hostel_manager","visitor","student"]
    table=st.sidebar.selectbox("table", table_names)

    create_table()
    if choice == "Add ":
        if table=='hostel_manager':
            st.subheader("Enter manager Details:")
            create(table)
        elif table=='student':
            st.subheader("Enter student Details:")
            create(table)
        elif table=='visitor':
            st.subheader("Enter visitor Details:")
            create(table)
    elif choice == "View ":
        if table=='hostel_manager':
            st.subheader("Enter manager Details:")
            read(table)
        elif table=='student':
            st.subheader("Enter student Details:")
            read(table)
        elif table=='visitor':
            st.subheader("Enter visitor Details:")
            read(table)

    elif choice == "Edit":
        if table=='student':
            st.subheader("Enter STUDENT Details:")
            update(table)

    elif choice == "Remove ":
        if table=='hostel_manager':
            st.subheader("Enter manager Details:")
            delete(table)
        elif table=='student':
            st.subheader("Enter student Details:")
            delete(table)
        elif table=='visitor':
            st.subheader("Enter visitor Details:")
            delete(table)

    elif choice=='Query':
        st.subheader("Enter the Query:")
        quer()

if __name__ == '__main__':
    main()