terraform {
  required_providers {
    random = {
      source = "hashicorp/random"
      version = "2.3.1"
    }
  }
}

provider "random" {
  # Configuration options
}


resource random_integer name {
  min = 0
  max = 100
}
