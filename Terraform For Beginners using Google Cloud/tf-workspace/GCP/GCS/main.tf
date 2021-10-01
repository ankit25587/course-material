
resource "google_storage_bucket" "GCS1" {
  
  name = "tf-course-bucket-from-terraform"
  storage_class = "NEARLINE"
  location = "US-CENTRAL1"
  labels = {
    "env" = "tf_env"
    "dep" = "complience"
  }
  uniform_bucket_level_access = true

  lifecycle_rule {
    condition {
      age = 5
    }
    action {
      type = "SetStorageClass"
      storage_class = "COLDLINE"
    }
  }

  retention_policy {
    is_locked = true
    retention_period = 864000
  }

}

resource "google_storage_bucket_object" "picture" {
  name = "vodafone_logo"
  bucket = google_storage_bucket.GCS1.name
  source = "vodafone.jpg"
}