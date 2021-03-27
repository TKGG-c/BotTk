import discord.py
from discord.ext import commands

@client.event = commands.Bot(command_prefix="!", case_insensitive=True)

async def on_ready():
    print('BOT ONLINE {0.user}'.format(client))

@client.command()
async def Slv(ctx):
    await ctx.send(f'Ta salvado meu amigo!, {ctx.author}')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {ctx.author}')

@client.command()
async def myline(ctx):
    await ctx.send(
        f'Sua line é a LINE S1LL, Todos os jogadores da guilda é da sua line!, {ctx.author}'
    )

@client.command()
async def quediaehoje(ctx):
    await ctx.send(f'Boa tarde! Hoje é Sexta-feira, 26/03/2021, {ctx.author}')

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, user: discord.Member, *, razao='none'):
  await user.ban(reason=razao)

@client.command()
async def teste4g(ctx):
    await ctx.send(
        f'Aqui não fazemos teste no jogo, apenas mande print das suas estatiscas, abates etc. no PV do 4G Gustavinn, ir até o chat de formulário e esperar o resultado! Tmj é nois! {ctx.author}'
    )


@client.command()
async def treinos(ctx):
   embed = discord.Embed(
     title = 'Treinos semanais',
     description = 'Opa, \n Hoje é dia de treino em squad, Hoje, ás 19:00, esteja aqui e digite:\n Cade o treino?',
     colour = 2732500
   )

   embed.set_author(name='4G G4M1NG', icon_url='https://media.discordapp.net/attachments/801212774754942996/824065124716380190/i0V4JpgS5Qtnulbfppmw9x2gbS5E6UVdqqVzraF7RM22Qsf0iJ1xI4HaYIKAKKgC0CSry2yOk4RUARUAQsEVDitQROhykCioAiYI.png')

   embed.set_thumbnail(url='https://logodownload.org/wp-content/uploads/2018/09/free-fire-logo-8.png')

   embed.set_image(url='https://media.discordapp.net/attachments/801212774754942996/824065124716380190/i0V4JpgS5Qtnulbfppmw9x2gbS5E6UVdqqVzraF7RM22Qsf0iJ1xI4HaYIKAKKgC0CSry2yOk4RUARUAQsEVDitQROhykCioAiYI.png')

   embed.set_footer(text='4G | Todos os direitos reservados')

   await ctx.send(embed = embed)

@client.event
async def on_member_join(member):
  canal = client.get_channel("820787684368056320")
  regras = client.get_channel("813821163888443452")
  msg = "Seja bem vindo a 4G G4M1NG!{}. Leia as {}".format(member.mention, regras.mention)
  await client.send_message (canal, msg)

client.run('ODIxNzM2NjU2NzYyNjk5ODI2.YFID5g.WZo0qTbGfRxYaT-h1sEw1uLWYG4')
