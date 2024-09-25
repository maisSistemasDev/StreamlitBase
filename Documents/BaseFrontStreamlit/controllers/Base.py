import streamlit as st
from abc import ABC, abstractmethod
import requests

class API(ABC):

    def __init__(self, base_url:str ,path:str) -> None:
        self.session = requests.sessions.Session()
        if 'token' in st.session_state:
            token = st.session_state['token']
            self.session.headers = {'Authorization':f'Bearer {token}'}
        self.base_url = base_url
        self.path = path

    def get(self,**args)->requests.Response:
        url = self.base_url + self.path
        res = self.session.get(url,**args)
        return res
    
    def post(self,**args)->requests.Response:
        url = self.base_url + self.path
        res = self.session.post(url,**args)
        res.raise_for_status()
        return res
    
    def put(self,**args)->requests.Response:
        url = self.base_url + self.path
        res = self.session.put(url, **args)
        res.raise_for_status()
        return res





        
        
