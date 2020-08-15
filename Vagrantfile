Vagrant.configure(2) do |config|
  config.vm.box = "centos/7"
  config.vm.hostname = "monitsys"
  config.vm.provider "virtualbox" do |v|
    v.name = "monitsys"
    v.memory = 2048
    v.cpus= 2
    config.vm.network "public_network", bridge: "bridge0"
    config.vm.provision "shell", path: "conf.sh"
    config.vm.synced_folder ".", "/vagrant", type: "smb"
end
end