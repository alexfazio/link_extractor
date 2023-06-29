
import requests
import streamlit as st
from bs4 import BeautifulSoup


def simple_link_extractor(url, extension, extras):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    links = soup.find_all("a", href=True)

    code = ""

    for link in links:
        href = link["href"]
        if href.endswith(extension):
            absolute_url: str = urljoin(url, href)
            if extras == "wget":
                code += ("wget" + " " + absolute_url + "\n")
            else:
                code += (absolute_url + "\n")
    st.code(code, language='python')
    # st.write(absolute_url)
    # st.code(absolute_url, language="python", line_numbers=False)
