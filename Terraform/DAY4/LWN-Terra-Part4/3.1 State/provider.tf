# Terraform Block
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.0"
    }
  }
  # Adding Backend as S3 for Remote State Storage
  backend "s3" {
    bucket = "lwm-terraform-part4"
    key    = "myterra/terraform.tfstate"
    region = "ap-southeast-1"
    dynamodb_table = "terra-table"
  }
}

# Provider Block
provider "aws" {
  region  = "ap-southeast-1"
}