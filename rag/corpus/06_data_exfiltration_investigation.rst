Data Exfiltration Investigation
==============================

Document Metadata
-----------------
- Owner: Threat Detection and Response
- Approver: CISO
- Review cadence: Semiannual

Purpose
-------
This playbook establishes procedures for investigating and containing suspected
unauthorized data transfer from company environments.

Trigger Examples
----------------
- Large outbound transfers to unsanctioned destinations
- Atypical download volume from sensitive repositories
- Encrypted archive creation followed by external upload
- Unexpected use of data transfer utilities or cloud sync tools

Priority Assessment
-------------------
Prioritize based on:
- Data classification involved
- Transfer size and duration
- Identity privilege level
- Destination trust profile and jurisdiction

Investigation Steps
-------------------
1. Identify source system, identity, destination, and transfer method.
2. Validate whether movement matches approved business activity.
3. Determine exact data set scope and record sensitivity tier.
4. Correlate endpoint, proxy, CASB, and cloud audit logs.
5. Assess whether transfer is ongoing and whether additional channels exist.

Containment Actions
-------------------
- Block destination channels and suspend impacted identities.
- Restrict repository permissions to minimum required users.
- Disable risky transfer tools pending policy review.
- Preserve logs and endpoint artifacts for legal hold.

Legal and Privacy Coordination
------------------------------
Engage Legal and Privacy Office immediately when:
- Regulated data types are involved
- Cross-border transfer obligations may apply
- Breach notification thresholds may be met

Evidence Package
----------------
- Data inventory and classification mapping
- Timeline of transfer events
- Identity activity and access history
- Destination attribution and risk assessment
- Containment action log with timestamps

Remediation and Prevention
--------------------------
- Tighten DLP policies and anomaly thresholds.
- Enforce just-in-time access for sensitive repositories.
- Add or tune detections for archive-and-upload behavior.

Closure Criteria
----------------
- Unauthorized transfer path closed
- Scope and impact documented
- Required notifications completed
- Control improvements assigned with owners and due dates
