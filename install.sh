#!/bin/bash

# --- COLORS ---
GREEN="\033[92m"
CYAN="\033[96m"
RED="\033[91m"
YELLOW="\033[93m"
RESET="\033[0m"

# --- FUNCTIONS ---
banner() {
    clear
    echo -e "${CYAN}
  _   _           _     _____                 _                                  _   
 | \ | |         | |   |  __ \               | |                                | |  
 |  \| | _____  _| |_  | |  | | _____   _____| | ___  _ __  _ __ ___   ___ _ __ | |_ 
 | . \` |/ _ \ \/ / __| | |  | |/ _ \ \ / / _ \ |/ _ \| '_ \| '_ \` _ \ / _ \ '_ \| __|
 | |\  |  __/>  <| |_  | |__| |  __/\ V /  __/ | (_) | |_) | | | | | |  __/ | | | |_ 
 |_| \_|\___/_/\_\\__| |_____/ \___| \_/ \___|_|\___/| .__/|_| |_| |_|\___|_| |_|\__|
                                                     | |                             
                                                     |_|                             
${YELLOW}🔥 SUPAR GOD MODE VPS & NETWORK OPTIMIZER ⚡
             🛡 MADE BY NINJA
${RESET}"
}

optimize_network_ram_disk() {
    echo -e "${GREEN}🚀 MAX Boosting Network, RAM, Disk, VPS...${RESET}"

    sudo modprobe tcp_bbr
    echo 'tcp_bbr' | sudo tee -a /etc/modules-load.d/modules.conf
    {
        echo 'net.core.default_qdisc=fq'
        echo 'net.ipv4.tcp_congestion_control=bbr'
        echo 'net.ipv4.tcp_fastopen=3'
        echo 'net.ipv4.tcp_mtu_probing=1'
        echo 'net.ipv4.tcp_sack=1'
        echo 'net.ipv4.tcp_window_scaling=1'
        echo 'net.ipv4.tcp_timestamps=1'
        echo 'net.core.rmem_max=67108864'
        echo 'net.core.wmem_max=67108864'
        echo 'net.ipv4.tcp_rmem=4096 87380 67108864'
        echo 'net.ipv4.tcp_wmem=4096 65536 67108864'
        echo 'net.core.netdev_max_backlog=5000'
        echo 'net.core.somaxconn=1024'
        echo 'vm.swappiness=10'
        echo 'vm.dirty_ratio=10'
        echo 'vm.dirty_background_ratio=5'
        echo 'vm.overcommit_memory=1'
        echo 'vm.vfs_cache_pressure=50'
        echo 'fs.file-max=2097152'
        echo 'net.ipv6.conf.all.disable_ipv6=1'
        echo 'net.ipv6.conf.default.disable_ipv6=1'
    } | sudo tee -a /etc/sysctl.conf

    sudo ulimit -n 1048576

    sudo bash -c "echo 'deadline' > /sys/block/sda/queue/scheduler" || true

    sudo systemd-resolve --flush-caches
    sudo rm -f /etc/resolv.conf
    {
        echo 'nameserver 1.1.1.1'
        echo 'nameserver 8.8.8.8'
        echo 'nameserver 9.9.9.9'
    } | sudo tee /etc/resolv.conf

    sudo sysctl -p

    echo -e "${GREEN}✅ MAX Network, RAM, Disk Optimization Done.${RESET}\n"
}

deep_clean_system() {
    echo -e "${YELLOW}🧹 Deep Cleaning System, Saving Money...${RESET}"

    sudo apt update && sudo apt upgrade -y
    sudo apt autoremove --purge -y && sudo apt autoclean -y

    sudo apt purge -y snapd lxd lxd-client
    sudo rm -rf ~/snap /snap /var/snap /var/lib/snapd

    sudo systemctl disable --now bluetooth cups avahi-daemon ModemManager ufw rsyslog cron apport
    sudo systemctl disable --now snapd systemd-timesyncd

    sudo journalctl --vacuum-time=1d
    sudo sed -i 's/#SystemMaxUse=.*/SystemMaxUse=30M/' /etc/systemd/journald.conf
    sudo systemctl restart systemd-journald

    sudo dpkg --list | grep linux-image | awk '{print $2}' | grep -v $(uname -r) | xargs sudo apt purge -y

    sudo rm -rf ~/.cache/* /var/tmp/* /tmp/* /root/.cache/*

    history -c
    history -w

    sudo systemctl set-default multi-user.target

    sudo apt install -y cpufrequtils
    echo 'GOVERNOR="performance"' | sudo tee /etc/default/cpufrequtils
    sudo systemctl restart cpufrequtils

    sudo systemctl daemon-reexec

    echo -e "${YELLOW}✅ System Deep Clean and Slimming Done!${RESET}\n"
}

full_god_optimize() {
    optimize_network_ram_disk
    deep_clean_system
}

menu() {
    banner
    echo -e "${CYAN}Choose your GOD MODE OPTIMIZATION:${RESET}"
    echo -e "${GREEN}1️⃣  MAX Network, RAM, Disk Boost ⚡"
    echo -e "2️⃣  DEEP Clean VPS (Save Money 💸)"
    echo -e "${RED}3️⃣  FULL SUPAR GOD MODE (Everything) 🚀${RESET}\n"

    read -rp "Enter choice [1-3]: " choice
    case "$choice" in
        1) optimize_network_ram_disk ;;
        2) deep_clean_system ;;
        3) full_god_optimize ;;
        *) echo -e "${RED}❌ Invalid selection.${RESET}" ;;
    esac
}

# --- MAIN ---
menu
