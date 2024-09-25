from abc import ABC
import streamlit as st

class CSS:
    def __init__(self, css_dict=None):
        self._dict = css_dict or {}
        self._string = ""
        if(css_dict):
            self._convert()

    def _convert(self):
        self._string = ""
        for prop, value in self._dict.items():
            self._string += f"{prop}: {value};\n"
        

    def props(self, prop, value):
        self._dict[prop] = value
        self._convert()
    
    @property
    def style(self):
        return self._string



class BaseStyles(ABC):
    
    css = CSS()
    target:str = ""
    
    
    def set_style(self):
        html = f"""<style>
        {self.target} {{{self.css.style} }}\n
        </style>
        """     
        st.markdown(html, unsafe_allow_html=True)   
    
    
    

    