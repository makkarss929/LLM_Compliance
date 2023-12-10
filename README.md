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
    "cardholder_agreement:": [],
    "privacy_policy": [],
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