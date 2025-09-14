variable "tags" {
  default = {
    "env"   = "dev"
    "owner" = "admin"
  }
}

output "tags_length" {
  value = length(var.tags)          # Output: 2
}

output "tags_keys" {
  value = keys(var.tags)            # Output: ["env", "owner"]
}

output "tags_values" {
  value = values(var.tags)          # Output: ["dev", "admin"]
}

output "list_check" {
  value = contains(["a", "b", "c"], "b")  # Output: true
}

output "merged_maps" {
  value = merge(
    { a = 1, b = 2 },
    { b = 3, c = 4 }
  )  # Output: { a = 1, b = 3, c = 4 }
}

output "flattened_list" {
  value = flatten([["a", "b"], ["c"]]) # Output: ["a", "b", "c"]
}