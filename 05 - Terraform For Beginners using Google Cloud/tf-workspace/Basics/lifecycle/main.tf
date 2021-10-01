resource random_integer name {
  min = 20
  max = 350

    lifecycle{
        #create_before_destroy = true
        #prevent_destroy = true
        ignore_changes = [min, max]
    }

}
