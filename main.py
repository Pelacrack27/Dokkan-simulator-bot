import discord
import random
import neverSleep

client = discord.Client()

featured_ssr_goku2 = [
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/7/73/Card_1024280_thumb.png/revision/latest/scale-to-width-down/120?cb=20220426040336",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/a/ae/Card_1024310_thumb.png/revision/latest/scale-to-width-down/120?cb=20220426060801",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/2/20/Card_1017880_thumb.png/revision/latest/scale-to-width-down/120?cb=20190829035025",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/3/31/Card_1022640_thumb.png/revision/latest/scale-to-width-down/120?cb=20211230080241",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/b/bf/Card_1021320_thumb.png/revision/latest/scale-to-width-down/120?cb=20210331131538",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/9/98/Card_1019580_thumb.png/revision/latest/scale-to-width-down/120?cb=20201105071645",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/c/c3/Card_1021800_thumb.png/revision/latest/scale-to-width-down/120?cb=20210809081331",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/d/d0/Card_1018110_thumb.png/revision/latest/scale-to-width-down/120?cb=20200202233829"
]

featured_ssr_cell = [
    "<https://static.wikia.nocookie.net/dbz-dokkanbattle/images/1/11/Card_1024370_thumb.png/revision/latest/scale-to-width-down/120?cb=20220426051407",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/1/1c/Card_1024240_thumb.png/revision/latest/scale-to-width-down/120?cb=20220426063352",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/8/8b/Card_1017610_thumb.png/revision/latest/scale-to-width-down/120?cb=20190829035023",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/2/28/Card_1022820_thumb.png/revision/latest/scale-to-width-down/120?cb=20211202073154",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/8/89/Card_1021280_thumb.png/revision/latest/scale-to-width-down/120?cb=20210331131353",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/2/24/Card_1019620_thumb.png/revision/latest/scale-to-width-down/120?cb=20201106101145",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/3/35/Card_1020080_thumb.png/revision/latest/scale-to-width-down/120?cb=20201004105257",
    "<https://static.wikia.nocookie.net/dbz-dokkanbattle/images/8/8a/Card_1018260_thumb.png/revision/latest/scale-to-width-down/120?cb=20200402002017"
]

featured_ssr_gohan = [
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/d/dc/Card_1011810_thumb.png/revision/latest/scale-to-width-down/120?cb=20171228080425",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/9/96/Card_1013850_thumb.png/revision/latest/scale-to-width-down/120?cb=20181212001716",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/f/f1/Card_1011050_thumb.png/revision/latest/scale-to-width-down/120?cb=20171211083850"
]

featured_ssr_buu = [
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/6/6b/Card_1001960_thumb.png/revision/latest/scale-to-width-down/120?cb=20151022175148",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/b/b4/Card_1020520_thumb.png/revision/latest/scale-to-width-down/120?cb=20200829051523",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/a/aa/Card_1008140_thumb.png/revision/latest/scale-to-width-down/120?cb=20160901130901",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/c/cf/Card_1001970_thumb.png/revision/latest/scale-to-width-down/120?cb=20151022214945",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/4/4b/Card_1001950_thumb.png/revision/latest/scale-to-width-down/120?cb=20180901002337",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/7/72/Card_1018670_thumb.png/revision/latest/scale-to-width-down/120?cb=20200507075541",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/d/d7/Card_1013180_thumb.png/revision/latest/scale-to-width-down/120?cb=20180708215012",
]

cualquier_sr_gohan = [
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/3/39/Card_1011790_thumb.png/revision/latest/scale-to-width-down/120?cb=20171228080455",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random"
]

cualquier_sr_buu = [
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/b/bd/Card_1003550_thumb.png/revision/latest/scale-to-width-down/120?cb=20150925221457",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/d/dc/Card_1010590_thumb.png/revision/latest/scale-to-width-down/120?cb=20170925121648",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/f/fa/Card_1004560_thumb.png/revision/latest/scale-to-width-down/120?cb=20160403133232",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/d/d7/Card_1003820_thumb.png/revision/latest/scale-to-width-down/120?cb=20151026231413",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/9/90/Card_1001980_thumb.png/revision/latest/scale-to-width-down/120?cb=20151022215410",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random"
]

cualquier_sr_goku2 = [
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/4/40/Card_1001720_thumb.png/revision/latest/scale-to-width-down/120?cb=20150914221625",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/6/65/Card_1003750_thumb.png/revision/latest/scale-to-width-down/120?cb=20151026231128",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/6/62/Card_1001990_thumb.png/revision/latest/scale-to-width-down/120?cb=20151009162655",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/9/9a/Card_1001120_thumb.png/revision/latest/scale-to-width-down/120?cb=20150925131432",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random"
]

cualquier_sr_cell = [
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/4/4f/Card_1000080_thumb.png/revision/latest/scale-to-width-down/120?cb=20150922211527",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/5/52/Card_1002790_thumb.png/revision/latest/scale-to-width-down/120?cb=20171123185807",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/b/b9/Card_1003250_thumb.png/revision/latest/scale-to-width-down/120?cb=20151015213043",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random"
]


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

    activity = discord.Game(name="!ayuda - summons disponibles")
    await client.change_presence(status=discord.Status.online,
                                 activity=activity)


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    if msg.startswith("!ayuda"):
        await message.channel.send("!multigoku - Multisummon goku dokkan fest")
        await message.channel.send("!multicell - Multisummon cell dokkan fest")
        await message.channel.send("!multizdokkan - Multisummon Extreme Z dokkan fest")
        await message.channel.send("!multibuu - Multisummon majin buu saga")
      

    if msg.startswith("!multigoku"):
        await message.channel.send("**Empezando multisummon:**")
        await message.channel.send("SSR Cell INT (LR) - 5 puntos")
        await message.channel.send("featured SSR - 3 puntos")
        await message.channel.send("SSR cualquiera - 2 puntos")
        await message.channel.send("SR - 1 punto")
        await message.channel.send(
            "https://c.tenor.com/E30Z_TKyvn4AAAAd/dokkan-summon.gif")
        puntos = 0
        if random.randint(1, 10000) >= 9500:
            random1 = random.choice(featured_ssr_goku2)
            await message.channel.send(random1)
            if random1 == "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/2/20/Card_1017880_thumb.png/revision/latest/scale-to-width-down/120?cb=20190829035025":
                puntos = puntos + 5
            else:
                puntos = puntos + 3
        else:
            await message.channel.send(
                "<:SSR_eclair:971672682712141844> Random")
            puntos = puntos + 2
        for i in range(0, 9):
            numero = random.randint(1, 10000)
            if numero >= 9500:
                random2 = random.choice(featured_ssr_goku2)
                await message.channel.send(random2)
                if random2 == "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/2/20/Card_1017880_thumb.png/revision/latest/scale-to-width-down/120?cb=20190829035025":
                    puntos = puntos + 5
                else:
                    puntos = puntos + 3
            elif numero >= 9000:
                await message.channel.send(
                    "<:SSR_eclair:971672682712141844> Random")
                puntos = puntos + 2
            elif numero >= 3000:
                await message.channel.send(random.choice(cualquier_sr_goku2))
                puntos = puntos + 1
            else:
                await message.channel.send(
                    "<:R_eclair:971673105024045056> Personaje kk")
        await message.channel.send("Total de puntos:")
        await message.channel.send(puntos)
        await message.channel.send("**Multisummon finalizado**")

    if msg.startswith("!multicell"):
        await message.channel.send("**Empezando multisummon:**")
        await message.channel.send("SSR Gohan SSJ (LR) - 5 puntos")
        await message.channel.send("featured SSR - 3 puntos")
        await message.channel.send("SSR cualquiera - 2 puntos")
        await message.channel.send("SR - 1 punto")
        await message.channel.send(
            "https://c.tenor.com/E30Z_TKyvn4AAAAd/dokkan-summon.gif")
        puntos = 0
        if random.randint(1, 10000) >= 9500:
            random1 = random.choice(featured_ssr_cell)
            await message.channel.send(random1)
            if random1 == "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/8/8b/Card_1017610_thumb.png/revision/latest/scale-to-width-down/120?cb=20190829035023":
                puntos = puntos + 5
            else:
                puntos = puntos + 3
        else:
            await message.channel.send(
                "<:SSR_eclair:971672682712141844> Random")
            puntos = puntos + 2
        for i in range(0, 9):
            numero = random.randint(1, 10000)
            if numero >= 9500:
                random2 = random.choice(featured_ssr_cell)
                await message.channel.send(random2)
                if random2 == "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/8/8b/Card_1017610_thumb.png/revision/latest/scale-to-width-down/120?cb=20190829035023":
                    puntos = puntos + 5
                else:
                    puntos = puntos + 3
            elif numero >= 9000:
                await message.channel.send(
                    "<:SSR_eclair:971672682712141844> Random")
                puntos = puntos + 2
            elif numero >= 3000:
                await message.channel.send(random.choice(cualquier_sr_cell))
                puntos = puntos + 1
            else:
                await message.channel.send(
                    "<:R_eclair:971673105024045056> Personaje kk")
        await message.channel.send("Total de puntos:")
        await message.channel.send(puntos)
        await message.channel.send("**Multisummon finalizado**")

    if msg.startswith("!multizdokkan"):
        await message.channel.send("**Empezando multisummon:**")
        await message.channel.send("featured SSR - 3 puntos")
        await message.channel.send("SSR cualquiera - 2 puntos")
        await message.channel.send("SR - 1 punto")
        await message.channel.send(
            "https://c.tenor.com/E30Z_TKyvn4AAAAd/dokkan-summon.gif")
        puntos = 0
        if random.randint(1, 10000) >= 9500:
            random1 = random.choice(featured_ssr_gohan)
            await message.channel.send(random1)
            puntos = puntos + 3
        else:
            await message.channel.send(
                "<:SSR_eclair:971672682712141844> Random")
            puntos = puntos + 2
        for i in range(0, 9):
            numero = random.randint(1, 10000)
            if numero >= 9500:
                random2 = random.choice(featured_ssr_gohan)
                await message.channel.send(random2)
                puntos = puntos + 3
            elif numero >= 9000:
                await message.channel.send(
                    "<:SSR_eclair:971672682712141844> Random")
                puntos = puntos + 2
            elif numero >= 3000:
                await message.channel.send(random.choice(cualquier_sr_gohan))
                puntos = puntos + 1
            else:
                await message.channel.send(
                    "<:R_eclair:971673105024045056> Personaje kk")
        await message.channel.send("Total de puntos:")
        await message.channel.send(puntos)
        await message.channel.send("**Multisummon finalizado**")

    if msg.startswith("!multibuu"):
        await message.channel.send("**Empezando multisummon:**")
        await message.channel.send("featured SSR - 3 puntos")
        await message.channel.send("SSR cualquiera - 2 puntos")
        await message.channel.send("SR - 1 punto")
        await message.channel.send(
            "https://c.tenor.com/E30Z_TKyvn4AAAAd/dokkan-summon.gif")
        puntos = 0
        if random.randint(1, 10000) >= 9500:
            random1 = random.choice(featured_ssr_buu)
            await message.channel.send(random1)
            puntos = puntos + 3
        else:
            await message.channel.send(
                "<:SSR_eclair:971672682712141844> Random")
            puntos = puntos + 2
        for i in range(0, 9):
            numero = random.randint(1, 10000)
            if numero >= 9500:
                random2 = random.choice(featured_ssr_buu)
                await message.channel.send(random2)
                puntos = puntos + 3
            elif numero >= 9000:
                await message.channel.send(
                    "<:SSR_eclair:971672682712141844> Random")
                puntos = puntos + 2
            elif numero >= 3000:
                await message.channel.send(random.choice(cualquier_sr_buu))
                puntos = puntos + 1
            else:
                await message.channel.send(
                    "<:R_eclair:971673105024045056> Personaje kk")
        await message.channel.send("Total de puntos:")
        await message.channel.send(puntos)
        await message.channel.send("**Multisummon finalizado**")


neverSleep.awake('https://DokkansimulatorV2.pelayomuniz.repl.co', False)
client.run("OTcxMzU4MDk1NDc5NTYyMjg0.G9WcEU.sq0DY1ihQ_qzD4nVFMgtr2pV88uCtG9ZOsKlyI")
