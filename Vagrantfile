# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  #Configuration des machines d'attaques
    (200..204).each do |i|
      config.vm.define "node-#{i}" do |node|
        node.vm.box = "ubuntu/bionic64"
        node.vm.hostname = "node#{i}"
        node.vm.network "public_network", bridge: "wlo1", ip: "192.168.1.#{i}"
        node.vm.provider "virtualbox" do |vb|
          vb.memory = "1024"
        end
        node.vm.provision "shell", inline: <<-SHELL
          sudo apt-get update
          sudo apt-get install -y python openssh-server python3-pip build-essential libssl-dev libffi-dev python3-dev
          sudo adduser --quiet --disabled-password --shell /bin/bash --home /home/test --gecos "User" test
          echo test:passer | sudo chpasswd
          sudo echo "test	ALL=(ALL:ALL) ALL" >> /etc/sudoers
          #Copie clé SSH
          sudo mkdir -p /home/test/.ssh
          sudo cat /vagrant/id_rsa.pub >> /home/test/.ssh/authorized_keys
          sudo chown -R test:test /home/test/.ssh
          sudo chmod 700 /home/test/.ssh
          sudo chmod 600 /home/test/.ssh/authorized_keys
          sudo service ssh restart
          sudo apt-get install hping3 -y 
        SHELL
        node.vm.provision "shell", path: "script.sh"
      end
    end
  #Configuration du serveur WEB  
  config.vm.define "server" do |server|
    server.vm.box = "ubuntu/bionic64"
    server.vm.hostname = "server"
    server.vm.network "public_network", bridge: "wlo1", ip: "192.168.1.253"
    server.vm.network "private_network", ip: "192.168.113.253"
    server.vm.provider "virtualbox" do |vb|
      vb.memory = "1024"
    end
    server.vm.provision "shell", path: "script.sh"
    server.vm.provision "shell", inline: <<-SHELL
      
    #Creation de l'utilisateur webadmin
      sudo adduser --quiet --disabled-password --shell /bin/bash --home /home/webadmin --gecos "User" webadmin
      echo webadmin:passer | sudo chpasswd
      sudo echo "webadmin	ALL=(ALL:ALL) ALL" >> /etc/sudoers

    #Copie de la clé ssh
      sudo mkdir -p /home/webadmin/.ssh
      sudo cat /vagrant/id_rsa.pub >> /home/webadmin/.ssh/authorized_keys
      sudo chown -R webadmin:webadmin /home/webadmin/.ssh
      sudo chmod 700 /home/webadmin/.ssh
      sudo chmod 600 /home/webadmin/.ssh/authorized_keys

    #installation des paquets necessaire
      # sudo apt-get update
      # debconf-set-selections <<< 'mysql-server mysql-server/root_password password Passer.123/'
      # debconf-set-selections <<< 'mysql-server mysql-server/root_password_again password Passer.123/'
      # sudo apt-get install -y apache2 mysql-server php libapache2-mod-php php-mysql openssh-server python3-pip build-essential libssl-dev libffi-dev python3-dev
      # sudo ufw allow in "Apache"
      # sudo service ssh restart
      # sudo service apache2 restart
    
    #Création du répertoire wordpress
      #sudo mkdir -p /var/www/html/wordpress
      # sudo cp -R /vagrant/wordpress/ /var/www/html/
      # sudo chown -R www-data:www-data /var/www/html/wordpress

    # Redemaarage des services
      # sudo service ssh restart
      # sudo service apache2 restart
    
    #Création de la base données mysql appelé webadmin et le mot de passe d'admin de wordpress est passer
      
      # sudo mysql -u root -p"Passer.123/" -e "CREATE USER 'webadmin'@'localhost' IDENTIFIED BY 'Passer.123/';"
      # sudo mysql -u root -p"Passer.123/" -e "CREATE DATABASE webadmin;"
      # sudo mysql -u root -p"Passer.123/" -e "GRANT ALL ON webadmin.* TO 'webadmin'@'localhost';"
      # sudo mysql -u root -p"Passer.123/" webadmin < /vagrant/webadmin.sql
    
      # sudo userdel -r vagrant
      # sudo useradd -m -s /bin/bash vagrant

    SHELL
    #server.vm.provision "file", source: "./wordpress/", destination: "/var/www/html/wordpress"
  end
  end

 
