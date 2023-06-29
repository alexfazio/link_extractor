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

from urllib.parse import urljoin

import requests
import streamlit as st
from bs4 import BeautifulSoup

# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="TEST 3", page_icon=":link:")

# LAYING OUT THE TOP SECTION OF THE APP
row1_1, row1_2 = st.columns((2, 3))

with row1_1:
    st.title("🔗 Link Extractor V0.0.2")

# LAYING OUT THE MIDDLE SECTION OF THE APP
col1, col2 = st.columns(2)


# APP
with col1:

    url = st.text_input('URL:', 'https://huggingface.co/TencentARC/T2I-Adapter/tree/main/models')
    extension = st.text_input('Filter by file extension, e.g. .pdf', '.pth')
    extras = st.selectbox(
        "Extras",
        ("", "wget"),
    )

    submit = st.button('Process')

    if submit:

        st.write('URL:', url)
        st.write('Extension:', extension)
        st.write('Extras:', extras)
        st.write('---')

        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")


        links = soup.find_all("a", href=True)

        code = ""

        for link in links:
            href = link["href"]
            if href.endswith(extension):
                absolute_url: str = urljoin(url, href)
                if extras != wget:
                    code += (absolute_url + "\n")
                else:
                    code += ("wget" + " " + absolute_url + "\n")
        st.code(code, language='python')
                #st.write(absolute_url)
                #st.code(absolute_url, language="python", line_numbers=False)
