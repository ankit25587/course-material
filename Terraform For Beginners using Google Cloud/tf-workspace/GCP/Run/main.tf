resource "google_cloud_run_service" "run-app-from-tf" {
  name = "run-app-from-tf"
  location = "asia-southeast1"
  
  template {
    spec {
      containers {
        #image = "gcr.io/google-samples/hello-app:1.0"
        image = "gcr.io/google-samples/hello-app:2.0"
      }
    }
  }

  traffic {
    revision_name = "run-app-from-tf-vqn2c"
    percent = 50
  }
  traffic {
    revision_name = "run-app-from-tf-pkt92"
    percent = 50
  }


  
}


resource "google_cloud_run_service_iam_policy" "pub_access" {
  service = google_cloud_run_service.run-app-from-tf.name
  location = google_cloud_run_service.run-app-from-tf.location
  policy_data = data.google_iam_policy.pub-1.policy_data
}

data "google_iam_policy" "pub-1" {
  binding {
    role = "roles/run.invoker"
    members = [ "allUsers", ]
  }
}
