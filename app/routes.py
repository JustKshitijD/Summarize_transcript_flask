from flask import Flask, request, jsonify
from .utils import summarize_text

app = Flask(__name__)

@app.route("/")
def home():
    return {"message": "Welcome to the Flask API running on Colab!"}

@app.route("/earnings_transcript_summary", methods=["POST"])
def summarize():
    data = request.get_json()

    # Check for missing fields
    if "transcript_text" not in data:       
      return jsonify({"error": "No transcript_text content provided"}), 400
    if "company_name" not in data:
      return jsonify({"error": "No company_name provided"}), 400

    content = data.get("transcript_text", "")
    company_name=data.get("company_name", "")

    # Check for empty data
    if not content:
        return jsonify({"error": "No transcript_text content provided"}), 400
    if not company_name:
        return jsonify({"error": "No company_name provided"}), 400

    summary_financial_performance = summarize_text(content,"financial performance",company_name)
    summary_market_dynamics = summarize_text(content,"market dynamics",company_name)
    summary_expansion_plans = summarize_text(content,"expansion plans",company_name)
    summary_environmental_risks = summarize_text(content,"environmental_risks",company_name)
    summary_regulatory_or_policy_changes = summarize_text(content,"regulatory or policy changes",company_name)

    return jsonify({"company_name": company_name, "financial_performance": summary_financial_performance, "market_dynamics": summary_market_dynamics, "expansion_plans": summary_expansion_plans, "environmental_risks": summary_environmental_risks, "regulatory_or_policy_changes": summary_regulatory_or_policy_changes})
