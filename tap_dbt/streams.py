"""Stream class for tap-dbt."""

from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, cast
import singer_sdk.typing as th
import requests
from singer_sdk.authenticators import APIAuthenticatorBase, SimpleAuthenticator
from singer_sdk.streams import RESTStream
from singer_sdk.helpers.jsonpath import extract_jsonpath
import logging
SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")


class DBTStream(RESTStream):
    """dbt stream class."""

    # url_base = "https://cloud.getdbt.com/api/v2"
    primary_keys = ["id"]
    replication_key = None
    response_jsonpath = "$.data[*]"


    @property
    def url_base(self):
        return self.config.get('base_url', 'https://cloud.getdbt.com/api/v2')

    @property
    def http_headers(self) -> dict:
        headers = super().http_headers
        headers["Accept"] = "application/json"
        return headers

    @property
    def authenticator(self) -> APIAuthenticatorBase:
        return SimpleAuthenticator(
            stream=self,
            auth_headers={
                "Authorization": f"Token {self.config.get('api_key')}",
            },
        )



class AccountBasedStream(DBTStream):

    def ttt(self):
        pass
    # @property
    # def partitions(self) -> List[dict]:
    #     """Return a list of partition key dicts (if applicable), otherwise None."""

    #     if "{account_id}" in self.path:
    #         return [{"account_id": id} for id in cast(list, self.config["account_ids"])]
    #     raise ValueError(
    #         "Could not detect partition type for dbt stream "
    #         f"'{self.name}' ({self.path}). "
    #         "Expected a URL path containing '{account_id}'. "
    #     )


class AccountsStream(AccountBasedStream):
    name = "accounts"
    path = "/accounts/{account_id}"
    schema_filepath = SCHEMAS_DIR / "accounts.json"

    # def parse_response(self, response: requests.Response) -> Iterable[dict]:
    #     yield response.json()["data"]


class JobsStream(AccountBasedStream):
    name = "jobs"
    path = "/accounts/{account_id}/jobs"
    schema_filepath = SCHEMAS_DIR / "jobs.json"

    def get_url_params(
        self,
        partition: Optional[dict],
        next_page_token: int,
    ) -> Dict[str, Any]:
        return {"order_by": "updated_at"}


class ProjectsStream(AccountBasedStream):
    name = "projects"
    path = "/accounts/{account_id}/projects"

    schema_filepath = SCHEMAS_DIR / "projects.json"



class RunsStream(AccountBasedStream):
    name = "runs"
    path = "/accounts/85/runs"
    # schema_filepath = SCHEMAS_DIR / "runs.json"

    schema = th.PropertiesList(
        th.Property("name", th.StringType),
        th.Property(
            "id",
            th.IntegerType,
            description="The user's system ID",
        ),
        th.Property(
            "git_branch",
            th.StringType,
            description="The user's email address",
        ),
        th.Property("git_sha", th.StringType),
        th.Property("dbt_version", th.StringType),
        th.Property(
            "updated_at",
            th.StringType,
            description="State name in ISO 3166-2 format",
        ),
        th.Property("zip", th.StringType),
    ).to_dict()


    response_jsonpath = "$.data[*]"
    page_size = 100

    def get_url_params(
        self,
        partition: Optional[dict],
        next_page_token: int,
    ) -> Dict[str, Any]:

        return {
            "order_by": "updated_at",
            "limit": self.page_size,
            "offset": next_page_token,
        }

    def get_next_page_token(
        self, response: requests.Response, previous_token: Optional[Any]
    ) -> Any:
        previous_token = previous_token or 0
        data = response.json()

        if len(data["data"]):
            return previous_token + self.page_size

        return None

    def parse_response(self, response: requests.Response) -> Iterable[dict]:
        """Parse the response and return an iterator of result records.
        Args:
            response: A raw `requests.Response`_ object.
        Yields:
            One item for every item found in the response.
        .. _requests.Response:
            https://requests.readthedocs.io/en/latest/api/#requests.Response
        """
        logger = logging.getLogger()
        logger.info("***** UNPARSED RESPONSE *****")
        logger.info(response.json())
        logger.info("***** PARSED RESPONSE *****")
        logger.info(list(extract_jsonpath(self.records_jsonpath, input=response.json())))

        yield from extract_jsonpath(self.records_jsonpath, input=response.json())