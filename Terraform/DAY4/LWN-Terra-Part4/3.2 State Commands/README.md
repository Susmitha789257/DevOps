# Terraform State Commands

## Terraform Commands
  - terraform show
  - terraform refresh
  - terraform plan (internally calls refresh - temporary refresh)
  - terraform fmt
  - terraform validate
  - terraform state list
  - terraform state show <resource_type>.<resource_name>
  - terraform force-unlock LockID
  - terraform taint
  - terraform untaint
  - terraform apply -target command
  - terraform import <resource_type>.<resource_name> <resource_id>