# -*- coding: utf-8 -*-
# Copyright 2018-2022 Streamlit Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import streamlit as st
from my_functions import simple_link_extractor
from my_functions import wget
from my_functions import rm
from my_functions import civitai

# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="TEST 3", page_icon=":link:")

# LAYING OUT THE TOP SECTION OF THE APP
row1_1, row1_2 = st.columns((2, 3))

with row1_1:
    st.title("🔗 Link Extractor V0.0.3")

# LAYING OUT THE MIDDLE SECTION OF THE APP
col1, col2 = st.columns(2)


# APP
with col1:

    url = st.text_input('URL:', 'https://huggingface.co/TencentARC/T2I-Adapter/tree/main/models')
    extension = st.text_input('Filter by file extension, e.g. .pdf', '.pth')
    extras = st.selectbox(
        "Extras",
        ("None", "wget", "rm", "civitai"),
    )

    submit = st.button('Process')
    history = []

    if submit:

        st.write('URL:', url)
        st.write('Extension:', extension)
        st.write('Extras:', extras)
        st.write('---')

        history.append(url)

        if extras == "None":
            simple_link_extractor(url, extension)

        if extras == "wget":
            wget(url, extension)

        if extras == "rm":
            rm(url, extension)

        if extras == "civitai":
            civitai(url, extension)

with col2:
    st.table(history)
