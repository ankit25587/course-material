resource "google_bigquery_dataset" "bd_ds" {
  dataset_id = "ds_from_tf"
}

resource "google_bigquery_table" "table_tf" {
  table_id = "table_from_tf"
  dataset_id = google_bigquery_dataset.bd_ds.dataset_id

}