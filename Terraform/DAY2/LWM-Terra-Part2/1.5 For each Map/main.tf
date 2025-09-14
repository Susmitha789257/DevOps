terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "~> 3.0"
    }
  }
}

provider "aws" {
  region  = "ap-south-1"
}

# Create 3 S3 Buckets
resource "aws_s3_bucket" "mys3bucket" {

  # for_each Meta-Argument
  for_each = {
    dev  = "my-dapp-bucket-LWM"
    qa   = "my-qapp-bucket-LWM"
    uat  = "my-uapp-bucket-LWM"
  }

  bucket = "${each.key}-${each.value}"          # dev-my-dapp-bucket-LWM
  acl    = "private"                             # acl - Access control list

  tags = {
    Environment = "MY-${each.key}-LWM"          # MY-dev-LWM
    bucketname  = "${each.key}-${each.value}"   # dev-my-dapp-bucket-LWM
    eachvalue   = each.value                    # my-dapp-bucket-LWM
  }
}