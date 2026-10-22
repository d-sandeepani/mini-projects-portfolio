# Bloom Café — Website Testing Report

## 1. Project Information

- **Project:** Bloom Café — Responsive WordPress Business Website
- **Website:** https://bloomcafesite.wordpress.com/
- **Platform:** WordPress.com
- **Theme:** Twenty Twenty-Five
- **Tester:** [Dilki]
- **Test date:** [2026.10.12]

## 2. Testing Objective

To check whether the published website pages, main navigation, responsive layouts, and contact form behave as expected.

## 3. Test Environment

- Desktop browser: [Version 155.0.8059.85 ]
- Mobile testing method: [Dimensions 375 x 667]
- Tablet testing method: [Dimensions 768 x 1024]

## 4. Test Results

| ID | Test case | Expected result | Reported result | Status |
|---|---|---|---|---|
| TC-01 | Open Home page | Home page loads | Page opened | PASS |
| TC-02 | Open About page | About page loads | Page opened | PASS |
| TC-03 | Open Contact page | Contact page loads | Page opened | PASS |
| TC-04 | Test main navigation | Links open the correct pages | Links worked | PASS |
| TC-05 | Check desktop layout | Content displays correctly | Desktop view checked | PASS |
| TC-06 | Check tablet layout | Content displays correctly | Tablet view checked | PASS |
| TC-07 | Check mobile layout | Content displays correctly | Mobile view checked | PASS |
| TC-08 | Submit contact form | Submission receives a response | Test submission completed | PASS |
| TC-09 | Check feedback handling | Submission is available in the normal Feedback list | Test submission restored from Spam | PASS |
| TC-10 | Review image alternative text | Meaningful images have appropriate alternative text | Reviewed | CHECKED |
| TC-11 | Review heading structure | Main and section headings follow a clear hierarchy | Home page H1 and H2 headings reviewed | CHECKED |
| TC-12 | Verify contact email notification | Notification email is delivered | Not confirmed | NOT VERIFIED |
| TC-13 | Verify SEO title and meta description | Available SEO fields are configured appropriately | Fields not found in current interface | NOT VERIFIED |
| TC-14 | Verify search engine visibility setting | Setting can be checked and documented | Setting not found in current interface | NOT VERIFIED |

## 5. Issues and Limitations

- Contact form email notification delivery has not been verified.
- SEO title and meta description settings have not been verified.
- Search engine visibility settings have not been verified.
- Test results reflect the checks reported during development and should be repeated after significant changes.

## 6. Evidence

Screenshots are stored in the repository's `screenshots/` folder:

- `home-desktop.png`
- `home-mobile.png`
- `about.png`
- `contact.png`

## 7. Summary

The main pages, navigation, desktop/tablet/mobile layouts, and contact form were reported as tested successfully. Some SEO settings and email notification delivery remain unverified.

**Report status:** Initial testing report — update when additional verification is completed.
