from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request
import tempfile
import uuid
import os
import requests
from pdfminer.high_level import extract_text
import openai
import os
import json
import time

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

openai.api_key  = os.getenv('OPENAI_API_KEY')

def get_completion_from_messages(messages, 
                                 model="gpt-3.5-turbo", 
                                 temperature=0, 
                                 ):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature
        )
    return response.choices[0].message["content"]


class WebScraper:

    def __init__(self):
        self.temp_dir = tempfile.tempdir

    def page(self, url):
        html = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(html, 'html.parser')
        text = "\n".join([s.text for s in soup.findAll("p")])
        return text
    
    def pdf(self, url):

        r = requests.get(self, url, stream=True)
        random_ = str(uuid.uuid4())

        path = os.path.join(self.temp_dir.name, f"{random_}.pdf")
        chunk_size = 2000
        with open(path, 'wb') as fd:
            for chunk in r.iter_content(chunk_size):
                fd.write(chunk)


        text = extract_text(path)
        text = "\n".join(text.split())

        return text
    

class LLMCompliance:

    def __init__(self) -> None:
        pass
    

    def non_complaince(self, key, text, compliance_rules):
        delimiter = "####"
        system_message = f"""
        You will be provided with customer service queries. \
        The customer service query will be delimited with \
        {delimiter} characters.
        Output a python list of objects, where each object has \
        the following format:

            'non_compliance_rules': <a list of non-compliance rules>

        COMPLIANCE RULES:
        {compliance_rules}
        """

        user_message_1 = f"""Match {key} agreement against compliance rules and return list of non-compliance rules. If you don't find match between {key} agreement and compliance rules, just return empty list, don't try to make up an answer. Don't make up new terms which are not available in the context.
        {key} agreement: ```{text}```
        """
        messages =  [  
        {'role':'system', 
        'content': system_message},    
        {'role':'user', 
        'content': f"{delimiter}{user_message_1}{delimiter}"},  
        ] 
        response = get_completion_from_messages(messages)
        return eval(response)['non_compliance_rules']
    
    
    def pipeline(self, pages, compliance_rules):

        context = dict()

        for key, url in pages.items():
            try:
                if url.endswith(".pdf"):
                    text = WebScraper().pdf(url)
                else:
                    text = WebScraper().page(url)
            except:
                text = ''
            context[key] = text

        results = dict()
        for key, text in context.items():
            results[key] = self.non_complaince(key, text, compliance_rules)
            time.sleep(20) # Adding sleep to avoid rate limting issues (3 requests per min)

        return results

