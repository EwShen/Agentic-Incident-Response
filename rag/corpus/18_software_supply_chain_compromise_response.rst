Software Supply Chain Compromise Response
=========================================

Document Metadata
-----------------
- Owner: Product Security
- Approver: VP Engineering and CISO
- Review cadence: Semiannual

Purpose
-------
This playbook addresses compromise in software supply chain components,
including build pipelines, dependencies, package repositories, and signing keys.

Trigger Conditions
------------------
- Malicious dependency or package update detection
- Build pipeline tampering indicators
- Unauthorized artifact signing activity
- Threat intelligence linking upstream dependency to compromise

Immediate Response
------------------
- Freeze affected build and release pipelines.
- Revoke compromised signing credentials and tokens.
- Block distribution of suspect artifacts.
- Notify engineering leads and incident command team.

Investigation Priorities
------------------------
- Identify first compromised component and trust boundary failure.
- Determine which builds/artifacts are affected.
- Validate integrity of source control, CI runners, and artifact storage.
- Assess customer and internal deployment exposure.

Containment Actions
-------------------
- Pin dependencies to known-good versions.
- Rebuild artifacts from trusted clean environment.
- Rotate all pipeline secrets and service account credentials.
- Enforce two-person approval for release promotion during recovery.

Recovery and Validation
-----------------------
- Re-establish trusted build provenance.
- Re-sign and republish verified artifacts.
- Validate downstream consumers have patched versions deployed.

Communication
-------------
- Provide internal advisory with affected versions and remediation path.
- Coordinate external disclosure with Legal and communications teams.
- Track customer support impact and field escalation requests.

Closure Criteria
----------------
- Build/release trust chain restored
- Compromised artifacts withdrawn and replaced
- Exposure scope documented with customer impact assessment
- Preventive controls integrated into SDLC workflow
