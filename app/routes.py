from flask import Flask, request, jsonify
from .utils import summarize_text

app = Flask(__name__)

@app.route("/")
def home():
    return {"message": "Welcome to the Flask API running on Colab!"}

@app.route("/earnings_transcript_summary", methods=["POST"])
def summarize():
    data = request.get_json()
    # print("data: ",data)
    content = data.get("transcript_text", "")
    # print("content: ",content)
    company_name=data.get("company_name", "")
    # print("company_name: ",company_name)
    if not content:
        return jsonify({"error": "No content provided"}), 400

    summary_financial_performance = summarize_text(content,"financial performance",company_name)
    print("summary_financial_performance: ",summary_financial_performance)
    print("#################################################")
    summary_market_dynamics = summarize_text(content,"market dynamics",company_name)
    print("summary_market_dynamics: ",summary_market_dynamics)
    print("#################################################")
    summary_expansion_plans = summarize_text(content,"expansion plans",company_name)
    print("summary_expansion_plans: ",summary_expansion_plans)
    print("#################################################")
    summary_environmental_risks = summarize_text(content,"environmental_risks",company_name)
    print("summary_environmental_risks: ",summary_environmental_risks)
    print("#################################################")
    summary_regulatory_or_policy_changes = summarize_text(content,"regulatory or policy changes",company_name)
    print("summary_regulatory_or_policy_changes: ",summary_regulatory_or_policy_changes)
    print("#################################################")
    
    return jsonify({"company_name": company_name, "financial_performance": summary_financial_performance, "market_dynamics": summary_market_dynamics, "expansion_plans": summary_expansion_plans, "environmental_risks": summary_environmental_risks, "regulatory_or_policy_changes": summary_regulatory_or_policy_changes})
