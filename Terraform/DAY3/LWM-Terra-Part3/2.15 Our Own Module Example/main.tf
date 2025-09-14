module aws_vpc {
  source = "/opt/modules/vpc/"
  tags = "LWM-vpc"
  cidr_block = "12.0.0.0/16"
  pub_cidr_block = "12.0.1.0/24"
  pri_cidr_block = "12.0.2.0/24"
}