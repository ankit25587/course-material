from google.cloud import bigquery

client = bigquery.Client.from_service_account_json('keys.json')

table_id = "single-odyssey-349606.ds_from_python.emp_py"

job_config = bigquery.LoadJobConfig(
    schema=[
        bigquery.SchemaField("name", "STRING"),
        bigquery.SchemaField("company", "STRING"),
		bigquery.SchemaField("joiningdate", "DATE")
    ],
	source_format=bigquery.SourceFormat.CSV, skip_leading_rows=1, autodetect=True,
)
file_path=r'employee.csv'
source_file = open(file_path, "rb")
job = client.load_table_from_file(source_file, table_id, job_config=job_config)

job.result()  # Waits for the job to complete.

table = client.get_table(table_id)  # Make an API request.