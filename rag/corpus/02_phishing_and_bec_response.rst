Phishing and Business Email Compromise Response
================================================

Document Metadata
-----------------
- Owner: Messaging Security Team
- Approver: SOC Manager
- Review cadence: Quarterly

Purpose
-------
This playbook defines end-to-end response actions for phishing and business email compromise (BEC)
incidents affecting employee mailboxes and collaboration channels.

Threat Overview
---------------
Common attack patterns include:
- Credential harvesting pages masquerading as SSO portals
- Malware-laced attachments using macro or archive obfuscation
- Executive impersonation and invoice/payment fraud
- OAuth consent phishing for mailbox API access

Entry Criteria
--------------
Trigger this playbook when one or more conditions are present:
- User-reported suspicious email with malicious indicators
- Secure email gateway high-confidence phishing verdict
- Unusual mailbox forwarding/OAuth grant changes
- Confirmed sign-in anomalies tied to phishing lure activity

Initial Validation Steps
------------------------
- Confirm sender authenticity, return path, and lookalike domains.
- Extract and detonate attachments and URLs in sandbox tooling.
- Validate domain age, WHOIS patterns, and infrastructure reputation.
- Correlate email telemetry by message ID, sender, and campaign subject.

Containment Actions
-------------------
- Quarantine malicious messages tenant-wide.
- Block sender domains, URLs, and attachment hashes.
- Disable or reset compromised user credentials.
- Revoke active sessions and refresh MFA claims.
- Remove unauthorized mailbox rules and OAuth grants.

Investigation Workflow
----------------------
1. Identify patient zero and campaign spread.
2. Determine whether credentials were submitted.
3. Confirm adversary access to mailbox or shared resources.
4. Review message search results for internal lateral phishing.
5. Assess financial fraud attempts and business process abuse.

Evidence to Collect
-------------------
- Full message headers and raw MIME content
- URL redirect chain and final landing content
- Authentication events before and after lure interaction
- Mailbox audit logs for rule, delegate, and send-as changes
- Payment workflow communications if fraud attempt exists

Decision Matrix
---------------
- If credentials submitted but no access observed:
  - Force password reset and enforce phishing-resistant MFA
  - Monitor account and related identities for 7 days
- If mailbox compromise confirmed:
  - Escalate severity, isolate identity, and perform full mailbox review
- If payment redirection requested:
  - Engage Finance and Legal immediately; preserve all communications

Recovery Actions
----------------
- Restore mailbox configuration to approved baseline.
- Re-enable account access after identity hardening checks.
- Notify impacted users with targeted guidance and verification steps.
- Add campaign indicators to blocklists and detection rules.

Communication Requirements
--------------------------
- SOC update to stakeholders within 60 minutes for Severity 2+
- Daily campaign status summary while active
- Final closure memo including affected users and controls improved

Closure Criteria
----------------
- Malicious messages contained across tenant
- All impacted identities remediated
- No active adversary session remains
- Lessons learned and detection improvements documented
