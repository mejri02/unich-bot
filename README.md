# Unich Auto BOT

An automated bot for Unich airdrop platform that handles mining, task completion, and account management.

[![GitHub](https://img.shields.io/badge/GitHub-mejri02-blue?style=flat&logo=github)](https://github.com/mejri02/unich-bot)
[![Python](https://img.shields.io/badge/Python-3.8+-green?style=flat&logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Features

- 🔄 **Automatic Mining**: Starts and manages mining sessions automatically
- ✅ **Task Automation**: Completes available tasks and claims rewards
- 🔐 **Multi-Account Support**: Manage multiple accounts simultaneously
- 🌐 **Proxy Support**: Run with HTTP/SOCKS4/SOCKS5 proxies with rotation capability
- 🔒 **Token Management**: Automatic token validation and expiration checking
- 📊 **Real-time Logging**: Detailed console output with colored formatting
- ⚡ **Async Operations**: Fast and efficient async/await implementation
- 🔄 **Auto-retry**: Built-in retry mechanism for failed requests

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/mejri02/unich-bot.git
   cd unich-bot
   ```

2. **Install required dependencies**
   ```bash
   pip install -r requirements.txt
   ```

   or install manually:
   ```bash
   pip install aiohttp aiohttp-socks colorama pytz
   ```

## Configuration

### 1. Get Your Token

1. Visit [Unich Airdrop](https://unich.com/en/airdrop/sign-up?ref=3X1BES)
2. Sign up or log in to your account
3. Open browser Developer Tools (F12)
4. Go to the **Network** tab
5. Refresh the page or perform any action on the site
6. Look for API requests to `api.unich.com`
7. Click on any request and go to the **Headers** section
8. Find the **Authorization** header in the Request Headers
9. Copy the token value after `Bearer ` (without "Bearer " prefix)

### 2. Setup Token File

Create a `tokens.txt` file in the bot directory and add your tokens (one per line):

```
your_token_here
another_token_here
```

### 3. Setup Proxy (Optional)

Create a `proxy.txt` file in the bot directory and add your proxies (one per line):

**Supported formats:**
```
http://username:password@host:port
http://host:port
socks4://host:port
socks5://username:password@host:port
```

**Example:**
```
http://user123:pass456@proxy1.example.com:8080
socks5://10.0.0.1:1080
http://proxy2.example.com:3128
```

## Usage

1. **Run the bot**
   ```bash
   python bot.py
   ```

2. **Select proxy mode**
   ```
   1. Run With Proxy
   2. Run Without Proxy
   Choose [1/2] ->
   ```

3. **If using proxy, choose rotation option**
   ```
   Rotate Invalid Proxy? [y/n] ->
   ```

The bot will then:
- Validate all tokens
- Process each account automatically
- Start mining sessions
- Complete available tasks
- Display balance and rewards
- Wait 12 hours before repeating

## Features Breakdown

### Account Management
- Automatic token validation and expiration checking
- Multi-account processing with detailed logging
- Secure token decoding and verification

### Mining Operations
- Checks current mining status
- Automatically starts mining if not active
- Handles mining session management

### Task Completion
- Fetches available tasks
- Automatically completes unclaimed tasks
- Claims rewards for completed tasks
- Skips already completed tasks

### Proxy Support
- Multiple proxy protocol support (HTTP, SOCKS4, SOCKS5)
- Proxy rotation for failed connections
- Per-account proxy assignment
- Automatic proxy validation

### Error Handling
- Automatic retry mechanism (up to 5 retries)
- Connection validation before operations
- Detailed error logging with timestamps
- Graceful handling of expired tokens

## Output Example

```
=========================[Account 1/3]=========================
Proxy  : http://proxy.example.com:8080
Account: abc***xyz@gmail.com
Balance: 1250 FD Points
Mining : Started Successfully
Tasks  :
   Follow Twitter ✓ Completed - Reward: 100 FD Points
   Join Telegram Already Completed
   Share Post ✓ Completed - Reward: 50 FD Points
```

## Troubleshooting

### Token Issues
- **Invalid Token Data**: Your token format is incorrect. Regenerate from browser console
- **Token Already Expired**: Get a new token from the Unich platform

### Connection Issues
- **Connection Not 200 OK**: Check your internet connection or proxy settings
- **Failed to Fetch Info**: API might be down, wait and retry

### Proxy Issues
- Enable proxy rotation with `y` when prompted
- Ensure proxy format is correct
- Test proxies independently before use

## Configuration Options

The bot runs with a 12-hour cycle by default. Each cycle:
1. Processes all accounts
2. Checks and starts mining
3. Completes available tasks
4. Waits 12 hours before repeating

## Security Notes

⚠️ **Important Security Information:**
- Never share your tokens with anyone
- Keep your `tokens.txt` file secure and private
- Don't commit `tokens.txt` or `proxy.txt` to version control
- Use `.gitignore` to exclude sensitive files

## Referral Code

Support the project by using referral code: **3X1BES**

Register here: [https://unich.com/en/airdrop/sign-up?ref=3X1BES](https://unich.com/en/airdrop/sign-up?ref=3X1BES)

## Disclaimer

This bot is for educational purposes only. Use at your own risk. The author is not responsible for any account restrictions or bans that may occur from using this bot. Always follow the platform's Terms of Service.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

If you encounter any issues or have questions:
- Open an issue on [GitHub](https://github.com/mejri02/unich-bot/issues)
- Contact the developer: mejri02

## Changelog

### Version 1.0.0
- Initial release
- Multi-account support
- Automatic mining
- Task completion
- Proxy support with rotation
- Token validation

---

**Star ⭐ this repository if you find it helpful!**

Made with ❤️ by [mejri02](https://github.com/mejri02)

