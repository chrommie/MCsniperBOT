import logging.handlers
import os
import sys
from datetime import datetime

import discord
from discord.ext import commands

import config
from database.postgres_handler import setup_tables

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s | %(asctime)s | %(name)s | %(message)s",
    handlers=[
        logging.StreamHandler(stream=sys.stdout),
    ],
)

start_time = datetime.now().strftime("%d/%m/%Y | %H:%M")


class MCsniperBOT(commands.AutoShardedBot):
    def __init__(self):
        super().__init__(
            command_prefix=config.PREFIX,
            case_insensitive=True,
            intents=discord.Intents.all(),
        )

    async def on_ready(self):
        self.remove_command("help")
        await setup_tables()
        await self.cog_loader()

    async def cog_loader(self, directory="./cogs"):
        for file in os.listdir(directory):
            if file.endswith(".py"):
                self.load_extension(f"{directory[2:].replace('/', '.')}.{file[:-3]}")
                print(f"=> {file[:-3]} Loaded")
            elif not (file in ["__pycache__"] or file.endswith(("pyc", "txt"))):
                print(f"[{file}]")
                await self.cog_loader(f"{directory}/{file}")

    async def on_command_error(self, ctx, error):
        ignored = (
            commands.CommandNotFound,
            commands.DisabledCommand,
            commands.NoPrivateMessage,
            commands.CheckFailure,
        )

        if isinstance(error, ignored):
            return

        if hasattr(ctx.command, "on_error"):
            return

        error = getattr(error, "original", error)

        raise error


if __name__ == "__main__":
    MCsniperBOT().run(config.TOKEN)
