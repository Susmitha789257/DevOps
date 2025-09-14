locals {
  Project = "Armageddon"
}

# Create S3 Buckets
resource "aws_s3_bucket" "mys3bucket" {
  bucket = "my-dapp-bucket-666"  
  acl    = "private"
  tags = {
    "project" = "Project-${local.Project}-S3Bucket"
  }
}

resource "aws_instance" "my-ec2-vm" {
  ami           = "ami-005835d578c62050d"
  instance_type = "t2.micro"
  tags = {
    "Name"    = "web"
    "project" = "Project-${local.Project}-EC2-Instance"
  }
}

# Resource Block to Create VPC in ap-south-1
resource "aws_vpc" "my-vpc-1" {
  cidr_block = "10.0.0.0/16"
  tags = {
    "Name"    = "terra-vpc-mumbai"
    "Author"  = "Mithran"
    "project" = "Project-${local.Project}-VPC"
  }
}