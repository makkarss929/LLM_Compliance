## LLM Complaince API

## Input Schema for route `/non_compliance` - POST request


```json
{
    "pages": {
        "home_page": "https://www.joinguava.com/",
        "terms_of_use": "https://www.joinguava.com/legal/terms-of-use",
        "cardholder_agreement:": "https://www.joinguava.com/legal/cardholder-agreement",
        "privacy_policy": "https://www.joinguava.com/legal/privacy-policy",
        "disclosures": "https://assets.website-files.com/60870f72a4e980b691d8c688/649d9f720f97b79ca4a89c98_Guave%20E-SIGN%20Disclosures%20(draft)%20(002)-LS-6.22.23%20(LC)-compressed.pdf"
        },
    "compliance_rules" : "https://stripe.com/docs/treasury/marketing-treasury"
}
```
## Output Schema


```json
{
    "home_page": [],
    "terms_of_use": [],
    "cardholder_agreement:": [
        "BusinessCard Purpose. TheCard is to be used for business purpose point-of-sale, debit card and AutomatedTeller Machine (ATM) transactions only. The Card may not be used for personal purposes. You acknowledge and understand that the Card shall not be treated asa consumer card under the provisions of state and federal law.",
        "ProhibitedEntity Type or Account Activity[1] \n\nAny violation of the terms listed inthis agreement, access or use the Services for any illegal purpose or violateany law, statute, ordinance, or regulation; provide false, inaccurate ormisleading information may lead to suspension and/or closure of your Guava Bankaccount and debit card.",
        "AdditionalRisk Associated with Use of Business Purpose Cards. Youwill not have the benefit of any consumer law limiting liability with respectto the unauthorized use of your Card."
    ],
    "privacy_policy": [],
    "disclosures": []
}
```

## Deployment Instructions

1. clone the `repo`.
2. Place `.env` in root of folder.

### Execute API using Docker

```bash
docker build -t llm_compliance_api .
docker run -p 5001:5001 -m 1G llm_compliance_api
```

### Execute API using virtual environments


```bash
cd LLM_Compliance/
python3 -m venv venv
# Linux
source venv/bin/activate
# windows
.\venv\Scripts\activate.bat

pip install --no-cache-dir -r requirements.txt

python app.py
```