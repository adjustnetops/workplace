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
	    sshCommand remote: remote, command: 'sudo dnf -y install wget'
            sshCommand remote: remote, command: 'wget https://download.virtualbox.org/virtualbox/rpm/el/virtualbox.repo' 
            sshCommand remote: remote, command: 'sudo mv virtualbox.repo /etc/yum.repos.d'
            sshCommand remote: remote, command: 'wget -q https://www.virtualbox.org/download/oracle_vbox.asc'
	    sshCommand remote: remote, command: 'sudo rpm --import oracle_vbox.asc'
	    sshCommand remote: remote, command: 'sudo dnf -y install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm'
            sshCommand remote: remote, command: 'sudo dnf -y install binutils kernel-devel kernel-headers libgomp make patch gcc glibc-headers glibc-devel dkms'
            sshCommand remote: remote, command: 'sudo dnf install -y VirtualBox-6.1'
	    sshCommand remote: remote, command: 'sudo usermod -aG vboxusers $USER'
	    sshCommand remote: remote, command: 'sudo /usr/lib/virtualbox/vboxdrv.sh setup'
	    sshCommand remote: remote, command: 'sudo dnf -y install https://releases.hashicorp.com/vagrant/${VERSION}/vagrant_${VERSION}_x86_64.rpm'
    }
    stage('Start services'){
	sshCommand remote: remote, command: 'mkdir repo'
        sshCommand remote: remote, command: 'cd repo && ls -a'
        sshCommand remote: remote, command: 'vagrant up'
    }
}
    }
