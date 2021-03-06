#!/usr/bin/env python3
# thoth-storages
# Copyright(C) 2018, 2019, 2020 Fridolin Pokorny
#
# This program is free software: you can redistribute it and / or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

"""Storage and database adapters for Thoth."""

from .advisers import AdvisersResultsStore
from .advisers_cache import AdvisersCacheStore
from .analyses import AnalysisResultsStore
from .analyses_by_digest import AnalysisByDigest
from .analyses_cache import AnalysesCacheStore
from .buildlogs import BuildLogsStore
from .buildlogs_analyses import BuildLogsAnalysisResultsStore
from .buildlogs_analyses_cache import BuildLogsAnalysesCacheStore
from .ceph import CephStore
from .dependency_monkey_reports import DependencyMonkeyReportsStore
from .graph import GraphDatabase
from .graph_backup import GraphBackupStore
from .inspections import InspectionResultsStore
from .inspections import InspectionBuildsStore
from .inspections import InspectionStore
from .package_analyses import PackageAnalysisResultsStore
from .provenance import ProvenanceResultsStore
from .provenance_cache import ProvenanceCacheStore
from .result_schema import RESULT_SCHEMA
from .si_bandit import SIBanditResultsStore
from .si_cloc import SIClocResultsStore
from .solvers import SolverResultsStore
from .sync import sync_adviser_documents
from .sync import sync_analysis_documents
from .sync import sync_dependency_monkey_documents
from .sync import sync_documents
from .sync import sync_inspection_documents
from .sync import sync_package_analysis_documents
from .sync import sync_provenance_checker_documents
from .sync import sync_solver_documents


__name__ = "thoth-storages"
__version__ = "0.23.2"
