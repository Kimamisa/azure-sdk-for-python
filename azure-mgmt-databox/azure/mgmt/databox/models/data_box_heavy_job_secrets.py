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

from .job_secrets import JobSecrets


class DataBoxHeavyJobSecrets(JobSecrets):
    """The secrets related to a databox heavy job.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param job_secrets_type: Required. Constant filled by server.
    :type job_secrets_type: str
    :ivar cabinet_pod_secrets: Contains the list of secret objects for a
     databox heavy job.
    :vartype cabinet_pod_secrets:
     list[~azure.mgmt.databox.models.DataBoxHeavySecret]
    """

    _validation = {
        'job_secrets_type': {'required': True},
        'cabinet_pod_secrets': {'readonly': True},
    }

    _attribute_map = {
        'job_secrets_type': {'key': 'jobSecretsType', 'type': 'str'},
        'cabinet_pod_secrets': {'key': 'cabinetPodSecrets', 'type': '[DataBoxHeavySecret]'},
    }

    def __init__(self, **kwargs):
        super(DataBoxHeavyJobSecrets, self).__init__(**kwargs)
        self.cabinet_pod_secrets = None
        self.job_secrets_type = 'DataBoxHeavy'
