# Assume you have a file `hello.txt` with content: Hello World

output "file_content" {
  value = file("${path.module}/hello.txt") 
  # Output: "Hello World"
}

output "file_base64" {
  value = filebase64("${path.module}/hello.txt") 
  # Output: base64-encoded string of the file
}

output "absolute_path" {
  value = abspath("./")             # Output: absolute path to the current directory
}
