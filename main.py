import discord

client = discord.Client()
prefix = "!!"


#Help functions for events

def get_parameters(message):
    args = message.content.split()
    return args

def clamp(n, minn, maxn):
    return max(min(maxn, n), minn)

#Events

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):

    #Protects from potential loops from the bot itself.
    if message.author == client.user:
        return

    #Help menu
    if message.content.lower().startswith(prefix + 'help'):
        await show_help(message)

    #Create Temporary Voice Channel
    if message.content.lower().startswith(prefix + 'voice'):
        await create_voice(message)

@client.event
async def show_help(message):

    commands={}
    commands[prefix+"help"] = "Prints help menu that on how to use the bot"
    commands[prefix+"voice {name} {slots}"] = "Create a Temporary Voice Channel"

    msg = discord.Embed(title='Squire Bot',description="Python bot by MorgtheBrit")

    #loop around adding commands to the embed object msg
    for command,description in commands.items():
        msg.add_field(name=command,value=description, inline=False)

    #print help menu to channel
    await message.channel.send(embed=msg)

@client.event
async def create_voice(message):

    #Specify the category
    server = message.author.guild
    vccat = server.get_channel("Channelid")

    #Extract parameters and create the voice channel
    args = get_parameters(message)

    try:
        if(len(args) == 3):
            args[2] = clamp(int(args[2]), 0, 99)

            vc = await vccat.create_voice_channel(name=args[1], user_limit=args[2])
        else:
            msg = discord.Embed(title='Opps something went wrong!' ,description='Please provide !!voice {name} {slots}')
            await message.channel.send(embed=msg)
    except discord.errors.HTTPException:
        msg = discord.Embed(title='Opps something went wrong!' ,description='Please ensure your name is between 1-99')
        await message.channel.send(embed=msg)

client.run('Token')
