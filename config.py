from decouple import config

TELEGRAM_BOT_TOKEN = config('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHAT_ID    = config('TELEGRAM_CHAT_ID')
GAS_THRESHOLD_GWEI  = config('GAS_THRESHOLD_GWEI', default=15, cast=int)  # обычно ставят 10-20 gwei
CHECK_INTERVAL      = config('CHECK_INTERVAL', default=6, cast=int)
