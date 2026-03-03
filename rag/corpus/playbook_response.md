# Incident Response Playbook Snippets

## Phishing Suspected
- Validate the sender domain and SPF/DKIM status.
- Inspect attachment hashes and URLs in a sandbox.
- If malicious, isolate affected mailbox and revoke active sessions.
- Reset credentials and enable MFA if not already enforced.
- Search tenant-wide for matching indicators (subject, hash, domain).

## Impossible Travel Alert
- Compare source IP geolocation with known VPN egress points.
- Correlate with device fingerprint and user agent.
- Check for successful MFA and conditional access policy decisions.
- If suspicious, force sign-out and password reset.
- Open a high-priority incident if privileged accounts are involved.

## Malware Beaconing
- Validate destination domain reputation and TLS cert anomalies.
- Isolate endpoint from network while preserving forensic artifacts.
- Capture process tree and persistence mechanisms.
- Block IOC set (domain, IP, hash) at EDR and firewall layers.
- Escalate to containment phase if lateral movement evidence exists.
