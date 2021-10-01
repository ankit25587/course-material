resource random_integer rint{
    min = 80
    max = 200
}

resource random_string rstring {
  length  = 15
}


output name1 {
  value       = random_integer.rint.result
}

output name2 {
  value       = random_string.rstring.result
}
