Post-Incident Review and Lessons Learned
========================================

Document Metadata
-----------------
- Owner: Security Program Management
- Approver: CISO
- Review cadence: After each Severity 1-2, monthly rollup for all severities

Purpose
-------
This procedure defines required post-incident review activities to convert
incident experience into measurable security and operational improvements.

Review Timeline
---------------
- Severity 1 and 2 incidents: review within 5 business days
- Severity 3 and 4 incidents: review within 10 business days

Participants
------------
- Incident Commander
- SOC and detection engineering representatives
- Affected platform/application owners
- IAM/Endpoint/Cloud SMEs as relevant
- Legal/Privacy representatives when data exposure is involved

Required Inputs
---------------
- Final incident timeline
- Root cause analysis
- Detection and response performance metrics
- Control gaps and remediation proposals
- Communications effectiveness review

Root Cause Framework
--------------------
Each review must cover:
- Initial access path
- Control failure point(s)
- Detection delay and blind spots
- Response bottlenecks and decision friction
- Dependency and ownership gaps

Output Artifacts
----------------
- Corrective action plan with owners and deadlines
- Detection tuning requests and validation criteria
- Process changes and runbook updates
- Executive summary for leadership review

Action Quality Criteria
-----------------------
- Specific: clearly scoped technical or process change
- Measurable: success metric defined
- Achievable: owner has resources and authority
- Relevant: linked to observed failure mode
- Time-bound: target completion date set

Program Metrics
---------------
Track and trend over time:
- Mean time to detect (MTTD)
- Mean time to contain (MTTC)
- Mean time to recover (MTTR)
- Reopen rate and recurrence rate
- Detection precision and false-positive ratio

Governance
----------
- Overdue corrective actions escalated at weekly risk review.
- Severity 1 corrective actions require executive sponsor sign-off.
- Closure requires evidence that controls are implemented and validated.

Closure Criteria
----------------
- All high-priority corrective actions assigned
- Ownership and target dates approved
- Residual risks documented and accepted by accountable leaders
- Lessons incorporated into training and playbook updates
