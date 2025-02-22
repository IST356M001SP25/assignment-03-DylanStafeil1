
'''
Write a streamlit to input one string of package data. 
It should use the `packaging.py` module to parse the string 
and output the package info as it appears. 
Calculate the total package size and display that.

see one_package.png for a screenshot
'''
import streamlit as st
from packaging import parse_packaging, calc_total_units

st.title('Process One Package')
st.write('Enter package data and click the button to process it')
package_data = st.text_input('Enter package data')
btn_process = st.button('Process Package')

if btn_process:
    package_info = parse_packaging(package_data)
    total_size = calc_total_units(package_info)
    
    st.write('Package Info:')
    st.write(package_info)
    st.write(f'Total Package Size: {total_size}')