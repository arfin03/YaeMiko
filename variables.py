# https://github.com/Infamous-Hydra/YaeMiko
# https://github.com/Team-ProjectCodeX


class Config(object):
    # Configuration class for the bot

    # Enable or disable logging
    LOGGER = True

    # <================================================ REQUIRED ======================================================>
    # Telegram API configuration
    API_ID = "23182647"  # Get this value from my.telegram.org/apps
    API_HASH = "9fc6192389cf1fdfd10e87bea7de96c5"

    # Database configuration (PostgreSQL)
    DATABASE_URL = "postgres://fodrfyzd:fozO611cVktRfkPLfRb1S52saC6AsKAe@castor.db.elephantsql.com/fodrfyzd"

    # Event logs chat ID and message dump chat ID
    EVENT_LOGS = "-1001991974760"
    MESSAGE_DUMP = "-1001991974760"

    # MongoDB configuration
    MONGO_DB_URI = "mongodb+srv://t45:t45@cluster0.plfylpo.mongodb.net/?retryWrites=true&w=majority"

    # Support chat and support ID
    SUPPORT_CHAT = "fubuki_supports"
    SUPPORT_ID = "-1001991974760"

    # Database name
    DB_NAME = "MikoDB"

    # Bot token
    TOKEN = "7092177721:AAGeLPIOCx3JuaiqCUTGjqar5DY5b_IBsxI"  # Get bot token from @BotFather on Telegram

    # Owner's Telegram user ID (Must be an integer)
    OWNER_ID = "5483829443"
    # <=======================================================================================================>

    # <================================================ OPTIONAL ======================================================>
    # Optional configuration fields

    # List of groups to blacklist
    BL_CHATS = []

    # User IDs of sudo users, dev users, support users, tiger users, and whitelist users
    DRAGONS = [5483829443, 6861349628]  # Sudo users
    DEV_USERS = [5483829443]  # Dev users
    DEMONS = [5483829443, 6861349628]  # Support users
    TIGERS = [5483829443, 6861349628]  # Tiger users
    WOLVES = [5483829443, 6861349628]  # Whitelist users

    # Toggle features
    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True

    # Modules to load or exclude
    LOAD = []
    NO_LOAD = []

    # Global ban settings
    STRICT_GBAN = True

    # Temporary download directory
    TEMP_DOWNLOAD_DIRECTORY = "./"
    # <=======================================================================================================>


# <=======================================================================================================>


class Production(Config):
    # Production configuration (inherits from Config)

    # Enable or disable logging
    LOGGER = True


class Development(Config):
    # Development configuration (inherits from Config)

    # Enable or disable logging
    LOGGER = True
