#!/usr/bin/python3
#-*-coding:utf-8-*-
# mudah buatmu sulit bagiku
# bye Script START 
from datetime import datetime, timedelta
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
import os
console = Console()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def simpan_lisensi(lisensi):
    with open("license.txt", "w") as f:
        for user in lisensi:
            f.write(f"{user['username']},{user['lisensi_key']},{user['tanggal_expired'].strftime('%Y-%m-%d')},{user['status']},{str(user['approved'])}\n")

def load_lisensi():
    try:
        lisensi = []
        with open("license.txt", "r") as f:
            for line in f.readlines():
                username, lisensi_key, tanggal_expired, status, approved = line.strip().split(",")
                lisensi.append({
                    "username": username,
                    "lisensi_key": lisensi_key,
                    "tanggal_expired": datetime.strptime(tanggal_expired, "%Y-%m-%d"),
                    "status": status,
                    "approved": approved.lower() == "true"
                })
        return lisensi
    except FileNotFoundError:
        return []

def logo():
    banner = (
        "[bold white]╦  ┬┌─┐┌─┐┌┐┌┌─┐┌─┐╦╔═┌─┐┬ ┬  ╦═╗┌─┐┌─┐┬┌─┐┌┬┐┬─┐┌─┐┌─┐┬\n"
        "[bold white]║  ││  ├┤ │││└─┐├┤ ╠╩╗├┤ └┬┘  ╠╦╝├┤ │ ┬│└─┐ │ ├┬┘├─┤└─┐│[bold cyan] YoU hEr0\n"
        "[bold white]╩═╝┴└─┘└─┘┘└┘└─┘└─┘╩ ╩└─┘ ┴   ╩╚═└─┘└─┘┴└─┘ ┴ ┴└─┴ ┴└─┘┴[bold black] "
    )
    console.print(
        Panel(
            banner,
            title="[bold black]🔥 DAFTAR LICENSE KEY 🔥[/bold black]",
            subtitle="[bold black]Powered by ScriptKiddie[/bold black]",
            border_style="white"
        )
    )

def main():
    while True:
        clear_screen()
        logo()
        console.print(
            "[bold white][/bold white]",
            justify="center"
        )
        console.print(" 01. Registrasi License")
        console.print(" 02. Data Member Registrasi")
        console.print(" 00. Keluar")
        pilihan = console.input("[bold white] ➤ Start Input : [/bold white]")
        if pilihan == "1":
            tambah_lisensi()
            pass
        elif pilihan == "2":
            daftar_lisensi()
            pass
        elif pilihan == "99":
            approve_lisensi()
            pass
        elif pilihan == "00":
            break
        else:
            console.print("[bold red] ➤ Pilihan tidak valid![/bold red]")
            console.input("[bold white] ➤ Tekan Enter untuk melanjutkan...[/bold white]")

def generate_expired_date(days):
    return datetime.now() + timedelta(days=days)

def tambah_lisensi():
    clear_screen()
    logo()
    console.print(" 01. 3 hari")
    console.print(" 02. 7 hari")
    console.print(" 03. 14 hari")
    pilihan_masa_aktif = console.input("[bold white] ➤ Masukkan masa aktif : [/bold white]")
    days = {"1": 1, "2": 7, "3": 14}
    if pilihan_masa_aktif in days:
        username_baru = console.input("[bold white] ➤ Masukkan username license baru : [/bold white]")
        lisensi_key_baru = f"{username_baru[:3].upper()}-{username_baru[3:6].upper()}-{username_baru[6:9].upper()}"
        lisensi_baru = {
            "username": username_baru,
            "lisensi_key": lisensi_key_baru,
            "tanggal_expired": generate_expired_date(days[pilihan_masa_aktif]),
            "status": "Pending",
            "approved": False
        }
        lisensi = load_lisensi()
        lisensi.append(lisensi_baru)
        simpan_lisensi(lisensi)
        console.print(f"[bold green] ➤ License baru {username_baru} telah ditambahkan![/bold green]")

def approve_lisensi():
    username_to_approve = console.input("[bold white] ➤ Masukkan username untuk approve: [/bold white]")
    lisensi = load_lisensi()
    for user in lisensi:
        if user["username"] == username_to_approve:
            user["approved"] = True
            simpan_lisensi(lisensi)
            console.print(f"[bold green] ➤ License untuk {username_to_approve} telah diapprove![/bold green]")
            return
    console.print("[bold red] ➤ Username tidak ditemukan![/bold red]")

def approve_lisensi():
    username_to_approve = console.input("[bold white] ➤ Ketik username baru : [/bold white]")
    lisensi = load_lisensi()
    for user in lisensi:
        if user["username"] == username_to_approve:
            user["approved"] = True
            simpan_lisensi(lisensi)
            console.print(f"[bold green]License untuk {username_to_approve} telah diapprove![/bold green]")
            return
    console.print("[bold red]Username tidak ditemukan![/bold red]")

def daftar_lisensi():
    console.print("[bold green] ➤ Daftar Lisensi[/bold green]")
    lisensi = load_lisensi()
    clear_screen()
    table = Table(title="")
    table.add_column("No", justify="center", style="cyan")
    table.add_column("Username", justify="left", style="white")
    table.add_column("Lisensi Key", justify="left", style="white")
    table.add_column("Masa Aktif", justify="left", style="white")
    table.add_column("Tanggal Expired", justify="left", style="white")
    table.add_column("Status", justify="left", style="white")
    table.add_column("Approved", justify="left", style="white")
    count = 1
    for user in lisensi:
        tanggal_expired_str = user["tanggal_expired"].strftime("%Y-%m-%d")
        masa_aktif = (user["tanggal_expired"] - datetime.now()).days
        if user["tanggal_expired"] < datetime.now():
            status = "[bold red]Expired[/bold red]"
        else:
            status = user["status"]
        approved = "[bold green]Yes[/bold green]" if user["approved"] else "[bold red]No[/bold red]"
        table.add_row(str(count), user["username"], user["lisensi_key"], f"{masa_aktif} hari", tanggal_expired_str, status, approved)
        count += 1
    console.print(table)
    exit()

if __name__ == "__main__":
    main()
