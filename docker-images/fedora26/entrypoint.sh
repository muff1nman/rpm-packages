#!/bin/bash

set -e

: ${SSH_USERNAME:=user}
: ${SSH_USERPASS:=$(dd if=/dev/urandom bs=1 count=15 | base64)}

__create_rundir() {
	mkdir -p /var/run/sshd
}

__create_user() {
# Create a user to SSH into as.
useradd $SSH_USERNAME
echo -e "$SSH_USERPASS\n$SSH_USERPASS" | (passwd --stdin $SSH_USERNAME)
echo ssh user password: $SSH_USERPASS
}

__create_hostkeys() {
ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key -N '' 
}

__setup_gpg() {
    sudo -u $SSH_USERNAME bash << EOF
        cd
        echo "%_gpg_name Andrew DeMaria RPM Signing Key <rpmsign@andrewdemaria.com>" > .rpmmacros
	export GPG_TTY=$(tty)
        gpg2 --import << EZF
-----BEGIN PGP PRIVATE KEY BLOCK-----
Version: GnuPG v2.0.22 (GNU/Linux)

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
oIN8SXAzrMo=
=jJjJ
-----END PGP PRIVATE KEY BLOCK-----
EZF

echo '5D37D073B801D3C8F2B7F8D5F1FA01525717778A:6:' | gpg2 --import-ownertrust
        
EOF
}

# Call all functions
__create_rundir
__create_hostkeys
__create_user
__setup_gpg

rm -f /run/nologin

exec "$@"

