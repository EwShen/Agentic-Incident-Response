Lost or Stolen Device Incident Response
=======================================

Document Metadata
-----------------
- Owner: Endpoint and IT Security
- Approver: IT Operations Director
- Review cadence: Quarterly

Purpose
-------
This playbook governs response procedures for lost or stolen company-managed
endpoints and mobile devices that may expose corporate data.

Trigger Conditions
------------------
- Employee report of lost/stolen device
- Device geofence anomaly with communication loss
- Law enforcement notice involving company asset recovery

Immediate Actions
-----------------
- Verify asset ownership and last known device posture.
- Trigger remote lock and wipe, where technically feasible.
- Revoke active sessions and enterprise access tokens.
- Disable VPN and high-risk application access tied to device.

Risk Assessment
---------------
Evaluate:
- Disk encryption status and key escrow health
- Device management compliance state
- Data classification of locally cached content
- Privilege level of associated user account

Investigation Steps
-------------------
- Review recent authentication and access attempts.
- Check for suspicious activity after reported loss time.
- Confirm whether backup device or account takeover occurred.
- Track recovery efforts and external report references.

Containment and Recovery
------------------------
- Issue replacement device with hardened baseline.
- Reset user credentials and enforce fresh MFA registration.
- Restore approved data from secure backups.

Communication Requirements
--------------------------
- Notify employee manager and IT support queue.
- Escalate to Legal/Privacy for high-risk data scenarios.
- Update incident record with status every business day until closure.

Closure Criteria
----------------
- Device risk neutralized via wipe, recovery, or compensating controls
- No suspicious post-loss access remains
- User access restored on compliant replacement asset
- Follow-up control gaps documented
