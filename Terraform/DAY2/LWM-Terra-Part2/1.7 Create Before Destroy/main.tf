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
  region  = "ap-south-1"
}

# Create EC2 Instance
# Resource Block to Create VPC in ap-south-1 which uses default provider
resource "aws_vpc" "my-vpc-1" {
  cidr_block = "11.0.0.0/16"
  tags = {
    "Name" = "terra-vpc-mumbai"
  }
  lifecycle {
    create_before_destroy = true
  }
}