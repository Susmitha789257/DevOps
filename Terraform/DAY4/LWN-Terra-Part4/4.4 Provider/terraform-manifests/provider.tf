# Terraform Block
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.0"
    }
    null = {
      source = "hashicorp/null"
      version = "~> 3.0.0"
    }
    time = {
      source = "hashicorp/time"
      version = "~> 0.6.0"
    }      
  }
}

# Provider Block
provider "aws" {
  region  = var.aws_region
}
