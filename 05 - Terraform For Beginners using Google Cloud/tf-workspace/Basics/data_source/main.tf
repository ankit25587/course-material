data local_file foo {
  filename = "sample1.txt"
}

output name1 {
  value       = data.local_file.foo.content
}

