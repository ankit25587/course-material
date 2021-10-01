resource "google_spanner_instance" "spanner_tf" {
  name = "spannertf"
  config = "regional-asia-south1"
  display_name = "Spanner from TF"
  num_nodes = 1
  labels = {
    "env" = "learningtf"
  }
  
}


resource "google_spanner_database" "db1"{
    name = "db1"
    instance =  google_spanner_instance.spanner_tf.name
}