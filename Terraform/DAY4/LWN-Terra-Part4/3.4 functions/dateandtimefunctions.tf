output "current_timestamp" {
  value = timestamp()               # Output: "2025-05-12T10:30:00Z" (example)
}

output "formatted_date" {
  value = formatdate("YYYY-MM-DD", timestamp())  # Output: "2025-05-12"
}
