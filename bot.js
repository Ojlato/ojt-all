const TelegramBot = require('node-telegram-bot-api');
const token = '7789371758:AAG8lND1uESoWYKm7fhb2G_o0p9ThypH4-A';
const bot = new TelegramBot(token, {polling: true});

bot.on('message', (msg) => {
    const chatId = msg.chat.id;
    const usertext=msg.text;
    if(usertext=='/start') {
        bot.sendMessage(chatId,"Welcome to MyBot upgraded via NodeJS")
    }
});console.log("Loading...");
  