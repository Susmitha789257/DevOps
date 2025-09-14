variable "names" {
  default = ["Dev", "Test", "Prod"]
}

output "joined_names" {
  value = join("|", var.names)         # Output: "Dev|Test|Prod"
}

output "split_name" {
  value = split("-", "Dev-Test-Prod")  # Output: ["Dev", "Test", "Prod"]
}

output "lowercase" {
  value = lower("TERRAFORM")           # Output: "terraform"
}

output "uppercase" {
  value = upper("terraform")           # Output: "TERRAFORM"
}

output "trimmed" {
  value = trimspace("  Hello Terraform  ") # Output: "Hello Terraform"
}

output "replaced" {
  value = replace("version-1.0", "1.0", "2.0") # Output: "version-2.0"
}