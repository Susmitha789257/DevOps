# Input Variables
variable "ec2_ami_id" {
  description = "AMI ID"
  type = string  
  default = "ami-08cd358d745620807"
}

variable "ec2_instance_type" {
  description = "EC2 Instance Type"
  type = string
  default = "t2.micro"
}