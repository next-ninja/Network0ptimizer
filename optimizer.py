import subprocess
import os

# --- COLORS ---
GREEN = "\033[92m"
CYAN = "\033[96m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def run(cmd):
    subprocess.run(cmd, shell=True)

def banner():
    os.system("clear")
    print(f"""{CYAN}
  _   _           _     _____                 _                                  _   
 | \ | |         | |   |  __ \               | |                                | |  
 |  \| | _____  _| |_  | |  | | _____   _____| | ___  _ __  _ __ ___   ___ _ __ | |_ 
 | .  |/ _ \ \/ / __| | |  | |/ _ \ \ / / _ \ |/ _ \| '_ \| '_  _ \ / _ \ '_ \| __|
 | |\  |  __/>  <| |_  | |__| |  __/\ V /  __/ | (_) | |_) | | | | | |  __/ | | | |_ 
 |_| \_|\___/_/\_\\__| |_____/ \___| \_/ \___|_|\___/| .__/|_| |_| |_|\___|_| |_|\__|
                                                     | |                             
                                                     |_|                             
{YELLOW}🔥 SUPAR GOD MODE VPS & NETWORK OPTIMIZER ⚡
             🛡 MADE BY NINJA
{RESET}
""")

def optimize_network_ram_disk():
    print(f"{GREEN}🚀 MAX Boosting Network, RAM, Disk, VPS...{RESET}")
    cmds = [
        # Load BBR TCP Congestion Control
        "modprobe tcp_bbr",
        "echo 'tcp_bbr' | tee -a /etc/modules-load.d/modules.conf",
        "echo 'net.core.default_qdisc=fq' >> /etc/sysctl.conf",
        "echo 'net.ipv4.tcp_congestion_control=bbr' >> /etc/sysctl.conf",

        # TCP Optimizations
        "echo 'net.ipv4.tcp_fastopen=3' >> /etc/sysctl.conf",
        "echo 'net.ipv4.tcp_mtu_probing=1' >> /etc/sysctl.conf",
        "echo 'net.ipv4.tcp_sack=1' >> /etc/sysctl.conf",
        "echo 'net.ipv4.tcp_window_scaling=1' >> /etc/sysctl.conf",
        "echo 'net.ipv4.tcp_timestamps=1' >> /etc/sysctl.conf",
        "echo 'net.core.rmem_max=67108864' >> /etc/sysctl.conf",
        "echo 'net.core.wmem_max=67108864' >> /etc/sysctl.conf",
        "echo 'net.ipv4.tcp_rmem=4096 87380 67108864' >> /etc/sysctl.conf",
        "echo 'net.ipv4.tcp_wmem=4096 65536 67108864' >> /etc/sysctl.conf",

        # Buffer settings
        "echo 'net.core.netdev_max_backlog=5000' >> /etc/sysctl.conf",
        "echo 'net.core.somaxconn=1024' >> /etc/sysctl.conf",

        # Memory optimization
        "echo 'vm.swappiness=10' >> /etc/sysctl.conf",
        "echo 'vm.dirty_ratio=10' >> /etc/sysctl.conf",
        "echo 'vm.dirty_background_ratio=5' >> /etc/sysctl.conf",
        "echo 'vm.overcommit_memory=1' >> /etc/sysctl.conf",
        "echo 'vm.vfs_cache_pressure=50' >> /etc/sysctl.conf",

        # File descriptors
        "ulimit -n 1048576",
        "echo 'fs.file-max=2097152' >> /etc/sysctl.conf",

        # Kill IPv6
        "echo 'net.ipv6.conf.all.disable_ipv6=1' >> /etc/sysctl.conf",
        "echo 'net.ipv6.conf.default.disable_ipv6=1' >> /etc/sysctl.conf",

        # Boost disk I/O
        "echo 'deadline' > /sys/block/sda/queue/scheduler || true",

        # Flush DNS and set fastest resolvers
        "systemd-resolve --flush-caches",
        "rm -f /etc/resolv.conf",
        "echo 'nameserver 1.1.1.1' > /etc/resolv.conf",
        "echo 'nameserver 8.8.8.8' >> /etc/resolv.conf",
        "echo 'nameserver 9.9.9.9' >> /etc/resolv.conf",

        # Apply settings
        "sysctl -p"
    ]
    for cmd in cmds:
        run(f"sudo bash -c \"{cmd}\"")
    print(f"{GREEN}✅ MAX Network, RAM, Disk Optimization Done.{RESET}\n")

def deep_clean_system():
    print(f"{YELLOW}🧹 Deep Cleaning System, Saving Money...{RESET}")
    cmds = [
        # Update & clean
        "apt update && apt upgrade -y",
        "apt autoremove --purge -y && apt autoclean -y",

        # Remove snaps, lxd
        "apt purge -y snapd lxd lxd-client",
        "rm -rf ~/snap /snap /var/snap /var/lib/snapd",

        # Kill useless services
        "systemctl disable --now bluetooth cups avahi-daemon ModemManager ufw rsyslog cron apport",
        "systemctl disable --now snapd systemd-timesyncd",

        # Clean logs
        "journalctl --vacuum-time=1d",
        "sed -i 's/#SystemMaxUse=.*/SystemMaxUse=30M/' /etc/systemd/journald.conf",
        "systemctl restart systemd-journald",

        # Remove old kernels
        "dpkg --list | grep linux-image | awk '{print $2}' | grep -v $(uname -r) | xargs sudo apt purge -y",

        # Empty Trash and Cache
        "rm -rf ~/.cache/* /var/tmp/* /tmp/* /root/.cache/*",

        # Clear bash history
        "history -c && history -w",

        # Set no GUI
        "systemctl set-default multi-user.target",

        # Force CPU governor to performance
        "apt install -y cpufrequtils",
        "echo 'GOVERNOR=\"performance\"' > /etc/default/cpufrequtils",
        "systemctl restart cpufrequtils",

        # Restart services
        "systemctl daemon-reexec"
    ]
    for cmd in cmds:
        run(f"sudo bash -c \"{cmd}\"")
    print(f"{YELLOW}✅ System Deep Clean and Slimming Done!{RESET}\n")

def full_god_optimize():
    optimize_network_ram_disk()
    deep_clean_system()

def menu():
    banner()
    print(f"{CYAN}Choose your GOD MODE OPTIMIZATION:{RESET}")
    print(f"{GREEN}1️⃣  MAX Network, RAM, Disk Boost ⚡")
    print(f"2️⃣  DEEP Clean VPS (Save Money 💸)")
    print(f"{RED}3️⃣  FULL SUPAR GOD MODE (Everything) 🚀\n{RESET}")

    choice = input("Enter choice [1-3]: ").strip()
    if choice == "1":
        optimize_network_ram_disk()
    elif choice == "2":
        deep_clean_system()
    elif choice == "3":
        full_god_optimize()
    else:
        print(f"{RED}❌ Invalid selection.{RESET}")

if __name__ == "__main__":
    menu()
