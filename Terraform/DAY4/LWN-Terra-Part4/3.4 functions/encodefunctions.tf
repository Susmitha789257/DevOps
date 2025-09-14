output "base64_encoded" {
  value = base64encode("hello")     # Output: aGVsbG8=
}

output "base64_decoded" {
  value = base64decode("aGVsbG8=")  # Output: hello
}