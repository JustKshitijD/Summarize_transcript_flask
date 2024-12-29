import google.generativeai as genai
import os

# Function to get a summary 
def summarize_text(text, section, company):
    os.environ["API_KEY"]="AIzaSyC8NkRrznR8GKQuM2CPGn6MC4xP0mk-Na4"
    if "API_KEY" not in os.environ:
        raise ValueError("API_KEY environment variable is not set.")
    # Set the environment variable
    genai.configure(api_key=os.environ["API_KEY"])

    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content([f"Please summarize the {section} from {company} company's earning transcript:\n\n{text}"])    # We said 'Please summarize the following text', so it will summarize
    return response.text
