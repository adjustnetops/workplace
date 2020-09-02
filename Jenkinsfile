#!/usr/bin/env groovy
def remote = [:]
    remote.host = '192.168.200.68'
    remote.name = 'node'
    
    remote.allowAnyHosts = true
    node() {
        remote.user = 'root'
        remote.password = 'YsBBB4zgzn9Fjoe'
        withCredentials([usernamePassword(credentialsId: 'kitrumvm', passwordVariable: 'YsBBB4zgzn9Fjoe', usernameVariable: 'root')]){
    stage('install services'){
	    sshCommand remote: remote, command: 'apt update'
	    sshCommand remote: remote, command: 'apt install virtualbox'
	    sshCommand remote: remote, command: 'curl -O https://releases.hashicorp.com/vagrant/2.2.9/vagrant_2.2.9_x86_64.deb'
	    sshCommand remote: remote, command:'apt install ./vagrant_2.2.9_x86_64.deb'
    }
    stage('Start services'){
	sh 'mkdir test'  
        sh 'cd test && ls -a'
        sh 'vagrant up'
    }
}
    }
