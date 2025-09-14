terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "6.13.0"
    }
  }
}

provider "aws" {
    region = "ap-southeast-1"
    access_key = "my-access-key"
    secret_key = "my-secret-key"
}
#main vpc
resource "aws_vpc" "vpc-name" {
  cidr_block       = "10.0.0.0/16"
  instance_tenancy = "default"

  tags = {
    Name = "Terra-vpc"
  }
}
#public subnet
resource "aws_subnet" "pubsub" {
  vpc_id     = aws_vpc.vpc-name.id
  cidr_block = "10.0.1.0/24"

  tags = {
    Name = "pub"
  }
}

#private subnet
resource "aws_subnet" "prisub" {
  vpc_id     = aws_vpc.vpc-name.id
  cidr_block = "10.0.2.0/24"

  tags = {
    Name = "pri"
  }
}

#s3 bucket
resource "aws_s3_bucket" "s3" {
  bucket = "my-tf-test-bucket"

  tags = {
    Name        = "My bucket"
    Environment = "Dev"
  }
}

#s3 bucket
resource "aws_s3_bucket" "s31" {
  bucket = "my-tf-test-bucket1"

  tags = {
    Name        = "My bucket1"
    Environment = "Dev"
  }
}