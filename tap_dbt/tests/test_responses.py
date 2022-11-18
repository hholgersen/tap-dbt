import json
from unittest import mock
from tap_dbt.streams import AccountsStream, RunsStream, ProjectsStream, JobsStream
from tap_dbt.tap import TapDBT
from singer_sdk._singerlib import Catalog
from unittest.mock import patch

from .config.responses import (
    RUNS,
    ACCOUNT,
    PROJECTS,
    JOBS
)

SAMPLE_CONFIG = {
    "api_key": "xyz",
    "account_ids": ["1001"],
    "base_url": "https://example.com"
}


@patch("singer_sdk.streams.rest.RESTStream._request")
def test_get_records(mocked_response):
    mocked_response.json.return_value = RUNS
    tap1 = TapDBT(SAMPLE_CONFIG)
    stream1 = RunsStream(tap=tap1, name="abc")

    records = stream1.get_records({})
    assert len(list(records)) == 2

