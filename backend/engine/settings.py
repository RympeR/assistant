import os

PREDEFINED_COMMANDS = []
CUSTOM_COMMANDS = []
MIDDLEWARE_CLASSES = (
    'backend.engine.middleware.CommandMiddleware.CommandMiddleware',
    'backend.engine.middleware.ResponseMiddleware.ResponseMiddleware',
)
MODULE_CLASSES = (
    'backend.modules.weather_commands.WeatherApi.WeatherApi',
    'backend.modules.base_commands.BaseCommands.BaseCommands',
    'backend.modules.system_commands.windows_system.WindowsSystem',
)

CUSTOM_COMMANDS_FILE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'custom_commands.txt')

if not os.path.exists(CUSTOM_COMMANDS_FILE_PATH):
    with open(CUSTOM_COMMANDS_FILE_PATH, 'w') as f:
        f.write('')

with open(CUSTOM_COMMANDS_FILE_PATH, 'r') as f:
    for line in f:
        CUSTOM_COMMANDS.append(line.strip())
