# THIS FILE IS AUTOMATICALLY GENERATED.
# Disclaimer: Please test this file before using in production.
"""
Generated blueprint DSL (.py)
"""

import json  # no_qa
import os  # no_qa

from calm.dsl.builtins import *  # no_qa


# Secret Variables
BP_CRED_Cred_OS_KEY = read_local_file("BP_CRED_Cred_OS_KEY")
BP_CRED_fortigate_PASSWORD = read_local_file("BP_CRED_fortigate_PASSWORD")
Profile_Default_variable_phpIPAM_token = read_local_file(
    "Profile_Default_variable_phpIPAM_token"
)

# Credentials
BP_CRED_Cred_OS = basic_cred(
    "centos",
    BP_CRED_Cred_OS_KEY,
    name="Cred_OS",
    type="KEY",
    default=True,
)
BP_CRED_fortigate = basic_cred(
    "admin",
    BP_CRED_fortigate_PASSWORD,
    name="fortigate",
    type="PASSWORD",
)


class Service1(Service):

    pass


class webservercalm_timeResources(AhvVmResources):

    memory = 2
    vCPUs = 2
    cores_per_vCPU = 1
    disks = [AhvVmDisk.Disk.Scsi.cloneFromImageService("CentOS7", bootable=True)]
    nics = [AhvVmNic.NormalNic.ingress("@@{subnet_ref.uuid}@@")]

    guest_customization = AhvVmGC.CloudInit(
        filename=os.path.join("specs", "webservercalm_time_cloud_init_data.yaml")
    )


class webservercalm_time(AhvVm):

    name = "webserver-@@{calm_time}@@"
    resources = webservercalm_timeResources
    categories = {"Backup-SLA": "Bronze"}


class Webserver(Substrate):

    os_type = "Linux"
    provider_type = "AHV_VM"
    provider_spec = webservercalm_time
    provider_spec_editables = read_spec(
        os.path.join("specs", "Webserver_create_spec_editables.yaml")
    )
    readiness_probe = readiness_probe(
        connection_type="SSH",
        disabled=False,
        retries="5",
        connection_port=22,
        address="@@{platform.status.resources.nic_list[0].ip_endpoint_list[0].ip}@@",
        delay_secs="60",
        credential=ref(BP_CRED_Cred_OS),
    )

    @action
    def __pre_create__():

        CalmTask.SetVariable.escript(
            name="FetchSubnetID",
            filename=os.path.join(
                "scripts",
                "Substrate_Webserver_Action___pre_create___Task_FetchSubnetID.py",
            ),
            target=ref(Webserver),
            variables=["phpipam_subnet_id"],
        )
        CalmTask.HTTP.post(
            "https://@@{phpIPAM_address}@@/api/Calm/addresses/first_free/@@{phpipam_subnet_id}@@/",
            body=json.dumps({"description": "@@{name}@@"}),
            headers={"Token": "@@{phpIPAM_token}@@", "Accept": "application/json"},
            secret_headers={},
            content_type="application/json",
            verify=False,
            status_mapping={200: True},
            response_paths={"vm_ip": "$.data"},
            name="FetchIPfromIPAM",
            target=ref(Webserver),
        )
        CalmTask.HTTP.post(
            "https://127.0.0.1:9440/api/nutanix/v3/subnets/list",
            body=json.dumps({}),
            headers={},
            secret_headers={},
            content_type="application/json",
            verify=False,
            status_mapping={200: True},
            response_paths={
                "subnet_uuid": '$.entities[?(@.status.name == "@@{subnet}@@")].metadata.uuid'
            },
            name="Fetch NIC UUID",
            target=ref(Webserver),
        )
        CalmTask.SetVariable.escript(
            name="Create NIC JSON",
            filename=os.path.join(
                "scripts",
                "Substrate_Webserver_Action___pre_create___Task_CreateNICJSON.py",
            ),
            target=ref(Webserver),
            variables=["subnet_ref"],
        )

    @action
    def __post_delete__():

        CalmTask.HTTP.delete(
            "https://@@{phpIPAM_address}@@/api/Calm/addresses/@@{address}@@/@@{phpipam_subnet_id}@@",
            body=json.dumps({}),
            headers={"Token": "@@{phpIPAM_token}@@", "Accept": "application/json"},
            secret_headers={},
            content_type="application/json",
            verify=False,
            status_mapping={200: True, 400: True, 500: True},
            response_paths={},
            name="Release IP",
            target=ref(Webserver),
        )


class Package1(Package):

    services = [ref(Service1)]

    @action
    def __install__():

        CalmTask.Exec.ssh(
            name="Install",
            filename=os.path.join(
                "scripts", "Package_Package1_Action___install___Task_Install.sh"
            ),
            cred=ref(BP_CRED_Cred_OS),
            target=ref(Service1),
        )
        CalmTask.Exec.ssh(
            name="Firewall",
            filename=os.path.join(
                "scripts", "Package_Package1_Action___install___Task_Firewall.sh"
            ),
            cred=ref(BP_CRED_Cred_OS),
            target=ref(Service1),
        )
        CalmTask.Exec.escript(
            name="Forti_AddIP",
            filename=os.path.join(
                "scripts", "Package_Package1_Action___install___Task_Forti_AddIP.py"
            ),
            target=ref(Service1),
        )
        CalmTask.Exec.escript(
            name="Forti_UpdateGroup",
            filename=os.path.join(
                "scripts",
                "Package_Package1_Action___install___Task_Forti_UpdateGroup.py",
            ),
            target=ref(Service1),
        )

    @action
    def __uninstall__():

        CalmTask.Exec.escript(
            name="Forti_UpdateGroup",
            filename=os.path.join(
                "scripts",
                "Package_Package1_Action___uninstall___Task_Forti_UpdateGroup.py",
            ),
            target=ref(Service1),
        )


class d5d66387_deployment(Deployment):

    min_replicas = "1"
    max_replicas = "1"
    default_replicas = "1"

    packages = [ref(Package1)]
    substrate = ref(Webserver)


class Default(Profile):

    deployments = [d5d66387_deployment]

    subnet = CalmVariable.WithOptions.FromTask(
        CalmTask.HTTP.post(
            "https://127.0.0.1:9440/api/nutanix/v3/subnets/list",
            body=json.dumps({}),
            headers={},
            secret_headers={},
            content_type="application/json",
            verify=False,
            status_mapping={200: True},
            response_paths={"subnet": "$.entities.status.name"},
            name="",
        ),
        label="",
        is_mandatory=True,
        is_hidden=False,
        description="",
    )

    fortigate_endpoint = CalmVariable.Simple(
        "10.200.100.159",
        label="",
        is_mandatory=False,
        is_hidden=True,
        runtime=False,
        description="",
    )

    phpIPAM_token = CalmVariable.Simple.Secret(
        Profile_Default_variable_phpIPAM_token,
        label="",
        is_mandatory=False,
        is_hidden=True,
        runtime=False,
        description="",
    )

    phpIPAM_address = CalmVariable.Simple(
        "10.200.100.160",
        label="",
        is_mandatory=False,
        is_hidden=True,
        runtime=False,
        description="",
    )


class LinuxWebserver(Blueprint):

    services = [Service1]
    packages = [Package1]
    substrates = [Webserver]
    profiles = [Default]
    credentials = [BP_CRED_Cred_OS, BP_CRED_fortigate]


class BpMetadata(Metadata):

    categories = {"TemplateType": "Vm"}
