import streamlit as st
from typing import Callable

class LoginForm:

    def __init__(self, on_submit:Callable,callback:Callable,username_label="E-mail", password_label="Password"):
        self.payload:dict = {}
        self.username_label = username_label
        self.password_label = password_label
        self.submit = None
        self.on_sumbit = on_submit
        self.callback = callback
    def render(self):

        form  = st.form("Login", border=True)
        self.payload["username"] = form.text_input(label=self.username_label,key="username")
        self.payload["password"] = form.text_input(label=self.password_label, key="password")
        self.submit = form.form_submit_button("Enviar")
        if(self.submit):
            with st.status("Verificando suas credenciais..."):
                result = self.on_sumbit(self.payload)
                self.callback(result)




