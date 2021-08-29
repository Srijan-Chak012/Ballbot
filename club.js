const fetch = require("node-fetch")
const cheerio = require("cheerio")

module.exports = function (msg, args) {
    fetch("https://stackoverflow.com/questions/63141471/how-to-get-information-of-an-url-with-discord-js").then(res => res.text())
        .then(html => {
            const $ = cheerio.load(html)
            const title = $("meta[property='og:title']")[0] || $("meta[name='twitter:title']")
            const image = $("meta[property='og:image']")[0] || $("meta[name='twitter:image']")[0]
            const nothing = $("meta[property='og:thisdoesntexists']")[0] // Try get something that doesn't exists

            msg.channel.send(title ? title.attribs.content : "no title") // How to get Information of an URL with discord.js
            msg.channel.send(description ? description.attribs.content : "no description") // Short description
            msg.channel.send(image ? image.attribs.content : "no image") // https://cdn.sstatic.net/Sites/stackoverflow/Img/apple-touch-icon@2.png?v=73d79a89bded
            msg.channel.send(nothing ? nothing.attribs.content : "Literally, nothing") // Literally, nothing
        })
}
