#!/usr/bin/env groovy

node(){
  stage('test'){
    //sh 'echo test'sshCommand remote: remote, command: "sudo apt update"
    def remote = [:]
    remote.host = '192.168.200.68'
    remote.user = 'root'
    remote.password = 'YsBBB4zgzn9Fjoe'
    remote.allowAnyHosts = true    
    sshCommand remote: remote, command: "sudo apt install virtualbox"
    sshCommand remote: remote, command: "curl -O https://releases.hashicorp.com/vagrant/2.2.9/vagrant_2.2.9_x86_64.deb"
    sshCommand remote: remote, command: "sudo apt install ./vagrant_2.2.9_x86_64.deb"
    
  }
}
