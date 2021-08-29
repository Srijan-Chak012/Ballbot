const replies = ["your mom", "bhak bsdk", "chutiye", "fine, ye le choo choo"];

module.exports = function (msg, args) {
    console.log(args);
    keywords = args.join(" ");
    console.log(keywords);
    // const index = Math.floor(Math.random() * replies.length);
    if(keywords == "Ronaldo" || keywords == "Cristiano Ronaldo"){
        msg.channel.send("Not my :goat: ");
    } else if (keywords == "Messi" || keywords == "Lionel Messi"){
        msg.channel.send("There is only one :goat: ");
    } else if (keywords == "Pele"){
        msg.channel.send("BRB, Going to check if he's scoring goals against the dogs in my backyard");
    } else if (keywords == "Maradona"){
        msg.channel.send("All-time legend, rest in peace you god");
    } else if (keywords == "Hazard" || keywords == "Eden Hazard"){
        msg.channel.send("Dat ass tho :fire: :weary: ");
    }
};
