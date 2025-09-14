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
  region  = "ap-southeast-1"
}

resource "aws_vpc" "vpc1" {
  cidr_block       = "10.0.0.0/16"
  instance_tenancy = "default"

  tags = {
    Name = "Terra-VPC-1"
  }
}

# Create 3 S3 Buckets
resource "aws_s3_bucket" "mys3bucket" {

  # for_each Meta-Argument
  for_each = {
    dev  = "my-dapp-bucket-lwm"
    qa   = "my-qapp-bucket-lwm"
    uat  = "my-uapp-bucket-lwm"
  }

  bucket = "${each.key}-${each.value}"          # dev-my-dapp-bucket-LWM
  acl    = "private"

  tags = {
    Environment = "MY-${each.key}-lwm"          # MY-dev-LWM
    bucketname  = "${each.key}-${each.value}"   # dev-my-dapp-bucket-LWM
    eachvalue   = each.value                    # my-dapp-bucket-LWM
  }
}

# Create 6 IAM Users
resource "aws_iam_user" "myuser" {
  for_each = toset(["TJack", "TJames", "TMadhu", "TDave", "TMithran", "TAashik"])
  name     = each.key
}