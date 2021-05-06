# THIS FILE IS AUTOMATICALLY GENERATED.
# Disclaimer: Please test this file before using in production.
"""
Generated blueprint DSL (.py)
"""

import json  # no_qa
import os  # no_qa

from calm.dsl.builtins import *  # no_qa


# Secret Variables
BP_CRED_cred_PCDemo_PASSWORD = read_local_file("BP_CRED_cred_PCDemo_PASSWORD")
BP_CRED_cred_FortiGate_PASSWORD = read_local_file("BP_CRED_cred_FortiGate_PASSWORD")
BP_CRED_cred_phpIPAM_PASSWORD = read_local_file("BP_CRED_cred_phpIPAM_PASSWORD")
BP_CRED_cred_PrismCentral_PASSWORD = read_local_file(
    "BP_CRED_cred_PrismCentral_PASSWORD"
)

# Credentials
BP_CRED_cred_PCDemo = basic_cred(
    "admin",
    BP_CRED_cred_PCDemo_PASSWORD,
    name="cred_PCDemo",
    type="PASSWORD",
    default=True,
)
BP_CRED_cred_FortiGate = basic_cred(
    "admin",
    BP_CRED_cred_FortiGate_PASSWORD,
    name="cred_FortiGate",
    type="PASSWORD",
)
BP_CRED_cred_phpIPAM = basic_cred(
    "demoenv",
    BP_CRED_cred_phpIPAM_PASSWORD,
    name="cred_phpIPAM",
    type="PASSWORD",
)
BP_CRED_cred_PrismCentral = basic_cred(
    "wolfgang@ntnx.test",
    BP_CRED_cred_PrismCentral_PASSWORD,
    name="cred_PrismCentral",
    type="PASSWORD",
)


class phpIPAM(Service):

    vlan_id = CalmVariable.Simple(
        "", label="", is_mandatory=False, is_hidden=False, runtime=False, description=""
    )

    subnet_id = CalmVariable.Simple(
        "", label="", is_mandatory=False, is_hidden=False, runtime=False, description=""
    )

    gw_id = CalmVariable.Simple(
        "", label="", is_mandatory=False, is_hidden=False, runtime=False, description=""
    )

    gw_ip = CalmVariable.Simple(
        "", label="", is_mandatory=False, is_hidden=False, runtime=False, description=""
    )

    subnet = CalmVariable.Simple(
        "", label="", is_mandatory=False, is_hidden=False, runtime=False, description=""
    )

    vlan_number = CalmVariable.Simple(
        "", label="", is_mandatory=False, is_hidden=False, runtime=False, description=""
    )

    @action
    def __create__():
        """System action for creating an application"""

        CalmTask.SetVariable.escript(
            name="Get free VLAN",
            filename=os.path.join(
                "scripts", "Service_phpIPAM_Action___create___Task_GetfreeVLAN.py"
            ),
            target=ref(phpIPAM),
            variables=["vlan_id", "vlan_number"],
        )
        CalmTask.SetVariable.escript(
            name="Get free Network",
            filename=os.path.join(
                "scripts", "Service_phpIPAM_Action___create___Task_GetfreeNetwork.py"
            ),
            target=ref(phpIPAM),
            variables=["subnet_id"],
        )
        CalmTask.Exec.escript(
            name="Assign VLAN to Tenant",
            filename=os.path.join(
                "scripts",
                "Service_phpIPAM_Action___create___Task_AssignVLANtoTenant.py",
            ),
            target=ref(phpIPAM),
        )
        CalmTask.Exec.escript(
            name="Assign Subnet to Tenant",
            filename=os.path.join(
                "scripts",
                "Service_phpIPAM_Action___create___Task_AssignSubnettoTenant.py",
            ),
            target=ref(phpIPAM),
        )
        CalmTask.SetVariable.escript(
            name="Get Gateway IP",
            filename=os.path.join(
                "scripts", "Service_phpIPAM_Action___create___Task_GetGatewayIP.py"
            ),
            target=ref(phpIPAM),
            variables=["gw_id", "gw_ip"],
        )
        CalmTask.SetVariable.escript(
            name="Get Network Details",
            filename=os.path.join(
                "scripts", "Service_phpIPAM_Action___create___Task_GetNetworkDetails.py"
            ),
            target=ref(phpIPAM),
            variables=["subnet"],
        )


class Fortigate(Service):

    pass


class PrismCentralDemo(Service):

    task_uuid = CalmVariable.Simple(
        "", label="", is_mandatory=False, is_hidden=False, runtime=False, description=""
    )

    subnet_uuid = CalmVariable.Simple(
        "", label="", is_mandatory=False, is_hidden=False, runtime=False, description=""
    )

    @action
    def __create__():
        """System action for creating an application"""

        CalmTask.SetVariable.escript(
            name="Create Tenant Subnet",
            filename=os.path.join(
                "scripts",
                "Service_PrismCentralDemo_Action___create___Task_CreateTenantSubnet.py",
            ),
            target=ref(PrismCentralDemo),
            variables=["task_uuid"],
        )
        CalmTask.SetVariable.escript(
            name="MonitorVLAN",
            filename=os.path.join(
                "scripts",
                "Service_PrismCentralDemo_Action___create___Task_MonitorVLAN.py",
            ),
            target=ref(PrismCentralDemo),
            variables=["subnet_uuid"]
        )


class existing_phpIPAM(Substrate):

    os_type = "Linux"
    provider_type = "EXISTING_VM"
    provider_spec = read_provider_spec(
        os.path.join("specs", "existing_phpIPAM_provider_spec.yaml")
    )

    readiness_probe = readiness_probe(
        connection_type="SSH",
        disabled=True,
        retries="5",
        connection_port=22,
        address="@@{ip_address}@@",
        delay_secs="60",
    )


class existing_Fortigate(Substrate):

    os_type = "Linux"
    provider_type = "EXISTING_VM"
    provider_spec = read_provider_spec(
        os.path.join("specs", "existing_Fortigate_provider_spec.yaml")
    )

    readiness_probe = readiness_probe(
        connection_type="SSH",
        disabled=True,
        retries="5",
        connection_port=22,
        address="@@{ip_address}@@",
        delay_secs="60",
    )


class existing_PrismCentralDemo(Substrate):

    os_type = "Linux"
    provider_type = "EXISTING_VM"
    provider_spec = read_provider_spec(
        os.path.join("specs", "existing_PrismCentralDemo_provider_spec.yaml")
    )

    readiness_probe = readiness_probe(
        connection_type="SSH",
        disabled=True,
        retries="5",
        connection_port=22,
        address="@@{ip_address}@@",
        delay_secs="60",
    )


class Package1(Package):

    services = [ref(phpIPAM)]

    @action
    def __uninstall__():

        CalmTask.Exec.escript(
            name="Release Subnet",
            filename=os.path.join(
                "scripts", "Package_Package1_Action___uninstall___Task_ReleaseSubnet.py"
            ),
            target=ref(phpIPAM),
        )
        CalmTask.Exec.escript(
            name="Release VLAN",
            filename=os.path.join(
                "scripts", "Package_Package1_Action___uninstall___Task_ReleaseVLAN.py"
            ),
            target=ref(phpIPAM),
        )
        CalmTask.Exec.escript(
            name="Release GW IP",
            filename=os.path.join(
                "scripts", "Package_Package1_Action___uninstall___Task_ReleaseGWIP.py"
            ),
            target=ref(phpIPAM),
        )


class Package2(Package):

    services = [ref(Fortigate)]


class Package3(Package):

    services = [ref(PrismCentralDemo)]

    @action
    def __uninstall__():

        CalmTask.Exec.escript(
            name="Delete Subnet",
            filename=os.path.join(
                "scripts", "Package_Package3_Action___uninstall___Task_DeleteSubnet.py"
            ),
            target=ref(PrismCentralDemo),
        )


class _0720591e_deployment(Deployment):

    name = "0720591e_deployment"
    min_replicas = "1"
    max_replicas = "1"
    default_replicas = "1"

    packages = [ref(Package1)]
    substrate = ref(existing_phpIPAM)


class b6867c95_deployment(Deployment):

    min_replicas = "1"
    max_replicas = "1"
    default_replicas = "1"

    packages = [ref(Package2)]
    substrate = ref(existing_Fortigate)


class a6542720_deployment(Deployment):

    min_replicas = "1"
    max_replicas = "1"
    default_replicas = "1"

    packages = [ref(Package3)]
    substrate = ref(existing_PrismCentralDemo)


class Default(Profile):

    deployments = [_0720591e_deployment, b6867c95_deployment, a6542720_deployment]

    tenant_prefix = CalmVariable.Simple(
        "demo3",
        label="Tenant ID",
        is_mandatory=False,
        is_hidden=False,
        runtime=True,
        description="",
    )

    phpIPAM_section = CalmVariable.Simple(
        "DACHLab",
        label="Demo Network Section",
        is_mandatory=False,
        is_hidden=False,
        runtime=True,
        description="",
    )

    phpIPAM_network_space = CalmVariable.Simple(
        "Demo-Networks",
        label="",
        is_mandatory=False,
        is_hidden=False,
        runtime=True,
        description="",
    )

    phpIPAM_gw_space = CalmVariable.Simple(
        "Demo-Network",
        label="",
        is_mandatory=False,
        is_hidden=False,
        runtime=True,
        description="",
    )


class CreateDemoTenant(Blueprint):

    services = [phpIPAM, Fortigate, PrismCentralDemo]
    packages = [Package1, Package2, Package3]
    substrates = [existing_phpIPAM, existing_Fortigate, existing_PrismCentralDemo]
    profiles = [Default]
    credentials = [
        BP_CRED_cred_PCDemo,
        BP_CRED_cred_FortiGate,
        BP_CRED_cred_phpIPAM,
        BP_CRED_cred_PrismCentral,
    ]
