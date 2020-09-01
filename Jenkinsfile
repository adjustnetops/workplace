#!/usr/bin/env groovy
def remote = [:]
    remote.host = '192.168.200.68'
    remote.name = 'node'
    
    remote.allowAnyHosts = true
    node() {
        remote.user = 'root'
        remote.password = 'YsBBB4zgzn9Fjoe'
        withCredentials([usernamePassword(credentialsId: 'kitrumvm', passwordVariable: 'YsBBB4zgzn9Fjoe', usernameVariable: 'root')]){
    stage('Checkout'){
        checkout([$class: 'GitSCM', 
        branches: [[name: '*/master']],  
        extensions: [[$class: 'targetDirectory', targetDirectory: 'test']], 
        userRemoteConfigs: [[url: 'git@github.com:adjustawesometeam/workplace.git']]])
    }
    stage('Start services'){
        sh 'cd test && ls -a'
        sh 'vagrant up'
    }
}
    }
