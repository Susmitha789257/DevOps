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

# Resource Block to Create VPC in ap-south-1
# meta-argument
resource "aws_vpc" "my-vpc-1" {
  cidr_block = "10.0.0.0/16"
  count      = 2
  tags = {
    "Name" = "terra-vpc-mumbai-${count.index}"
  }
}