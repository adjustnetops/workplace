#!/usr/bin/env groovy
def remote = [:]
    remote.host = '192.168.200.68'
    remote.name = 'node'
    
    remote.allowAnyHosts = true
    node() {
        remote.user = 'root'
        remote.password = 'YsBBB4zgzn9Fjoe'
        withCredentials([usernamePassword(credentialsId: 'remote_machine', passwordVariable: 'YsBBB4zgzn9Fjoe', usernameVariable: 'root')])
        //stage('Remote SSH'){
        //sh 'sudo -S apt update'
        //sh 'sudo -S apt install -y virtualbox'
        //sh'curl -O https://releases.hashicorp.com/vagrant/2.2.9/vagrant_2.2.9_x86_64.deb'
        //sh 'sudo -S apt install -y ./vagrant_2.2.9_x86_64.deb'
        //sh 'mkdir test'

    }
    stage('Checkout'){
        checkout([$class: 'GitSCM', 
        branches: [[name: '*/master']], 
        doGenerateSubmoduleConfigurations: false, 
        extensions: [[$class: 'targetDirectory', 
            targetDirectory: 'test']], 
        submoduleCfg: [], 
        userRemoteConfigs: [[url: 'ssh://git@github.com:adjustawesometeam/workplace.git']]])
    }
    stage('Start services'){
        sh 'cd test && ls -a'
        sh 'vagrant up'
    }
