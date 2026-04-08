import discord

# --- CONFIGURAÇÕES ---
TOKEN = 'MTQ4OTcxMjA0OTY5NjI4MDczOQ.GrURd_.AQsYhNJwVIxE2SqmQQabptCIJnZESYfpjs1Zqw'
ID_DO_CANAL_ALVO = 1489710885412012123 
ID_DO_AMIGO = 524318995822936065    

intents = discord.Intents.default()
intents.members = True 

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'✅ Bot ligado! Vigindo apenas o ID: {ID_DO_AMIGO}')

@client.event
async def on_user_update(before, after):
    if after.id == ID_DO_AMIGO:
        # Verifica se o link da imagem mudou
        if before.display_avatar.url != after.display_avatar.url:
            canal = client.get_channel(ID_DO_CANAL_ALVO)
            if canal:
                embed = discord.Embed(
                    title="📸 Alerta de Nova Foto!",
                    description=f"O teu amigo **{after.name}** mudou a foto de perfil!",
                    color=discord.Color.green()
                )
                embed.set_image(url=after.display_avatar.url)
                await canal.send(embed=embed)
                print(f"LOG: Nova foto de {after.name} enviada!")

client.run(TOKEN)