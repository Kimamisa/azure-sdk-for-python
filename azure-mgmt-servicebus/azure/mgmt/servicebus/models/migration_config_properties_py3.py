# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .resource_py3 import Resource


class MigrationConfigProperties(Resource):
    """Single item in List or Get Migration Config operation.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource Id
    :vartype id: str
    :ivar name: Resource name
    :vartype name: str
    :ivar type: Resource type
    :vartype type: str
    :ivar provisioning_state: Provisioning state of Migration Configuration
    :vartype provisioning_state: str
    :ivar pending_replication_operations_count: Number of entities pending to
     be replicated.
    :vartype pending_replication_operations_count: long
    :param target_namespace: Required. Existing premium Namespace ARM Id name
     which has no entities, will be used for migration
    :type target_namespace: str
    :param post_migration_name: Required. Name to access Standard Namespace
     after migration
    :type post_migration_name: str
    :ivar migration_state: State in which Standard to Premium Migration is,
     possible values : Unknown, Reverting, Completing, Initiating, Syncing,
     Active
    :vartype migration_state: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'provisioning_state': {'readonly': True},
        'pending_replication_operations_count': {'readonly': True},
        'target_namespace': {'required': True},
        'post_migration_name': {'required': True},
        'migration_state': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'pending_replication_operations_count': {'key': 'properties.pendingReplicationOperationsCount', 'type': 'long'},
        'target_namespace': {'key': 'properties.targetNamespace', 'type': 'str'},
        'post_migration_name': {'key': 'properties.postMigrationName', 'type': 'str'},
        'migration_state': {'key': 'properties.migrationState', 'type': 'str'},
    }

    def __init__(self, *, target_namespace: str, post_migration_name: str, **kwargs) -> None:
        super(MigrationConfigProperties, self).__init__(**kwargs)
        self.provisioning_state = None
        self.pending_replication_operations_count = None
        self.target_namespace = target_namespace
        self.post_migration_name = post_migration_name
        self.migration_state = None
