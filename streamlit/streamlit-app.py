import streamlit as st
import requests
import json
from utils import createUser, chat, post
# Page title
st.title("AIDe")


# Server URL

# response
# userId

# First prompt
prompt = st.text_input("Start journaling your thoughts")

# Button
if st.button('Generate response'):
    #response code here
    response = "TEST STRING Sorry to hear that"
    st.write(response)

# response =
# Print response









    response = createUser("1", "shane", "01234567")
    userId = response["userId"]
    print(chat(userId, "good morning")['content'])
