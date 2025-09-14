# Create VPC with Workspaces
resource "aws_vpc" "vpc1" {
  cidr_block       = "12.0.0.0/16"
  instance_tenancy = "default"
  count            = terraform.workspace == "default" ? 2 : 1    # Condition
  tags = {
    Name = "vpc-${terraform.workspace}-${count.index}"  # vpc-dev-0 
  }
}