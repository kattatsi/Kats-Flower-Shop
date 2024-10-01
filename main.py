from game import game

def main():
   play = game()
   while(play.run == True):
      cmd = input("input: ").split()
      play.go(cmd)

main()