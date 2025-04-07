# Last-Chaos-ep2-Docker


This repository is a **portable Dockerized adaptation** of the CentOS-based server image originally extracted from **`Pony Chaos`**. The main goal of this project is to containerize the Last Chaos EP2 private server environment, making it easier to deploy across machines running Docker, regardless of OS.

### 🛠️ Current Status

All core servers — **LoginServer**, **GameServer**, **Connector**, **Helper**, **Messenger**, and **Billing** — are properly built and launched inside Docker containers. No visible errors are thrown during the build or runtime phases, and all screen sessions appear stable (`screen -r gameserver`, etc.).

> **However**: Upon logging into an account and attempting to enter a channel, the game client displays the message:  
> `Unable to connect to gameserver.`  
>  
> This issue is still under investigation. No socket errors or crash logs are visible at this stage. If you have suggestions, feel free to open an issue or contribute.

### 🚀 Getting Started

To run this setup, all you need is Docker and Docker Compose.

1. Clone this repository
2. Build the containers:

   ```bash
   docker-compose build --no-cache
   ```
   and then

   ```bash
   docker-compose up -d
   ```
That’s it — the server stack will be running in the background.

### 💡 Inspiration
This Docker setup was heavily inspired by the work shared at:

🔗 https://github.com/splt5k/Docker-LC

Big thanks to the original author(s) for sharing such a great starting point.

### Client
the client can be aquired through this link, though I am pretty sure it should work to any EP2 client (if you can edit the ip).

https://disk.yandex.ru/d/YJ7nN3sJ7bh4s
