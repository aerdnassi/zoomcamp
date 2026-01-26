terraform {
  required_providers {
    google = {
      source = "hashicorp/google"
      version = "6.8.0"
    }
  }
}

provider "google" {
  credentials = file(var.credentials_file_path)
  project = var.project_id
  region  = var.region
}


resource "google_storage_bucket" "data-lake-bucket" {
  name          = var.bucket_name
  location      = var.location

  # Optional, but recommended settings:
  storage_class = "STANDARD"
  uniform_bucket_level_access = true

  versioning {
    enabled     = true
  }

  lifecycle_rule {
    action {
      type = "Delete"
    }
    condition {
      age = 30  // days
    }
  }

  force_destroy = true
}


resource "google_bigquery_dataset" "dataset" {
  dataset_id = var.dataset_name
  project    = var.project_id
  location   = var.location
}