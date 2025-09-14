# Create EC2 Instance - Amazon Linux
resource "aws_instance" "my-ec2-vm" {
  ami                    = "ami-079b5e5b3971bd10d"
  instance_type          = var.instance_type
  key_name               = "terraform-key"
  count                  = terraform.workspace == "default" ? 1 : 1    
	user_data              = file("apache-install.sh")  
  tags = {
    "Name" = "vm-${terraform.workspace}-0"
  }

  # local-exec provisioner (Creation-Time Provisioner - Triggered during Create Resource)
  provisioner "local-exec" {
    command = "echo ${self.private_ip} >> creation-time-private-ip.txt"
    working_dir = "local-exec-output-files/"
    #on_failure = continue
  }

  # local-exec provisioner - (Destroy-Time Provisioner - Triggered during Destroy Resource)
  provisioner "local-exec" {
    when    = destroy
    command = "echo Destroy-time provisioner Instanace Destroyed at `date` >> destroy-time.txt"
    working_dir = "local-exec-output-files/"
  }  
}







