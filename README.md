
# Article Classifier and Summarizer

A Streamlit app that classifies articles with URL or Text input into categories (e.g., politics, sports, technology, entertainment) and analyzes their tone (negative, positive, or neutral) using ChatGPT-Turbo API. In addition, the app summarizes the news article into different sections and streams back in real time.

# Web App
Click [Here](https://huggingface.co/spaces/Kaludi/News-Classifier-and-Summarizer_App "Here") To View This App Online!

![image](https://user-images.githubusercontent.com/63890666/227810609-aebd76d7-c36c-442b-9857-56ec47bb169f.png)

## Features

-   Classify articles into categories (politics, sports, technology, entertainment)
-   Analyze the tone of the article (negative, positive, neutral)
-   Summarize news articles into different sections
-   Accepts text input or URL input for article analysis

## Usage
    
1.  Enter your OpenAI API key in the designated text input field.
    
2.  Choose an input option (Text or URL) and paste the article text or URL in the corresponding field.
    
3.  Click on the "Classify and Summarize" button to see the results.

## Installation

1.  Clone the repository

`git clone https://github.com/Kaludii/News-Classifier-and-Summarizer.git` 

2.  Change the working directory

`cd News-Classifier-and-Summarizer` 

3.  Install the required dependencies

`pip install -r requirements.txt` 

4.  Run the Streamlit app

`streamlit run app.py` 

5.  Open your browser and go to the specified address (usually `http://localhost:8501`)
    
## Dependencies

-   [streamlit](https://streamlit.io/)
-   [openai](https://github.com/openai/openai)
-   [requests](https://docs.python-requests.org/)
-   [beautifulsoup4](https://www.crummy.com/software/BeautifulSoup/)
