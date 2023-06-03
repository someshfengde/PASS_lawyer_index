# %%
import pandas as pd 
import numpy as np 
from pathlib import Path
from glob import glob
from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader, download_loader
import os 
# downloading the loader
loader = download_loader("SimpleDirectoryReader")

# the dataset files
dataset_a1 = "dataset/summary/A1"
dataset_a2 = "dataset/summary/A2"

# loading the files 
dataset_a1_files = glob(f"{dataset_a1}/*.txt")
dataset_a2_files = glob(f"{dataset_a2}/*.txt")

# combining the data
comb_data = dataset_a1_files + dataset_a2_files

# creating the documents
documents = SimpleDirectoryReader(input_files=comb_data).load_data()
# creating indexing from documents
index = GPTVectorStoreIndex.from_documents(documents=documents, openai_api_key=os.environ["OPENAI_API_KEY"])

# creating the query engine
query_engine = index.as_query_engine()


# getting response for query 

response = query_engine.query("what is the law case?")
print(response)

def get_response(query):
    # combining the data
    comb_data = dataset_a1_files + dataset_a2_files

    # creating the documents
    documents = SimpleDirectoryReader(input_files=comb_data).load_data()
    # creating indexing from documents
    index = GPTVectorStoreIndex.from_documents(documents=documents, openai_api_key=os.environ["OPENAI_API_KEY"])

    # creating the query engine
    query_engine = index.as_query_engine()
    response = query_engine.query(query)
    return response


# %%



