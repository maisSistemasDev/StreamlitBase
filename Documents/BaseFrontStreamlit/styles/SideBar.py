import streamlit as st
from .BaseStyles import BaseStyles

class Content(BaseStyles):   
    def __init__(self):
        self.target = '[data-testid="stSidebarContent"]'

class Icon(BaseStyles):
    def __init__(self, active=False):
        self.target = '.st-emotion-cache-xtjyj5 .e16edly10'
        if(not active):
            self.target = '.st-emotion-cache-6tkfeg'
    

class Link(BaseStyles):
    def __init__(self, active=False):
        self.target = '.st-emotion-cache-1rtdyuf'
        self.icon = Icon(active)
    def set_style(self):
        self.icon.css = self.css
        self.icon.set_style()
        super().set_style()

        

class NavLink(BaseStyles):
    def __init__(self):
        self.target = '[data-testid="stSidebarNavLink"]'
        self.Link = Link
        
        
        
        
    
        
    
     
    
          
        

