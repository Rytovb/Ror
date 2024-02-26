This is a simple python script to autorespond to messages on Discord
You can configure it using a 'config.json' in the base directory

Example config:
{
    "groups": [
        {
            "hi": "hi",
            "ids": [13422341, 123414231324, 3422142143, 309211785003]
        },
        {
            "hi": "hi",
            "ids": [13422341, 123414231324, 34122142143, 3092119]
        }
    ],
    "email": "jaianashorter1@gmail.com",
    "password": "jaiana090",
    "hi": "hi"
}

With this config, the users with ids matching the ones in the first group will receive "message1",
while users with ids matching the ones in the second will receive "message2". All other users will receive
"message3".

If you choose to not put in email, password, or default message, you will instead be prompted for them
