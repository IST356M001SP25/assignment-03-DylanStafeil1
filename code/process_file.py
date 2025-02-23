'''
Next, write a streamlit to read ONE file of packaging information. 
You should output the parsed package and total package size for each package in the file.

Screenshot available as process_file.png
'''

import streamlit as st
import packaging
from io import StringIO
import json

def process_file(text):
    packages = []
    for line in text.split("\n"):
        line = line.strip()
        pkg = packaging.parse_packaging(line)
        total = packaging.calc_total_units(pkg)
        unit = packaging.get_unit(pkg)
        packages.append(pkg)
        st.info(f"{line} ➡️ Total 🟰 Size: {total} {unit}")
    return packages

st.title("Process File")
st.write("Upload a file with package data and click the button to process it")
file = st.file_uploader("Upload file", type=["txt"])
btn_process = st.button("Process File")

if file:
    json_filename = file.name.replace(".txt", ".json")
    file_contents = file.getvalue().decode("utf-8")
    packages = file_contents.split('\n')
    package = []
    text = StringIO(file.getvalue().decode("utf-8")).read()
    process_file(text)
    length = len(packages)
    with open(f"./data/{json_filename}", "w") as f:
        json.dump(packages, f, indent=4)
    st.success(f"{length} packages written to {json_filename}", icon="💾")