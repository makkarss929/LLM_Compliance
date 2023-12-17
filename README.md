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
    "compliance_rules" : "'Avoid the terms in this list for any marketing programs you create because only financial institutions licensed as banks can use them.\n\nStripe or [Your Brand] bank\nBank account\nBank balance\nBanking\nBanking account\nBanking product\nBanking platform\nDeposits\nMobile banking\n[Your Brand] pays interest\n[Your Brand] sets interest rates\n[Your Brand] advances funds\nPhrases that suggest your users receive banking products or services directly from bank partners, for example:\nCreate a [Bank Partner] bank account\nA better way to bank with [Bank Partner]\nMobile banking with [Bank Partner]'"
}
```
## Output Schema


```json
{
    "home_page": [
        {
            "non_compliance_rules": []
        }
    ],
    "terms_of_use": [
        {
            "non_compliance_rules": []
        }
    ],
    "cardholder_agreement:": [
        {
            "non_compliance_rules": [
                "Banking services associated with our services are provided by Piermont Bank, Member FDIC(“Bank”).",
                "The Bank will issue or cause to be issued, a Mastercard Debit Card in your name (“Card”).",
                "The Card is to be used for business purpose point-of-sale, debit card and AutomatedTeller Machine (ATM) transactions only.",
                "The Card may not be used for personal purposes.",
                "TheCard services described in this section will be available to you only as long as you continue to use Guava Bank’s services and Guava Bank maintains our banking relationship with Piermont Bank.",
                "The Card allows you to directly access your sub account within the FBO account relationship Guava Bank has with Piermont bank.",
                "You must sign your Card before it may be used.",
                "You agree to require both a Card and a PIN to be used together to obtain cash at designated ATMs.",
                "TheBank policy is to post and pay Card transactions in the order they are received.",
                "Only stop-payment requests from the person who authorized the transaction will be honored.",
                "You may access your account by ATM using your Card and PIN to:",
                "Card holder may use the Card to purchase goods (in person, online, or by phone), pay for services (in person, online, or by phone), get cash from a merchant, if the merchant permits, or from a participating financial institution, and do anything that a participating merchant will accept.",
                "TheBank will not be liable if:",
                "Youwill not have the benefit of any consumer law limiting liability with respectto the unauthorized use of your Card.",
                "Any violation of the terms listed inthis agreement, access or use the Services for any illegal purpose or violateany law, statute, ordinance, or regulation; provide false, inaccurate ormisleading information may lead to suspension and/or closure of your Guava Bankaccount and debit card.",
                "You are liable for Card transactions not authorized if the Bank can provethat the transaction was processed in good faith and in compliance with acommercially reasonable security procedure, unless otherwise required by law.",
                "You agree to examine your receipts and periodic statements using ordinary care and to report any errors or problems to us within a reasonable time.",
                "If you do not report within one year, we will be entitled to treat such information as correct and you will be precluded from asserting otherwise.",
                "If you fail to report to us within 14 days from when the statement was first mailed or made available to you, we will not be required to pay interest on any refund to which you may be entitled.",
                "Call or write us immediately with errors or questions about electronic transfers at the telephone number or address listed below.",
                "If you tell us orally, we may require your complaint or question in writing within 14 business days.",
                "If you provide us with timely notice of an error or problem in your periodic statement, we will investigate the matter and notify you of the results within a reasonable amount of time.",
                "You may ask for copies of the documents that we used in our investigation."
            ]
        }
    ],
    "privacy_policy": [
        {
            "non_compliance_rules": []
        }
    ],
    "disclosures": {
        "non_compliance_rules": []
    }
}
```

## Deployment Instructions

1. clone the `repo`.
2. Place `.env` in root of folder.
3. Run `docker commands`.

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
