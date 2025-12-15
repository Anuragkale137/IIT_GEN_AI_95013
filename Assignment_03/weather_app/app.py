import streamlit as st

st.set_page_config(page_title="Login App")

st.title("Login Page")

def login(username, password):
    # Fake authentication
    return username == password

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if login(username, password):
            st.session_state.logged_in = True
            st.success("Login successful. Go to Weather page 👉")
        else:
            st.error("Invalid username or password")
else:
    st.success("You are already logged in. Use sidebar to navigate.")
