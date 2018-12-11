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

from msrest.serialization import Model


class ChangeNotReimportedDelta(Model):
    """The delta in a change that is not re-imported.

    :param anchor: The anchor.
    :type anchor: str
    :param dn_attributes: The delta attributes for distinguished names.
    :type dn_attributes:
     list[~azure.mgmt.adhybridhealthservice.models.AttributeDelta]
    :param attributes: The attributes.
    :type attributes:
     list[~azure.mgmt.adhybridhealthservice.models.AttributeDelta]
    :param operation_type: The operation type. Possible values include:
     'Undefined', 'None', 'Add', 'Replace', 'Update', 'Delete', 'Obsolete',
     'DeleteAdd'
    :type operation_type: str or
     ~azure.mgmt.adhybridhealthservice.models.DeltaOperationType
    """

    _attribute_map = {
        'anchor': {'key': 'anchor', 'type': 'str'},
        'dn_attributes': {'key': 'dnAttributes', 'type': '[AttributeDelta]'},
        'attributes': {'key': 'attributes', 'type': '[AttributeDelta]'},
        'operation_type': {'key': 'operationType', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ChangeNotReimportedDelta, self).__init__(**kwargs)
        self.anchor = kwargs.get('anchor', None)
        self.dn_attributes = kwargs.get('dn_attributes', None)
        self.attributes = kwargs.get('attributes', None)
        self.operation_type = kwargs.get('operation_type', None)
