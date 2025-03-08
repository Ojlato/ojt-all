const TelegramBot = require('node-telegram-bot-api');
const token = '7789371758:AAG8lND1uESoWYKm7fhb2G_o0p9ThypH4-A';
const bot = new TelegramBot(token, { polling: true });
const { default: axios } = require('axios');
const { regexp } = require('assert-plus');

async function prise(symbol) {
    const to=Math.floor(Date.now()/1000);
    const from=to-86400;
    const Response=await axios.get(`https://api.nobitex.ir/market/udf/history?symbol=${symbol}&resolution=D&from=${from}&to=${to}`);
    // console.log(Response.data)
    if (Response.data["s"] == "ok"); {
        return Response.data["c"];
    }
}

let symbolsMessage = "";
async function getSymbolsListMessage() {
    symbolsMessage = "";
    const response = await axios.get("https://api.nobitex.net/v2/orderbook/all");
    for (const symbol in response.data) {
        symbolsMessage += ` ${symbol}
`
    };return symbolsMessage
};getSymbolsListMessage()

const Regex = /irt$/i;
bot.on("text", async (msg) => {
    const chatId = msg.chat.id;
    const userMessage = msg.text;
    let notControllerMessage = true;
    if (userMessage == "/start") {
        notControllerMessage = false;
        bot.sendMessage(chatId, 'به بخش قیمت لحظه ای ارزها خوش آمدید', {
            reply_markup: {
                keyboard: [
                    [{ text: "لیست نمادها" }]
                ],resize_keyboard: true,
                one_time_keyboard: false
            }
        });};if (userMessage == "لیست نمادها") {
        notControllerMessage = false;
        bot.sendMessage(chatId, symbolsMessage)
    };if (Regex.test(userMessage)) {
        const p = await prise(userMessage);
        notControllerMessage = false;
        bot.sendMessage(chatId, `قیمت ارز موردنظر شما ${p} تومان است`);
    };if (notControllerMessage) {
        bot.sendMessage(chatId, 'لطفا از بحث خارج نشوید و از دستورات موجود استفاده کنید');
    }});console.log("Symbol Fetched..");
