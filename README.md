# Ethereum Mainnet Gas Checker + Telegram Alerts

Простой и быстрый чекер цены газа в **Ethereum Mainnet** с мгновенными уведомлениями в Telegram, когда газ падает ниже заданного порога.

Идеально для снайперов, фармеров аирдропов, деплоя контрактов и всех, кто ждёт дешёвый газ на ETH!

## 🚀 Особенности
- Обновление каждые **~6 секунд**
- Уведомления только при низком газе (настраивается)
- Уведомление, когда газ снова вырос
- Минимальная нагрузка
- Работает **24/7** на VPS, Render, Railway, Fly.io или домашнем ПК

---

## 📦 Установка и запуск

### 1. Клонирование репозитория

```bash
git clone https://github.com/hudsoonme/ethereum-gas-checker.git
cd ethereum-gas-checker
```

---

### 2. Установка зависимостей

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

### 3. Настройка `.env`

```bash
cp .env.example .env
nano .env
```

Пример содержимого:

```
TELEGRAM_BOT_TOKEN=123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11
TELEGRAM_CHAT_ID=-1001234567890
GAS_THRESHOLD_GWEI=15       # ниже какого газа слать алерт (рекомендуется 10–20)
CHECK_INTERVAL=6
```

---

## 🤖 Создание Telegram-бота

1. Написать **@BotFather**  
2. Команда `/newbot` → придумать имя → получить токен  
3. Написать своему боту любое сообщение  
4. Узнать `chat_id`:  

```
https://api.telegram.org/bot<ТОКЕН>/getUpdates
```

или использовать **@userinfobot**

---

## ▶️ Запуск

### Быстрый запуск в screen

```bash
screen -S ethgas
python checker.py
```

Отсоединиться: **Ctrl + A**, затем **D**  
Вернуться:

```bash
screen -r ethgas
```

---

## 🟢 Запуск 24/7

### 1) Через `screen` (самый простой вариант)

```bash
screen -S ethgas
python checker.py
```

---

### 2) Через `systemd` (VPS)

Создать сервис:

```bash
sudo nano /etc/systemd/system/ethgas.service
```

Содержимое файла:

```ini
[Unit]
Description=Ethereum Gas Checker
After=network.target

[Service]
WorkingDirectory=/home/user/ethereum-gas-checker
ExecStart=/home/user/ethereum-gas-checker/venv/bin/python /home/user/ethereum-gas-checker/checker.py
Restart=always
RestartSec=10
User=user
Environment=PYTHONUNBUFFERED=1

[Install]
WantedBy=multi-user.target
```

Активация:

```bash
sudo systemctl daemon-reload
sudo systemctl enable --now ethgas.service
```

Проверка логов:

```bash
journalctl -u ethgas.service -f
```

---

## 🎉 Готово!

Теперь ты никогда не пропустишь дешёвый газ на **Ethereum Mainnet**.  
Удачных транзакций и жирных снайпов на ETH!

Автор: **[@edotoday_eth](https://x.com/edotoday_eth)**


