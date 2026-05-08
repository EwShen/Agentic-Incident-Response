Third-Party Security Incident Coordination
==========================================

Document Metadata
-----------------
- Owner: Vendor Risk Security
- Approver: CISO
- Review cadence: Semiannual

Purpose
-------
This playbook defines how to assess and respond when a vendor, partner,
or managed service provider experiences a security incident that may affect the company.

Trigger Conditions
------------------
- Vendor incident notification
- Threat intelligence linking partner compromise to shared systems
- Suspicious activity on integrations tied to external providers

Initial Assessment
------------------
- Identify all integrations, data exchanges, and trust relationships.
- Determine potentially impacted business services and data classes.
- Validate vendor-provided indicators, timelines, and containment status.

Containment Actions
-------------------
- Disable or restrict high-risk integrations.
- Rotate shared credentials, certificates, and API keys.
- Increase monitoring for vendor-linked identities and traffic paths.
- Enforce temporary segmentation for partner connectivity.

Vendor Engagement Requirements
------------------------------
Request these minimum artifacts from vendor:
- Incident timeline and root cause summary
- Scope of affected systems and data
- Indicators of compromise and mitigations
- Independent validation or attestation, if available

Internal Investigation
----------------------
- Review logs for vendor-origin activity matching IOC set.
- Assess downstream impact to internal and customer systems.
- Confirm whether contractual notification clauses were met.

Legal and Compliance
--------------------
- Engage Legal for contractual and liability review.
- Engage Privacy for potential breach notification obligations.
- Document decision trail for regulator or auditor requests.

Recovery and Exit Criteria
--------------------------
- Re-enable integrations only after control verification.
- Establish conditional monitoring period post-restoration.
- Update vendor risk rating and contract security requirements.

Closure Criteria
----------------
- Potential blast radius fully assessed
- Shared trust paths remediated and validated
- Stakeholder and legal obligations completed
- Vendor corrective actions tracked to completion
