Incident Classification and Severity Matrix
==========================================

Document Metadata
-----------------
- Owner: Security Operations
- Approver: CISO
- Review cadence: Quarterly or after Severity 1 incident
- Applies to: All corporate and production environments

Purpose
-------
This document defines how Northstar Biolabs classifies security incidents, assigns severity,
and drives consistent escalation and resource allocation.

Scope
-----
This policy applies to:
- Workforce identities and endpoints
- On-premise and cloud infrastructure
- SaaS platforms and collaboration systems
- Customer-facing and internal business services

Out of Scope
------------
- Pure availability issues with no security signal (handled by service reliability process)
- HR-only policy violations with no security system impact

Classification Categories
-------------------------
- Credential compromise
- Malware infection
- Data exposure
- Unauthorized access
- Business email compromise
- Denial of service
- Insider misuse
- Third-party vendor compromise

Severity Model
--------------
Severity is determined using impact, confidence, and spread potential.

- Severity 1 (Critical)
  - Confirmed active compromise with material business risk
  - Regulated data confirmed exposed or encrypted
  - Enterprise service disruption with security root cause
- Severity 2 (High)
  - Confirmed compromise with limited blast radius
  - High likelihood of escalation without urgent containment
  - Privileged account misuse suspected or confirmed
- Severity 3 (Moderate)
  - Suspicious behavior with moderate confidence
  - Localized impact and no current lateral movement evidence
- Severity 4 (Low)
  - Security event with low confidence or minimal impact
  - Informational or benign activity requiring tracking only

Impact Scoring Rubric
---------------------
Use the highest score observed across dimensions.

- Data sensitivity
  - 4: Regulated or highly confidential data
  - 3: Internal confidential business data
  - 2: Internal non-sensitive data
  - 1: Public data
- Operational impact
  - 4: Multi-business-unit outage
  - 3: Single critical service degraded
  - 2: Limited user or subsystem impact
  - 1: No operational impact
- Adversary capability indicators
  - 4: Ransomware/lateral movement/C2 persistence
  - 3: Credential theft with privilege access
  - 2: Commodity malware or suspicious sign-ins
  - 1: Reconnaissance-only signals

Escalation Triggers
-------------------
Immediate incident commander assignment is required when any of the following occur:
- Privileged account involvement
- Patient or customer regulated data exposure indicators
- Lateral movement evidence
- Ransomware behavior indicators
- Security control disablement on critical systems

Response Time Objectives
------------------------
- Severity 1: Triage start within 15 minutes
- Severity 2: Triage start within 30 minutes
- Severity 3: Triage start within 2 hours
- Severity 4: Triage start within 1 business day

Operational Requirements by Severity
------------------------------------
- Severity 1
  - Open bridge call within 20 minutes
  - Notify executive sponsor within 30 minutes
  - Begin legal/privacy assessment within 60 minutes
- Severity 2
  - Assign incident commander within 30 minutes
  - Send stakeholder update within 60 minutes
- Severity 3
  - Assign case owner within 2 hours
  - Document containment decision within same business day
- Severity 4
  - Route to backlog or tuning queue with rationale

Reclassification Guidance
-------------------------
Incidents must be reclassified when new evidence changes impact or confidence.
Examples:
- S3 from suspicious sign-in -> S2 when token theft is confirmed
- S2 malware event -> S1 when encryption activity spreads to file shares

Mandatory Artifacts
-------------------
- Initial triage summary
- Severity rationale and impact notes
- Timeline with UTC timestamps
- Containment actions and approvals
- Final closure and lessons learned references

Closure Criteria
----------------
Incident severity can be closed only when:
- Immediate threat is contained
- Eradication activities are complete or accepted risk is documented
- Business owner accepts restoration state
- Required post-incident review tasks are tracked
