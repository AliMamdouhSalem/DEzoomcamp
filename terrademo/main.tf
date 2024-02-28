terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "5.18.0"
    }
  }
}

provider "google" {
  credentials = "./keys/my-creds.json"
  project     = "dezoomcamp-414922"
  region      = "us-central1"
}

resource "google_storage_bucket" "demo-bucket" {
  name          = "dezoomcamp-414922-terrabuck"
  location      = "US"
  force_destroy = true

  lifecycle_rule {
    condition {
      age = 3
    }
    action {
      type = "Delete"
    }
  }

  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}

resource "google_bigquery_dataset" "demo-dataset" {
  dataset_id = "dezoomcamp414922bqdataset"
  delete_contents_on_destroy = true
}