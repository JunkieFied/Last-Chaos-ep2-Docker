# Last-Chaos-ep2-Docker

This repository is a **portable Dockerized adaptation** of the CentOS-based server image originally extracted from **`Pony Chaos`**. The main goal of this project is to containerize the Last Chaos EP2 private server environment, making it easier to deploy across machines running Docker, regardless of OS.

### Current Status

All core servers are fully operational inside Docker containers:

- **LoginServer** - User authentication (port 4001)
- **Connector** - Server assignment and routing (port 4006)
- **GameServer** - Game world (port 4101)
- **Helper / SubHelper** - Guild, ranking, trade systems
- **Messenger** - Chat and friend system (port 4105)
- **CashServer (Billing)** - Item shop and lottery

Players can log in, select a server, create characters, and enter the game world.

### Prerequisites

- **Docker Desktop** (Windows/Mac) or Docker Engine (Linux)
- **Last Chaos EP2 client** — [Download here](https://disk.360.yandex.ru/d/YJ7nN3sJ7bh4s) (includes `CheckTool.exe` for server configuration)
- ~4GB RAM available for Docker

### Getting Started

1. **Clone this repository:**
   ```bash
   git clone https://github.com/junkiefied/Last-Chaos-ep2-Docker.git
   cd Last-Chaos-ep2-Docker
   ```

2. **Build and start the containers:**
   ```bash
   docker compose build
   docker compose up -d
   ```

3. **Wait ~3 minutes** for the GameServer to fully load all game data. You can monitor progress:
   ```bash
   docker exec lc_server screen -ls
   ```

4. **Configure your game client:**
   Use `CheckTool.exe` or `PonyChaos Editor.exe` to set the server address in `sl.dta`:
   - IP: `127.0.0.1`
   - Port: `4001`

5. **Create an account:**
   ```bash
   docker exec lc_mysql mysql -u root -e "
   SET sql_mode='';
   INSERT INTO newproject_db_auth.bg_user (user_id, truepasswd, passwd, chk_service, partner_id, active_time, create_date)
   VALUES ('myuser', 'mypassword', SHA2(CONCAT('myuser','phoohie1yaihooyaequae7PuiWoeNgahjieth3ru3yeeghaepahb7aeYaipe2we6zii6mai6uweig8siasheinoungeoyeiLohShi2xoh2xi8ooxee9ahpiehahc9Phe','mypassword'),256), 'Y', 'LC', NOW(), NOW());
   SET @uid = LAST_INSERT_ID();
   INSERT INTO newproject_db_auth.t_users (a_idname, a_passwd, a_portal_index, a_end_date, a_enable)
   VALUES ('myuser', '', @uid, '2030-01-01 00:00:00', 1);
   "
   ```
   Replace `myuser` and `mypassword` with your desired credentials.

6. **Launch the game client** and log in.

### Architecture

```
Docker Host (Windows/Mac/Linux)
  |
  +-- lc_mysql (MySQL 5.7)
  |     Database with pristine game data
  |     Port 3306
  |
  +-- lc_server (CentOS 7)
        All game server binaries run here via screen sessions
        Ports: 4001, 4006, 4101, 4102, 4105, 50401
        |
        +-- Connector (registry/router)
        +-- LoginServer (authentication)
        +-- GameServer (game world)
        +-- Helper (guilds/rankings)
        +-- SubHelper (trade/data)
        +-- Messenger (chat)
        +-- CashServer (billing, runs on Mono)
```

### Technical Notes

- **LD_PRELOAD bind interceptor:** The server binaries are configured with `IP=127.0.0.1` so clients receive the correct address. A `bindfix.so` library (via `LD_PRELOAD`) intercepts `bind()` calls to change `127.0.0.1` to `0.0.0.0`, allowing Docker port forwarding to reach the services.
- **CashServer:** Runs via Mono (.NET runtime) with `MONO_IOMAP=all` for path compatibility. Copied to `/tmp/CashServer` at startup to avoid Docker volume file-locking issues.
- **MySQL 5.7** is used with `--sql-mode=""` to disable strict mode, matching the original MySQL 5.1 behavior expected by the legacy binaries.
- **Database:** A pristine SQL dump (`pristine_clean.sql`) from the original OVA is imported on first start.

### Useful Commands

```bash
# View running server screens
docker exec lc_server screen -ls

# Attach to a screen (Ctrl+A, D to detach)
docker exec -it lc_server screen -r gameserver1

# Check MySQL logs
docker logs lc_mysql --tail 20

# View server ports
docker exec lc_server netstat -tlnp

# Full restart
docker compose down && docker compose up -d
```

### Inspiration

This Docker setup was heavily inspired by the work shared at:
https://github.com/splt5k/Docker-LC

Big thanks to the original author(s) for sharing such a great starting point.
