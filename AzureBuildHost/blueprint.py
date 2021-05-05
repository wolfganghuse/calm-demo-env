"""
Generated blueprint DSL (.py)
"""

import json  # no_qa
import os  # no_qa

from calm.dsl.builtins import *  # no_qa


# Secret Variables
BP_CRED_cred_os_KEY = read_local_file("BP_CRED_cred_os_KEY")
Profile_Default_variable_PAT = read_local_file("Profile_Default_variable_PAT")

# Credentials
BP_CRED_cred_os = basic_cred(
    "centos",
    BP_CRED_cred_os_KEY,
    name="cred_os",
    type="KEY",
    default=True,
)


class Service1(Service):

    pass


class vmcalm_timeResources(AhvVmResources):

    memory = 4
    vCPUs = 2
    cores_per_vCPU = 1
    disks = [AhvVmDisk.Disk.Scsi.cloneFromImageService("CentOS7", bootable=True)]
    nics = [AhvVmNic.NormalNic.ingress("NTNX-DEMO01_IPAM", cluster="NTNX-DEMO01")]

    guest_customization = AhvVmGC.CloudInit(
        filename=os.path.join("specs", "vmcalm_time_cloud_init_data.yaml")
    )


class vmcalm_time(AhvVm):

    name = "azurebuild-@@{calm_time}@@"
    resources = vmcalm_timeResources


class svc_AzureBuild(Substrate):

    os_type = "Linux"
    provider_type = "AHV_VM"
    provider_spec = vmcalm_time
    provider_spec_editables = read_spec(
        os.path.join("specs", "svc_AzureBuild_create_spec_editables.yaml")
    )
    readiness_probe = readiness_probe(
        connection_type="SSH",
        disabled=True,
        retries="5",
        connection_port=22,
        address="@@{platform.status.resources.nic_list[0].ip_endpoint_list[0].ip}@@",
        delay_secs="60",
        credential=ref(BP_CRED_cred_os),
    )


class Package1(Package):

    services = [ref(Service1)]

    @action
    def __install__():

        CalmTask.Exec.ssh(
            name="Install Packages",
            filename=os.path.join(
                "scripts", "Package_Package1_Action___install___Task_InstallPackages.sh"
            ),
            target=ref(Service1),
        )
        CalmTask.Exec.ssh(
            name="Install Docker",
            filename=os.path.join(
                "scripts", "Package_Package1_Action___install___Task_InstallDocker.sh"
            ),
            cred=ref(BP_CRED_cred_os),
            target=ref(Service1),
        )
        CalmTask.Exec.ssh(
            name="Install Azure Build Host",
            filename=os.path.join(
                "scripts",
                "Package_Package1_Action___install___Task_InstallAzureBuildHost.sh",
            ),
            cred=ref(BP_CRED_cred_os),
            target=ref(Service1),
        )


class _98854c90_deployment(Deployment):

    name = "98854c90_deployment"
    min_replicas = "1"
    max_replicas = "1"
    default_replicas = "1"

    packages = [ref(Package1)]
    substrate = ref(svc_AzureBuild)


class Default(Profile):

    deployments = [_98854c90_deployment]

    azure_org = CalmVariable.Simple(
        "wolfganghuse",
        label="",
        is_mandatory=False,
        is_hidden=False,
        runtime=True,
        description="",
    )

    pool = CalmVariable.Simple(
        "default",
        label="",
        is_mandatory=False,
        is_hidden=False,
        runtime=True,
        description="",
    )

    PAT = CalmVariable.Simple.Secret(
        Profile_Default_variable_PAT,
        label="",
        is_mandatory=False,
        is_hidden=False,
        runtime=True,
        description="",
    )


class AzureBuildHost(Blueprint):
    """AzureBuildHost"""

    services = [Service1]
    packages = [Package1]
    substrates = [svc_AzureBuild]
    profiles = [Default]
    credentials = [BP_CRED_cred_os]


class BpMetadata(Metadata):

    categories = {"TemplateType": "Vm"}
