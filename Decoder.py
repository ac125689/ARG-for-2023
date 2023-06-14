import streamlit as st
from encoder_and_decoder import encode_binary,encode_to_hex,encode_Unicode,url_encoder,base64_encode,morse_code_encoder,decode_binary,decode_from_hex,decode_Unicode,url_decoder,base64_decode,morse_code_decoder

def decoder():
    mess = st.text_area('Past the code here')
    sele = st.selectbox('Select wich type do you want?',['Binary encoder','Hex encoder','Unicode encoder','Url encoder','Base64 encoder','Morse code encoder','Binary decoder','Hex decoder','Unicode decoder','Url decoder','Base64 decoder','Morse code decoder'])
    if sele == 'Binary encoder':
        if st.button('Encode to binary'):
            st.success(encode_binary(mess))
    if sele == 'Hex encoder':
        if st.button('Encode to hex'):
            st.success(encode_to_hex(mess))
    if sele == 'Unicode encoder':
        if st.button('Encode to unicode'):
            st.success(encode_Unicode(mess))
    if sele == 'Url encoder':
        if st.button('Encode to url'):
            st.success(url_encoder(mess))
    if sele == 'Base64 encoder':
        if st.button('Encode to base64'):
            st.success(base64_encode(mess))
    if sele == 'Morse code encoder':
        if st.button('Encode to morse code'):
            st.success(morse_code_encoder(mess))
    if sele == 'Binary decoder':
        if st.button('decoder to binary'):
            st.success(decode_binary(mess))
    if sele == 'Hex decoder':
        if st.button('decoder to hex'):
            st.success(decode_from_hex(mess))
    if sele == 'Unicode decoder':
        if st.button('decoder to unicode'):
            st.success(decode_Unicode(mess))
    if sele == 'Url decoder':
        if st.button('decoder to url'):
            st.success(url_decoder(mess))
    if sele == 'Base64 decoder':
        if st.button('decoder to base64'):
            st.success(base64_decode(mess))
    if sele == 'Morse code decoder':
        if st.button('decoder to morse code'):
            st.success(morse_code_decoder(mess))