import pytest
import json

from cdk_regulome_dev.network_stack import NetworkStack

from aws_cdk import App
from aws_cdk import Environment

from aws_cdk.assertions import Template


ENVIRONMENT = Environment(
    account='testing',
    region='testing'
)


def test_match_with_snapshot(snapshot):
    app = App()
    stack = NetworkStack(
        app,
        'NetworkStack',
        env=ENVIRONMENT
    )
    template = Template.from_stack(stack)
    snapshot.assert_match(
        json.dumps(
            template.to_json(),
            indent=4,
            sort_keys=True
        ),
        'network_stack_template.json'
    )
