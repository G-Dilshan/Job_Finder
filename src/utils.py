import fitz  # PyMuPDF
from langchain.chains import LLMChain
from .model import llm_define
from apify_client import ApifyClient
import os
from dotenv import load_dotenv

load_dotenv()

llm = llm_define()

# Load Apify api
APIFY_API_TOKEN = os.getenv('APIFY_API_TOKEN')
LINKEDIN_APIFY_ACTOR = os.getenv('LINKEDIN_APIFY_ACTOR')
apify_client = ApifyClient(token=APIFY_API_TOKEN)

# Extract text from PDF
def extract_text_from_pdf(uploaded_file):
    doc = fitz.open(stream=uploaded_file.read(), filetype='pdf')
    text = ''
    for page in doc:
        text += page.get_text()
    return text

# Ask Gemini to generate output
def ask_gemini(prompt, text_input):
    llm_chain = LLMChain(llm=llm, prompt=prompt)
    response = llm_chain.invoke(text_input)
    if isinstance(response, dict) and 'choices' in response:
        return response['choices'][0]['message']['content']
    return response

def fetch_linkedin_jobs(search_query, location="Sri Lanka", rows=50):
    all_jobs = []
    
    # Split the search_query into a list of job titles
    search_query_list = [keyword.strip() for keyword in search_query.split(",")]

    for keyword in search_query_list:
        run_input = {
            "title": keyword,
            "location": location,
            "maxItems": rows,
            "remote": ["1", "2", "3"],
            "contract_type": ["F", "P", "T", "C"],
            "time_interval": "DAY",
            "proxyConfiguration": {
                "useApifyProxy": True,
                "apifyProxyGroups": ["RESIDENTIAL"]
            }
        }

        # Call the LinkedIn API via Apify
        run = apify_client.actor(LINKEDIN_APIFY_ACTOR).call(run_input=run_input)
        jobs = list(apify_client.dataset(run['defaultDatasetId']).iterate_items())
        
        # Add jobs to the overall list
        all_jobs.extend(jobs)
    
    return all_jobs


# def fetch_linkedin_jobs(search_query, location="Sri Lanka", rows=50):
#     run_input = {
#         # "title": search_query,
#         "title": "AI Engineer",
#         "location": location,
#         "maxItems": rows,
#         "remote": ["1", "2", "3"],
#         "contract_type": ["F", "P", "T", "C"],
#         "time_interval": "DAY",
#         "proxyConfiguration": {
#             "useApifyProxy": True,
#             "apifyProxyGroups": ["RESIDENTIAL"]
#         }
#     }

#     run = apify_client.actor(LINKEDIN_APIFY_ACTOR).call(run_input=run_input)
#     jobs = list(apify_client.dataset(run['defaultDatasetId']).iterate_items())
#     return jobs
