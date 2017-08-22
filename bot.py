import discord
import asyncio
import random
import config
from discord.ext import commands

lista = ['NO XDDDDDD', 'Si', 'Quien sabe', 'No lo sé pero lo que si sé es que estoy to bueno.', 'Antes primero responde mi pregunta: es bueno follar con chicas 3 años menor que yo?', 'No', 'Claro que no', 'Obviamente', 'No te entendi porque estoy jugando a 240hz full hd en realidad virtual, por favor, repite de nuevo la pregunta.']
favsi = ['\U00002764', '\U0001F501']
puntuen = ['\N{KEYCAP TEN}', '1\U000020e3', '2\U000020e3', '3\U000020e3', '4\U000020e3', '5\U000020e3', '6\U000020e3', '7\U000020e3', '8\U000020e3', '9\U000020e3', '0\U000020e3']

description = '¡Hola, soy DayggerBot, el 5to bot hecho por Eleiber#9406 basado en el administrador del servidor de GuitarHeroStyles: Daygger#0021, este bot aún está en desarrollo y por ahora tiene algunos comandos administrativos y otros divertidos, esperamos que me uses bien!'

bot = commands.Bot(command_prefix='!', description=description)

@bot.event
async def on_ready():
    print('Conectado como:')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(game=discord.Game(name='!help'))
    
@bot.command()
async def say(*,message):
    """Haces que diga lo que quieras"""
    await bot.say(message)  

@bot.command(pass_context=True)
async def avatar(ctx, member : discord.Member):
    """Obtiene el avatar de un usuario."""
    await bot.say(member.avatar_url)

@bot.command(name='8ball')
async def ball():
    """Una 8ball bastante interesante"""
    await bot.say(random.choice(lista))

@bot.command()
async def repetir(times : int, content='repitiendo...'):
    """Repite un mensaje varias veces."""
    for i in range(times):
        await bot.say(content)

@bot.command()
async def invitar():
    """Comando para invitar a este bot a tu servidor"""
    invite = 'https://discordapp.com/oauth2/authorize?&client_id=' + bot.user.id + '&scope=bot&permissions=0'
    await bot.say('Aqui tienes el link para invitarme a tu servidor')
    await bot.say(invite)

@bot.command(description='Para cuando no te puedes decidir entre varias cosas.')
async def elige(*elecciones : str):
    """Elige entre varias cosas que le digas."""
    await bot.say(random.choice(elecciones))

@bot.command(pass_context=True, description='Adivina tu edad de una manera muy eficaz, acierta el 100% de las veces mientras no mientas en ninguno de los valores exigidos')
async def edad(ctx):
    """Adivina tu edad con un comando."""
    await bot.say('Adivinaremos tu edad')
    await bot.say('Por favor ingrese su edad.')
    msg = await bot.wait_for_message(author=ctx.message.author)
   
    edad = ('Tu edad es: ' + msg.content)
    await bot.say(edad)
    answ = await bot.say('Por favor díganos si el programa funcionó, reaccione con :thumbsup: o :thumbsdown:')
    def check(reaction, user):
        e = str(reaction.emoji)
        return e.startswith(('\U0001F44D', '\U0001F44E'))
    res = await bot.wait_for_reaction(message=answ, check=check)
    reactemoji = await bot.say('Gracias por valorar el comando! Estás ayudando a hacer crecer el bot!')
    
@commands.has_permissions(ban_members=True)
@bot.command(pass_context=True)
async def ban(ctx):
    """Banea a un usuario del servidor siempre y cuando tengas los permisos"""
    for member in ctx.message.mentions:
        await bot.ban(member, delete_message_days=0)
        await bot.say('El usuario ha sido baneado satisfactoriamente')

@commands.has_permissions(kick_members=True)
@bot.command(pass_context=True)
async def kick(ctx):
    """Kickea a un usuario del servidor siempre y cuando tengas los permisos"""
    for member in ctx.message.mentions:
        await bot.kick(member)
        await bot.say('El usuario ha sido kickeado satisfactoriamente')

@commands.has_permissions(ban_members=True)
@bot.command(pass_context=True)
async def unban(ctx):
    """Este comando está en desarrollo"""
    await bot.say('Este comando aun no ha sido terminado')

@bot.event
async def on_message(message):
    await bot.process_commands(message)
    if message.content.startswith('daygger'):
        await bot.send_message(message.channel, 'El mejor cantante')
    elif message.content.startswith('eleiber'):
        await bot.send_message(message.channel, 'El mejor programador de python')
    elif message.content.startswith('best'):
        await bot.send_message(message.channel, 'El depurador del universo')
    elif message.content.startswith('mega'):
        await bot.send_message(message.channel, 'El/la hermafrodita')
    elif message.content.startswith('pero'):
        await bot.send_message(message.channel, 'qxd')
    elif message.content.startswith('din00'):
        await bot.send_message(message.channel, 'El dinosaurio más cool')
    elif message.content.startswith('celestial'):
        await bot.send_message(message.channel, 'Celestina la futanari')
    elif message.content.startswith('pey'):
        await bot.send_message(message.channel, 'THIENEA GAYUAHy')
    elif message.content.startswith('andere'):
        await bot.send_message(message.channel, 'GTA San andere')
    elif "puntuen" in message.content.lower():
        await bot.add_reaction(message, emoji=random.choice(puntuen))
    elif "fav si" in message.content.lower():
        await bot.add_reaction(message, emoji=random.choice(favsi))
    elif "rt si" in message.content.lower():
        await bot.add_reaction(message, emoji=random.choice(favsi))

bot.run(config.token)
