import time
from platform import python_version

from telethon import version

from . import StartTime, catversion, get_readable_time, hmention, mention, reply_id

CAT_IMG = Config.ALIVE_PIC
CUSTOM_ALIVE_TEXT = Config.CUSTOM_ALIVE_TEXT or "๐ฐ แดส สแดแด ษช๊ฑ แดกแดสแดษชษดษข ๊ฑแดแดแดแด๊ฑ๊ฑ๊ฐแดสสส ๐ฐ"
EMOJI = Config.CUSTOM_ALIVE_EMOJI or "๐ฐ"


@bot.on(admin_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    reply_to_id = await reply_id(alive)
    uptime = await get_readable_time((time.time() - StartTime))
    _, check_sgnirts = check_data_base_heal_th()
    if CAT_IMG:
        cat_caption = f"<b>{CUSTOM_ALIVE_TEXT}</b>\n\n"
        cat_caption += f"<b>{EMOJI} ๐ญ๐๐๐ : {hmention}</b>\n"
        cat_caption += f"<b>{EMOJI} ๐ค๐น๐ฝ๐ฒ๐ถ๐ฎ :</b> <code>{uptime}</code>\n"
        cat_caption += (
            f"<b>{EMOJI} ๐๐๐ฝ๐ฑ๐ธ๐ท ๐ฟ๐ฎ๐ป๐ผ๐ฒ๐ธ๐ท :</b> <code>{python_version()}</code>\n"
        )
        cat_caption += (
            f"<b>{EMOJI} ๐ฃ๐ฎ๐ต๐ฎ๐ฝ๐ฑ๐ธ๐ท ๐ฟ๐ฎ๐ป๐ผ๐ฒ๐ธ๐ท :</b> <code>{version.__version__}</code>\n"
        )
        cat_caption += f"<b>{EMOJI} ๐ค๐ต๐ฝ๐ฒ๐ถ๐ช๐ฝ๐ฎ ๐ฟ๐ฎ๐ป๐ผ๐ฒ๐ธ๐ท :</b> <code>{catversion}</code>\n"
        cat_caption += f"<b>{EMOJI} ๐๐ช๐ฝ๐ช๐ซ๐ช๐ผ๐ฎ :</b> <code>{check_sgnirts}</code>\n\n"
        cat_caption += "    <a href = https://github.com/chrisdroid1/Ultimate2><b>๐ค๐ต๐ฝ๐ฒ๐ถ๐ช๐ฝ๐ฎ</b></a> | <a href = https://t.me/Ult_imate><b>๐๐ฑ๐ช๐ท๐ท๐ฎ๐ต</b></a> | <a href = https://t.me/Ultim_ate><b>๐๐ป๐ธ๐พ๐น</b></a>"
        await alive.client.send_file(
            alive.chat_id,
            CAT_IMG,
            caption=cat_caption,
            parse_mode="html",
            reply_to=reply_to_id,
            link_preview=False,
            allow_cache=True,
        )
        await alive.delete()
    else:
        await edit_or_reply(
            alive,
            f"<b>{CUSTOM_ALIVE_TEXT}</b>\n\n"
            f"<b>{EMOJI} ๐ญ๐๐๐ : {hmention}</b>\n"
            f"<b>{EMOJI} ๐ค๐น๐ฝ๐ฒ๐ถ๐ฎ :</b> <code>{uptime}</code>\n"
            f"<b>{EMOJI} ๐๐๐ฝ๐ฑ๐ธ๐ท ๐ฟ๐ฎ๐ป๐ผ๐ฒ๐ธ๐ท :</b> <code>{python_version()}</code>\n"
            f"<b>{EMOJI} ๐ฃ๐ฎ๐ต๐ฎ๐ฝ๐ฑ๐ธ๐ท ๐ฟ๐ฎ๐ป๐ผ๐ฒ๐ธ๐ท :</b> <code>{version.__version__}</code>\n"
            f"<b>{EMOJI} ๐ค๐ต๐ฝ๐ฒ๐ถ๐ช๐ฝ๐ฎ ๐ฟ๐ฎ๐ป๐ผ๐ฒ๐ธ๐ท :</b> <code>{catversion}</code>\n"
            f"<b>{EMOJI} ๐๐ช๐ฝ๐ช๐ซ๐ช๐ผ๐ฎ :</b> <code>{check_sgnirts}</code>\n\n"
            "    <a href = https://github.com/chrisdroid1/Ultimate2><b>๐ค๐ต๐ฝ๐ฒ๐ถ๐ช๐ฝ๐ฎ</b></a> | <a href = https://t.me/Ult_imate><b>๐๐ฑ๐ช๐ท๐ท๐ฎ๐ต</b></a> | <a href = https://t.me/Ultim_ate><b>๐๐ป๐ธ๐พ๐น</b></a>",
            parse_mode="html",
        )


@bot.on(admin_cmd(outgoing=True, pattern="ialive$"))
@bot.on(sudo_cmd(pattern="ialive$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    tgbotusername = Config.TG_BOT_USERNAME
    reply_to_id = await reply_id(alive)
    cat_caption = f"**แตหกแตโฑแตแตแตแต โฑหข แตแต แตโฟแต แดฟแตโฟโฟโฑโฟแต**\n"
    cat_caption += f"**  -๐ญ๐๐๐ :** {mention}\n"
    cat_caption += f"**  -๐๐๐ฝ๐ฑ๐ธ๐ท ๐ฟ๐ฎ๐ป๐ผ๐ฒ๐ธ๐ท  :** `{python_version()}\n`"
    cat_caption += f"**  -๐ฃ๐ฎ๐ต๐ฎ๐ฝ๐ฑ๐ธ๐ท ๐ฟ๐ฎ๐ป๐ผ๐ฒ๐ธ๐ท :** `{version.__version__}\n`"
    cat_caption += f"**  -๐ค๐ต๐ฝ๐ฒ๐ถ๐ช๐ฝ๐ฎ ๐ฟ๐ฎ๐ป๐ผ๐ฒ๐ธ๐ท :** `{catversion}`\n"
    results = await bot.inline_query(tgbotusername, cat_caption)  # pylint:disable=E0602
    await results[0].click(alive.chat_id, reply_to=reply_to_id, hide_via=True)
    await alive.delete()


# UniBorg Telegram UseRBot
# Copyright (C) 2020 @UniBorg
# This code is licensed under
# the "you can't use this for anything - public or private,
# unless you know the two prime factors to the number below" license
# 543935563961418342898620676239017231876605452284544942043082635399903451854594062955
# เดตเดฟเดตเดฐเดฃเด เดเดเดฟเดเตเดเตเดฎเดพเดฑเตเดฑเดฟเดเตเดเตเดฃเตเดเต เดชเตเดเตเดจเตเดจเดตเตผ
# เดเตเดฐเตเดกเดฟเดฑเตเดฑเต เดตเตเดเตเดเดพเตฝ เดธเดจเตเดคเตเดทเดฎเต เดเดณเตเดณเต..!
# uniborg


def check_data_base_heal_th():
    # https://stackoverflow.com/a/41961968
    is_database_working = False
    output = "No Database is set"
    if not Config.DB_URI:
        return is_database_working, output
    from userbot.plugins.sql_helper import SESSION

    try:
        # to check database we will execute raw query
        SESSION.execute("SELECT 1")
    except Exception as e:
        output = f"โ {str(e)}"
        is_database_working = False
    else:
        output = "Functioning"
        is_database_working = True
    return is_database_working, output


CMD_HELP.update(
    {
        "alive": "__**PLUGIN NAME :** Alive__\
      \n\n๐** CMD โฅ** `.alive`\
      \n**USAGE   โฅ  **To see wether your bot is working or not.\
      \n\n๐** CMD โฅ** `.ialive`\
      \n**USAGE   โฅ  **__Status of bot will be showed by inline mode with button__."
    }
)
