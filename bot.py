import random
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# تابعی برای شروع بازی
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('سلام! بیایید بازی دوز (Tic-Tac-Toe) را شروع کنیم. برای شروع، دستور /play را وارد کنید.')

# تابعی برای بازی دوز
def play(update: Update, context: CallbackContext) -> None:
    context.user_data['board'] = [' ' for _ in range(9)]
    context.user_data['turn'] = 'X'
    update.message.reply_text('بازی شروع شد! برای انتخاب خانه، شماره آن را (1-9) وارد کنید.\n\n' + display_board(context.user_data['board']))

# تابعی برای نمایش تخته بازی
def display_board(board):
    return f"""
    {board[0]} | {board[1]} | {board[2]}
    ---------
    {board[3]} | {board[4]} | {board[5]}
    ---------
    {board[6]} | {board[7]} | {board[8]}
    """

# تابعی برای پردازش حرکات کاربر
def make_move(update: Update, context: CallbackContext) -> None:
    board = context.user_data.get('board')
    turn = context.user_data.get('turn')

    if not board:
        update.message.reply_text('لطفاً ابتدا دستور /play را وارد کنید.')
        return

    try:
        move = int(update.message.text) - 1
        if board[move] != ' ':
            update.message.reply_text('این خانه پر است! لطفاً خانه دیگری انتخاب کنید.')
            return
    except (ValueError, IndexError):
        update.message.reply_text('لطفاً یک شماره معتبر (1-9) وارد کنید.')
        return

    board[move] = turn
    if check_winner(board, turn):
        update.message.reply_text(f'تبریک! شما برنده شدید!\n\n{display_board(board)}')
        return
    elif ' ' not in board:
        update.message.reply_text('بازی مساوی شد!')
        return

    # نوبت سیستم
    turn = 'O' if turn == 'X' else 'X'
    context.user_data['turn'] = turn
    system_move(board)
    if check_winner(board, turn):
        update.message.reply_text(f'متاسفم! سیستم برنده شد!\n\n{display_board(board)}')
        return
    elif ' ' not in board:
        update.message.reply_text('بازی مساوی شد!')
        return

    update.message.reply_text(display_board(board))

# تابعی برای حرکت سیستم
def system_move(board):
    empty_cells = [i for i, cell in enumerate(board) if cell == ' ']
    if empty_cells:
        move = random.choice(empty_cells)
        board[move] = 'O'

# تابعی برای بررسی برنده
def check_winner(board, player):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # سطرها
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # ستون‌ها
        [0, 4, 8], [2, 4, 6]              # قطرها
    ]
    return any(all(board[i] == player for i in combo) for combo in winning_combinations)

def main() -> None:
    updater = Updater("7244681466:AAF_Wt7KbmfNU_tPQoH8dLEOuIQgm-Clo_A")

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("play", play))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, make_move))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
