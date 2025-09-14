resource "aws_vpc" "my-vpc" {
  cidr_block       = var.cidr_block
  instance_tenancy = "default"

  tags = {
    "Name" = var.tags
  }
}

resource "aws_subnet" "public-subnet" {
  vpc_id     = aws_vpc.my-vpc.id
  cidr_block = var.pub_cidr_block

  tags = {
    "Name" = "${var.tags}-public-subnet"
  }
}

resource "aws_subnet" "private-subnet" {
  vpc_id     = aws_vpc.my-vpc.id
  cidr_block = var.pri_cidr_block

  tags = {
    "Name" = "${var.tags}-private-subnet"
  }
}