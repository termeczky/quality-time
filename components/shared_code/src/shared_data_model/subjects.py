"""Data model subjects."""

from .meta.subject import Subject

SUBJECTS = {
    "development_environment": Subject(
        name="Development environment",
        description="A software development and/or maintenance environment, consisting of infrastructure, pipelines, "
        "and tools needed to build, test, and deploy software.",
        subjects={
            "development_environment_pipeline": Subject(
                name="Pipeline and/or job",
                description="One or more pipelines and/or jobs to build, test, and deploy software.",
                metrics=[
                    "failed_jobs",
                    "job_runs_within_time_period",
                    "pipeline_duration",
                    "unused_jobs",
                ],
            ),
            "development_environment_tool": Subject(
                name="Development tool",
                description="A software development and/or maintenance tool.",
                metrics=[
                    "source_up_to_dateness",
                    "source_version",
                    "software_version",
                ],
            ),
        },
    ),
    "process": Subject(
        name="Process",
        description="A software development, maintenance, and/or operations process.",
        subjects={
            "process_backlog": Subject(
                name="Backlog management",
                description="A process to manage the product backlog.",
                metrics=["user_story_points", "velocity"],
            ),
            "process_development": Subject(
                name="Development process",
                description="A software development and/or maintenance process.",
                metrics=[
                    "merge_requests",
                    "pipeline_duration",
                    "unmerged_branches",
                ],
            ),
            "process_defect": Subject(
                name="Defect management",
                description="A process to manage known defects.",
                metrics=[
                    "issues",
                ],
            ),
            "process_operations": Subject(
                name="Operations process",
                description="A process to manage software in production.",
                metrics=[
                    "average_issue_lead_time",
                    "change_failure_rate",
                    "job_runs_within_time_period",
                ],
            ),
            "process_technical_debt": Subject(
                name="Technical debt management",
                description="A process to manage outstanding technical debt.",
                metrics=[
                    "dependencies",
                    "issues",
                    "remediation_effort",
                    "suppressed_violations",
                    "todo_and_fixme_comments",
                ],
            ),
            "process_test": Subject(
                name="Test process",
                description="A software test process.",
                metrics=[
                    "manual_test_duration",
                    "manual_test_execution",
                    "tests",
                    "test_cases",
                    "uncovered_branches",
                    "uncovered_lines",
                ],
            ),
        },
        metrics=[
            "time_remaining",
        ],
    ),
    "report": Subject(
        name="Quality report",
        description="A software quality report.",
        metrics=["metrics", "missing_metrics"],
    ),
    "software": Subject(
        name="Software",
        description="A custom software application or component.",
        subjects={
            "software_source_code": Subject(
                name="Software source code",
                description="Custom software source code.",
                metrics=[
                    "commented_out_code",
                    "complex_units",
                    "dependencies",
                    "duplicated_lines",
                    "loc",
                    "long_units",
                    "many_parameters",
                    "software_version",
                    "security_warnings",
                    "violations",
                ],
            ),
            "software_tests": Subject(
                name="Software tests",
                description="A test suite for custom software.",
                metrics=[
                    "performancetest_duration",
                    "performancetest_stability",
                    "tests",
                    "test_cases",
                    "uncovered_branches",
                    "uncovered_lines",
                ],
            ),
            "software_documentation": Subject(
                name="Software documentation",
                description="Documentation of custom software.",
                metrics=[
                    "source_up_to_dateness",
                    "time_remaining",
                ],
            ),
        },
        metrics=[
            "scalability",
            "slow_transactions",
        ],
    ),
    "team": Subject(
        name="Team",
        description="A team developing, maintaining and/or operation custom software.",
        metrics=["sentiment"],
    ),
}
