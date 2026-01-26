variable "project_id" {
  description = "ZoomCamp GCP Project"
  type        = string
  default     = "dtc-de-course-485514"
}

variable "credentials_file_path" {
  description = "Path to GCP credentials JSON file"
  type        = string
  default     = "./keys/dtc-de-course-485514-1f277335332d.json"
}

variable "location" {
  description = "GCP location"
  type        = string
  default     = "US"
}

variable "region" {
  description = "GCP region"
  type        = string
  default     = "us-central1"
}

variable "bucket_name" {
  description = "The name of the GCS bucket to create"
  type        = string
  default     = "dtc-de-course-bucket-485514"
}

variable "dataset_name" {
  description = "The name of the BigQuery dataset to create"
  type        = string
  default     = "dtc_dataset"
}