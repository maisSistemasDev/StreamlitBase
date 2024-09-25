from controllers.Auth import Login, Session
from components.LoginForm import LoginForm
import streamlit as st

def callback(result:dict):
    if(not result.get('access_token')):
        st.error('Usuário ou senha incorretos', icon=':material/error:')
    else:
        st.rerun()        


def on_submit(payload):
    login = Login("https://auto-api.maisistemasdev.com","/api-auth/token/")
    res = login.sign_in(username=payload.get("username"), password=payload.get("password"))
    return res

LoginPage = LoginForm(on_submit=on_submit, callback=callback).render()
