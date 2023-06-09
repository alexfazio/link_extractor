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

"""An example of showing geographic data."""

import os

import altair as alt
import numpy as np
import pandas as pd
import pydeck as pdk
import streamlit as st
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="TEST 3", page_icon=":taxi:")

# LAYING OUT THE TOP SECTION OF THE APP
row1_1, row1_2 = st.columns((2, 3))

with row1_1:
    st.title("Link Extractor V0")

# APP
name = st.text_input('Enter your name:', 'John Doe')
st.write('Your name is', name)

url = "https://huggingface.co/TencentARC/T2I-Adapter/tree/main/models"  # Replace with the target webpage URL
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

links = soup.find_all("a", href=True)

for link in links:
    href = link["href"]
    if href.endswith(".pth"):
        absolute_url = urljoin(url, href)
        print(absolute_url)

