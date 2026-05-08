Cloud Misconfiguration and Exposure
===================================

Document Metadata
-----------------
- Owner: Cloud Security Engineering
- Approver: Head of Infrastructure Security
- Review cadence: Quarterly

Purpose
-------
This playbook addresses cloud incidents caused by misconfiguration,
excessive privilege, or unintended public exposure.

Common Scenarios
----------------
- Public storage bucket exposure
- Overly permissive IAM role assignment
- Disabled logging or detection controls
- Security group or firewall rule drift

Detection Inputs
----------------
- CSPM and CIEM alerts
- Cloud audit logs and API anomaly detections
- External attack-surface monitoring notifications

Containment Actions
-------------------
- Remove public access and enforce least-privilege IAM changes.
- Rotate exposed credentials and revoke high-risk tokens.
- Enable or restore cloud audit logging immediately.
- Apply temporary SCP or policy guardrails to stop recurrence.

Investigation Actions
---------------------
- Determine exposure duration and accessed object scope.
- Correlate cloud access logs with source IPs and API callers.
- Identify IaC commit or manual action that introduced drift.
- Assess whether data was copied, modified, or deleted.

Data Exposure Assessment
------------------------
- Enumerate impacted buckets, tables, or secrets stores.
- Map exposed objects to data classification taxonomy.
- Validate actual access evidence versus theoretical exposure.

Remediation Plan
----------------
- Correct IaC templates and re-deploy approved baseline.
- Implement policy-as-code checks in CI/CD gates.
- Add preventive controls for high-risk service configurations.
- Update asset ownership and on-call mapping.

Prevention Follow-Up
--------------------
- Continuous misconfiguration scanning with routed alerts
- Periodic access reviews for privileged cloud roles
- Chaos testing for cloud security controls and logging resilience

Closure Criteria
----------------
- Misconfiguration corrected and validated in runtime
- Access risk reduced to approved baseline
- Any exposure notifications completed as required
- Recurrence prevention controls tracked to completion
