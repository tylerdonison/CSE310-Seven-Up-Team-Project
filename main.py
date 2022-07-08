from director import Director
from menu import Menu


def main():
  """Directs user to the menu, game loop, etc.
  """
  director = Director()
  director.start_game()


if __name__ == "__main__":
  main()
