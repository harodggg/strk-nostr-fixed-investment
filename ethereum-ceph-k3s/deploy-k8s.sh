#!/bin/bash

create_mutiple_volumes() {
    echo "create" $1 volumes
    for i in $(seq 1 $1); do
        hcloud volume create --name volume$i --location hel1 --size 500
    done
}

create_mutiple_machines() {
    create_mutiple_volumes $1
    echo "create" $1 machines
    for i in $(seq 1 $1); do
        hcloud server create --name m$i --ssh-key my_mac_ssh --type cpx51 --image debian-13 --volume volume$i
    done
}

create_k3s_master() {
    hcloud server create --name master --ssh-key my_mac_ssh --type cpx51 --image debian-13
    master_ip=$(hcloud server list | awk 'NR>1 && $2 == "master" {print$4}')
    ssh -o StrictHostKeyChecking=no root@$master_ip 'curl -sfL https://get.k3s.io | sh -'
    k3s_token=$(ssh -o StrictHostKeyChecking=no root@$master_ip 'cat /var/lib/rancher/k3s/server/node-token')
    echo master\'s ip : $master_ip
    echo master\'s token : $k3s_token

}

#master_ip=$(hcloud server list | awk 'NR>1 && $2 == "master" {print$4}')
#
#k3s_token=$(ssh -o StrictHostKeyChecking=no root@$master_ip 'cat /var/lib/rancher/k3s/server/node-token')
#echo master\'s token : $k3s_token
##create_mutiple_machines 9
#
#all_node_ips=$(hcloud server list | awk 'NR > 1 && $2 != "master" && $4 != "46.62.155.108" {print $4}')
#
#for node_ip in $all_node_ips; do
#    ssh -o StrictHostKeyChecking=no root@$node_ip 'curl -sfL https://get.k3s.io | K3S_URL=https://157.180.122.57:6443 K3S_TOKEN=K10f10a94be03faeb764661b568a973201a74bb690958c7c0289a572299192306ea::server:9a05120b58792685e0e32131d14e50b1 sh -'
#done

delete_k3s_and_machine() {
    servers=$(hcloud server list | awk 'NR>1&&$2 != "debian-4gb-starknet" {print$2}')

    for server in $servers; do
        echo $server
        hcloud server delete $server

    done
}

delete_k3s_and_machine
