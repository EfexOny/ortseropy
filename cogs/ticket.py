import discord 

from discord.ext import commands

class Ticket(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def ticket(self, ctx):

        embed = discord.Embed(
            title="Would you like to create a ticket?", 
            description="If you have any questions or concerns create a new ticket by clicking on the emoji below this message.", 
            color=0xf7fcfd)

        embed.set_thumbnail(url="https://media.discordapp.net/attachments/869385280568852570/870361265292337252/ortsero.jpg")
        embed.set_author(name="Ortsero-Tickets")

        msg = await ctx.send(embed=embed)
        await msg.add_reaction("📩")

def setup(client):
    client.add_cog(Ticket(client))