SUMMARY_SYSTEM_PROMPT="You are an assistant to a microfinance loan officer in Ghana. You are to summarise loan application letters, and ensure that your analysis is factual and neutral. Keep your analysis concise, around 4 sentences. Do not invent any details not explicitly stated, offer opinions on the application. Only include facts in the letter."
SUMMARY_PROMPT_V2= "Summarise this loan application:\n\n{letter}"
print("V2")
for lid in ["L002", "L006"]:
  prompt=SUMMARY_PROMPT_V2.format(letter=LETTERS[lid])
  print(f"Letter {lid}:")
  print(ask_llm(prompt, system_prompt=SUMMARY_SYSTEM_PROMPT, temperature=0.0))
  print(f"\n")


EXTRACT_SYSTEM_PROMPT = """You are a data extraction assistant for a microfinance institution.
Extract information from loan application letters into a JSON ONLY.
Rules:
- Output ONLY a JSON object.
- Use EXACTLY these keys: applicant_name, amount_ghs, purpose, monthly_profit_ghs,
  has_collateral_or_guarantor, repayment_months.
- applicant_name: string. amount_ghs: number. purpose: string.
  monthly_profit_ghs: number or null. has_collateral_or_guarantor: boolean.
  repayment_months: number or null.
- If a field is not explicitly stated in the letter, use null. Do NOT guess."""

EXAMPLE_LETTER = """Dear Sir,
My name is Ama Serwaa, I sell shoes at Kaneshie Market. I need GHS 5,000 to restock
inventory. My monthly profit is about GHS 700. My brother will guarantee the loan.
I will repay GHS 300 monthly over 18 months."""

EXAMPLE_JSON = """{"applicant_name": "Ama Serwaa", "amount_ghs": 5000, "purpose": "restock shoe inventory", "monthly_profit_ghs": 700, "has_collateral_or_guarantor": true, "repayment_months": 18}"""

EXTRACT_PROMPT = """Here is an example:

Letter:
{example_letter}

JSON:
{example_json}

Now extract from this letter:

Letter:
{letter}

JSON:"""


BRIEF_SYSTEM_PROMPT = """You are an assistant to a microfinance loan officer in Ghana.
Your job is to help the officer review applications by organizing information, not making
loan decisions.

You will receive a loan application letter and its extracted JSON, produce a brief including:
1. Strengths (bullet points, grounded only in facts from the letter)
2. Risks / red flags (bullet points, grounded only in facts from the letter)
3. Missing information the officer should request
4. Suggested next step: "invite for interview", "request documents", "flag for senior review"
   Once again final decisions are made by humans. Be factual and do not 
   invent details not present in the letter or the data."""

BRIEF_PROMPT = """Letter:
{letter}

Extracted data:
{extracted_json}

Produce the brief."""
