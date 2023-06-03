# %%
import pandas as pd 
import numpy as np 
from pathlib import Path
from glob import glob
from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader, download_loader, StorageContext, load_index_from_storage
import os 
from dotenv import load_dotenv
from flask import Flask 
from flask import request
# loading the local environment 
load_dotenv('.env')
# flask application
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World!"


index = None

def initialize_index(): 
    global index
    # indexing the files.
    loader = download_loader("SimpleDirectoryReader")


    # the dataset files
    dataset_a1 = "dataset/summary/A1"
    dataset_a2 = "dataset/summary/A2"
    index_dir = "index"

    # loading the files 
    dataset_a1_files = glob(f"{dataset_a1}/*.txt")
    dataset_a2_files = glob(f"{dataset_a2}/*.txt")

    # combining the data
    comb_data = dataset_a1_files + dataset_a2_files
    # creating the documents
    storage_context = StorageContext.from_defaults()
    # creating indexing from documents
    if os.path.exists(index_dir):
        index = load_index_from_storage(index_dir)
    else: 
        documents = SimpleDirectoryReader(input_files=comb_data).load_data()
        index = GPTVectorStoreIndex.from_documents(documents=documents, openai_api_key=os.environ["OPENAI_API_KEY"],storage_context= storage_context)
        storage_context.persist(index_dir)


from flask import request

@app.route("/query", methods=["GET"])
def query_index():
  global index
  query_text = request.args.get("text", None)
  if query_text is None:
    return "No text found, please include a ?text=blah parameter in the URL", 400
  query_engine = index.as_query_engine()
  response = query_engine.query(query_text)
  return str(response), 200

# # creating the query engine
# query_engine = index.as_query_engine()
# storage_context = StorageContext.from_defaults()

# # getting response for query 

# response = query_engine.query("what is the law case?")
# print(response)

# def get_response(query):
#     # combining the data
#     comb_data = dataset_a1_files + dataset_a2_files

#     # creating the documents
#     documents = SimpleDirectoryReader(input_files=comb_data).load_data()
#     # creating indexing from documents
#     index = GPTVectorStoreIndex.from_documents(documents=documents, openai_api_key=os.environ["OPENAI_API_KEY"])

#     # creating the query engine
#     query_engine = index.as_query_engine()
#     response = query_engine.query(query)
#     return response

if __name__ == "__main__":
    initialize_index()
    app.run(host="0.0.0.0", port=5601)
# %%



