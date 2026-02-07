resource "aws_s3_bucket" "input_bucket" {
  bucket = "event-input-bucket-demo"
}

resource "aws_s3_bucket" "report_bucket" {
  bucket = "event-report-bucket-demo"
}

