import discord

client = discord.Client()
prefix = "!!"

#Help functions for events

def get_parameters(message):
    args = message.content.slice(prefix.length).trim().split(/ +/g)
    args.shift().lower()
    return args

def check_cat(catname):
    if(discord.CategoryChannel(name=catname))
        return(True)
    else
        return(False)

def create_tempcat(catname):
    tempcat = create_category_channel(name=catname,position=server.channels.array().length + 1)
    return(tempcat.id)


#Events

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    #Help menu
    if message.content.lower().startswith(prefix + 'help'):
        #initialize array to allow for simple adding of additional commands
    	commands={}
        commands['!!help']='Sends the user a help menu that outlines all functionality of the bot'
    	commands['!!voice']='Create a temporary voice channel'

    	msg = discord.Embed(title='Squire Bot', description="A simple Python bot by MorgtheBrit") #initialize the embeded object
    	for command,description in commands.items(): #loop around adding commands to the embed object msg
    	       msg.add_field(name=command,value=description)
    	await message.channel.send(embed=msg) #print help menu to channel

@client.event
async def create_voice():
    if message.content.lower().startswith(prefix + 'voice'):
        if(check_cat("Temp Voice") == False)
            create_tempcat("Temp Voice")

        args[] = get_parameters(message)
        assert (args.length = 2), "You did not provide adequate information please provide !!voice {name} {slots}"
        vc = discord.VoiceChannel(name=args[0], user_limit=args[1])


client.run('Token')
