import streamlit as st
from encoder_and_decoder import encode_binary,encode_to_hex,encode_Unicode,url_encoder,base64_encode,morse_code_encoder,decode_binary,decode_from_hex,decode_Unicode,url_decoder,base64_decode,morse_code_decoder

def decoder():
    mess = st.text_area('Past the riddle here')
    sele = st.selectbox('Select wich type do you want?',['Binary encoder','Hex encoder','Unicode encoder','Url encoder','Base64 encoder','Morse code encoder','Binary decoder','Hex decoder','Unicode decoder','Url decoder','Base64 decoder','Morse code decoder'])
    if sele == 'Binary encoder':
        if st.button('Encode to binary'):
            st.success(encode_binary(mess))