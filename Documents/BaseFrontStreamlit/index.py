import streamlit as st
from styles import SideBar, LoginForm, Body
from styles.BaseStyles import CSS
from controllers.Auth import Session


session = Session()


pages = []   

view = LoginForm.AppView()
submit = LoginForm.SubmitButton()
container = LoginForm.Box()
container_ext = LoginForm.Box2()

container.css = CSS({'max-width':'300px !important'})
container.set_style()
container_ext.css = CSS({'display':'flex','align-items':'center'})
container_ext.set_style()



login = st.Page("./pages/page_login.py", default=True)
pg = st.navigation([login],position='hidden')
submit.container.css = CSS({'display':'flex !important', 'justify-content':'center !important'}) 
submit.css = CSS({'background':'#4a1ca6 !important', 'color':'#fff !important', 'border-color':'#fff !important'})
submit.set_style()
submit.target += ':hover'
submit.css = CSS({'background':'#694ea0 !important', 'color':'#fff !important', 'border-color':'#fff !important'})
submit.set_style()

pg.run()


