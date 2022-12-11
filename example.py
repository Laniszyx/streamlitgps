import streamlit as st
from streamlit_js_eval import get_geolocation,streamlit_js_eval,copy_to_clipboard,create_share_link
import pandas as pd
import time 

import json

st.write(f"User agent is _{streamlit_js_eval(js_expressions='window.navigator.userAgent', want_output = True, key = 'UA')}_")

st.write(f"Screen width is _{streamlit_js_eval(js_expressions='screen.width', want_output = True, key = 'SCR')}_")

st.write(f"Browser language is _{streamlit_js_eval(js_expressions='window.navigator.language', want_output = True, key = 'LANG')}_")

st.write(f"Page location is _{ streamlit_js_eval(js_expressions='window.location.origin', want_output = True, key = 'LOC')}_")

# Copying to clipboard only works with a HTTP connection

copy_to_clipboard("Text to be copied!", "Copy something to clipboard (only on HTTPS)", "Successfully copied" , component_key = "CLPBRD")

# Share something using the sharing API
create_share_link(dict({'title': 'streamlit-js-eval', 'url': 'https://github.com/aghasemi/streamlit_js_eval', 'text': "A description"}), "Share a URL (only on mobile devices)", 'Successfully shared', component_key = 'shdemo')
                
tlat = 0
tlong = 0

if st.checkbox("Check my location"):
    f = 1
    
while f == 1:
    loc = get_geolocation()
    st.write(f"Your coordinates are {loc}")
    st.write(loc)
    st.write(loc['coords']['latitude'])
    st.write(loc['coords']['longitude'])
    
    lat = loc['coords']['latitude']
    long = loc['coords']['longitude']
    
    df = pd.DataFrame([[lat,long]]
        ,columns=['lat', 'lon'])
    
    st.map(df)
    time.sleep(5)
