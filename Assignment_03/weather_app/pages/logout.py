import streamlit as st

st.title("Logout")

if "logged_in" in st.session_state and st.session_state.logged_in:
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.success("Thanks for using the application 🙏")
else:
    st.info("You are already logged out.")
