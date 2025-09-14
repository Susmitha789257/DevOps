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

# Resource Block to Create VPC in ap-south-1
# meta-argument
resource "aws_vpc" "my-vpc-1" {
  cidr_block = "10.0.0.0/16"
  count      = 2
  tags = {
    "Name" = "terra-vpc-mumbai-${count.index}"
  }
  depends_on = [aws_s3_bucket.mys3bucket]
}

# Create 6 IAM Users
resource "aws_iam_user" "myuser" {
  for_each = toset(["TJack", "TJames", "TMadhu", "TDave", "TMithran", "TAashik"])
  name     = each.key
  depends_on = [aws_vpc.my-vpc-1]
}