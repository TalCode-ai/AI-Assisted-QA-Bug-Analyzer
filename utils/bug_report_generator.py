from datetime import datetime
from pathlib import Path
from utils.ai_bug_analyzer import analyze_error


def generate_bug_report(
        test_name,
        error_message,
        screenshot_path,
        current_url="N/A",
        browser_name="N/A",
        folder_path="reports/bug_reports"
):
    reports_folder = Path(folder_path)
    reports_folder.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    file_name = f"{test_name}_{timestamp}.txt"
    file_path = reports_folder / file_name
    ai_analysis = analyze_error(error_message)

    report_content = f"""
Bug Report
==========

Test Name:
{test_name}

Status:
Failed
Browser:
{browser_name}

Current URL:
{current_url}

Error Message:
{error_message}

AI Analysis:
{ai_analysis}

Screenshot:
{screenshot_path}

Created At:
{timestamp}
"""

    file_path.write_text(report_content, encoding="utf-8")

    return str(file_path)