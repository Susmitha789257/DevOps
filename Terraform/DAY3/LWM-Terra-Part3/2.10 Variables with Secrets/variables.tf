# Input Variables
variable "aws_region" {
  description = "Region in which AWS Resources to be created"
  type        = string
  default     = "ap-south-1"
}

variable "db_username" {
  description = "AWS RDS Database Administrator Username"
  type        = string
  sensitive   = true
}

variable "db_password" {
  description = "AWS RDS Database Administrator Password"
  type        = string
  sensitive   = true
}

variable "aws_access_key" {
  description = "AWS account access key"
  type        = string
  sensitive   = true
}

variable "aws_secret_key" {
  description = "AWS account secret key"
  type        = string
  sensitive   = true
}