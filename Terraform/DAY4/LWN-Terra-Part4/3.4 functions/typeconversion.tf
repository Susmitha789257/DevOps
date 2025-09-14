output "to_string" {
  value = tostring(123)             # Output: "123"
}

output "to_list" {
  value = tolist(["a", "b", "c"])   # Output: ["a", "b", "c"]
}

output "to_map" {
  value = tomap({ a = 1, b = 2 })   # Output: { a = 1, b = 2 }
}