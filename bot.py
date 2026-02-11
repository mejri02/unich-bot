import requests
import time
import json
import random
import sys
import os
from datetime import datetime
from colorama import init, Fore, Back, Style

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
{Fore.MAGENTA}{Back.BLACK}║{Fore.YELLOW}{Back.BLACK}                      ║        UNICH MINING TERMINAL        ║                {Fore.MAGENTA}{Back.BLACK}║{Style.RESET_ALL}
{Fore.MAGENTA}{Back.BLACK}║{Fore.YELLOW}{Back.BLACK}                      ║           v5.0 • MASTER            ║                {Fore.MAGENTA}{Back.BLACK}║{Style.RESET_ALL}
{Fore.MAGENTA}{Back.BLACK}║{Fore.YELLOW}{Back.BLACK}                      ╚══════════════════════════════════════╝                {Fore.MAGENTA}{Back.BLACK}║{Style.RESET_ALL}
{Fore.MAGENTA}{Back.BLACK}║                                                                                    ║{Style.RESET_ALL}
{Fore.MAGENTA}{Back.BLACK}║{Fore.GREEN}{Back.BLACK}                      ╔══════════════════════════════════════╗                {Fore.MAGENTA}{Back.BLACK}║{Style.RESET_ALL}
{Fore.MAGENTA}{Back.BLACK}║{Fore.GREEN}{Back.BLACK}                      ║  👑 AUTHOR: MEJRI02                ║                {Fore.MAGENTA}{Back.BLACK}║{Style.RESET_ALL}
{Fore.MAGENTA}{Back.BLACK}║{Fore.GREEN}{Back.BLACK}                      ║  🔗 GITHUB: /mejri02/unich         ║                {Fore.MAGENTA}{Back.BLACK}║{Style.RESET_ALL}
{Fore.MAGENTA}{Back.BLACK}║{Fore.GREEN}{Back.BLACK}                      ║  💎 TG: @mejri02                  ║                {Fore.MAGENTA}{Back.BLACK}║{Style.RESET_ALL}
{Fore.MAGENTA}{Back.BLACK}║{Fore.GREEN}{Back.BLACK}                      ╚══════════════════════════════════════╝                {Fore.MAGENTA}{Back.BLACK}║{Style.RESET_ALL}
{Fore.MAGENTA}{Back.BLACK}║                                                                                    ║{Style.RESET_ALL}
{Fore.MAGENTA}{Back.BLACK}╚════════════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}
"""

USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 Version/17.0 Safari/605.1.15',
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
    def success(message):
        print(f"{Fore.WHITE}[{Logger._get_timestamp()}] {Fore.GREEN}✔{Style.RESET_ALL} {Fore.GREEN}{message}{Style.RESET_ALL}")
    
    @staticmethod
    def mining(message):
        print(f"{Fore.WHITE}[{Logger._get_timestamp()}] {Fore.CYAN}⛏{Style.RESET_ALL} {Fore.CYAN}{message}{Style.RESET_ALL}")
    
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
                    self.proxies = [line.strip() for line in f.readlines() if line.strip() and not line.startswith('#')]
                if self.proxies:
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
    print(f"{Fore.CYAN}{Back.BLACK}║{Fore.WHITE}{Back.BLACK}⚡ INITIALIZING SYSTEM{Style.RESET_ALL}{Fore.CYAN}{Back.BLACK} {' ' * 39}║{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{Back.BLACK}╚{'═'*60}╝{Style.RESET_ALL}\n")
    
    while True:
        proxy_choice = input(f"{Fore.YELLOW}❓ USE PROXY? (y/n): {Style.RESET_ALL}").lower()
        if proxy_choice in ['y', 'n']:
            config.use_proxy = proxy_choice == 'y'
            break
    
    if config.use_proxy:
        if not config.load_proxies():
            with open('proxies.txt', 'w') as f:
                f.write("# PROXIES - ONE PER LINE\n")
                f.write("# 127.0.0.1:8080\n")
            input(f"\n{Fore.GREEN}Press ENTER after adding proxies{Style.RESET_ALL}")
            config.load_proxies()
    
    print(f"\n{Fore.CYAN}{'▰'*60}{Style.RESET_ALL}\n")
    return

class UnichBot:
    def __init__(self):
        self.base_url = 'https://api.unich.com'
        self.cycle_stats = {'earned': 0, 'completed': 0, 'failed': 0}
        self.total_stats = {'earned': 0, 'completed': 0, 'mining_starts': 0, 'failed': 0}
        
    def random_headers(self, token):
        return {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json',
            'User-Agent': random.choice(USER_AGENTS),
            'Accept': 'application/json',
            'Origin': 'https://unich.com',
            'Referer': 'https://unich.com/',
        }
    
    def read_tokens(self):
        try:
            if not os.path.exists(config.token_file):
                with open(config.token_file, 'w') as f:
                    f.write("# UNICH TOKENS - ONE PER LINE\n")
                    f.write("# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...\n")
                return []
            
            with open(config.token_file, 'r') as f:
                tokens = [line.strip() for line in f.readlines() 
                         if line.strip() and not line.startswith('#')]
            
            return [t for t in tokens if len(t.split('.')) == 3]
            
        except Exception:
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
        except:
            pass
        return None
    
    def start_mining(self, token):
        url = f"{self.base_url}/airdrop/user/v1/mining/start"
        result = self.make_request('POST', url, token, {})
        
        if result and result.get('code') == 'OK':
            self.total_stats['mining_starts'] += 1
            log.mining(f"MINING ACTIVATED")
            return True
        return False
    
    def get_mining_data(self, token):
        url = f"{self.base_url}/airdrop/user/v1/mining/recent"
        return self.make_request('GET', url, token)
    
    def get_tasks(self, token):
        url = f"{self.base_url}/airdrop/user/v1/social/list-by-user"
        response = self.make_request('GET', url, token)
        
        if response and response.get('code') == 'OK':
            data = response.get('data', {})
            if isinstance(data, dict):
                return data.get('items', [])
        return []
    
    def get_task_name(self, task_id):
        task_id_lower = task_id.lower()
        
        if '7eafd90b' in task_id_lower or 'twitter' in task_id_lower or 'follow' in task_id_lower:
            return '🐦 Twitter Follow'
        if '7eaff279' in task_id_lower or 'retweet' in task_id_lower:
            return '🔄 Twitter Retweet'
        if 'ac5ecbca' in task_id_lower or 'daily' in task_id_lower:
            return '📅 Daily Login'
        if 'fe48ae1c' in task_id_lower or 'discord' in task_id_lower:
            return '💬 Join Discord'
        if '698c87378ec06af901e2a074' in task_id_lower:
            return '🐦 Follow Unich'
        if '698c87378ec06af901e2a075' in task_id_lower:
            return '🔄 Retweet Post'
        if '3c135ca6' in task_id_lower:
            return '📆 Check-in'
        if '3c13659d' in task_id_lower:
            return '👥 Join Community'
        if 'e629d6ab' in task_id_lower:
            return '📢 Share Post'
        if '01e2a074' in task_id_lower:
            return '🤝 Invite Friend'
        if '01e2a075' in task_id_lower:
            return '👤 Complete Profile'
        
        if len(task_id) >= 8:
            return f'📋 Task {task_id[-8:].upper()}'
        return f'📋 Task {task_id[:6]}'
    
    def claim_task(self, token, task_id):
        url = f"{self.base_url}/airdrop/user/v1/social/claim/{task_id}"
        result = self.make_request('POST', url, token, {"evidence": task_id})
        
        if result:
            if result.get('code') == 'OK' or result.get('message') == 'OK':
                reward = result.get('data', {}).get('pointReward', 40)
                task_name = self.get_task_name(task_id)
                
                self.cycle_stats['earned'] += reward
                self.cycle_stats['completed'] += 1
                self.total_stats['earned'] += reward
                self.total_stats['completed'] += 1
                
                return True, reward, task_name
            elif result.get('code') == 'ALREADY_CLAIMED':
                return False, 0, self.get_task_name(task_id)
        
        self.cycle_stats['failed'] += 1
        self.total_stats['failed'] += 1
        return False, 0, self.get_task_name(task_id)
    
    def print_cycle_completion(self):
        if self.cycle_stats['completed'] > 0 or self.cycle_stats['failed'] > 0:
            print(f"\n{Fore.CYAN}{Back.BLACK}╔{'═'*50}╗{Style.RESET_ALL}")
            print(f"{Fore.CYAN}{Back.BLACK}║{Fore.WHITE}{Back.BLACK}📊 CYCLE SUMMARY{Style.RESET_ALL}{Fore.CYAN}{Back.BLACK} {' ' * 35}║{Style.RESET_ALL}")
            print(f"{Fore.CYAN}{Back.BLACK}╠{'═'*50}╣{Style.RESET_ALL}")
            if self.cycle_stats['completed'] > 0:
                print(f"{Fore.CYAN}{Back.BLACK}║{Style.RESET_ALL}   ✅ COMPLETED: {Fore.GREEN}{self.cycle_stats['completed']:>3}{Style.RESET_ALL} TASKS              {Fore.CYAN}{Back.BLACK}║{Style.RESET_ALL}")
                print(f"{Fore.CYAN}{Back.BLACK}║{Style.RESET_ALL}   💰 EARNED: {Fore.GREEN}{self.cycle_stats['earned']:>6}{Style.RESET_ALL} POINTS            {Fore.CYAN}{Back.BLACK}║{Style.RESET_ALL}")
            if self.cycle_stats['failed'] > 0:
                print(f"{Fore.CYAN}{Back.BLACK}║{Style.RESET_ALL}   ❌ FAILED: {Fore.RED}{self.cycle_stats['failed']:>5}{Style.RESET_ALL} TASKS              {Fore.CYAN}{Back.BLACK}║{Style.RESET_ALL}")
            print(f"{Fore.CYAN}{Back.BLACK}╚{'═'*50}╝{Style.RESET_ALL}\n")
        
        self.cycle_stats = {'earned': 0, 'completed': 0, 'failed': 0}
    
    def print_task_result(self, success, reward, task_name):
        if success:
            print(f"{Fore.GREEN}  └─✅ {task_name} • +{reward} PTS{Style.RESET_ALL}")
        else:
            print(f"{Fore.YELLOW}  └─⏭️  {task_name} • ALREADY DONE{Style.RESET_ALL}")
    
    def animate_cooldown(self, minutes):
        for remaining in range(minutes, 0, -1):
            elapsed = minutes - remaining
            percentage = int((elapsed / minutes) * 100)
            bars = 40
            filled = int(bars * elapsed / minutes)
            bar = '█' * filled + '░' * (bars - filled)
            next_time = datetime.fromtimestamp(datetime.now().timestamp() + (remaining * 60)).strftime('%H:%M:%S')
            print(f"\r{Fore.BLUE}⏳ COOLDOWN: [{bar}] {percentage}% | NEXT: {next_time} | {remaining:2d} MIN{Style.RESET_ALL}", end='', flush=True)
            time.sleep(60)
        print()
    
    def run(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(BANNER)
        
        tokens = self.read_tokens()
        if not tokens:
            print(f"\n{Fore.RED}⚠️ NO TOKENS FOUND - Add to tokens.txt{Style.RESET_ALL}")
            return
        
        print(f"\n{Fore.GREEN}✅ LOADED {len(tokens)} ACCOUNT{'S' if len(tokens)>1 else ''}{Style.RESET_ALL}")
        time.sleep(1.5)
        
        cycle = 0
        while True:
            cycle += 1
            print(f"\n{Fore.YELLOW}{'═'*60}{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}🌀 CYCLE #{cycle:03d} • {datetime.now().strftime('%H:%M:%S')}{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}{'═'*60}{Style.RESET_ALL}\n")
            
            for idx, token in enumerate(tokens):
                print(f"{Fore.CYAN}┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓{Style.RESET_ALL}")
                print(f"{Fore.CYAN}┃{Style.RESET_ALL}  👤 ACCOUNT #{idx+1:02d}{' ' * 50}{Fore.CYAN}┃{Style.RESET_ALL}")
                print(f"{Fore.CYAN}┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛{Style.RESET_ALL}")
                
                mining = self.get_mining_data(token)
                
                if mining and 'data' in mining:
                    data = mining['data']
                    balance = data.get('mUn', 0)
                    is_mining = data.get('isMining', False)
                    
                    status = f"{Fore.GREEN}● ACTIVE{Style.RESET_ALL}" if is_mining else f"{Fore.RED}○ INACTIVE{Style.RESET_ALL}"
                    
                    print(f"  {Fore.CYAN}💰 Balance:{Style.RESET_ALL} {Fore.WHITE}{balance:>11,}{Style.RESET_ALL}")
                    print(f"  {Fore.CYAN}⛏️  Status:{Style.RESET_ALL} {status}")
                    
                    if not is_mining:
                        if self.start_mining(token):
                            time.sleep(2)
                    
                    tasks = self.get_tasks(token)
                    
                    if tasks:
                        unclaimed = [t for t in tasks if isinstance(t, dict) and not t.get('claimed', False)]
                        
                        if unclaimed:
                            print(f"\n  {Fore.MAGENTA}📋 PENDING MISSIONS:{Style.RESET_ALL} {len(unclaimed)}")
                            print()
                            
                            for i, task in enumerate(unclaimed, 1):
                                task_id = task.get('id', '')
                                if task_id:
                                    print(f"  {Fore.YELLOW}{i:2d}.{Style.RESET_ALL} ", end='')
                                    success, reward, task_name = self.claim_task(token, task_id)
                                    self.print_task_result(success, reward, task_name)
                                    time.sleep(1)
                        else:
                            print(f"\n  {Fore.GREEN}✨ ALL MISSIONS COMPLETE!{Style.RESET_ALL}")
                    else:
                        print(f"\n  {Fore.YELLOW}⚠️ No missions available{Style.RESET_ALL}")
                else:
                    print(f"\n  {Fore.RED}❌ Connection failed{Style.RESET_ALL}")
                
                print(f"\n{Fore.CYAN}{'─'*60}{Style.RESET_ALL}\n")
                time.sleep(2)
            
            self.print_cycle_completion()
            
            print(f"{Fore.BLUE}{'═'*60}{Style.RESET_ALL}")
            print(f"{Fore.BLUE}🌙 COOLDOWN • 60 MINUTES{Style.RESET_ALL}")
            print(f"{Fore.BLUE}{'═'*60}{Style.RESET_ALL}\n")
            
            self.animate_cooldown(60)

if __name__ == "__main__":
    try:
        setup_interface()
        bot = UnichBot()
        bot.run()
    except KeyboardInterrupt:
        print(f"\n\n{Fore.RED}👋 BOT STOPPED • MEJRI02{Style.RESET_ALL}\n")
        sys.exit(0)
