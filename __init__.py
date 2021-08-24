icon_colors = {
    'github': '4078C0',
    'youtube':'CD201F',
    'facebook':'1877F2',
    'twitter':'1DA1F2',
    'instagram': 'E4405F',
    'bootstrap': '0275D8',
    'google': '4285F4',
    'reddit': 'FF5700',
    'rss': 'EE802F',
    'skype': '00AFF0',
    'slack': '3AAF85',
    'discord': '5865F2',
    'twitch': '6441A5',
    'whatsapp': '25D366',
}

def set_color(color: str) -> str:
    return icon_colors.get(color, color)