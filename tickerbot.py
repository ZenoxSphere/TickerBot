import discord
import yfinance as yf

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!'):
        ticker = (message.content.upper().lstrip("!"))
        stock = yf.Ticker(ticker)
        data = stock.info
        output = ("Name: " + data['longName'] + "\n" + "Ticker: " + data['symbol'] + "\n" + "Current Price: " + str(data['currentPrice']) + data['currency'] + "\n" + "Dividend: " + str(data['dividendRate']) + data['currency'])
        await message.channel.send(output)

client.run('')	# Discord bot API key goes here
