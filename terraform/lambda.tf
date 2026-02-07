resource "aws_lambda_function" "processor" {
  function_name = "event-processor"
  role          = aws_iam_role.lambda_role.arn
  handler       = "processor.lambda_handler"
  runtime       = "python3.10"

  filename = "../lambda/processor.zip"
}

resource "aws_lambda_function" "reporter" {
  function_name = "daily-reporter"
  role          = aws_iam_role.lambda_role.arn
  handler       = "reporter.lambda_handler"
  runtime       = "python3.10"

  filename = "../lambda/reporter.zip"
}
