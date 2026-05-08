Incident Triage Workflow
=======================

Document Metadata
-----------------
- Owner: Security Operations Center
- Approver: Director of Security Engineering
- Review cadence: Every 6 months

Purpose
-------
This workflow standardizes first-response triage to ensure rapid, repeatable,
and evidence-driven incident decisions.

Triage Intake
-------------
Capture and normalize these mandatory fields at case open:
- Alert source and detection rule ID
- First-seen and last-seen timestamps (UTC)
- Affected identities, devices, workloads, and data stores
- Business service ownership and criticality

Normalization Standard
----------------------
All events are translated to:
- Who: user/service identity
- What: suspicious action or artifact
- Where: host, app, tenant, region
- When: timeline and dwell indicators
- Impact: observed or potential business harm

Evidence Collection
-------------------
- Pull identity, endpoint, network, and cloud activity logs.
- Preserve volatile evidence before host isolation when feasible.
- Record chain-of-custody details for every exported artifact.
- Store evidence in approved case repository with immutable timestamps.

Minimum Triage Checks
---------------------
- Validate alert quality and known false-positive patterns.
- Verify enrichment: geolocation, asset criticality, vulnerability context.
- Determine whether this event links to an active incident.
- Assess current blast radius and immediate containment need.

Decision Points
---------------
- Is this a true positive, false positive, or undetermined?
- Is privilege escalation present or likely?
- Is lateral movement or persistence indicated?
- Does impact justify severity escalation?

Severity Assignment
-------------------
Apply severity policy and include explicit rationale using:
- Confirmed impact
- Confidence level
- Spread potential
- Data sensitivity involved

Output Requirements
-------------------
Every triage cycle must produce:
- Incident summary in plain language
- Confirmed indicators of compromise
- Immediate containment recommendation
- Assigned owner and next checkpoint time
- Open questions and evidence gaps

Handoff Rules
-------------
- Escalate to Incident Commander for Severity 1 and 2.
- Handoff to detection engineering for confirmed false positives requiring tuning.
- Open dependent tasks for IAM, endpoint, cloud, and legal teams as needed.

SLA Targets
-----------
- First analyst touch: <= 15 minutes for high-priority queue
- Initial severity decision: <= 30 minutes
- First stakeholder update: <= 60 minutes for Severity 2+

Quality Controls
----------------
- Peer review required for Severity 1 closure recommendation.
- Weekly triage QA checks on sampling of closed incidents.
- Metrics tracked: time-to-triage, reclassification rate, false-positive ratio.
