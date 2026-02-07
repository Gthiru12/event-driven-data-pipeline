resource "aws_cloudwatch_event_rule" "daily_report" {
  name                = "daily-report-rule"
  schedule_expression = "cron(54 06 * * ? *)"
}

resource "aws_cloudwatch_event_target" "report_target" {
  rule      = aws_cloudwatch_event_rule.daily_report.name
  target_id = "report-lambda"
  arn       = aws_lambda_function.reporter.arn
}

