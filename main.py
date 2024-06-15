import discord
import asyncio

# Token bot Discord Anda
TOKEN = 'MTI1MDI2MjMzODAwMzY2NTA1OQ.G01YjM.lS0MA4-emGcRRKmXdHqKgItKOPOnP9ZOvupToo'

# Pesan yang ingin dikirim berulang
pesan = "kn"

# ID server tempat pesan akan dikirim
server_id = '1005847086677377134'

# Interval waktu dalam detik antara setiap pengiriman pesan
interval = 60  # Misalnya setiap 60 detik (1 menit)

client = discord.Client()

@client.event
async def on_ready():
    print(f'Bot {client.user} telah terhubung ke Discord!')

    # Menggunakan asyncio untuk mengulang pengiriman pesan setiap interval
    while True:
        await asyncio.sleep(interval)
        try:
            # Mencari objek server berdasarkan ID
            server = client.get_guild(int(server_id))
            if server:
                # Mencari channel text dengan nama tertentu di server
                channel = discord.utils.get(server.text_channels, name='nama-channel')  # Ganti 'nama-channel' dengan nama channel yang sesuai
                if channel:
                    await channel.send(pesan)
                else:
                    print(f'Channel tidak ditemukan di server dengan ID {server_id}.')
            else:
                print(f'Server dengan ID {server_id} tidak ditemukan.')
        except Exception as e:
            print(f'Error: {e}')

# Menjalankan bot dengan token yang disediakan
client.run(TOKEN)
