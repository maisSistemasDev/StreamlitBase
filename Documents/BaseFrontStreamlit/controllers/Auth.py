from .Base import API
import streamlit as st
import os

class Session:

    def create(self, data:dict) -> None:
        for k in data.keys():
            st.session_state[k] = data[k]
    
    @property
    def token(self)->str|None:
        if 'access_token' in st.session_state.keys():
            return st.session_state['access_token']
        else:
            return None
    
    @property
    def refresh_token(self)->str|None:
        if 'refresh_token' in st.session_state.keys():
            return st.session_state['refresh_token']
        else:
            return None
    
    def logout(self):
        if 'access_token' in st.session_state.keys():
            del st.session_state['access_token']


class Login(API):
    client_id = st.secrets['secrets']["CLIENT_ID"]
    client_secret = st.secrets['secrets']["CLIENT_SECRET"]
    
    
    def sign_in(self, username:str, password:str):
        
        payload = {
        "client_id": self.client_id,
        "client_secret": self.client_secret,
        "grant_type":"password",
        "password":password,
        "username":username
        }

        print(payload)

        try:
            res = self.post(json=payload)
            if(res.status_code == 200):
                json_res = res.json()
                session = Session()
                session.create(json_res)
                return json_res
            else:
                return {'error':res.reason}
        except Exception as e:
            return {'error':str(e)}

