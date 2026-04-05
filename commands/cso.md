---
description: Chief Security Officer review — vulnerability assessment, auth patterns, secret management, dependency risks
arguments:
  - name: scope
    description: "Focus area: 'full' (entire project), 'deps' (dependencies only), 'auth' (authentication/authorization), 'api' (API security), or a specific path. Defaults to 'full'."
    required: false
---

Analyze the project's security posture from a Chief Security Officer perspective.

## Steps

### 1. Gather current state

Run in parallel:
- `gh issue list --state open --label "security,vulnerability,auth,cve" --json number,title,labels,milestone,createdAt` — open security issues
- Check for dependency audit files or lockfiles (`package-lock.json`, `poetry.lock`, `requirements.txt`, `go.sum`)
- Check for `.env.example` or `.env` files — secret management patterns
- Check for security-related config (`SECURITY.md`, `cors`, `helmet`, `csrf`, authentication middleware)
- `git log --oneline -30 --all -- '*.lock' '*.txt' 'requirements*'` — recent dependency changes

If `$ARGUMENTS` provides a scope, narrow analysis to that area.

### 2. Dependency security

- Run `npm audit` / `pip audit` / equivalent for the project's package manager
- Check lockfile age — when were dependencies last updated?
- Identify dependencies with known CVEs or that are unmaintained (no commits in 12+ months)
- Check for pinned versions due to past incidents
- Look for unnecessary dependencies that expand the attack surface

### 3. Authentication & authorization audit

- **Auth flow**: How is authentication implemented? (JWT, session, OAuth, API keys)
- **Token storage**: Where are tokens stored? (httpOnly cookies vs localStorage vs memory)
- **Token lifecycle**: Are tokens rotated? Is there expiry? Is there revocation?
- **Authorization**: Is there role-based access control? Is it consistently enforced?
- **Password handling**: Is password hashing using a strong algorithm (bcrypt, argon2)?
- **Rate limiting**: Are auth endpoints rate-limited to prevent brute force?
- **MFA**: Is multi-factor authentication available/enforced for sensitive operations?

### 4. API security

- **Input validation**: Are API inputs validated and sanitized? Check for raw SQL, unsanitized HTML, unvalidated file uploads
- **CORS configuration**: Is CORS properly configured? Overly permissive (`*`) is a red flag
- **Error handling**: Do error responses leak internal details (stack traces, DB schemas, internal paths)?
- **Rate limiting**: Are API endpoints rate-limited?
- **Authentication bypass**: Are there endpoints that should require auth but don't?
- **Mass assignment**: Are API endpoints vulnerable to mass assignment (accepting unexpected fields)?
- **IDOR**: Are object-level authorization checks in place (can user A access user B's resources)?

### 5. Secret management

- **Hardcoded secrets**: Scan for hardcoded API keys, passwords, tokens in source code
- **Environment variables**: Are secrets loaded from environment, not committed?
- **`.gitignore` coverage**: Are `.env`, credential files, and key files properly gitignored?
- **Secret rotation**: Is there a process for rotating secrets?
- **Logging**: Are secrets accidentally logged? Check log statements for sensitive data

### 6. Infrastructure security

- **HTTPS**: Is TLS enforced? Are there HTTP-only endpoints?
- **Headers**: Security headers present? (`X-Frame-Options`, `X-Content-Type-Options`, `Strict-Transport-Security`, `Content-Security-Policy`)
- **Docker**: If containerized, is the image running as non-root? Are there unnecessary capabilities?
- **Database**: Are connections encrypted? Are credentials properly managed?
- **File uploads**: If supported, are file types validated? Is there size limiting? Are uploads sandboxed?

### 7. OWASP Top 10 check

Evaluate against current OWASP Top 10:
1. **Broken Access Control** — Authorization bypass, IDOR, privilege escalation
2. **Cryptographic Failures** — Weak hashing, plaintext transmission, improper key management
3. **Injection** — SQL injection, NoSQL injection, command injection, XSS
4. **Insecure Design** — Missing threat modeling, insecure business logic
5. **Security Misconfiguration** — Default credentials, unnecessary features, verbose errors
6. **Vulnerable Components** — Outdated dependencies, known CVEs
7. **Authentication Failures** — Weak passwords, missing MFA, session fixation
8. **Data Integrity Failures** — Unsigned updates, insecure deserialization, CI/CD integrity
9. **Logging Failures** — Missing audit logs, insufficient monitoring, secret leakage in logs
10. **SSRF** — Server-side request forgery in URL fetching or webhook features

### 8. Apply CSO principles

1. **Defense in depth** — No single layer should be the only protection. If auth fails, authorization should still block. If authorization fails, data-level isolation should still protect.
2. **Least privilege** — Every component should have the minimum permissions needed. API keys, DB users, container capabilities — all should be scoped down.
3. **Secrets are toxic** — Every secret in the codebase is a ticking bomb. Minimize them, rotate them, never log them.
4. **Dependencies are attack surface** — Every dependency is code you didn't write but are responsible for. Audit regularly, update promptly.
5. **Fail secure** — When something breaks, it should deny access, not grant it. Default-deny is always safer than default-allow.
6. **Assume breach** — Design as if attackers are already inside. Encrypt at rest, validate internal calls, segment networks.

### 9. Present findings

Structure output as:

```
## Security Posture Summary
- Overall posture: [strong / adequate / concerns / critical gaps]
- Last dependency update: date
- Open security issues: N
- Critical findings: N

## Severity Assessment
| Finding | Severity | Category | Status |
|---------|----------|----------|--------|
| ... | Critical/High/Medium/Low | OWASP category | Open/Mitigated |

## Dependency Security
- Audit results summary
- Outdated/vulnerable packages
- Unnecessary dependencies

## Authentication & Authorization
- Auth mechanism summary
- Strengths and weaknesses
- Missing controls

## API Security
- Input validation coverage
- Authorization consistency
- Error handling quality

## Secret Management
- Hardcoded secrets found (if any)
- Environment variable hygiene
- .gitignore coverage

## OWASP Top 10 Coverage
| Category | Status | Notes |
|----------|--------|-------|
| 1-10 | Covered/Partial/Gap | ... |

## Recommendations
- **Critical** (fix before next release)
- **High** (fix within current milestone)
- **Medium** (schedule for upcoming work)
- **Low** (nice to have)
```

### 10. Cross-reference with CTO/PM views

If `/cto` or `/pm` has been run in this session, cross-reference:
- Are security issues properly prioritized in milestones?
- Is technical debt creating security risk?
- Are there features planned that need security review first?

Do NOT execute any changes or fixes. This is analysis only — recommend actions for the user to decide.
