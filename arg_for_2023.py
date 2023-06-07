import streamlit as st
from streamlit_option_menu import option_menu
from stories import Stories
from home import home
def dissclamer():
    place = st.empty()
    e = place.text_input('Disclamer This content is only for students who are in West Windsor-Plainsboro High School South write your school email address everything after @ symbol')
    if e == 'wwprsd.org':
        main()
        place.empty()

def config():
    st.set_page_config(
    page_title='Shutter Moments',
    page_icon= '😴',
    layout="wide")   
def hide_st():
    hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
    st.markdown(hide_st_style, unsafe_allow_html=True)
back = """
<style>
[class="main css-uf99v8 egzxvld5"] {
background-image: url("https://www.toptal.com/designers/subtlepatterns/uploads/double-bubble-outline.png");
background-repeat: repeat;
background-attachment: fixed;
}
"""
config()
hide_st()
def main():
    st.cache()
    st.markdown(back,True)
    selected = option_menu(
            menu_title=None,
            options=['Home','Stories','Decoder','Admin Login'],
            icons=['house-door-fill','card-checklist','person-fill'],
            menu_icon='cast',
            default_index=0,
            orientation="horizontal",
            styles= {"nav-link": {"font-size": "18px", "text-align": "center", "margin":"0px", "--hover-color": "#64A3E8"}}
    )
    if "Home" == selected:
        home()
    if "Stories" == selected:
        Stories()




if __name__ == "__main__":
    dissclamer()
