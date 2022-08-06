import streamlit as st

st.title('🎈 Different ways to display images')

##### st.image
st.header('1. Using `st.image`')

from PIL import Image
img = Image.open('streamlit-logo-secondary-colormark-darktext.png')
st.image(img)

st.code('''from PIL import Image
  img = Image.open('streamlit-logo-secondary-colormark-darktext.png')
  st.image(img)
''')


##### st.markdown
st.header('2. Using `st.markdown`')

# Source: https://pmbaumgartner.github.io/streamlitopedia/sizing-and-images.html
import base64
from pathlib import Path

def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded
def img_to_html(img_path):
    img_html = "<img src='data:image/png;base64,{}' class='img-fluid'>".format(
      img_to_bytes(img_path)
    )
    return img_html

st.markdown(img_to_html('streamlit-logo-secondary-colormark-darktext.png'), unsafe_allow_html=True)

