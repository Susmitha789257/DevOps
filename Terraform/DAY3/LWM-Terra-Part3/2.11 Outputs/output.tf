# Define Output Values
# Attribute Reference: EC2 Instance Public IP
output "pub_ip" {
  description = "My machine public ip"
  value       = aws_instance.my-ec2-vm.public_ip
}

output "pri_ip" {
  description = "My machine private ip"
  value       = aws_instance.my-ec2-vm.private_ip
}