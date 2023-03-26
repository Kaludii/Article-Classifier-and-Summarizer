
# Article Classifier and Summarizer

This repository contains a Streamlit app that classifies news articles into categories (e.g., politics, sports, technology, entertainment) and analyzes their tone (negative, positive, or neutral). In addition, the app summarizes the news article into different sections.

# Web App
Click [Here](https://huggingface.co/spaces/Kaludi/News-Classifier-and-Summarizer_App "Here") To View This App Online!


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