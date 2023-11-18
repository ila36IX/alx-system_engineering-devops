# Secure File Transfer Protocol (`sftp`)
![](https://media.tenor.com/w1zY5ak1IpUAAAAC/phineas-ferb.gif)

> Picture your code that in the remote server as a big freight packed in a truck, arriving at the loading dock of your local machine.
* 🚚 The truck is the `sftp` command
* 🛒 The freight is you code or any data that exist in remote server
* 🏗️ The "loading dock" is your lacal machine

---
## Introduction
`sftp` is a way to transfer files and directories between your local machine and the remote server, in secure and encrypted connection. 

## Using Command Line (OpenSSH)

```bash
sftp username@hostname
```
Replace `username` with your username and `hostname` with the server's IP address or hostname.
#### With vagrant machines
If you using Vagrant, you can get it with this way:
1. First run this command in your cmd/powershell:
```shell
run vagrant ssh-config
```
2. Note those variables `IdentityFile`, `Port`, `User`, `HostName`
3. Then run this to connect to the vagrant machine:
```shell
sftp -tIdentityFile "<IdentityFile>" -oPort=<Port> <User>@<HostName>
```
## Navigaation
Everything remains the same, except that the usual commands are applicable to the **remote server**, and commands prefixed with "l" are applicable to the **local machine**. For instance, `ls` will list all the files/directories that exist on the **remote server**, but when you use `lls` (where the additional "l" stands for local), it will list the files existing on the **local machine**.

## Uploading Files

```bash
put localfile.txt remotefile.txt
```

Replace `localfile.txt` with the path to your local file and `remotefile.txt` with the desired remote file name.
## Downloading Files

```bash
get remotefile.txt localfile.txt
```
Replace `remotefile.txt` with the remote file name and `localfile.txt` with the desired local file name if you want to rename it.

