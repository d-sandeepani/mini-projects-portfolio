# NovaCart — Findings and Limitations Report

## 1. Project Overview

This report summarizes the findings from a small AI-assisted customer support workflow demonstration using fictional NovaCart customer messages.

The dataset contains 10 fictional messages across five categories: Order, Refund, Delivery, Product Question, and Complaint.

## 2. Classification Findings

The AI classified all 10 sample messages into the expected categories.

- Total messages tested: 10
- Correct classifications observed: 10
- Incorrect classifications observed: 0
- Observed classification accuracy: 100%

Calculation:

Accuracy = (Correct classifications / Total messages) × 100

Accuracy = (10 / 10) × 100 = 100%

This result applies only to this small fictional dataset and does not establish expected accuracy on real customer messages.

## 3. Response-Drafting Findings

The AI generated draft responses for all 10 messages.

The drafts generally:
- Used polite and professional language.
- Acknowledged customer concerns.
- Identified missing information.
- Avoided promising refunds or compensation.
- Directed account-specific checks to an authorized support channel.

These observations describe the draft wording. They do not prove that every response is suitable for real-world use.

## 4. Risks Identified

Potential risks in AI-assisted customer support include:

- Incorrect classification of ambiguous messages.
- Unsupported claims about order status or delivery dates.
- Incorrect statements about refund eligibility.
- Invented product availability or material specifications.
- Requests for unnecessary sensitive information.
- Responses that sound polite but do not resolve the customer's issue.
- Overreliance on AI-generated content without human review.

## 5. Human Review

A human reviewer should verify each draft for factual accuracy, privacy, tone, missing information, and compliance with applicable business policies.

A draft should remain Pending until the reviewer has actually checked it and recorded a decision.

## 6. Limitations

- Only 10 fictional messages were tested.
- The dataset contains two messages per category.
- The examples do not represent the full variety of real customer requests.
- The results have not been validated using real customer support data.
- No live customer support platform or business database was connected.
- No actual customer responses were sent.
- The project does not measure time saved or financial benefits.

## 7. Recommendations

1. Test a larger and more diverse fictional dataset.
2. Include ambiguous messages and messages containing multiple concerns.
3. Record and investigate incorrect classifications.
4. Compare outputs from repeated AI runs.
5. Have a human reviewer assess all generated drafts.
6. Update prompts when documented issues are found.
7. Keep customer information private when applying these methods in real settings.

## 8. Conclusion

This demonstration shows a possible workflow for using AI to support message classification and response drafting while retaining human oversight.

The initial results are promising for the limited examples tested, but further evaluation is necessary before considering real-world use.

## 9. Project Disclaimer

NovaCart is fictional, and all customer messages are sample data created for this portfolio project. Findings are limited to the demonstrated examples.
