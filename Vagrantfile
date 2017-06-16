# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "ubuntu/xenial64"
  config.vm.hostname = "qb-online"

  config.vm.network :forwarded_port, guest: 8020, host: 8020
  config.vm.network :private_network, type: "dhcp"
  config.vm.network :public_network, bridge: 'en0: Wi-Fi (AirPort)'

  config.vm.synced_folder ".", "/home/ubuntu/qb-online"

  config.vm.provision "ansible" do |ansible|
    ansible.verbose = "v"
    ansible.host_key_checking = "false"
    ansible.limit = "all"
    ansible.playbook = "deployment/dev/vagrant/setup.yml"
  end

  config.vm.provider "virtualbox" do |v|
    v.memory = 1024
  end
end