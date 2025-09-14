variable "vpc_id" {
  description = "VPC id to read from Console"
  type        = string
}

data "aws_vpc" "my-vpc" {
  id = var.vpc_id 
}

resource "aws_subnet" "my-sub" {
  vpc_id            = data.aws_vpc.my-vpc.id
  availability_zone = "ap-south-1a"
  cidr_block        = "55.0.1.0/24"
}