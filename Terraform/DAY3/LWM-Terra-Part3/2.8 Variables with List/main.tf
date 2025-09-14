# Create EC2 Instance
resource "aws_instance" "my-ec2-vm" {
  ami                    = var.ec2_ami_id
  instance_type          = var.ec2_instance_type[2]
  count                  = var.ec2_instance_count
  tags = {
    "Name" = "myec2vm"
  }
}