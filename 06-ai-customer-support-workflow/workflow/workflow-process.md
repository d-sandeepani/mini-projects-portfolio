# NovaCart — AI-Assisted Customer Support Workflow

## 1. Project Overview

This project demonstrates a simple AI-assisted workflow for handling fictional customer support messages.

The workflow uses AI to classify customer messages and draft responses. A human reviewer checks the results before any response could be used.

NovaCart is a fictional business created for this portfolio project.

## 2. Workflow Steps

### Step 1: Receive Customer Messages

Collect sample customer messages for the demonstration.

The current dataset contains 10 fictional customer messages, identified by unique message IDs.

### Step 2: Classify Messages

Use the classification prompt to assign each message to a category.

The categories used in this project are:

- Order
- Refund
- Delivery
- Product Question
- Complaint

Record the predicted category in the workflow tracker.

### Step 3: Check Classification Results

Compare the AI-predicted category with the expected category assigned to each fictional sample.

Record whether each classification is correct.

Review any incorrect or uncertain predictions rather than assuming the AI is always accurate.

### Step 4: Generate Response Drafts

Use the response-generation prompt to produce a draft response for each message.

The AI should use only the available information, maintain a professional tone, and identify missing information.

### Step 5: Identify Risks

Check for unsupported claims, invented information, privacy concerns, inappropriate promises, and missing details.

Examples include unverified order status, refund eligibility, delivery estimates, and product availability.

### Step 6: Conduct Human Review

A human reviewer checks the classification, response accuracy, tone, privacy, and potential business-policy issues.

The reviewer decides whether a response should be approved, revised, escalated, or left pending.

### Step 7: Record Results

Record classifications, draft responses, identified risks, and review status in the workflow tracker.

Keep review notes in the project documentation.

### Step 8: Document Limitations

Explain that the project uses fictional data and a small sample.

Do not claim that the workflow has been tested on real customers or integrated with a live customer support system.

## 3. Human Review Rules

- Never assume that an AI-generated answer is correct.
- Do not invent order details, refund approvals, tracking information, delivery dates, or product specifications.
- Do not request passwords or full payment card details.
- Do not claim that an action has been completed unless it has been verified.
- Refer account-specific questions to an authorized support channel.
- Do not send AI-generated drafts to real customers without appropriate human review.

## 4. Current Project Status

The project includes a fictional sample dataset, classification prompt, response-generation prompt, human-review checklist, preliminary review notes, and workflow tracker.

The review status must reflect the work actually completed. Any draft that has not been reviewed and verified should remain Pending.

## 5. Limitations

- Only 10 fictional customer messages are included.
- The results do not demonstrate performance on real-world customer data.
- No live customer support platform is connected.
- No real customer messages have been sent.
- No real order, delivery, refund, or customer-account systems have been accessed.
- The workflow does not independently make business decisions.

## 6. Potential Future Improvements

- Test the prompts on a larger and more varied fictional dataset.
- Include ambiguous messages and messages that fit more than one category.
- Record reviewer corrections and explain why changes were made.
- Compare classification results across multiple test runs.
- Improve prompts based on documented findings.
- Add screenshots showing the actual project files and workflow outputs.