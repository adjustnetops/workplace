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
	    sh 'apt update'
	    sh 'apt install virtualbox'
	    sh 'curl -O https://releases.hashicorp.com/vagrant/2.2.9/vagrant_2.2.9_x86_64.deb'
	    sh 'apt install ./vagrant_2.2.9_x86_64.deb'
    }
    stage('Start services'){
	sh 'mkdir test'  
        sh 'cd test && ls -a'
        sh 'vagrant up'
    }
}
    }
