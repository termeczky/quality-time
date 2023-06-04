"""Trello source."""

from shared_data_model.meta.entity import EntityAttributeType
from shared_data_model.meta.source import Source
from shared_data_model.parameters import (
    URL,
    Days,
    MultipleChoiceParameter,
    MultipleChoiceWithAdditionParameter,
    StringParameter,
)

ALL_TRELLO_METRICS = ["issues", "source_up_to_dateness"]

ISSUE_ENTITY = {
    "name": "issue",
    "attributes": [
        {"name": "Title", "url": "url"},
        {"name": "List"},
        {"name": "Due date", "type": EntityAttributeType.DATETIME},
        {"name": "Date of last activity", "key": "date_last_activity", "type": EntityAttributeType.DATETIME},
    ],
}

INACTIVE_DAYS_PARAMETER = Days(
    name="Number of days without activity after which to consider cards inactive",
    short_name="number of days without activity",
    default_value="30",
    metrics=["issues"],
)

LISTS_TO_IGNORE_PARAMETER = MultipleChoiceWithAdditionParameter(
    name="Lists to ignore (title or id)",
    short_name="lists to ignore",
    metrics=ALL_TRELLO_METRICS,
)

CARDS_TO_COUNT_PARAMETER = MultipleChoiceParameter(
    name="Cards to count",
    short_name="cards",
    placeholder="all cards",
    values=["inactive", "overdue"],
    metrics=["issues"],
)

TRELLO = Source(
    name="Trello",
    description="Trello is a collaboration tool that organizes projects into boards.",
    url="https://trello.com",
    parameters={
        "url": URL(
            name="URL",
            validate_on=["api_key", "token"],
            default_value="https://trello.com",
            metrics=ALL_TRELLO_METRICS,
        ),
        "api_key": StringParameter(
            name="API key",
            short_name="API key",
            help_url="https://trello.com/app-key",
            metrics=ALL_TRELLO_METRICS,
        ),
        "token": StringParameter(
            name="Token",
            help_url="https://trello.com/app-key",
            metrics=ALL_TRELLO_METRICS,
        ),
        "board": StringParameter(
            name="Board (title or id)",
            short_name="board",
            help_url="https://trello.com/1/members/me/boards?fields=name",
            mandatory=True,
            metrics=ALL_TRELLO_METRICS,
        ),
        "lists_to_ignore": LISTS_TO_IGNORE_PARAMETER,
        "cards_to_count": CARDS_TO_COUNT_PARAMETER,
        "inactive_days": INACTIVE_DAYS_PARAMETER,
    },
    entities={"issues": ISSUE_ENTITY},
)
