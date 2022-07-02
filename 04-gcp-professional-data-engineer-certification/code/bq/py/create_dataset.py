from google.cloud import bigquery

client = bigquery.Client.from_service_account_json('keys.json')

dataset_id = "single-odyssey-349606.ds_from_python"

dataset = bigquery.Dataset(dataset_id)

dataset.location = "US"

dataset_ref = client.create_dataset(dataset, timeout=30)

print("Created dataset {}.{}".format(client.project, dataset_ref.dataset_id))