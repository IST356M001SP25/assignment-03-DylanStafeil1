import streamlit as st
import packaging
from io import StringIO
import json
import os

'''
In this final program, you will re-write your `process_file.py` 
to keep track of the number of files and total number of lines 
that have been processed.

For each file you read, you only need to output the 
summary information eg. "X packages written to file.json".

Screenshot available as process_files.png
'''
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

if 'file_count' not in st.session_state:
    st.session_state.file_count = 0
if 'line_count' not in st.session_state:
    st.session_state.line_count = 0

if file and btn_process:
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
    st.session_state.file_count += 1
    st.session_state.line_count += length
    st.write(f"Total files processed: {st.session_state.file_count}")
    st.write(f"Total lines processed: {st.session_state.line_count}")
