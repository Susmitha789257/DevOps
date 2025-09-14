# Call our Custom Terraform Module which we built earlier

module "website_s3_bucket" {
  source = "./modules/s3"  # Mandatory
  bucket_name = var.my_s3_bucket
  tags = var.my_s3_tags
}


module "my-vpc" {
  source = "/root/myfolder/vpc"  # Mandatory
}