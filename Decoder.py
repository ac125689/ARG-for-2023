import streamlit as st
from encoder_and_decoder import encode_binary,encode_to_hex,encode_Unicode,url_encoder,base64_encode,morse_code_encoder,decode_binary,decode_from_hex,decode_Unicode,url_decoder,base64_decode,morse_code_decoder

def decoder():
    sele = st.text_area('past the code here')
    st.write(sele)