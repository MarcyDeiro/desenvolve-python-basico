import emoji

emoji_dict = {
    ":grinning:": "😀",
    ":smiley:": "😃",
    ":smile:": "😄",
    ":grin:": "😁",
    ":laughing:": "😆",
    ":sweat_smile:": "😅",
    ":joy:": "😂",
    ":rofl:": "🤣",
    ":slightly_smiling_face:": "🙂",
    ":upside_down_face:": "🙃",
    ":wink:": "😉",
    ":blush:": "😊",
    ":innocent:": "😇",
    ":heart:": "❤️",
    ":thumbs_up:": "👍",
    ":thumbs_down:": "👎",
    ":clap:": "👏",
    ":wave:": "👋",
    ":fire:": "🔥",
    ":star:": "⭐",
    ":rocket:": "🚀"
}

print("Lista de emojis disponíveis:")
for code, icon in emoji_dict.items():
    print(f"{code} -> {icon}")

frase_codificada = input("\nDigite uma frase usando os códigos de emojis acima: ")

frase_emojizada = emoji.emojize(frase_codificada, language='alias')

print("\nFrase emojizada:")
print(frase_emojizada)