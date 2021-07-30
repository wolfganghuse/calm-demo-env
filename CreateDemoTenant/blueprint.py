# THIS FILE IS AUTOMATICALLY GENERATED.
# Disclaimer: Please test this file before using in production.
"""
Generated blueprint DSL (.py)
"""

import json  # no_qa
import os  # no_qa

from calm.dsl.builtins import *  # no_qa


# Secret Variables
BP_CRED_cred_Vault_PASSWORD = read_local_file("BP_CRED_cred_Vault_PASSWORD")
BP_CRED_cred_PCDemo_PASSWORD = read_local_file("BP_CRED_cred_PCDemo_PASSWORD")
BP_CRED_cred_FortiGate_PASSWORD = read_local_file("BP_CRED_cred_FortiGate_PASSWORD")
BP_CRED_cred_phpIPAM_PASSWORD = read_local_file("BP_CRED_cred_phpIPAM_PASSWORD")
BP_CRED_cred_PrismCentral_PASSWORD = read_local_file(
    "BP_CRED_cred_PrismCentral_PASSWORD"
)
BP_CRED_cred_TenantAD_PASSWORD = read_local_file(
    "BP_CRED_cred_PrismCentral_PASSWORD"
)

# Credentials
BP_CRED_cred_Vault = basic_cred(
    "root",
    BP_CRED_cred_Vault_PASSWORD,
    name="cred_Vault",
    type="PASSWORD",
    default=True,
)
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
BP_CRED_cred_TenantAD = basic_cred(
    "wolfgang@ntnx.test",
    BP_CRED_cred_TenantAD_PASSWORD,
    name="cred_TenantAD",
    type="PASSWORD",
)

class Vault (Service):
    
    vault_token = CalmVariable.Simple(
        "", label="", is_mandatory=False, is_hidden=False, runtime=False, description=""
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


class Fortigate(Service):

    fortigate_csrf_token = CalmVariable.Simple(
        "", label="", is_mandatory=False, is_hidden=False, runtime=False, description=""
    )

    fortigate_cookie = CalmVariable.Simple(
        "", label="", is_mandatory=False, is_hidden=False, runtime=False, description=""
    )

   fortigate_in_id = CalmVariable.Simple(
        "", label="", is_mandatory=False, is_hidden=False, runtime=False, description=""
    )
   fortigate_out_id = CalmVariable.Simple(
        "", label="", is_mandatory=False, is_hidden=False, runtime=False, description=""
    )
   interface_name = CalmVariable.Simple(
        "", label="", is_mandatory=False, is_hidden=False, runtime=False, description=""
    )

class PrismCentralDemo(Service):

    ENV_UUID = CalmVariable.Simple(
        "", label="", is_mandatory=False, is_hidden=False, runtime=False, description=""
    )

    task_uuid = CalmVariable.Simple(
        "", label="", is_mandatory=False, is_hidden=False, runtime=False, description=""
    )

    nutanix_calm_user_uuid = CalmVariable.Simple(
        "", label="", is_mandatory=False, is_hidden=False, runtime=False, description=""
    )

    subnet_uuid = CalmVariable.Simple(
        "", label="", is_mandatory=False, is_hidden=False, runtime=False, description=""
    )

    subnet_name = CalmVariable.Simple(
        "", label="", is_mandatory=False, is_hidden=False, runtime=False, description=""
    )

<<<<<<< HEAD
    PROJECT_UUID = CalmVariable.Simple(
        "", label="", is_mandatory=False, is_hidden=False, runtime=False, description=""
    )

    project_name = CalmVariable.Simple(
        "", label="", is_mandatory=False, is_hidden=False, runtime=False, description=""
    )

    nutanix_calm_account_uuid = CalmVariable.Simple(
        "", label="", is_mandatory=False, is_hidden=False, runtime=False, description=""
    )

    nutanix_calm_user_uuid = CalmVariable.Simple(
        "", label="", is_mandatory=False, is_hidden=False, runtime=False, description=""
    )

    UID = CalmVariable.Simple(
        "", label="", is_mandatory=False, is_hidden=False, runtime=False, description=""
    )

    CLOUD_ACCOUNT_UUID = CalmVariable.Simple(
        "", label="", is_mandatory=False, is_hidden=False, runtime=False, description=""
    )

    PC_ACCOUNT_UUID = CalmVariable.Simple(
        "", label="", is_mandatory=False, is_hidden=False, runtime=False, description=""
    )

    ROLE_ADMIN_UUID = CalmVariable.Simple(
        "", label="", is_mandatory=False, is_hidden=False, runtime=False, description=""
    )

    ROLE_OPERATOR_UUID = CalmVariable.Simple(
        "", label="", is_mandatory=False, is_hidden=False, runtime=False, description=""
    )

    GROUP_ADMIN_UUID = CalmVariable.Simple(
        "", label="", is_mandatory=False, is_hidden=False, runtime=False, description=""
    )

    GROUP_OPERATOR_UUID = CalmVariable.Simple(
        "", label="", is_mandatory=False, is_hidden=False, runtime=False, description=""
    )

class TenantAD(Service):

    Distinguished_Name = CalmVariable.Simple(
        "", label="", is_mandatory=False, is_hidden=False, runtime=False, description=""
    )

    AD_PATH = CalmVariable.Simple(
        "", label="", is_mandatory=False, is_hidden=False, runtime=False, description=""
    )
=======
    project_uuid = CalmVariable.Simple(
        "", label="", is_mandatory=False, is_hidden=False, runtime=False, description=""
    )

    project_name = CalmVariable.Simple(
        "", label="", is_mandatory=False, is_hidden=False, runtime=False, description=""
    )

    nutanix_calm_account_uuid = CalmVariable.Simple(
        "", label="", is_mandatory=False, is_hidden=False, runtime=False, description=""
    )

    nutanix_calm_user_uuid = CalmVariable.Simple(
        "", label="", is_mandatory=False, is_hidden=False, runtime=False, description=""
    )


class existing_Vault(Substrate):


    os_type = "Linux"
    provider_type = "EXISTING_VM"
    provider_spec = read_provider_spec(
        os.path.join("specs", "existing_Vault_provider_spec.yaml")
    )

    readiness_probe = readiness_probe(
        connection_type="SSH",
        disabled=True,
        retries="5",
        connection_port=22,
        address="@@{ip_address}@@",
        delay_secs="60",
    )
>>>>>>> main


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

<<<<<<< HEAD
class existing_TenantAD(Substrate):

    os_type = "Windows"
    provider_type = "EXISTING_VM"
    provider_spec = read_provider_spec(
        os.path.join("specs", "existing_TenantAD_provider_spec.yaml")
    )

    readiness_probe = readiness_probe(
        connection_type="POWERSHELL",
        disabled=True,
        retries="5",
        connection_port=5985,
        address="@@{ip_address}@@",
        delay_secs="60",
    )
=======
class pkg_Vault(Package):
    
    services = [ref(Vault)]

    @action
    def __install__():

        CalmTask.Exec.escript(
            name="Create Policy",
            filename=os.path.join(
                "scripts", "Package_pkg_Vault_Action___install___Task_CreatePolicy.py"
            ),
            target=ref(Vault)
        )

        CalmTask.SetVariable.escript(
            name="Get Token",
            filename=os.path.join(
                "scripts", "Package_pkg_Vault_Action___install___Task_GetToken.py"
            ),
            target=ref(Vault),
            variables=["vault_token"]
        )
        CalmTask.Exec.escript(
            name="Write Vault",
            filename=os.path.join(
                "scripts",
                "Package_pkg_Vault_Action___install___Task_WriteVault.py",
            ),
            target=ref(Vault)
        )
>>>>>>> main


class pkg_phpIPAM(Package):

    services = [ref(phpIPAM)]

    @action
    def __install__():

        CalmTask.SetVariable.escript(
            name="Get free VLAN",
            filename=os.path.join(
                "scripts", "Package_pkg_phpIPAM_Action___install___Task_GetfreeVLAN.py"
            ),
            target=ref(phpIPAM),
            variables=["vlan_id", "vlan_number"],
        )
        CalmTask.SetVariable.escript(
            name="Get free Network",
            filename=os.path.join(
                "scripts",
                "Package_pkg_phpIPAM_Action___install___Task_GetfreeNetwork.py",
            ),
            target=ref(phpIPAM),
            variables=["subnet_id"],
        )
        CalmTask.Exec.escript(
            name="Assign VLAN to Tenant",
            filename=os.path.join(
                "scripts",
                "Package_pkg_phpIPAM_Action___install___Task_AssignVLANtoTenant.py",
            ),
            target=ref(phpIPAM),
        )
        CalmTask.Exec.escript(
            name="Assign Subnet to Tenant",
            filename=os.path.join(
                "scripts",
                "Package_pkg_phpIPAM_Action___install___Task_AssignSubnettoTenant.py",
            ),
            target=ref(phpIPAM),
        )
        CalmTask.SetVariable.escript(
            name="Get Gateway IP",
            filename=os.path.join(
                "scripts", "Package_pkg_phpIPAM_Action___install___Task_GetGatewayIP.py"
            ),
            target=ref(phpIPAM),
            variables=["gw_id", "gw_ip"],
        )
        CalmTask.SetVariable.escript(
            name="Get Network Details",
            filename=os.path.join(
                "scripts",
                "Package_pkg_phpIPAM_Action___install___Task_GetNetworkDetails.py",
            ),
            target=ref(phpIPAM),
            variables=["subnet"],
        )

    @action
    def __uninstall__():

        CalmTask.Exec.escript(
            name="Release Subnet",
            filename=os.path.join(
                "scripts",
                "Package_pkg_phpIPAM_Action___uninstall___Task_ReleaseSubnet.py",
            ),
            target=ref(phpIPAM),
        )
        CalmTask.Exec.escript(
            name="Release VLAN",
            filename=os.path.join(
                "scripts",
                "Package_pkg_phpIPAM_Action___uninstall___Task_ReleaseVLAN.py",
            ),
            target=ref(phpIPAM),
        )
        CalmTask.Exec.escript(
            name="Release GW IP",
            filename=os.path.join(
                "scripts",
                "Package_pkg_phpIPAM_Action___uninstall___Task_ReleaseGWIP.py",
            ),
            target=ref(phpIPAM),
        )

class pkg_TenantAD(Package):

    services = [ref(TenantAD)]

    @action
    def __install__():
    
        CalmTask.SetVariable.escript(
            name="create_ADPath",
            filename=os.path.join(
                "scripts", "Service_TenantAD_Action___create___Task_create_ADPath.py"
            ),
            target=ref(TenantAD),
            variables=["AD_PATH"],
        )

        CalmTask.Exec.powershell(
            name="CreateTenantOU",
            filename=os.path.join(
                "scripts", "Service_TenantAD_Action___create___Task_CreateTenantOU.py"
            ),
            cred=ref(BP_CRED_cred_TenantAD),
            target=ref(TenantAD)
        )

        CalmTask.SetVariable.escript(
            name="SetOUPath",
            filename=os.path.join(
                "scripts", "Service_TenantAD_Action___create___Task_SetOUPath.py"
            ),
            target=ref(TenantAD),
            variables=["Distinguished_Name"],
        )


    @action
    def __uninstall__():

        CalmTask.Exec.powershell(
            name="DeleteTenantOU",
            filename=os.path.join(
                "scripts", "pkg_TenantAD__uninstall__Task_DeleteTenantOU.py"
            ),
            cred=ref(BP_CRED_cred_TenantAD),
            target=ref(TenantAD),
        )



class pkg_Fortigate(Package):

    services = [ref(Fortigate)]

    @action
    def __install__():

        CalmTask.SetVariable.escript(
            name="Login Fortigate",
            filename=os.path.join(
                "scripts",
                "Package_pkg_Fortigate_Action___install___Task_LoginFortigate.py",
            ),
            target=ref(Fortigate),
            variables=["fortigate_csrf_token", "fortigate_cookie"],
        )
        CalmTask.SetVariable.escript(
            name="Create VLAN Interface",
            filename=os.path.join(
                "scripts",
                "Package_pkg_Fortigate_Action___install___Task_CreateVLANInterface.py",
            ),
            target=ref(Fortigate),
            variables=["interface_name"],
        )
        CalmTask.Exec.escript(
            name="Create Address Object",
            filename=os.path.join(
                "scripts",
                "Package_pkg_Fortigate_Action___install___Task_CreateAddressObject.py",
            ),
            target=ref(Fortigate),
        )

        CalmTask.SetVariable.escript(
            name="Create Basic Rules Incoming",
            filename=os.path.join(
                "scripts","pkg_Fortigate__install__Task_Create_Incoming_Rules.py"),
                variables=["fortigate_in_id"],
                target=ref(Fortigate)
        )

        CalmTask.SetVariable.escript(
            name="Create Basic Rules Outgoing",
            filename=os.path.join(
                "scripts","pkg_Fortigate__install__Task_Create_Outgoing_Rules.py"),
                variables=["fortigate_out_id"],
                target=ref(Fortigate)
        )

    @action
    def __uninstall__():

        CalmTask.SetVariable.escript(
            name="Login Fortigate",
            filename=os.path.join(
                "scripts",
                "Package_pkg_Fortigate_Action___uninstall___Task_LoginFortigate.py",
            ),
            target=ref(Fortigate),
            variables=["fortigate_csrf_token", "fortigate_cookie"],
        )
        CalmTask.Exec.escript(
            name="Delete Outgoing",
            filename=os.path.join(
                "scripts","pkg_Fortigate__uninstall__Task_Delete_Outgoing_Rules.py"),
                target=ref(Fortigate)
        )

        CalmTask.Exec.escript(
            name="Delete Incoming",
            filename=os.path.join(
                "scripts","pkg_Fortigate__uninstall__Task_Delete_Incoming_Rules.py"),
                target=ref(Fortigate)
        )

        CalmTask.Exec.escript(
            name="Delete Address Object",
            filename=os.path.join(
                "scripts",
                "Package_pkg_Fortigate_Action___uninstall___Task_DeleteAddressObject.py",
            ),
            target=ref(Fortigate),
        )
        CalmTask.Exec.escript(
            name="Delete VLAN Interface",
            filename=os.path.join(
                "scripts",
                "Package_pkg_Fortigate_Action___uninstall___Task_DeleteVLANInterface.py",
            ),
            target=ref(Fortigate),
        )

<<<<<<< HEAD
=======

>>>>>>> main
class pkg_PrismCentralDemo(Package):

    services = [ref(PrismCentralDemo)]

    @action
    def __install__():

        CalmTask.SetVariable.escript(
            name="Create Tenant Subnet",
            filename=os.path.join(
                "scripts",
<<<<<<< HEAD
                "pkg_PrismCentralDemo__install__Task_CreateTenantSubnet.py",
            ),
            target=ref(PrismCentralDemo),
            variables=["subnet_uuid","subnet_name"],
        )
        
        CalmTask.SetVariable.escript(
            name="Get User uuid",
            filename=os.path.join(
                "scripts",
                "pkg_PrismCentralDemo__install__Task_GetUserUUID.py",
            ),
            target=ref(PrismCentralDemo),
            variables=["nutanix_calm_user_uuid"]
        )

        CalmTask.SetVariable.escript(
            name="GenerateUID",
            filename=os.path.join(
                "scripts",
                "pkg_PrismCentralDemo__install__Task_GenerateUID.py",
            ),
            target=ref(PrismCentralDemo),
            variables=["UID","ROLE_ADMIN_UUID","ROLE_OPERATOR_UUID"]
=======
                "Package_pkg_PrismCentralDemo_Action___install___Task_CreateTenantSubnet.py",
            ),
            target=ref(PrismCentralDemo),
            variables=["subnet_uuid","subnet_name"],
>>>>>>> main
        )
        CalmTask.SetVariable.escript(
<<<<<<< HEAD
            name="getCloudAccount",
            filename=os.path.join(
                "scripts",
                "pkg_PrismCentralDemo__install__Task_getCloudAccount.py",
            ),
            target=ref(PrismCentralDemo),
            variables=["CLOUD_ACCOUNT_UUID","PC_ACCOUNT_UUID"]
=======
            name="Get User Uuid",
            filename=os.path.join(
                "scripts",
                "Package_pkg_PrismCentralDemo_Action___install___Task_GetUserUuid.py",
            ),
            target=ref(PrismCentralDemo),
            variables=["nutanix_calm_user_uuid"],
>>>>>>> main
        )
        CalmTask.SetVariable.escript(
<<<<<<< HEAD
            name="Create Project",
            filename=os.path.join(
                "scripts",
                "pkg_PrismCentralDemo__install__Task_CreateProject.py",
            ),
            target=ref(PrismCentralDemo),
            variables=["PROJECT_UUID","project_name"],
        )

        CalmTask.SetVariable.escript(
            name="Create Environment",
            filename=os.path.join(
                "scripts",
                "pkg_PrismCentralDemo__install__Task_CreateEnvironment.py",
            ),
            target=ref(PrismCentralDemo),
            variables=["ENV_UUID"]
        )

        CalmTask.SetVariable.escript(
            name="CreateAdminGroup",
            filename=os.path.join(
                "scripts",
                "pkg_PrismCentralDemo__install__Task_CreateAdminGroup.py",
            ),
            target=ref(PrismCentralDemo),
            variables=["GROUP_ADMIN_UUID"]
=======
            name="Get Account Uuid",
            filename=os.path.join(
                "scripts",
                "Package_pkg_PrismCentralDemo_Action___install___Task_AccountUuid.py",
            ),
            target=ref(PrismCentralDemo),
            variables=["nutanix_calm_account_uuid"],
>>>>>>> main
        )
        CalmTask.SetVariable.escript(
<<<<<<< HEAD
            name="CreateOperatorGroup",
            filename=os.path.join(
                "scripts",
                "pkg_PrismCentralDemo__install__Task_CreateOperatorGroup.py",
            ),
            target=ref(PrismCentralDemo),
            variables=["GROUP_OPERATOR_UUID"]
=======
            name="Create Project",
            filename=os.path.join(
                "scripts",
                "Package_pkg_PrismCentralDemo_Action___install___Task_CreateProject.py",
            ),
            target=ref(PrismCentralDemo),
            variables=["project_uuid","project_name"],
>>>>>>> main
        )

        CalmTask.Exec.escript(
            name="updateProject",
            filename=os.path.join(
                "scripts",
                "pkg_PrismCentralDemo__install__Task_updateProject.py",
            ),
            target=ref(PrismCentralDemo)
        )

        CalmTask.Exec.escript(
            name="EntitleMktBp",
            filename=os.path.join(
                "scripts",
                "pkg_PrismCentralDemo__install__Task_EntitleMktBp.py",
            ),
            target=ref(PrismCentralDemo)
        )


    @action
    def __uninstall__():

        CalmTask.SetVariable.escript(
            name="Delete Subnet",
            filename=os.path.join(
                "scripts",
                "Package_pkg_PrismCentralDemo_Action___uninstall___Task_DeleteSubnet.py",
            ),
            target=ref(PrismCentralDemo),
            variables=["task_uuid"],
        )
        CalmTask.Exec.escript(
            name="Monitor Delete Subnet",
            filename=os.path.join(
                "scripts",
                "Package_pkg_PrismCentralDemo_Action___uninstall___Task_MonitorDeleteSubnet.py",
            ),
            target=ref(PrismCentralDemo),
        )
        CalmTask.SetVariable.escript(
            name="Delete Project",
            filename=os.path.join(
                "scripts",
                "Package_pkg_PrismCentralDemo_Action___uninstall___Task_DeleteProject.py",
            ),
            target=ref(PrismCentralDemo),
            variables=["task_uuid"],
        )
        CalmTask.Exec.escript(
            name="Monitor Delete Project",
            filename=os.path.join(
<<<<<<< HEAD
                "scripts", "lib__Task_MonitorProgress.py"
            ),
            target=ref(PrismCentralDemo)
        )

        CalmTask.Exec.escript(
            name="DeleteAdminGroup",
            filename=os.path.join(
                "scripts", "pkg_PrismCentralDemo__uninstall__Task_DeleteAdminGroup.py"
=======
                "scripts",
                "Package_pkg_PrismCentralDemo_Action___uninstall___Task_MonitorDeleteProject.py",
>>>>>>> main
            ),
            target=ref(PrismCentralDemo),
        )

<<<<<<< HEAD
        CalmTask.Exec.escript(
            name="DeleteOperatorGroup",
            filename=os.path.join(
                "scripts", "pkg_PrismCentralDemo__uninstall__Task_DeleteOperatorGroup.py"
            ),
            target=ref(PrismCentralDemo),
        )
=======
>>>>>>> main

class _0720591e_deployment(Deployment):

    name = "0720591e_deployment"
    min_replicas = "1"
    max_replicas = "1"
    default_replicas = "1"

    packages = [ref(pkg_phpIPAM)]
    substrate = ref(existing_phpIPAM)

class TenantAD_deployment(Deployment):

    name = "TenantAD_deployment"
    min_replicas = "1"
    max_replicas = "1"
    default_replicas = "1"

    packages = [ref(pkg_TenantAD)]
    substrate = ref(existing_TenantAD)


class b6867c95_deployment(Deployment):

    min_replicas = "1"
    max_replicas = "1"
    default_replicas = "1"

    packages = [ref(pkg_Fortigate)]
    substrate = ref(existing_Fortigate)


class a6542720_deployment(Deployment):

    min_replicas = "1"
    max_replicas = "1"
    default_replicas = "1"

    packages = [ref(pkg_PrismCentralDemo)]
    substrate = ref(existing_PrismCentralDemo)

class Vault_deployment(Deployment):

    min_replicas = "1"
    max_replicas = "1"
    default_replicas = "1"

    packages = [ref(pkg_Vault)]
    substrate = ref(existing_Vault)


class Default(Profile):

<<<<<<< HEAD
    deployments = [_0720591e_deployment, b6867c95_deployment, a6542720_deployment, TenantAD_deployment]

    PASSWORD = CalmVariable.Simple(
        "nutanix/4u",
        label="username password",
        is_mandatory=False,
        is_hidden=False,
        runtime=True,
        description="",
    )

    USERID = CalmVariable.Simple(
        "OrgAdmin",
        label="Admin User",
        is_mandatory=False,
        is_hidden=False,
        runtime=True,
        description="",
    )

    LAST_NAME = CalmVariable.Simple(
        "Smith",
        label="Admin Last Name",
        is_mandatory=False,
        is_hidden=False,
        runtime=True,
        description="",
    )

    FIRST_NAME = CalmVariable.Simple(
        "John",
        label="Admin First Name",
        is_mandatory=False,
        is_hidden=False,
        runtime=True,
        description="",
    )

    ROOT_OU = CalmVariable.Simple(
        "Tenants",
        label="",
        is_mandatory=False,
        is_hidden=False,
        runtime=False,
        description="",
    )

    DOMAIN = CalmVariable.Simple(
        "ntnx.test",
        label="",
        is_mandatory=False,
        is_hidden=False,
        runtime=False,
        description="",
    )

    ROLE_OPERATOR = CalmVariable.Simple(
        "Operator",
        label="",
        is_mandatory=False,
        is_hidden=False,
        runtime=False,
        description="",
    )

    ROLE_ADMIN = CalmVariable.Simple(
        "Consumer",
        label="",
        is_mandatory=False,
        is_hidden=False,
        runtime=False,
        description="",
    )
=======
    deployments = [_0720591e_deployment, b6867c95_deployment, a6542720_deployment, Vault_deployment]
>>>>>>> main

    tenant_prefix = CalmVariable.Simple(
        "Demo3",
        label="Tenant ID",
        is_mandatory=False,
        is_hidden=False,
        runtime=True,
        description="",
    )


    ENV_PASSWORD = CalmVariable.Simple(
        "nutanix/4u",
        label="",
        is_mandatory=False,
        is_hidden=False,
        runtime=False,
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

<<<<<<< HEAD
    services = [phpIPAM, Fortigate, PrismCentralDemo, TenantAD]
    packages = [pkg_phpIPAM, pkg_Fortigate, pkg_PrismCentralDemo, pkg_TenantAD]
    substrates = [existing_phpIPAM, existing_Fortigate, existing_PrismCentralDemo, existing_TenantAD]
=======
    services = [phpIPAM, Fortigate, PrismCentralDemo, Vault]
    packages = [pkg_phpIPAM, pkg_Fortigate, pkg_PrismCentralDemo, pkg_Vault]
    substrates = [existing_phpIPAM, existing_Fortigate, existing_PrismCentralDemo, existing_Vault]
>>>>>>> main
    profiles = [Default]
    credentials = [
        BP_CRED_cred_PCDemo,
        BP_CRED_cred_FortiGate,
        BP_CRED_cred_phpIPAM,
        BP_CRED_cred_PrismCentral,
<<<<<<< HEAD
        BP_CRED_cred_TenantAD
=======
        BP_CRED_cred_Vault
>>>>>>> main
    ]
