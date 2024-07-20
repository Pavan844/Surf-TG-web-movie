from os import getenv
from dotenv import load_dotenv

load_dotenv("config.env")


class Telegram:
    API_ID = int(getenv("API_ID", "26009823"))
    API_HASH = getenv("API_HASH", "e545fc56028ee9404ef5b5bec64503ca")
    BOT_TOKEN = getenv("BOT_TOKEN", "6880540335:AAFDeWeaxU-1DMmNhi2C1IzIT6eqz1oVEn0")
    PORT = int(getenv("PORT", 8080))
    SESSION_STRING = getenv("SESSION_STRING", "BQGM4N8AeXUMX6Ry9x9vhjBLY3aiIyrlw4S0n7E9AHKBzPITDA7kthweho-G07MauJjnJYoMbiogTyjE0BeBNbNn52PoaJp5gHsEOm7GJ4ICUw8FQIKUyDiYFgqCKXTJ661pr4jRAz9MgduwZu7N_tIeA6Ed1m3cTI2BXAnW8CnmtYI8q0g7kjTdzPbCjVWrgDhbRtqJtvdD1Bkmuav9MysuOLZ1oLAIHw-BF68Jh_-HZgQQKu9XpAEqL7fVv9KxGWoG2p4obwgtGpSfHSAZn59BHZzyYGh21031VevFvAgLIh5GTXg5BDsEPkT4k8lkM81LoqAF-E4greTK3Xqw1x7Y3l_YvAAAAAGaHLavAQ")
    BASE_URL = getenv("BASE_URL").rstrip('https://perfect-valli-pavanlegend844-ad87ca49.koyeb.app/')
    DATABASE_URL = getenv("mongodb+srv://pasci55:qQojc1wFWR3toTWy@cluster0.jsv3b84.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    AUTH_CHANNEL = [channel.strip() for channel in getenv("AUTH_CHANNEL").split("-1002042127948,")]
    THEME = getenv("THEME", "quartz").lower()
    USERNAME = getenv("USERNAME", "admin")
    PASSWORD = getenv("PASSWORD", "admin")
    ADMIN_USERNAME = getenv("ADMIN_USERNAME", "pavan")
    ADMIN_PASSWORD = getenv("ADMIN_PASSWORD", "pavan@123")
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '10'))
    MULTI_CLIENT = bool(getenv('MULTI_CLIENT', 'False'))
    HIDE_CHANNEL = bool(getenv('HIDE_CHANNEL', 'False'))
