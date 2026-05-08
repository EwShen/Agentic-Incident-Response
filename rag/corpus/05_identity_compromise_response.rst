Identity Compromise Response
============================

Document Metadata
-----------------
- Owner: Identity Security Team
- Approver: IAM Director
- Review cadence: Quarterly

Purpose
-------
This document defines response actions for compromised workforce and service identities,
including account takeover, token theft, and unauthorized privilege changes.

Detection Signals
-----------------
- Impossible travel sign-ins
- MFA fatigue or repeated push denials
- Privileged role changes outside maintenance windows
- Suspicious OAuth consent grants
- Anomalous API activity from service principals

First-Hour Actions
------------------
- Validate identity risk from sign-in and endpoint context.
- Disable account or enforce emergency password reset.
- Revoke tokens and sign out all active sessions.
- Remove unauthorized MFA methods and app passwords.
- Snapshot current role assignments for forensic record.

Containment Depth Levels
------------------------
- Level A (suspected): session revocation and high-friction auth controls
- Level B (confirmed): account disablement and broad token invalidation
- Level C (privileged abuse): immediate privilege strip and emergency change freeze

Investigation Actions
---------------------
- Review sign-in history, device posture, and geolocation anomalies.
- Audit mailbox, file repositories, and admin portals for misuse.
- Verify creation of persistence artifacts (forwarding, OAuth, delegated access).
- Determine whether additional identities were compromised.

Service Identity Response
-------------------------
- Rotate client secrets/certificates and API keys.
- Restrict role scope to least privilege during investigation.
- Review workload logs for suspicious automation execution.

Recovery Actions
----------------
- Re-establish secure MFA with approved enrollment process.
- Reissue credentials after endpoint and phishing risk checks.
- Re-enable account access only after owner and manager verification.
- Monitor for re-compromise attempts for at least 14 days.

Communications
--------------
- Notify business owner for privileged or customer-impacting identities.
- Coordinate legal/privacy review if data access indicators exist.
- Document all access-restoration approvals.

Closure Criteria
----------------
- Unauthorized access path removed
- Credentials and tokens rotated where required
- No suspicious re-authentication observed in monitoring window
- Detection and policy control improvements tracked
