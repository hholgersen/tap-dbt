"""dbt tap class."""

from typing import List

from singer_sdk import Stream, Tap
from singer_sdk.helpers._classproperty import classproperty
from singer_sdk.typing import ArrayType, PropertiesList, Property, StringType

from tap_dbt.streams import AccountsStream, JobsStream, ProjectsStream, RunsStream

TAP_NAME = "tap-dbt"
STREAM_TYPES = [
    AccountsStream,
    JobsStream,
    ProjectsStream,
    RunsStream,
]


class TapDBT(Tap):
    """Singer tap for the dbt Cloud API."""

    name = TAP_NAME

    @classproperty
    def config_jsonschema(cls):
        return PropertiesList(
            Property(
                "api_key",
                StringType,
                description="API key for the dbt Cloud API",
                required=True,
            ),
            Property(
                "account_ids",
                ArrayType(StringType),
                description="dbt Cloud account IDs",
                required=True,
            ),
            Property(
                "base_url",
                StringType,
                description="Base URL for the dbt Cloud API",
                default="https://cloud.getdbt.com/api/v2",
            ),
            Property(
                "user_agent",
                StringType,
                default=f"{cls.name}/{cls.plugin_version} {cls.__doc__}",
                description="User-Agent to make requests with",
            ),
        ).to_dict()

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]


cli = TapDBT.cli
