# terraform plan --var="ec2_instance_type=t3.large" --var="ec2_instance_count=1"
# Terraform Block
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.0"
    }
  }
}

# Provider Block
provider "aws" {
  region  = var.aws_region
}