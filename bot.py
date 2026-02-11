import requests
import time
import json
import random
import sys
import os
from datetime import datetime
from colorama import init, Fore, Back, Style
from threading import Thread

init(autoreset=True)

BANNER = f"""
{Fore.MAGENTA}{Back.BLACK}╔════════════════════════════════════════════════════════════════════════════════════╗{Style.RESET_ALL}
{Fore.MAGENTA}{Back.BLACK}║                                                                                    ║{Style.RESET_ALL}
{Fore.MAGENTA}{Back.BLACK}║{Fore.CYAN}{Back.BLACK}                      ██╗   ██╗███╗   ██╗██╗ ██████╗██╗  ██╗                    {Fore.MAGENTA}{Back.BLACK}║{Style.RESET_ALL}
{Fore.MAGENTA}{Back.BLACK}║{Fore.CYAN}{Back.BLACK}                      ██║   ██║████╗  ██║██║██╔════╝██║  ██║                    {Fore.MAGENTA}{Back.BLACK}║{Style.RESET_ALL}
{Fore.MAGENTA}{Back.BLACK}║{Fore.CYAN}{Back.BLACK}                      ██║   ██║██╔██╗ ██║██║██║     ███████║                    {Fore.MAGENTA}{Back.BLACK}║{Style.RESET_ALL}
{Fore.MAGENTA}{Back.BLACK}║{Fore.CYAN}{Back.BLACK}                      ██║   ██║██║╚██╗██║██║██║     ██╔══██║                    {Fore.MAGENTA}{Back.BLACK}║{Style.RESET_ALL}
{Fore.MAGENTA}{Back.BLACK}║{Fore.CYAN}{Back.BLACK}                      ╚██████╔╝██║ ╚████║██║╚██████╗██║  ██║                    {Fore.MAGENTA}{Back.BLACK}║{Style.RESET_ALL}
{Fore.MAGENTA}{Back.BLACK}║{Fore.CYAN}{Back.BLACK}                       ╚═════╝ ╚═╝  ╚═══╝╚═╝ ╚═════╝╚═╝  ╚═╝                    {Fore.MAGENTA}{Back.BLACK}║{Style.RESET_ALL}
{Fore.MAGENTA}{Back.BLACK}║                                                                                    ║{Style.RESET_ALL}
{Fore.MAGENTA}{Back.BLACK}║{Fore.YELLOW}{Back.BLACK}                      ╔══════════════════════════════════════╗                {Fore.MAGENTA}{Back.BLACK}║{Style.RESET_ALL}
{Fore.MAGENTA}{Back.BLACK}║{Fore.YELLOW}{Back.BLACK}                      ║     UNICH AUTO MINER v2.0           ║                {Fore.MAGENTA}{Back.BLACK}║{Style.RESET_ALL}
{Fore.MAGENTA}{Back.BLACK}║{Fore.YELLOW}{Back.BLACK}                      ║     ████████████████████████████    ║                {Fore.MAGENTA}{Back.BLACK}║{Style.RESET_ALL}
{Fore.MAGENTA}{Back.BLACK}║{Fore.YELLOW}{Back.BLACK}                      ╚══════════════════════════════════════╝                {Fore.MAGENTA}{Back.BLACK}║{Style.RESET_ALL}
{Fore.MAGENTA}{Back.BLACK}║                                                                                    ║{Style.RESET_ALL}
{Fore.MAGENTA}{Back.BLACK}║{Fore.GREEN}{Back.BLACK}                      ╔══════════════════════════════════════╗                {Fore.MAGENTA}{Back.BLACK}║{Style.RESET_ALL}
{Fore.MAGENTA}{Back.BLACK}║{Fore.GREEN}{Back.BLACK}                      ║  👑 DEVELOPED BY: MEJRI02           ║                {Fore.MAGENTA}{Back.BLACK}║{Style.RESET_ALL}
{Fore.MAGENTA}{Back.BLACK}║{Fore.GREEN}{Back.BLACK}                      ║  🔗 GITHUB: mejri02/unich-bot       ║                {Fore.MAGENTA}{Back.BLACK}║{Style.RESET_ALL}
{Fore.MAGENTA}{Back.BLACK}║{Fore.GREEN}{Back.BLACK}                      ║  💎 TELEGRAM: @mejri02_ch           ║                {Fore.MAGENTA}{Back.BLACK}║{Style.RESET_ALL}
{Fore.MAGENTA}{Back.BLACK}║{Fore.GREEN}{Back.BLACK}                      ╚══════════════════════════════════════╝                {Fore.MAGENTA}{Back.BLACK}║{Style.RESET_ALL}
{Fore.MAGENTA}{Back.BLACK}║                                                                                    ║{Style.RESET_ALL}
{Fore.MAGENTA}{Back.BLACK}╚════════════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}
"""

USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 Version/17.0 Safari/605.1.15',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 Version/17.0 Mobile/15E148 Safari/604.1',
    'Mozilla/5.0 (iPad; CPU OS 17_0 like Mac OS X) AppleWebKit/605.1.15 Version/17.0 Mobile/15E148 Safari/604.1',
]

class Logger:
    @staticmethod
    def _get_timestamp():
        return f"{Fore.CYAN}{datetime.now().strftime('%H:%M:%S')}{Style.RESET_ALL}"
    
    @staticmethod
    def info(message):
        print(f"{Fore.WHITE}[{Logger._get_timestamp()}] {Fore.BLUE}➤{Style.RESET_ALL} {message}")
    
    @staticmethod
    def error(message):
        print(f"{Fore.WHITE}[{Logger._get_timestamp()}] {Fore.RED}✘{Style.RESET_ALL} {Fore.RED}{message}{Style.RESET_ALL}")
    
    @staticmethod
    def warning(message):
        print(f"{Fore.WHITE}[{Logger._get_timestamp()}] {Fore.YELLOW}⚠{Style.RESET_ALL} {Fore.YELLOW}{message}{Style.RESET_ALL}")
    
    @staticmethod
    def success(message):
        print(f"{Fore.WHITE}[{Logger._get_timestamp()}] {Fore.GREEN}✔{Style.RESET_ALL} {Fore.GREEN}{message}{Style.RESET_ALL}")
    
    @staticmethod
    def mining(message):
        print(f"{Fore.WHITE}[{Logger._get_timestamp()}] {Fore.CYAN}⛏{Style.RESET_ALL} {Fore.CYAN}{message}{Style.RESET_ALL}")
    
    @staticmethod
    def task(message):
        print(f"{Fore.WHITE}[{Logger._get_timestamp()}] {Fore.MAGENTA}📋{Style.RESET_ALL} {Fore.MAGENTA}{message}{Style.RESET_ALL}")
    
    @staticmethod
    def point(message):
        print(f"{Fore.WHITE}[{Logger._get_timestamp()}] {Fore.YELLOW}💎{Style.RESET_ALL} {Fore.YELLOW}{message}{Style.RESET_ALL}")

log = Logger()

class Config:
    def __init__(self):
        self.use_proxy = False
        self.proxies = []
        self.token_file = 'tokens.txt'
        self.proxy_file = 'proxies.txt'
        
    def load_proxies(self):
        try:
            if os.path.exists(self.proxy_file):
                with open(self.proxy_file, 'r') as f:
                    self.proxies = [line.strip() for line in f.readlines() if line.strip()]
                if self.proxies:
                    log.success(f"✅ Loaded {len(self.proxies)} proxies")
                    return True
            return False
        except:
            return False
    
    def get_random_proxy(self):
        if self.proxies:
            proxy = random.choice(self.proxies)
            return {'http': f'http://{proxy}', 'https': f'http://{proxy}'}
        return None

config = Config()

def setup_interface():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(BANNER)
    
    print(f"\n{Fore.CYAN}{Back.BLACK}╔{'═'*60}╗{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{Back.BLACK}║{Fore.WHITE}{Back.BLACK}⚡ INITIALIZATION SETUP{Style.RESET_ALL}{Fore.CYAN}{Back.BLACK} {' ' * 38}║{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{Back.BLACK}╚{'═'*60}╝{Style.RESET_ALL}\n")
    
    while True:
        proxy_choice = input(f"{Fore.YELLOW}❓ Use proxies? (y/n): {Style.RESET_ALL}").lower()
        if proxy_choice in ['y', 'n']:
            config.use_proxy = proxy_choice == 'y'
            break
    
    if config.use_proxy:
        if not config.load_proxies():
            log.warning("No proxies.txt found. Creating template...")
            with open('proxies.txt', 'w') as f:
                f.write("# One proxy per line - format: ip:port or user:pass@ip:port\n")
                f.write("# 127.0.0.1:8080\n")
                f.write("# user:password@127.0.0.1:3128\n")
            input(f"\n{Fore.GREEN}Press Enter to continue after adding proxies to proxies.txt...{Style.RESET_ALL}")
            config.load_proxies()
    
    print(f"\n{Fore.CYAN}{'▰'*60}{Style.RESET_ALL}\n")
    log.info(f"Configuration Complete")
    log.info(f"📁 Tokens file: {config.token_file}")
    if config.use_proxy:
        log.info(f"🔒 Proxy: Enabled ({len(config.proxies)} proxies)")
    else:
        log.info(f"🔓 Proxy: Disabled")
    time.sleep(2)

class UnichBot:
    def __init__(self):
        self.base_url = 'https://api.unich.com'
        self.stats = {'total_points': 0, 'tasks_completed': 0, 'mining_starts': 0}
        
    def random_headers(self, token):
        return {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json',
            'User-Agent': random.choice(USER_AGENTS),
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Origin': 'https://unich.com',
            'Referer': 'https://unich.com/',
            'Sec-Ch-Ua': '"Not_A Brand";v="8", "Chromium";v="120"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Platform': '"Windows"',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'Connection': 'keep-alive',
        }
    
    def read_tokens(self):
        try:
            if not os.path.exists(config.token_file):
                with open(config.token_file, 'w') as f:
                    f.write("# Paste your tokens here - one per line\n")
                    f.write("# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...\n")
                log.error(f"❌ tokens.txt not found! Template created.")
                return []
            
            with open(config.token_file, 'r') as f:
                tokens = [line.strip() for line in f.readlines() 
                         if line.strip() and not line.startswith('#')]
            
            valid_tokens = [t for t in tokens if len(t.split('.')) == 3]
            
            if valid_tokens:
                log.success(f"✅ Loaded {len(valid_tokens)} accounts")
            return valid_tokens
            
        except Exception as e:
            log.error(f"Token error: {str(e)}")
            return []
    
    def make_request(self, method, url, token=None, json=None):
        try:
            headers = self.random_headers(token) if token else {'Content-Type': 'application/json'}
            proxies = config.get_random_proxy() if config.use_proxy else None
            
            if method.upper() == 'GET':
                response = requests.get(url, headers=headers, proxies=proxies, timeout=30)
            else:
                response = requests.post(url, headers=headers, json=json, proxies=proxies, timeout=30)
            
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 401:
                return {'error': 'unauthorized'}
            return None
            
        except Exception as e:
            if config.use_proxy:
                log.warning(f"Proxy failed, retrying...")
            return None
    
    def start_mining(self, token):
        url = f"{self.base_url}/airdrop/user/v1/mining/start"
        result = self.make_request('POST', url, token, {})
        
        if result and result.get('code') == 'OK':
            self.stats['mining_starts'] += 1
            log.mining(f"Mining activated")
            return True
        return False
    
    def get_mining_data(self, token):
        url = f"{self.base_url}/airdrop/user/v1/mining/recent"
        return self.make_request('GET', url, token)
    
    def get_tasks(self, token):
        url = f"{self.base_url}/airdrop/user/v1/social/list-by-user"
        return self.make_request('GET', url, token)
    
    def claim_task(self, token, task_id, task_name):
        url = f"{self.base_url}/airdrop/user/v1/social/claim/{task_id}"
        result = self.make_request('POST', url, token, {"evidence": task_id})
        
        if result and result.get('code') == 'OK':
            reward = result.get('data', {}).get('pointReward', 0)
            self.stats['tasks_completed'] += 1
            self.stats['total_points'] += reward
            log.point(f"+{reward} points • {task_name}")
            return True
        return False
    
    def print_stats(self):
        print(f"\n{Fore.CYAN}{Back.BLACK}╔{'═'*50}╗{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{Back.BLACK}║{Fore.WHITE}{Back.BLACK}📊 SESSION STATISTICS{Style.RESET_ALL}{Fore.CYAN}{Back.BLACK} {' ' * 31}║{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{Back.BLACK}╠{'═'*50}╣{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{Back.BLACK}║{Style.RESET_ALL}   💰 Total Points Earned: {Fore.GREEN}{self.stats['total_points']:,}{Style.RESET_ALL}               {Fore.CYAN}{Back.BLACK}║{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{Back.BLACK}║{Style.RESET_ALL}   ✅ Tasks Completed: {Fore.GREEN}{self.stats['tasks_completed']}{Style.RESET_ALL}                      {Fore.CYAN}{Back.BLACK}║{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{Back.BLACK}║{Style.RESET_ALL}   ⛏️  Mining Starts: {Fore.GREEN}{self.stats['mining_starts']}{Style.RESET_ALL}                         {Fore.CYAN}{Back.BLACK}║{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{Back.BLACK}╚{'═'*50}╝{Style.RESET_ALL}\n")
    
    def animate_loading(self, seconds):
        animation = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", 
                    "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", 
                    "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
        for i in range(seconds * 2):
            print(f"\r{Fore.CYAN}⏳ Waiting {animation[i % 10]}{Style.RESET_ALL}", end='', flush=True)
            time.sleep(0.5)
        print()
    
    def run(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(BANNER)
        
        tokens = self.read_tokens()
        if not tokens:
            input(f"\n{Fore.RED}Press Enter to exit...{Style.RESET_ALL}")
            return
        
        log.success(f"🎮 Ready with {len(tokens)} warriors")
        time.sleep(1)
        
        cycle = 0
        while True:
            cycle += 1
            print(f"\n{Fore.YELLOW}{Back.BLACK}╔{'═'*60}╗{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}{Back.BLACK}║{Fore.WHITE}{Back.BLACK}🌀 CYCLE #{cycle} - {datetime.now().strftime('%H:%M:%S')}{Style.RESET_ALL}{Fore.YELLOW}{Back.BLACK} {' ' * 40}║{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}{Back.BLACK}╚{'═'*60}╝{Style.RESET_ALL}\n")
            
            for idx, token in enumerate(tokens):
                print(f"{Fore.CYAN}{'┏' + '━'*58 + '┓'}{Style.RESET_ALL}")
                print(f"{Fore.CYAN}┃{Style.RESET_ALL} {Fore.WHITE}👤 ACCOUNT #{idx+1}{Style.RESET_ALL} {' ' * 45} {Fore.CYAN}┃{Style.RESET_ALL}")
                print(f"{Fore.CYAN}{'┗' + '━'*58 + '┛'}{Style.RESET_ALL}")
                
                mining = self.get_mining_data(token)
                
                if mining and 'data' in mining:
                    balance = mining['data'].get('mUn', 0)
                    is_mining = mining['data'].get('isMining', False)
                    
                    bar_length = 30
                    filled = int(bar_length * (balance % 1000) / 1000)
                    bar = '█' * filled + '░' * (bar_length - filled)
                    
                    print(f"   {Fore.CYAN}💰 Balance: {Fore.WHITE}{balance:,}{Style.RESET_ALL}")
                    print(f"   {Fore.CYAN}📊 Mining:  {Fore.GREEN if is_mining else Fore.RED}{'● ACTIVE' if is_mining else '○ INACTIVE'}{Style.RESET_ALL}")
                    print(f"   {Fore.CYAN}📈 Progress: {Fore.WHITE}[{bar}]{Style.RESET_ALL}\n")
                    
                    if not is_mining:
                        log.mining("Attempting to start mining...")
                        self.start_mining(token)
                    
                    tasks_data = self.get_tasks(token)
                    if tasks_data and 'data' in tasks_data:
                        items = tasks_data['data'].get('items', [])
                        unclaimed = [t for t in items if not t.get('claimed')]
                        
                        if unclaimed:
                            log.task(f"Found {len(unclaimed)} mission{'s' if len(unclaimed)>1 else ''}")
                            print(f"{Fore.MAGENTA}{'  ┌' + '─'*56 + '┐'}{Style.RESET_ALL}")
                            
                            for task in unclaimed:
                                task_id = task.get('id', '')
                                task_name = task.get('name', task_id[-8:]).replace('_', ' ').title()
                                task_reward = task.get('reward', 0)
                                
                                print(f"{Fore.MAGENTA}  │{Style.RESET_ALL} {Fore.YELLOW}⚔️  {task_name[:30]:<30}{Style.RESET_ALL} {Fore.GREEN}+{task_reward:<5}{Style.RESET_ALL} {Fore.MAGENTA}│{Style.RESET_ALL}")
                                if self.claim_task(token, task_id, task_name):
                                    time.sleep(1.5)
                            
                            print(f"{Fore.MAGENTA}  └{'─'*56}┘{Style.RESET_ALL}\n")
                        else:
                            log.success("✨ All missions completed!")
                else:
                    log.error(f"Account #{idx+1} - Connection failed")
                
                print(f"{Fore.CYAN}{'▬'*60}{Style.RESET_ALL}\n")
                time.sleep(2)
            
            self.print_stats()
            
            next_time = (datetime.now().timestamp() + 3600)
            next_str = datetime.fromtimestamp(next_time).strftime('%H:%M:%S')
            
            print(f"{Fore.BLUE}{Back.BLACK}╔{'═'*60}╗{Style.RESET_ALL}")
            print(f"{Fore.BLUE}{Back.BLACK}║{Fore.WHITE}{Back.BLACK}🌙 COOLDOWN MODE - Next Cycle: {next_str}{Style.RESET_ALL}{Fore.BLUE}{Back.BLACK} {' ' * 28}║{Style.RESET_ALL}")
            print(f"{Fore.BLUE}{Back.BLACK}╚{'═'*60}╝{Style.RESET_ALL}\n")
            
            self.animate_loading(60)

if __name__ == "__main__":
    try:
        setup_interface()
        bot = UnichBot()
        bot.run()
    except KeyboardInterrupt:
        print(f"\n\n{Fore.RED}{Back.BLACK}👋 Thanks for using Unich Bot - Created by mejri02{Style.RESET_ALL}\n")
        sys.exit(0)
    except Exception as e:
        log.error(f"Fatal: {str(e)}")
        time.sleep(5)
