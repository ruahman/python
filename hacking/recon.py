import os
import subprocess


def recon_system(ip):
    os.system(f"nmap -A -p- -Pn {ip} -v")
    os.system(f"dirb {ip}")


def recon_subprocess(ip):
    subprocess.run(["nmap", "-A", "-p-", "-Pn", ip, "-v"], check=False)
    subprocess.run(["dirb", ip], check=False)


if __name__ == "__main__":
    recon_subprocess(input("What ip would you like to scan? "))
