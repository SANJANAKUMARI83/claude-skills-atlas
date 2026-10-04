---
name: threat-modeling
category: cybersecurity
tags: [threat-modeling, architecture, security-design]
---

# Lightweight Threat Modeling

## Purpose
Help teams identify security risks early by systematically examining assets, trust boundaries, threats, and mitigations.

## When to use
Use during feature planning, architecture reviews, major dependency changes, or before exposing a new service or API.

## Instructions
1. Define the system boundary, intended use, deployment context, and explicit exclusions.
2. List important assets, such as credentials, personal data, business records, and privileged operations.
3. Draw or describe components, data flows, entry points, external services, and trust boundaries.
4. For each flow, ask who can send input, what is trusted, what authorization is enforced, and what happens on failure.
5. Consider relevant threat categories: spoofing, tampering, repudiation, information disclosure, denial of service, and elevation of privilege.
6. Rank each threat using likelihood, impact, assumptions, and existing controls. Do not imply numeric precision without a defined scoring method.
7. Recommend mitigations that map directly to threats and identify an owner or verification test where possible.
8. Revisit the model when system boundaries, data sensitivity, or trust assumptions change.

## Inputs
- System purpose and architecture
- Data-flow description or diagram
- Assets and trust boundaries
- Deployment assumptions and existing controls

## Outputs
A concise threat register containing the threat, affected asset or flow, assumptions, impact, existing controls, recommended mitigation, and validation approach.

## Example
For a file-upload service, examine file type and size validation, storage permissions, malware scanning, access checks on downloads, and resource-exhaustion limits.

## Limitations
A threat model identifies plausible risks; it does not prove that a vulnerability exists. Validate important assumptions against implementation and deployment evidence.
