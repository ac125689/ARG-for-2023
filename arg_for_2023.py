import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_extras.add_vertical_space import add_vertical_space
from stories import Stories
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
        st.title("ARG for West Windsor-Plainsboro High School South")
        add_vertical_space()
        st.write("Introducing an exciting game that combines storytelling and puzzles, creating an immersive and engaging experience. Throughout the game, players will encounter captivating narratives interspersed with challenging puzzles. Whenever a story reaches a break, intriguing puzzles will be revealed, adding an extra layer of excitement and mystery.")
        add_vertical_space()
        st.write("Be prepared to encounter a mixture of letters and numbers, which may initially seem like a jumble. However, fear not! Utilize the decoder available in the game to decipher these codes and unlock their hidden messages. Each code cracked will provide valuable clues to progress further in the game.")
        add_vertical_space()
        st.write("It's important to note that this game comprises a total of 10 different stories, each with its own unique tale to unravel. To explore all the stories, players must solve numerous puzzles, testing their wit and problem-solving abilities to the fullest.")
        add_vertical_space()
        st.write("But there's more! This game isn't just about puzzles and storytelling; it also incorporates an intriguing scavenger hunt within a school setting. Players will embark on a thrilling quest, searching for clues and hidden items throughout the school to progress in their journey.")
        add_vertical_space()
        st.write("Get ready for an immersive adventure where your skills will be put to the test. Unlock the secrets within each story, solve the puzzles, and embark on an unforgettable scavenger hunt in the school. Are you up for the challenge?")
    if "Stories" == selected:
        Storiesx




if __name__ == "__main__":
    dissclamer()

