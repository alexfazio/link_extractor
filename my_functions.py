
import os
import requests
import streamlit as st
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def simple_link_extractor(url, extension):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    links = soup.find_all("a", href=True)

    code = ""

    for link in links:
        href = link["href"]
        if href.endswith(extension):
            absolute_url: str = urljoin(url, href)
            code += (absolute_url + "\n")
    st.code(code, language='python')
    # st.write(absolute_url)
    # st.code(absolute_url, language="python", line_numbers=False)


def wget(url, extension):
    """Returns URL as wget UNIX commands, by appending a wget command before each URL."""
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    links = soup.find_all("a", href=True)

    code = ""

    for link in links:
        href = link["href"]
        if href.endswith(extension):
            absolute_url: str = urljoin(url, href)
            code += ("wget" + " " + absolute_url + "\n")
    st.code(code, language='python')
    # st.write(absolute_url)
    # st.code(absolute_url, language="python", line_numbers=False)


def rm(url, extension):
    """Returns URL as wget UNIX commands, by appending a wget command before each URL."""
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    links = soup.find_all("a", href=True)

    code = ""

    for link in links:
        href = link["href"]
        if href.endswith(extension):
            absolute_url = urljoin(url, href)
            # Extract filename from path
            filename = os.path.basename(absolute_url.path)
            # Create UNIX command
            unix_command = f'rm {filename}'
    st.code(code, language='python')
    # st.write(absolute_url)
    # st.code(absolute_url, language="python", line_numbers=False)
