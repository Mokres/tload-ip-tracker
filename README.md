# 🌍 TLOAD IP Tracker

Lightweight IP intelligence tool für Kali, Termux und Python

## 📌 Features
✅ Track any IPv4 address
✅ Get your own public IP
✅ Location data (Country, Region, City, ZIP)
✅ GPS coordinates
✅ ISP & Organization info
✅ VPN/Proxy detection
✅ Mobile network detection
✅ Colored interface

## 📦 Installation

### Kali Linux / Ubuntu / Debian
```bash
sudo apt update
sudo apt install python3 python3-pip -y
git clone https://github.com/Mokres/tload-ip-tracker.git
cd tload-ip-tracker
pip3 install -r requirements.txt
python3 tload.py
```

### Termux (Android)
```bash
pkg update && pkg upgrade
pkg install python git -y
git clone https://github.com/Mokres/tload-ip-tracker.git
cd tload-ip-tracker
pip install -r requirements.txt
python tload.py
```

### Windows
```bash
git clone https://github.com/Mokres/tload-ip-tracker.git
cd tload-ip-tracker
pip install -r requirements.txt
python tload.py
```

## 🚀 Usage
```bash
python3 tload.py
```
1. Select option 1 to track an IP
2. Enter IP address
3. View detailed information
4. Option 2 shows your own IP
5. Option 3 exits

## ⚙️ Requirements
- Python 3.x
- Internet connection
- API: ip-api.com (free, 45 req/min)

## 📄 License
MIT License - Free to use and modify

Created by **Mokres** ❤️