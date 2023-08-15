# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command_group(
    "connectedmachine extension image",
)
class __CMDGroup(AAZCommandGroup):
    """Manage VM extension metadata available for Azure Arc-Enabled Servers.
    """
    pass


__all__ = ["__CMDGroup"]