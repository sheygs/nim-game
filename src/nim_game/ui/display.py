from config.constants import WELCOME_MESSAGE


def show_message(message=WELCOME_MESSAGE) -> None:
    """Display a message to the user.

    Args:
        message: The message to display
    """
    print(message)