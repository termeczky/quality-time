"""Data model subjects."""

from .meta.subject import Subjects

SUBJECTS = Subjects.parse_obj(
    {
        "ci": {
            "name": "CI-environment",
            "description": "A continuous integration environment.",
            "metrics": [
                "failed_jobs",
                "job_runs_within_time_period",
                "merge_requests",
                "performancetest_duration",
                "software_version",
                "source_up_to_dateness",
                "source_version",
                "unmerged_branches",
                "unused_jobs",
            ],
        },
        "process": {
            "name": "Process",
            "description": "A software development and/or maintenance process.",
            "metrics": [
                "average_issue_lead_time",
                "issues",
                "manual_test_duration",
                "manual_test_execution",
                "merge_requests",
                "source_up_to_dateness",
                "time_remaining",
                "unmerged_branches",
                "user_story_points",
                "velocity",
                "sentiment",
            ],
        },
        "report": {
            "name": "Quality report",
            "description": "A software quality report.",
            "metrics": ["metrics", "missing_metrics"],
        },
        "software": {
            "name": "Software",
            "description": "A custom software application or component.",
            "metrics": [
                "accessibility",
                "average_issue_lead_time",
                "commented_out_code",
                "complex_units",
                "dependencies",
                "duplicated_lines",
                "issues",
                "job_runs_within_time_period",
                "loc",
                "long_units",
                "manual_test_duration",
                "manual_test_execution",
                "many_parameters",
                "merge_requests",
                "performancetest_duration",
                "performancetest_stability",
                "remediation_effort",
                "scalability",
                "security_warnings",
                "slow_transactions",
                "software_version",
                "source_up_to_dateness",
                "source_version",
                "suppressed_violations",
                "test_cases",
                "tests",
                "uncovered_branches",
                "uncovered_lines",
                "unmerged_branches",
                "user_story_points",
                "violations",
            ],
        },
    },
)