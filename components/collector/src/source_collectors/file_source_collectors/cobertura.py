"""Cobertura coverage report collector."""

from datetime import datetime
from typing import Tuple

from defusedxml import ElementTree

from collector_utilities.type import Entities, Response, Responses, Value
from base_collectors import XMLFileSourceCollector, SourceUpToDatenessCollector


class CoberturaCoverageBaseClass(XMLFileSourceCollector):
    """Base class for Cobertura coverage collectors."""

    coverage_type = "Subclass responsibility (Cobertura has: lines, branches)"

    async def _parse_source_responses(self, responses: Responses) -> Tuple[Value, Value, Entities]:
        valid, covered = 0, 0
        for response in responses:
            tree = ElementTree.fromstring(await response.text())
            valid += int(tree.get(f"{self.coverage_type}-valid"))
            covered += int(tree.get(f"{self.coverage_type}-covered"))
        return str(valid - covered), str(valid), []


class CoberturaUncoveredLines(CoberturaCoverageBaseClass):
    """Source class to get the number of uncovered lines from Cobertura XML reports."""

    coverage_type = "lines"


class CoberturaUncoveredBranches(CoberturaCoverageBaseClass):
    """Source class to get the number of uncovered lines from Cobertura XML reports."""

    coverage_type = "branches"


class CoberturaSourceUpToDateness(XMLFileSourceCollector, SourceUpToDatenessCollector):
    """Collector to collect the Cobertura report age."""

    async def _parse_source_response_date_time(self, response: Response) -> datetime:
        tree = ElementTree.fromstring(await response.text())
        return datetime.utcfromtimestamp(int(tree.get("timestamp")) / 1000.)
