import util
import engine
import ui

BOARD_WIDTH = 100
BOARD_HEIGHT = 30

PLAYER_ICON = '@'
PLAYER_START_X = 1
PLAYER_START_Y = 2
PLAYER_HEALTH = 5

OTHER_NAME = "Miller"
OTHER2_NAME = "Cook"
OTHER3_NAME = "Cow"

OTHER_ICON = "M"
OTHER2_ICON = "C"
OTHER3_ICON = "K"

OTHER_HEALTH = 3
OTHER2_HEALTH = 3
OTHER3_HEALTH = 3

OTHER_GOAL = "flour"
OTHER2_GOAL = "information"
OTHER3_GOAL = "milk"

OTHER_START_X = 20
OTHER_START_Y = 3

OTHER_STEP = 1

question_prompts = [
    "What's the first name of 'Ooops I did it again' singer?\n(a) Christina\n(b) Britney\n(c) Jessica\n",
    "Which river passes through Vienna?\n(a) Vistula\n(b) Douro\n(c) Danube\n",
    "What color are bananas?\n(a) Red\n(b) Orange\n(c) Yellow\n",
    "What band Nergal plays in?\n(a) Behemoth\n(b) Acid Drinkers\n(c) Coma\n",
    "What is the capital of Australia?\n(a) Sydney\n(b) Canberra\n(c) Melbourne\n",
    "How many islands there are in Faroe Islands?\n(a) 412\n(b) 779\n(c) 18\n"
    ]

questions = [
    [question_prompts[0], "b", False],
    [question_prompts[1], "c", False],
    [question_prompts[2], "c", False],
    [question_prompts[3], "b", False],
    [question_prompts[4], "b", False],
]


def create_player():
    pass


def create_other():
    other = {
        'other_name': OTHER_NAME,
        'other_icon': OTHER_ICON,
        'position_x': OTHER_START_X,
        'position_y': OTHER_START_Y,
        'step': OTHER_STEP,
        'other_health': OTHER_HEALTH,
        'other_quiz': {
            'goal': OTHER_GOAL
            }
        }
    return other


def main():
    inventory = {}
    # player = create_player()

    player = {
        'player_icon': PLAYER_ICON,
        'position_x': PLAYER_START_X,
        'position_y': PLAYER_START_Y,
        'player_health': PLAYER_HEALTH
        }
    item = {
        'flour0': {
            'type': 'ingridient',
            'item_icon': 'F',
            'position_x': 11,
            'position_y': 2,
            'number': 2
            },
        'sugar0': {
            'type': 'ingridient',
            'item_icon': 'S',
            'position_x': 9,
            'position_y': 18,
            'number': 1
            },
        'sugar2': {
            'type': 'ingridient',
            'item_icon': 'S',
            'position_x': 55,
            'position_y': 25,
            'number': 1
            },
        'sugar3': {
            'type': 'ingridient',
            'item_icon': 'S',
            'position_x': 90,
            'position_y': 2,
            'number': 2
            }
         }

    empty_board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)
    other = create_other()

    is_running = True

    while is_running:

        board = engine.put_player_on_board(empty_board, player)

        board = engine.put_other_on_board(board, other)

        for item_key in item:
            board = engine.put_item_on_board(board, item, item_key)

        ui.display_board(board)

        key = util.key_pressed()

        engine.movement(board, player, key, other, BOARD_WIDTH, BOARD_HEIGHT)

        util.clear_screen()

        engine.item_vs_player(inventory, item, player)

        if engine.player_meets_other(other, player):
            engine.player_vs_other_quiz(player, other, item, questions)

        if key == 'i':
            message = 'This is your inventory content: '
            ui.print_message(message)
            ui.print_table(inventory)

        elif key == 'q':
            is_running = False


if __name__ == '__main__':
    main()
