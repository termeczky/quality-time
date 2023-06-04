"""Cobertura source."""

from shared_data_model.meta.source import Source
from shared_data_model.parameters import access_parameters

from .jenkins import JENKINS_TOKEN_DOCS, jenkins_access_parameters

COBERTURA = Source(
    name="Cobertura",
    description="Cobertura is a free Java tool that calculates the percentage of code accessed by tests.",
    url="https://cobertura.github.io/cobertura/",
    parameters=access_parameters(
        [
            "source_up_to_dateness",
            "source_version",
            "uncovered_branches",
            "uncovered_lines",
        ],
        source_type="Cobertura report",
        source_type_format="XML",
    ),
)

COBERTURA_JENKINS_PLUGIN = Source(
    name="Cobertura Jenkins plugin",
    description="Jenkins plugin for Cobertura, a free Java tool that calculates the percentage of code accessed "
    "by tests.",
    documentation={
        "source_up_to_dateness": JENKINS_TOKEN_DOCS,
        "uncovered_branches": JENKINS_TOKEN_DOCS,
        "uncovered_lines": JENKINS_TOKEN_DOCS,
    },
    url="https://plugins.jenkins.io/cobertura/",
    parameters=jenkins_access_parameters(
        ["source_up_to_dateness", "uncovered_branches", "uncovered_lines"],
        kwargs={
            "url": {
                "help": "URL to a Jenkins job with a coverage report generated by the Cobertura plugin. For example, "
                "'https://jenkins.example.org/job/cobertura' or https://jenkins.example.org/job/cobertura/job/master' "
                "in case of a pipeline job.",
            },
        },
    ),
)
