"""Octopus tap class."""

from __future__ import annotations

from singer_sdk import Tap
from singer_sdk import typing as th  # JSON schema typing helpers

# TODO: Import your custom stream types here:
from tap_octopus import streams


class TapOctopus(Tap):
    """Octopus tap class."""

    name = "tap-octopus"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "granularity",
            th.StringType,
            required=False,
            secret=False,  # Flag config as protected.
            description="The token to authenticate against the API service",
        ),
    ).to_dict()

    def discover_streams(self) -> list[streams.OctopusStream]:
        """Return a list of discovered streams.

        Returns:
            A list of discovered streams.
        """
        return [

            streams.ElectricStream(self),
            streams.GasStream(self)
        ]


if __name__ == "__main__":
    TapOctopus.cli()
