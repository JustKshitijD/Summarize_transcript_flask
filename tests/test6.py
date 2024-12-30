import requests
import json
import pdfplumber

def extract_text_from_pdf(pdf_file):
    text = ""
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text

file_path_1 = 'earning_call_dr_lal_pathlabs'
text_dr_lal_pathlabs = extract_text_from_pdf(file_path_1)

# Define the company name and transcript text
company_name = "Dr Lal Pathlabs"
transcript_text = text_dr_lal_pathlabs

# Create the payload
payload = {
    "company_name": company_name,
}

# Define the API endpoint
url = "http://127.0.0.1:5000/earnings_transcript_summary"

# Send the POST request with the JSON payload
response = requests.post(url, json=payload)

# Print the response
if response.status_code == 200:
    print("Response:", response.json())
else:
    print("Error:", response.status_code, response.text)
