import streamlit as st
from scrape import scrape_website, split_dom_content, clean_body_content, extract_body_content
from parse import parse_with_ollama

st.title("AI Web Scripting")
url = st.text_input("Enter a website URL: ")

if st.button("Scrape Site"): # if the button is clicked then...
    st.write("Scrapting the website...")
    result = scrape_website(url)

    print(result)
    body_content = extract_body_content(result)
    cleaned_content = clean_body_content(body_content)

    st.session_state.dom_content = cleaned_content

    with st.expander("View DOM Content"): #kind of toggle button
        st.text_area("DOM Content", cleaned_content, height=300) # View a little bit of content depends on height provided

#Ai Section...
 
if "dom_content" in st.session_state:
    parse_description = st.text_area("What do you want to parse?")

    if st.button("Parse Content"):
        if parse_description:
            st.write("Parsing the content")

            dom_chunks = split_dom_content(st.session_state.dom_content)
            result = parse_with_ollama(dom_chunks, parse_description)
            st.write("AI Result: ")
            st.write(result)