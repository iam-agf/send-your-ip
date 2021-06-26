# Send your IP

Sends your IP to a Telegram bot you own.
It's useful to connect your Raspberry Pi when you don't know how to leave it with a static IP.

## How it works

First of all, you must change the lines with the variables token (31) and user (32). 

##### Getting your token

To get a token, in Telegram look for the [@BotFather](https://t.me/BotFather) and create a new one with the 
command '/newbot' then just follow the instructions and you will get a token.

##### Getting your user id

Look for the bot [@JsonDumpBot](https://t.me/JsonDumpBot) , and you will receive a message that will include the
parameter "message"{"chat":{"id"}}. This number is you user id.


After getting these items, add them to the file, and run it. If something fails, you can contact me throught my [Twitter](https://twitter.com/iam_agf).


## Taking advantage in a Raspberry Pi.

To use this as a daemon each time you run your Raspberry Pi, you must follow these instructions in the terminal: First save the main file as `.ip.py` (the dot before the name is to hide the file instead of having it public) in your folder `/home/YOUR-USER-DIRECTORY`. run the command `sudo nano /etc/systemd/system/ip.service` and write in it

```
[Unit]
Description=Sends IP
Wants=network-online.target
After=network.target network-online.target

[Service]
Type=idle
WorkingDirectory=/home/YOUR-USER-DIRECTORY
ExecStart=/usr/bin/python3 /home/YOUR-USER-DIRECTORY/.ip.py
Restart=on-failure

[Install]
WantedBy=multi-user.target

```

Then save it. Now run

```
systemctl enable ip
systemctl daemon-reload
```

After this, reboot, and you will receive the message to your Telegram account.

Notice that this will only work when you're connecting to a network already registered in your Raspberry Pi, so first you will need to run your Raspberry Pi with a screen and a keyboard to make all this process. After it, next time you just turn on your Raspberry Pi it will send the message automatically without need to plug other things.
