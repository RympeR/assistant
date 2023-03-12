from engine import Engine
from engine.request.Command import CommandOBJ
from engine.request.Request import RequestOBJ
from threading import Thread

ENGINE = Engine()
commands = []

def engine_input_loop():
    global commands
    # while True:
    try:
        command = input('Enter command: ')
        # if command == 'exit':
        #     break
        commands = list(filter(lambda x: not x['done'], commands))
        commands.append({
            'command': command,
            'args': None,
            'kwargs': None,
            'done': False,
        })

    except Exception as e:
        print(e)

def engine_commands_loop():
    global commands
    # while any([not command['done'] for command in commands]):
    try:
        commands_obj = [CommandOBJ(
            command=command['command'],
            args=command['args'],
            kwargs=command['kwargs'],
        ) for command in commands if not command['done']]
        request = RequestOBJ(commands=commands_obj,language='en')
        print(ENGINE.process_request(request))
        for command in commands:
            command['done'] = True
    except Exception as e:
        print(e)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    engine_input_loop()
    engine_commands_loop()
    # main_thread = Thread(target=engine_input_loop)
    # commannd_thread = Thread(target=engine_commands_loop)
    # main_thread.start()
    # commannd_thread.start()
    # main_thread.join()
    # commannd_thread.join()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
