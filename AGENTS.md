# AGENTS.md

## Variables

- Agent Name: opsta_k8s_agent
- Working Directory: /Users/winggundamth/git/opsta-k8s-agent-12/opsta-k8s-agent
- Repository URL: https://github.com/opsta/opsta-k8s-agent-12
- Programming Language: Python 3.12
- LLM Model Name: Gemini Flash (latest, global)
- GCP Region: asia-southeast1
- GCP Project: zcloud-cicd
- Deployment Target: Agent Runtime (opsta-k8s-agent-12-stg, opsta-k8s-agent-12-prd)
- Terraform State Storage GCS Bucket Name: opsta-k8s-agent-12-tf

## Skills

- Always use `agents-cli` skills

## End-to-end Local Test Plan

- Run and start everything in local.
- Agent can directly call the LLM model on the Cloud.
- Don't commit, push, or deploy anything to git and Cloud until you fix everything and confirm it works via e2e test.
- Let me know when you have fixed and tested everything before I give you the call to commit code or deploy to GCP.

## Developer Rules & Constraints

- **Branch Protection & Feature Branch Workflow**
  - Configure the `main` branch of every repository as a **protected branch**.
  - For any new feature, branch from `main` using the prefix `feat/` (e.g., `feat/sales-subagent`).
  - Always **delete the feature branch** after it has been merged or when it is no longer needed.
- **Authenticated CLIs**
  - `gh`
  - `glab`
  - `gcloud`
- **Enforce Linting and Formatting**
- **Evaluations Execution**
- **Graceful Error Handling**
- **Long-Term Fixes Over Workarounds**

## Infrastructure Rules & Constraints

- **Infrastructure as Code**
- **Strict Version Pinning**
- **Use Latest Stable Versions for Core Tooling**
- **Local Package Installation**
- **Agent Runtime Configuration** with `min instance = 0` for both Staging and Production environments

## CI/CD Rules & Constraints

- **CI/CD Pipeline**
- **Zero Deprecation Warnings**
- **Tooling & Environment Constraints**
- **Pipeline Trigger Scope**
- **Staging Deployment**
- **Production Deployment**
- **Deployment Constraints**
- **Conventional Commits**
- **Job Separation & Ordering**
- **CI/CD Performance Optimization**
- **Self-Hosted Runners**

## Security

- **No Hardcoded Secrets**
- **Webhook Security**
- **SAST Scanning**
- **SCA Scanning**
- **Secrets Scanning**
- **IaC Scanning**
- **CI/CD Integration**
- **Local Security Enforcement**
- **Deployment Blocker**
- **Prompt Injection Protection**
- **Least Privilege (IAM)**

## Execution Mode

- **Local-First with Automatic Promotion**
- **Fully Autonomous**
- **Self-Correction**
- **Progressive Delivery**
- **Continuous State Sync**
- **Automated End-to-End Pipeline Execution**
- **Definition of Done**
