from director import Director

def main():
  """Directs user to the menu, game loop, etc.
  """
  director = Director()
  play = True
  while play:
    play = director.setup_game()


if __name__ == "__main__":
  main()
