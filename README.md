# Emu Bot (forked)
Emu Bot (forked) is a Discord bot that enables users start and close game servers.

## Features
1. `!startserver <sever_name>` starts the server named
2. `!closeserver <sever_name>` closes the server named
3. `!listservers`  list all servers available

The bot is able to start or close game servers via batch files or shell scripts.  An example start batch file:
```
@echo off
echo Checking for updates...
cd C:\Programs\steamcmd
steamcmd.exe +force_install_dir C:\gameservers\starrupture +login anonymous +app_update 3809400 +quit

echo Launching server
cd C:\gameservers\starrupture
start .\StarRuptureServerEOS.exe ^
 -Log ^
 -Port=9777 ^
 -ServerName="Here comes the Boom"
 ```

## Limitations
Emu Bot (forked) is currently hosted using the popular method of [Replit](https://replit.com/) and [UptimeRobot](https://uptimerobot.com/). Since Replit utilizes cloud computing, certain Python packages, including the `os` package, are different from their local machine counterparts. As a result, when Emu Bot is running in the cloud, it is unable to perform the `!startserver` and `!closeserver` commands. However, when the bot is run locally on my desktop, it allows users in (a) server(s) with Emu Bot to both remotely start and close the dedicated server.
