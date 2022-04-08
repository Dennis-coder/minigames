from models.game_model import GameModel
from views.game_view import GameView

def play():
    game_view = GameView()
    game_model = GameModel()

    game_model.observe(game_view)
    game_model.snake.observe(game_view.snake)
    game_model.food.observe(game_view.food)
    return game_model.run()


if __name__ == "__main__":
    score = play()
    print(f"Score: {score}")