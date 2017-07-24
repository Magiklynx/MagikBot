import discord  # Import the Discord programming library so you can use python with Discord
import random  # Import the random library so you can generate random numbers, or a random choice
from time import sleep  # From the time library, import sleep so we can add periods where the program will stall.

client = discord.Client()
token = '<BOT TOKEN>'

EIGHT_BALL = ["It is certain", "It is decidedly so", "Without a doubt", "Yes definitely", "You may rely on it",
			  "As I see it yes", "Most likely", "Outlook good", "Yes", "Signs point to yes", "Reply hazy try again",
			  "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again",
			  "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"]

KILL = (['a knife', 'a hammer', 'a bat', 'a piece of paper', 'an m1911', 'a nuke', 'an axe', 'a dildo'])

ADMINS = ([<LIST ADMINS>, <LIKE THIS>])

BOT = "<YOUR BOT ID>"


@client.event
async def on_ready():
	print('Logged in as ' + client.user.name + ' (ID:' + client.user.id + ')')
	print('On ' + str(len(client.servers)) + ' servers:')
	print('------')
	game = random.choice(['with your ❤', 'with Magik', 'alone', 'discord.gg/Q8JGjd3', '*help'])
	print('Playing ' + str(game))
	await client.change_presence(game=discord.Game(name=game))
	print("Loaded")


def parse_command(content):
	if not content.startswith('*'):
		return None, None
	cmd, *arg = content.strip('*').split(' ', 1)
	return cmd.lower(), arg[0] if arg else None


async def cmd_roll(message, _):
	roll_num = random.randint(0, 100)
	await client.send_message(message.channel, message.author.mention + ' your roll is ' + str(roll_num))
	print(str(message.author) + " rolled a " + str(
		roll_num) + "on server " + message.channel.server.name + " Owned by " + str(message.channel.server.owner.id))


async def cmd_8ball(message, question):
	predict = random.choice(EIGHT_BALL)
	await client.send_message(message.channel, message.author.mention + ': "' + question + '" ' + predict)
	print(str(
		message.author) + " asked the great ball " + question + "The answer was " + predict + "on server " + message.channel.server.name + " Owned by " + str(
		message.channel.server.owner.id))


async def cmd_kill(message, target_user: discord.Member = None):
	weapon = random.choice(KILL)
	if target_user is None:
		target_user = message.author.mention

	if message.author.id in ADMIN and target_user == "<@" + ADMIN[0] + ">":
		await client.send_message(message.channel, "Are you sure, mommy?")
	elif message.author.id in ADMIN and target_user == "<@" + BOT + ">":
		await client.send_message(message.channel, "I'm sorry mommy, I won't do it again.")
	elif target_user == "<@" + BOT + ">":
		await client.send_message(message.channel,
								  message.author.mention + ", you can't kill me if I kill you first :knife:.")
	else:
		await client.send_message(message.channel,
								  message.author.mention + ' has killed ' + target_user + ' with ' + weapon)
		print(str(
			message.author) + " killed " + target_user + "on server " + message.channel.server.name + " Owned by " + str(
			message.channel.server.owner.id))


async def cmd_flip(message, _):
	coin = random.choice(['Heads', 'Tails'])
	await client.send_message(message.channel, message.author.mention + ' The coin landed on: ' + coin)
	print(str(message.author) + " flipped a coin on server " + message.channel.server.name + " Owned by " + str(
		message.channel.server.owner.id))


async def cmd_say(message, _):
	if message.author.id in ADMINS:
		await client.delete_message(message)
		await client.send_message(message.channel, (parse_command(message.content))[1])
	else:
		await client.send_message(message.channel, message.content)
	print(str(message.author) + " made me say \"" + str(
		(parse_command(message.content))[1]) + "\" on server " + message.channel.server.name + " Owned by " + str(
		message.channel.server.owner.id))


async def cmd_serverinfo(message, _):
	if message.channel.server:
		await client.send_message(message.channel, 'You are currently in ' + str(message.channel) + ' (id: ' + str(
			message.channel.id) + ')')
		await client.send_message(message.channel, 'on server **' + message.channel.server.name + '** (id: ' + str(
			message.channel.server.id) + ') (region: ' + str(message.channel.server.region) + ')')
		await client.send_message(message.channel,
								  'owned by <@' + str(message.channel.server.owner.id) + '> (id: ' + str(
									  message.channel.server.owner.id) + ')')
	else:
		await client.send_message(message.channel, 'This isn\'t a server, it\'s a DM.')
	print(str(message.author) + " wanted server info on server " + message.channel.server.name + " Owned by " + str(
		message.channel.server.owner.id))


async def cmd_secret(message, _):
	await client.send_message(message.channel, 'http://i.imgur.com/OKACKPV.jpg')
	print(str(message.author) + " found the secret on server " + message.channel.server.name + " Owned by " + str(
		message.channel.server.owner.id))


async def cmd_invite(message, _):
	await client.send_message(message.channel,
							  'Click this to invite me to your discord server.\n\nhttp://magiklynx.tk/invite')
	if message.channel.server:
		print(str(message.author) + " asked for me on server " + message.channel.server.name + " Owned by " + str(message.channel.server.owner.id))
	else: 
		print(str(message.author) + " asked for me in DMs")


async def cmd_pingu(message, _):
	await client.send_message(message.channel, 'NOOT NOOT')
	print(str(message.author) + " made me pingu on server " + message.channel.server.name + " Owned by " + str(
		message.channel.server.owner.id))


async def cmd_hug(message, target_user):
	if message.author.mention == target_user:
		await client.send_message(message.channel, "You can't hug yourself!")
	else:
		await client.send_message(message.channel, target_user + " was hugged by " + message.author.mention)
		await client.send_file(message.channel, "images/hug.jpg")
	print(str(message.author) + " hugged "+ target_user + " on server " + message.channel.server.name + " Owned by " + str(
		message.channel.server.owner.id))


async def cmd_love(message, target_user):
	if target_user == "<@" + ADMIN[0] + ">":
		await client.send_message(message.channel, message.author.mention + " loves " + target_user + ". Just like everybody else")
		await client.send_file(message.channel, "images/love.jpg")
	elif message.author.mention == target_user:
		await client.send_message(message.channel, "Narcissistic much?")
	else: 
		await client.send_message(message.channel, message.author.mention + " loves " + target_user)
		await client.send_file(message.channel, "images/love.jpg")
	print(str(message.author) + " loved "+ target_user + " on server " + message.channel.server.name + " Owned by " + str(
		message.channel.server.owner.id))


async def cmd_insult(message, target_user):
	stupid = ["albatross-biting",
			  "arse-breath'd",
			  "bawdy",
			  "bear-biting",
			  "beef-witted",
			  "boil-brained",
			  "churlish",
			  "clapper-clawed",
			  "clod-brained",
			  "clumpish",
			  "cockered",
			  "cougar-fowling",
			  "dunder-headed",
			  "excrement-wallowing",
			  "fat-kidneyed",
			  "fen-sucked",
			  "fishwife-necked",
			  "flap-wagging",
			  "fusty",
			  "goatish",
			  "knotty-pated",
			  "mewling",
			  "odiferous",
			  "pelican-buggering",
			  "pigeon-liver'd",
			  "pribbling",
			  "profligate",
			  "raccoon-liver'd",
			  "reeky",
			  "rump-faced",
			  "rump-fed",
			  "rump-renting",
			  "self-rutting",
			  "shard-borne",
			  "spongy",
			  "tickle-brained",
			  "toad-spotted",
			  "unchin-snouted",
			  "weather-bitten",
			  "wind-breaking",
			  "yeasty"]

	jerk = ["basket-cockle",
			"boar-pig",
			"canker-blossom",
			"coxcomb",
			"flap-dragon",
			"flap-vampire bat",
			"flax-wench",
			"jackanapes",
			"knave",
			"miscreant",
			"nut-hook",
			"pignut",
			"pillock",
			"ratsbane",
			"scullion",
			"skainsmate",
			"skut",
			"varlot",
			"wagtail",
			"wantwit",
			"whey-face"]

	fat = ["avoirdupois",
		   "corpulent",
		   "elephantine",
		   "hogs-bodied",
		   "paunchy",
		   "plumpish",
		   "porcine",
		   "portly",
		   "rotund",
		   "swinish",
		   "thickset",
		   "whalelike"]

	lotn = ["affection-peddler",
			"bawd",
			"harlot",
			"minx",
			"profligate",
			"purveyor of the world's oldest profession",
			"rent-rump",
			"slattern",
			"strumpet"]

	activity = ["mosquito-buggering",
				"tail-leasing",
				"wainscoting"]

	animal = ["Ant",
			  "Bird",
			  "Cat",
			  "Chicken",
			  "Cow",
			  "Dog",
			  "Elephant",
			  "Fish",
			  "Fox",
			  "Horse",
			  "Kangaroo",
			  "Lion",
			  "Monkey",
			  "Penguin",
			  "Pig",
			  "Rabbit",
			  "Sheep",
			  "Tiger",
			  "Whale",
			  "Wolf"]

	relative = ["Daughter",
				"Daughter-in-law",
				"Girlfriend",
				"Granddaughter",
				"Grandmother",
				"Mother",
				"Mother-in-law",
				"Niece",
				"Sister",
				"Sister-in-law",
				"Wife"]

	insults = ["An aging, brain-addled " + random.choice(animal) + " has more brains than thou, thou " + random.choice(
		jerk) + "!",
			   "I shall not waste words with thee, but merely observe thou art a " + random.choice(
				   stupid) + " " + random.choice(stupid) + " " + random.choice(jerk) + ".",
			   "I would not expect a " + random.choice(stupid) + " " + random.choice(stupid) + " " + random.choice(
				   jerk) + " like thee to understand even the depths of thine own worthlessness!",
			   "In sooth, I have never seen a more " + random.choice(stupid) + random.choice(jerk) + " than thou!",
			   "Thou'rt a " + random.choice(fat) + " " + random.choice(stupid) + " " + random.choice(
				   jerk) + ". Be thou not cross with me, for I am but the bearer of these bad tidings.",
			   "Thou'rt so dull of wit, if I called thee a " + random.choice(stupid) + " " + random.choice(
				   stupid) + " " + random.choice(jerk) + ", thou wouldst take it as a compliment!",
			   "Verily, I am surprised that thou took time from thy busy " + random.choice(
				   activity) + " schedule to cross words with me, thou " + random.choice(jerk) + "!",
			   "Verily, thou art a " + random.choice(stupid) + " " + random.choice(jerk) + "!",
			   "What's that? Didst thou say thou art a pathetic " + random.choice(stupid) + " " + random.choice(
				   jerk) + "? Then thou speakest sooth!",
			   "Wouldst thou match wits with me, thou " + random.choice(stupid) + " " + random.choice(
				   jerk) + "? I see thou'rt unarmed for such a contest!",
			   "If brains were grain, thou wouldst not have sufficient quantity to feed thy " + random.choice(
				   fat) + " " + random.choice(relative) + "!",
			   "Thy " + random.choice(relative) + " is so " + random.choice(
				   fat) + ", when she sitteth in a hot bath, she maketh her own gravy!",
			   "Thy " + random.choice(relative) + " is a " + random.choice(fat) + " " + random.choice(
				   lotn) + ". If that offendeth thee, thou shouldst not shoot the messenger!",
			   "Thy " + random.choice(relative) + " is so " + random.choice(
				   fat) + ", when she doth sit around thy swine-pen of a house, she really sits around thy swine-pen of a house!",
			   "Thy " + random.choice(relative) + " is such a " + random.choice(stupid) + " " + random.choice(
				   stupid) + " " + random.choice(
				   lotn) + ", her attentions may be purchased with a scrap of paper enscrivened with the letters I.O.U.!",
			   "Thy " + random.choice(relative) + " is such a " + random.choice(stupid) + " " + random.choice(
				   lotn) + ", she will entertain any gentlemen with a brass farthing to spend and offer change from the transaction!"]

	if target_user == None:
		target_user = str(message.author.mention)

	await client.send_message(message.channel, target_user + ", " + random.choice(insults))
	print(str(
		message.author) + " insulted " + target_user + "on server " + message.channel.server.name + " Owned by " + str(
		message.channel.server.owner.id))


async def cmd_kick(message, _):
	def is_me(message):
		return message.author == client.user

	user = (parse_command(message.content))[1]

	if message.author.id in ADMINS:
		await client.kick(user)
		await client.send_message(message.channel, user + ' has been kicked.')
		sleep(5)
		await client.purge_from(message.channel, limit=1, check=is_me)


async def cmd_exit(message, _):
	if message.author.id in ADMINS:
		await client.send_message(message.channel, 'Oh, i-it\'s okay... I-I\'ll jus- \*crys\* just leave then.')
		await client.change_presence(game=discord.Game(name='packing her things'))
		sleep(10)
		quit()
	else:
		await client.send_message(message.channel, 'Hah, you can\'t get rid of me! Only ADMINS can do that.')
		print(str(
			message.author) + " tried to get rid of me on server " + message.channel.server.name + " Owned by " + str(
			message.channel.server.owner.id))


async def cmd_help(message, _):
	await client.send_message(message.channel, 'Okay, ' + message.author.mention + ' Check your Private Messages')
	await client.send_message(message.author, "```css\n"
											  " [Help]\n"
											  "		  roll : Roll a dice between 0 and 100.\n"
											  "	     8ball : Ask 8ball a question for a response.\n"
											  "	      kill : Kill another member with a special weapon.\n"
											  "      flipcoin : Flip a coin - Alias => coinflip.\n"
											  "	       say : Forces me to repeat what you said.\n"
											  "	     pingu : NOOT NOOT\n"
											  "	       hug : Hug that special person\n"
											  "	      love : Share your love with somebody\n"
											  "	    insult : Insults you, or who you mention\n"
											  "    serverinfo : Displays information about the server.\n"
											  "	    invite : Gives you a link to invite me to your server.\n"
											  "	      help : Displays this.\n"
											  "```")
	if message.channel.server:
		print(str(message.author) + " asked for me on server " + message.channel.server.name + " Owned by " + str(message.channel.server.owner.id))
	else: 
		print(str(message.author) + " asked for me in DMs")


commands = {
	'roll': cmd_roll,
	'8ball': cmd_8ball,
	'kill': cmd_kill,
	'flipcoin': cmd_flip,
	'coinflip': cmd_flip,
	'say': cmd_say,
	'serverinfo': cmd_serverinfo,
	'terces': cmd_secret,
	'invite': cmd_invite,
	'pingu': cmd_pingu,
	'kick': cmd_kick,
	'hug': cmd_hug,
	'love': cmd_love,
	'insult': cmd_insult,
	'fuckoff': cmd_exit,
	'gtfo': cmd_exit,
	'help': cmd_help,
}


async def think(message):
	if ':thinking:' in message.content:
		await client.add_reaction(message, ':thinking:')


@client.event
async def on_message(message):
	if message.author.bot:
		return

	cmd, arg = parse_command(message.content)
	if not cmd:
		return

	handler = commands.get(cmd)
	if handler:
		await handler(message, arg)


print('Starting...')
client.run(token)
