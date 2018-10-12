
- [Server Configuration](#server-configuration)
    - [1. Start a new Ubuntu Linux server instance on Amazon Lightsail. There are full details on setting up your Lightsail instance on the next page](#1-start-a-new-ubuntu-linux-server-instance-on-amazon-lightsail-there-are-full-details-on-setting-up-your-lightsail-instance-on-the-next-page)
    - [2. Follow the instructions provided to SSH into your server](#2-follow-the-instructions-provided-to-ssh-into-your-server)
    - [3. Update all currently installed packages](#3-update-all-currently-installed-packages)
    - [4. Ssh port number change](#4-ssh-port-number-change)
    - [5. UFW configuration](#5-ufw-configuration)
    - [6. Create a new User](#6-create-a-new-user)
    - [7. Give user sudo access](#7-give-user-sudo-access)
    - [8. Generate key for the grader](#8-generate-key-for-the-grader)
    - [9. Set timezone to UTC](#9-set-timezone-to-utc)
    - [10. Install and configure apache and Python mod_wsgi application](#10-install-and-configure-apache-and-python-mod_wsgi-application)
    - [11. Install and configure PostgreSQL](#11-install-and-configure-postgresql)
# Server Configuration


## 1. Start a new Ubuntu Linux server instance on [Amazon Lightsail](https://lightsail.aws.amazon.com/). There are full details on setting up your Lightsail instance on the next page

## 2. Follow the instructions provided to SSH into your server

## 3. Update all currently installed packages
1.  `sudo apt-get update`
2.  `sudo apt-get upgrade`
3.  
## 4. Ssh port number change

1. `sudo nano /etc/ssh/sshd_config`
2. find the port = 22
3. change `port = 22 -> port = 2200`
4. save /etc/ssh/sshd_config
5. `sudo service sshd restart`
6. you will have to log out and back in - this can be done with `shutdown -r now`
7. Reconnect using the ssh terminal on port 2200

## 5. UFW configuration

1. verify that it is not configured
2. `sudo ufw status`
   1. status inactive should be shown
3. add rules before turning it on
4. deny incoming connections
   2. `sudo ufw default deny incoming`
5. allow outgoing connections
   3. `sudo ufw default allow outgoing`
6. Allow SSH through port 2200
   4. `sudo ufw allow 2200/tcp`
7. Allow web traffic
   5. `sudo ufw allow www`
8. Allow NTP traffic
    1. `sudo ufw allow ntp`
9. Enable firewall **Don't do this before ensuring you will be able to access ssh through port 2200**
   6. `sudo ufw enable`
10. Command may disrupt existing ssh connections. Proceed with operation (y|n)?
11. `yes` and press enter
12. Verify settings of ufw
    1. `sudo ufw status`
    2. the following table should be displayed

Status: active

| To      | Action          | From          |
| ------- | --------------- | ------------- |
| 2200    | tcp ALLOW       | Anywhere      |
| 80      | tcp ALLOW       | Anywhere      |
| 123     | ALLOW           | Anywhere      |
| 2200    | tcp  (v6) ALLOW | Anywhere (v6) |
| 80      | tcp (v6) ALLOW  | Anywhere (v6) |
| 123(v6) | ALLOW           | Anywhere (v6) |

## 6. Create a new User

## 7. Give user sudo access

## 8. Generate key for the grader

1. on your local machine terminal
2. `ssh-keygen`
3. enter the name for the file of the keys
    1. `/c/users/austi/.ssh/grader`
    2. enter a passphrase for the key
    3. re-enter the passphrase for the key
        1. Udacity2018
4. the grader.pub file will be placed on the server to enable key based authentication.
5. install the public key
    1. `sudo mkdir /home/grader/.ssh`
    2. `sudo touch /home/grader/.ssh/authorized_keys`
    3. on your local machine read contents of public key
        1. `cat /c/users/austi/.ssh/grader.pub`
        2. copy contents of the local key to the authorized_keys file that was just created
    4. change permissions of the authorized keys to comply with ssh
        1. `sudo chmod 644 /home/grader/.ssh/authorized_keys`
        2. `sudo chmod 700 /home/grader/.ssh`
    5. login via ssh using the new private key from your local machine
        1. you will be prompted to enter the passphrase created previously
6. Disable the password login
    1. this will force everyone to login with a key
    2. `sudo nano /etc/ssh/sshd_config`
    3. find `PasswordAuthentication yes`
    4. change it to `PasswordAuthentication no`
    5. save the file
    6. restart the service to apply the changes
        1. `sudo service sshd restart`

## 9. Set timezone to UTC

1. `sudo timedatectl set-timezone UTC`
2. `timedatectl`

## 10. Install and configure apache and Python mod_wsgi application

## 11. Install and configure PostgreSQL
