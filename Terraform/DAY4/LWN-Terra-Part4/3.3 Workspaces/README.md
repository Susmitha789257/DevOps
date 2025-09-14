# Terraform Workspaces

## Introduction
- We are going to create 2 more workspaces (dev,qa) in addition to default workspace
- Update our terraform manifests to support `terraform workspace` 
  - Primarily for security group name to be unique for each workspace
  - In the same way for EC2 VM Instance Name tag. 
- Master the below listed `terraform workspace` commands
  - terraform workspace show
  - terraform workspace list
  - terraform workspace new
  - terraform workspace select
  - terraform workspace delete