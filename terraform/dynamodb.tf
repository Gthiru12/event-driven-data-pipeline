resource "aws_dynamodb_table" "event_table" {
  name         = "event-data"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "event_id"

  attribute {
    name = "event_id"
    type = "S"
  }
}

