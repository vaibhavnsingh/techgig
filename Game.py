''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():
    pass
    T = int(input("Enter no of levels : "))

    if not(1<= T <=10):
        return

    results = []
    for _ in range(T):
        print(_)
        no_of_players = int(input("Enter no of players/Villians : " ))
        if not(1<= no_of_players <=1000):
            return

        strength_of_villians = list(map(int,input().rstrip().split()))
        energy_of_player = list(map(int,input().rstrip().split()))

        print(no_of_players)
        print(strength_of_villians)
        print(energy_of_player)

        if not (len(strength_of_villians) == len(energy_of_player) == no_of_players):
            return
        else:
            print("Logic will apply")
            strength_of_villians.sort(reverse = True)
            energy_of_player.sort(reverse = True)
            print(strength_of_villians)
            print(energy_of_player)
            
            for x in range(len(energy_of_player)):
                if strength_of_villians[x] >= energy_of_player[x]:
                    results.append("LOSE")
                    break
            else:
                results.append("WIN")
    for res in results:
        print(res)



 # Write code here 

    
main()

