import os

import aws_cdk as cdk

from cdk_regulome_dev.network_stack import NetworkStack
from cdk_regulome_dev.config import config


ENVIRONMENT = cdk.Environment(
    account=config['account'],
    region=config['region'],
)

app = cdk.App()

NetworkStack(
    app,
    'DevNetworkStack',
    env=ENVIRONMENT,
    termination_protection=True,
)

app.synth()
