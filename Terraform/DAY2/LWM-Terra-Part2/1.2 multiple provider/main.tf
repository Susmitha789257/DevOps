# Terraform Block
terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "~> 4.0"
    }
  }
}

# Provider-1 for Mumbai (Default Provider)
provider "aws" {
  region = "ap-south-1"
}

# Provider-2 for Singapore
provider "aws" {
  region = "ap-southeast-1"
  alias  = "sing"
}

# Resource Block to Create VPC in ap-south-1 which uses default provider
resource "aws_vpc" "my-vpc-1" {
  cidr_block = "10.0.0.0/16"
  tags = {
    "Name" = "terra-vpc-mumbai"
  }
}

resource "aws_vpc" "my-vpc-2" {
  cidr_block = "10.0.0.0/16"
  provider   = aws.sing
  tags = {
    "Name" = "terra-vpc-singapore"
  }
}