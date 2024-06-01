terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "5.31.1"
    }
  }
}

provider "google" {
  credentials="./keys/creds.json"
  project = "daring-diode-425119-s0"
  region  = "us-central1"
}

resource "google_storage_bucket" "auto-expire" {
  name          = "daring-diode-425119-s0-terra-bucket"
  location      = "US"
  force_destroy = true

  lifecycle_rule {
    condition {
      age = 1
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