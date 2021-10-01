resource "google_redis_instance" "redis-from-tf" {
  name = "redis-from-tf"
  memory_size_gb = 1
  tier = "BASIC"

  location_id = "asia-southeast1-a"
  authorized_network = "default"

  redis_version = "REDIS_5_0"
  display_name = "Redis Instance from terraform"

}