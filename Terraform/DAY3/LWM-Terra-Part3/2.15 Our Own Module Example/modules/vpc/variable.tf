variable "cidr_block" {
  type        = string
  default     = "10.0.0.0/16"
  description = "The CIDR to create a VPC"
}

variable "pub_cidr_block" {
  type        = string
  default     = "10.0.1.0/24"
  description = "The CIDR to create a public Subnet"
}

variable "pri_cidr_block" {
  type        = string
  default     = "10.0.2.0/24"
  description = "The CIDR to create a private Subnet"
}

variable "tags" {
  type = string
  default = "MY_VPC"
  description = "Project Tags"
}