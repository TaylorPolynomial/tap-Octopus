"""Stream type classes for tap-octopus."""

from __future__ import annotations

import sys
import typing as t

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_octopus.client import OctopusStream

if sys.version_info >= (3, 9):
    import importlib.resources as importlib_resources
else:
    import importlib_resources


# TODO: Delete this is if not using json files for schema definition
SCHEMAS_DIR = importlib_resources.files(__package__) / "schemas"
# TODO: - Override `UsersStream` and `GroupsStream` with your own stream definition.
#       - Copy-paste as many times as needed to create multiple stream types.


class ElectricStream(OctopusStream):
    """Define custom stream."""

    name = "electric"
    path = "electricity-meter-points/1591011973471/meters/21E5385523/consumption"
    # primary_keys: t.ClassVar[list[str]] = ["id"]
    replication_key = "interval_end"
    is_sorted = True 
    is_timestamp_replication_key = True
    # Optionally, you may also use `schema_filepath` in place of `schema`:
    # schema_filepath = SCHEMAS_DIR / "users.json"  # noqa: ERA001
    schema = th.PropertiesList(
        th.Property(
            "consumption", 
            th.NumberType
        ),
        th.Property(
            "interval_start",
            th.DateTimeType
        ),
        th.Property(
            "interval_end",
            th.DateTimeType
        ),
    ).to_dict()


class GasStream(OctopusStream):
    """Define custom stream."""

    name = "gas"
    path = "gas-meter-points/1919231705/meters/E6E00207622020/consumption"
    # primary_keys: t.ClassVar[list[str]] = ["id"]
    replication_key = "interval_end"
    is_sorted = True 
    is_timestamp_replication_key = True
    # Optionally, you may also use `schema_filepath` in place of `schema`:
    # schema_filepath = SCHEMAS_DIR / "users.json"  # noqa: ERA001
    schema = th.PropertiesList(
        th.Property(
            "consumption", 
            th.NumberType
        ),
        th.Property(
            "interval_start",
            th.DateTimeType
        ),
        th.Property(
            "interval_end",
            th.DateTimeType
        ),
    ).to_dict()


class GroupsStream(OctopusStream):
    """Define custom stream."""

    name = "groups"
    path = "/groups"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    replication_key = "modified"
    schema = th.PropertiesList(
        th.Property("name", th.StringType),
        th.Property("id", th.StringType),
        th.Property("modified", th.DateTimeType),
    ).to_dict()
