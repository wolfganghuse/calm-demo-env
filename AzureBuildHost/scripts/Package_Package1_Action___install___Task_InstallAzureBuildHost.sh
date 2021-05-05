wget https://vstsagentpackage.azureedge.net/agent/2.177.1/vsts-agent-linux-x64-2.177.1.tar.gz
mkdir myagent && cd myagent
tar zxvf ~/vsts-agent-linux-x64-2.177.1.tar.gz
sudo ./bin/installdependencies.sh
./config.sh --unattended --url https://dev.azure.com/@@{azure_org}@@ --auth pat --token @@{PAT}@@ --pool @@{pool}@@ --agent @@{name}@@ --acceptTeeEula
sudo ./svc.sh install
sudo ./svc.sh start