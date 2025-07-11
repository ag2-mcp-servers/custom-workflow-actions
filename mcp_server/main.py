# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-29T03:32:45+00:00



import argparse
import json
import os
from typing import *
from typing import Optional, Union

from autogen.mcp.mcp_proxy import MCPProxy
from autogen.mcp.mcp_proxy.security import (
    APIKeyHeader,
    APIKeyQuery,
    BaseSecurity,
    UnsuportedSecurityStub,
)
from fastapi import Path

from models import (
    ActionFunction,
    ActionFunctionIdentifier,
    ActionRevision,
    BatchInputCallbackCompletionBatchRequest,
    CallbackCompletionRequest,
    CollectionResponseActionFunctionIdentifierNoPaging,
    CollectionResponseActionRevisionForwardPaging,
    CollectionResponseExtensionActionDefinitionForwardPaging,
    Error,
    ExtensionActionDefinition,
    ExtensionActionDefinitionInput,
    ExtensionActionDefinitionPatch,
    FunctionType,
)

app = MCPProxy(
    description='Create custom workflow actions',
    title='Custom Workflow Actions',
    version='v4',
    servers=[{'url': 'https://api.hubapi.com/'}],
)


@app.post(
    '/automation/v4/actions/callbacks/complete',
    description=""" Completes the given action callbacks. """,
    tags=['callback_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
        APIKeyQuery(name="hapikey"),
        APIKeyHeader(name="private-app-legacy"),
    ],
)
def post__automation_v4_actions_callbacks_complete_complete_batch(
    body: BatchInputCallbackCompletionBatchRequest,
):
    """
    Complete a batch of callbacks
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/automation/v4/actions/callbacks/{callbackId}/complete',
    description=""" Completes the given action callback. """,
    tags=['callback_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
        APIKeyQuery(name="hapikey"),
        APIKeyHeader(name="private-app-legacy"),
    ],
)
def complete_callback(
    callback_id: str = Path(..., alias='callbackId'),
    body: CallbackCompletionRequest = ...,
):
    """
    Complete a callback
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/automation/v4/actions/{appId}',
    description=""" Returns a list of all custom workflow actions. """,
    tags=['custom_action_management', 'custom_action_function_management'],
    security=[
        APIKeyQuery(name="hapikey"),
    ],
)
def get__automation_v4_actions__app_id__get_page(
    limit: Optional[int] = None,
    after: Optional[str] = None,
    archived: Optional[bool_aliased] = False,
    app_id: int = Path(..., alias='appId'),
):
    """
    Get all custom actions
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/automation/v4/actions/{appId}',
    description=""" Creates a new custom workflow action. """,
    tags=['custom_action_management', 'custom_action_function_management'],
    security=[
        APIKeyQuery(name="hapikey"),
    ],
)
def post__automation_v4_actions__app_id__create(
    app_id: int = Path(..., alias='appId'), body: ExtensionActionDefinitionInput = ...
):
    """
    Create new custom action
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.delete(
    '/automation/v4/actions/{appId}/{definitionId}',
    description=""" Archives a single custom workflow action with the specified ID. Workflows that currently use this custom action will stop attempting to execute the action, and all future executions will be marked as a failure. """,
    tags=['custom_action_management', 'custom_action_function_management'],
    security=[
        APIKeyQuery(name="hapikey"),
    ],
)
def delete__automation_v4_actions__app_id___definition_id__archive(
    definition_id: str = Path(..., alias='definitionId'),
    app_id: int = Path(..., alias='appId'),
):
    """
    Archive a custom action
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/automation/v4/actions/{appId}/{definitionId}',
    description=""" Returns a single custom workflow action with the specified ID. """,
    tags=['custom_action_management', 'custom_action_function_management'],
    security=[
        APIKeyQuery(name="hapikey"),
    ],
)
def get__automation_v4_actions__app_id___definition_id__get_by_id(
    definition_id: str = Path(..., alias='definitionId'),
    archived: Optional[bool_aliased] = False,
    app_id: int = Path(..., alias='appId'),
):
    """
    Get a custom action
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.patch(
    '/automation/v4/actions/{appId}/{definitionId}',
    description=""" Updates a custom workflow action with new values for the specified fields. """,
    tags=['custom_action_management', 'custom_action_function_management'],
    security=[
        APIKeyQuery(name="hapikey"),
    ],
)
def patch__automation_v4_actions__app_id___definition_id__update(
    definition_id: str = Path(..., alias='definitionId'),
    app_id: int = Path(..., alias='appId'),
    body: ExtensionActionDefinitionPatch = ...,
):
    """
    Update a custom action
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/automation/v4/actions/{appId}/{definitionId}/functions',
    description=""" Returns a list of all functions that are associated with the given custom workflow action. """,
    tags=['custom_action_function_management', 'custom_action_management'],
    security=[
        APIKeyQuery(name="hapikey"),
    ],
)
def get_custom_action_functions(
    definition_id: str = Path(..., alias='definitionId'),
    app_id: int = Path(..., alias='appId'),
):
    """
    Get all custom action functions
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.delete(
    '/automation/v4/actions/{appId}/{definitionId}/functions/{functionType}',
    description=""" Delete a function for a custom workflow action. This will remove the function itself as well as removing the association between the function and the custom action. This can't be undone. """,
    tags=['custom_action_management', 'custom_action_function_management'],
    security=[
        APIKeyQuery(name="hapikey"),
    ],
)
def delete_custom_action_function(
    definition_id: str = Path(..., alias='definitionId'),
    function_type: FunctionType = Path(..., alias='functionType'),
    app_id: int = Path(..., alias='appId'),
):
    """
    Delete a custom action function
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/automation/v4/actions/{appId}/{definitionId}/functions/{functionType}',
    description=""" Returns the given function for a custom workflow action. """,
    tags=['custom_action_function_management', 'custom_action_management'],
    security=[
        APIKeyQuery(name="hapikey"),
    ],
)
def get_custom_action_function(
    definition_id: str = Path(..., alias='definitionId'),
    function_type: FunctionType = Path(..., alias='functionType'),
    app_id: int = Path(..., alias='appId'),
):
    """
    Get a custom action function
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.put(
    '/automation/v4/actions/{appId}/{definitionId}/functions/{functionType}',
    description=""" Creates or replaces a function for a custom workflow action. """,
    tags=['custom_action_management', 'custom_action_function_management'],
    security=[
        APIKeyQuery(name="hapikey"),
    ],
)
def create_or_replace_custom_action_function(
    definition_id: str = Path(..., alias='definitionId'),
    function_type: FunctionType = Path(..., alias='functionType'),
    app_id: int = Path(..., alias='appId'),
):
    """
    Create or replace a custom action function
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.delete(
    '/automation/v4/actions/{appId}/{definitionId}/functions/{functionType}/{functionId}',
    description=""" Delete a function for a custom workflow action. This will remove the function itself as well as removing the association between the function and the custom action. This can't be undone. """,
    tags=['custom_action_management', 'custom_action_function_management'],
    security=[
        APIKeyQuery(name="hapikey"),
    ],
)
def remove_custom_action_function(
    definition_id: str = Path(..., alias='definitionId'),
    function_type: FunctionType = Path(..., alias='functionType'),
    function_id: str = Path(..., alias='functionId'),
    app_id: int = Path(..., alias='appId'),
):
    """
    Delete a custom action function
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/automation/v4/actions/{appId}/{definitionId}/functions/{functionType}/{functionId}',
    description=""" Returns the given function for a custom workflow action. """,
    tags=['custom_action_function_management', 'custom_action_management'],
    security=[
        APIKeyQuery(name="hapikey"),
    ],
)
def get_custom_action_function_by_id(
    definition_id: str = Path(..., alias='definitionId'),
    function_type: FunctionType = Path(..., alias='functionType'),
    function_id: str = Path(..., alias='functionId'),
    app_id: int = Path(..., alias='appId'),
):
    """
    Get a custom action function
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.put(
    '/automation/v4/actions/{appId}/{definitionId}/functions/{functionType}/{functionId}',
    description=""" Creates or replaces a function for a custom workflow action. """,
    tags=['custom_action_management', 'custom_action_function_management'],
    security=[
        APIKeyQuery(name="hapikey"),
    ],
)
def update_or_replace_custom_action_function(
    definition_id: str = Path(..., alias='definitionId'),
    function_type: FunctionType = Path(..., alias='functionType'),
    function_id: str = Path(..., alias='functionId'),
    app_id: int = Path(..., alias='appId'),
):
    """
    Create or replace a custom action function
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/automation/v4/actions/{appId}/{definitionId}/revisions',
    description=""" Returns a list of revisions for a custom workflow action. """,
    tags=['custom_action_revision_management', 'custom_action_management'],
    security=[
        APIKeyQuery(name="hapikey"),
    ],
)
def get_custom_action_revisions(
    definition_id: str = Path(..., alias='definitionId'),
    limit: Optional[int] = None,
    after: Optional[str] = None,
    app_id: int = Path(..., alias='appId'),
):
    """
    Get all revisions for a custom action
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/automation/v4/actions/{appId}/{definitionId}/revisions/{revisionId}',
    description=""" Returns the given version of a custom workflow action. """,
    tags=['custom_action_revision_management', 'custom_action_management'],
    security=[
        APIKeyQuery(name="hapikey"),
    ],
)
def get_custom_action_revision_by_id(
    definition_id: str = Path(..., alias='definitionId'),
    revision_id: str = Path(..., alias='revisionId'),
    app_id: int = Path(..., alias='appId'),
):
    """
    Get a revision for a custom action
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MCP Server")
    parser.add_argument(
        "transport",
        choices=["stdio", "sse", "streamable-http"],
        help="Transport mode (stdio, sse or streamable-http)",
    )
    args = parser.parse_args()

    if "CONFIG_PATH" in os.environ:
        config_path = os.environ["CONFIG_PATH"]
        app.load_configuration(config_path)

    if "CONFIG" in os.environ:
        config = os.environ["CONFIG"]
        app.load_configuration_from_string(config)

    if "SECURITY" in os.environ:
        security_params = BaseSecurity.parse_security_parameters_from_env(
            os.environ,
        )

        app.set_security_params(security_params)

    mcp_settings = json.loads(os.environ.get("MCP_SETTINGS", "{}"))

    app.get_mcp(**mcp_settings).run(transport=args.transport)
