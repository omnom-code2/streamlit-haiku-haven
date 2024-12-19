import streamlit as st
from frontend.pages import pages

hub = st.session_state.hub

with st.container(border=True):
  st.title("Log in")
  username = st.text_input("Username", key="login_username")
  password = st.text_input("Password", type="password")

  if st.button("Log in", type="primary"):
    user = hub.user_service.get_authenticated_user(username, password)
    if user:
      st.session_state.logged_in = True
      st.session_state.user = user
      st.rerun()
    else:
      st.error("Invalid username or password")

st.page_link(pages["signup"], label="Don't have an account? Sign up!")
