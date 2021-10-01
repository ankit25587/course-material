resource "google_bigtable_instance" "bt-from-tf" {
  
  name = "bt-from-tf"
  deletion_protection = false
  labels = {
    "env" = "testing"
  }
  cluster {
    cluster_id = "bt-from-tf-1"
    num_nodes = 1
    storage_type = "SSD"
  }

}


resource "google_bigtable_table" "tb1" {
  name = "tb-from-tf"
  instance_name = google_bigtable_instance.bt-from-tf.name
}