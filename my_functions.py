
import os
import sys
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
            filename = os.path.basename(absolute_url)
            # Create UNIX command
            unix_command = f'rm {filename}'
            code += unix_command + '\n'

    st.code(code, language='python')
    # st.write(absolute_url)
    # st.code(absolute_url, language="python", line_numbers=False)

import os
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup

def civitai (url, extension):
    """Returns URL as wget UNIX commands, by appending a wget command before each URL."""
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    links = soup.find_all("a", href=True)

    code = ""

    for link in links:
        href = link["href"]
        if href.startswith('https://civitai.com/api/download/models/'):
            # Split the URL into parts
            url_parts = href.split('/')
            # Extract the model ID from the URL
            model_id = url_parts[url_parts.index('models') + 1]
            # Construct the new URL
            new_url = "https://civitai.com/api/download/models/" + model_id
            # Construct the wget command
            unix_command = "wget " + new_url + " --content-disposition"
            code += unix_command + '\n'
        elif href.endswith(extension):
            absolute_url = urljoin(url, href)
            # Extract filename from path
            filename = os.path.basename(absolute_url)
            # Create UNIX command
            unix_command = f'wget {filename}'
            code += unix_command + '\n'

    st.code(code, language='python')

