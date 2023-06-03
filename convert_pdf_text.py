#%%
# import sys, pathlib, fitz
# from glob import glob 
# from tqdm import tqdm 

# filenames = glob("pdf_files/*.pdf")  # get document filename
# for fname in tqdm(filenames):
#     with fitz.open(fname) as doc:  # open document
#         text = chr(12).join([page.get_text() for page in doc])
#     # write as a binary file to support non-ASCII characters
#     print("converted_text/"+ fname[:fname.find('.pdf')] + ".txt")
#     fp = open("converted_text/"+ fname[:fname.find('.pdf')] + ".txt", "x")
#     fp.close()
#     pathlib.Path("converted_text/"+ fname[:fname.find('.pdf')] + ".txt").write_bytes(text.encode())
#%%

import sys, pathlib, fitz, os
from glob import glob 
from tqdm import tqdm 

# Create the 'converted_text' directory if it doesn't exist
if not os.path.exists("converted_text"):
    os.makedirs("converted_text")

filenames = glob("dataset/*.PDF")  # get document filenames
for fname in tqdm(filenames):
    with fitz.open(fname) as doc:  # open document
        text = chr(12).join([page.get_text() for page in doc])
    
    # Create a new .txt file with the corresponding name and write the content of the PDF into it
    txt_filename = "converted_text/" + os.path.basename(fname[:fname.find('.pdf')]) + ".txt"

    with open(txt_filename, "w", encoding="utf-8") as txt_file:
        txt_file.write(text)