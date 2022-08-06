import streamlit as st

st.title('🎈 Different ways to display images')

st.header('1. Using `st.image`')

from PIL import Image
img = Image.open('streamlit-logo-secondary-colormark-darktext.png')
st.image(img)

st.code('''from PIL import Image
  img = Image.open('streamlit-logo-secondary-colormark-darktext.png')
  st.image(img)
''')

st.header('2. Using `st.markdown`')

st.markdown('<img src="streamlit-logo-secondary-colormark-darktext.png">', unsafe_allow_html=True)

st.code('''st.markdown('<img src="streamlit-logo-secondary-colormark-darktext.png">', unsafe_allow_html=True)
''')
