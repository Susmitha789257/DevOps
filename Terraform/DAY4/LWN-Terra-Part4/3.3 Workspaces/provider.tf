# Terraform Block
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.0"
    }
  }
  backend "s3" {
    bucket = "lwm-terraform-part4"            # Change Bucket Name
    key    = "workspaces/terraform.tfstate"
    region = "ap-southeast-1"  
    dynamodb_table = "terra-table"  # For State Locking   
  }
}

# Provider Block
provider "aws" {
  region  = "ap-southeast-1"
}