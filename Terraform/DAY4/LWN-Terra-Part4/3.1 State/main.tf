# Resource Block to Create VPC in ap-south-1 which uses default provider
resource "aws_vpc" "my-vpc-1" {
  cidr_block = "10.0.0.0/16"
  tags = {
    "Name" = "terra-vpc-singapore"
  }
}

# Create EC2 Instance
resource "aws_instance" "my-ec2-vm" {
  ami           = "ami-00dc6910e7d33c5f8"
  instance_type = "t2.micro"
  tags = {
    "Name" = "web"
  }
}