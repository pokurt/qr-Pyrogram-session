from .src import app, check_session, create_qrcodes, nearest
import threading
from pyrogram import idle
import asyncio

async def main():
    await check_session(app, nearest.nearest_dc)
    creating_qrs = threading.Thread(target=create_qrcodes, daemon=True)
    creating_qrs.start()
    await idle()


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
