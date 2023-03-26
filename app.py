import openai
import streamlit as st
import requests
from bs4 import BeautifulSoup

def extract_article_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    paragraphs = soup.find_all('p')
    article_text = ' '.join([paragraph.text for paragraph in paragraphs])
    return article_text

def classify_and_summarize(api_key, text):
    openai.api_key = api_key
    chat = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an assistant that classifies news articles into categories, such as politics, sports, technology, and entertainment. You also write if the article is negative, positive, or neutral. Lastly, you also summarize the news article all in different sections."},
            {"role": "user", "content": f"Classify the category and tone, and also summarize this article into differen sections: {text}"}
        ],
        stream=True
    )
    
    response_text = st.empty()
    response_line = ""
    
    for chunk in chat:
        chunk_message = chunk['choices'][0]['delta']
        if chunk_message.get('content'):
            response_line += chunk_message['content']
            response_text.write("Response: " + response_line)

st.title("Article Classifier and Summarizer")

st.markdown("""
This application classifies articles into categories such as politics, sports, technology, and entertainment. It also analyzes the tone of the article as negative, positive, or neutral. Lastly, the application summarizes the news article into different sections.

To use the application, simply provide your OpenAI API key, choose an input option (text or URL), and paste the article text or URL. Then, click on the "Classify and Summarize" button to see the results.
""")


api_key = st.text_input("Enter your OpenAI API Key:", type="password")
input_option = st.selectbox("Input Option", ["Text", "URL"])

text = ""

if input_option == "Text":
    text = st.text_area("Paste the news article text here:")
else:
    url = st.text_input("Paste the news article URL here:")
    if url:
        text = extract_article_content(url)
        word_count = len(text.split())
        st.write(f"Article text extracted from the URL ({word_count} Words):")
        with st.container():
            st.markdown('<style>.scrollable {max-height: 200px; overflow-y: auto;}</style>', unsafe_allow_html=True)
            st.markdown(f'<div class="scrollable">{text}</div>', unsafe_allow_html=True)
            st.markdown("")

if st.button("Classify and Summarize"):
    if not api_key:
        st.warning("Please provide your OpenAI API key.")
    elif text:
        classify_and_summarize(api_key, text)
    else:
        st.warning("Please provide the article text or URL.")
