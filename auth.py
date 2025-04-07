
import streamlit as st

def check_login():
    if "authenticated" not in st.session_state:
        st.session_state["authenticated"] = False

    if not st.session_state["authenticated"]:
        with st.form("login"):
            user = st.text_input("Username")
            pwd = st.text_input("Password", type="password")
            submit = st.form_submit_button("Login")
            if submit:
                if user == "admin" and pwd == "fingpt":
                    st.session_state["authenticated"] = True
                else:
                    st.error("Invalid credentials")
    return st.session_state["authenticated"]
