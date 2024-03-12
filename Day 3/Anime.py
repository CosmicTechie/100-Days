print('''
   __
  |  ""--.--.._                                             __..    ,--.
  |       `.   "-.'""\_...-----..._   ,--. .--..-----.._.""|   |   /   /
  |_   _    \__   ).  \           _/_ |   \|  ||  ..    >  `.  |  /   /
    | | `.   ._)  /|\  \ .-"""":-"   "-.   `  ||  |.'  ,'`. |  |_/_  /
    | |_.'   |   / ""`  \  ===/  ..|..  \     ||      < ""  `.  "  |/__
    `.      .    \ ,--   \-..-\   /"\   /     ||  |>   )--   |    /    |
     |__..-'__||__\   |___\ __.:-.._..-'_|\___||____..-/  |__|--""____/
                           _______________________
                          /                      ,'
                         /      ___            ,'
                        /   _.-'  ,'        ,-'   /
                       / ,-' ,--.'        ,'   .'/
                      /.'     `.         '.  ,' /
                     /      ,-'       ,"--','  /
                          ,'        ,'  ,'    /
                         ,-'      ,' .-'     /
                      ,-'                   /
                    ,:_____________________/

''')


anime=input("Which Anime you like? : Dragon Ball or Naruto  \n")
anime=anime.lower()

if anime=='dragon ball' or anime=='dragonball':
  char=input("Which character can win against Goku ?: Vegita or Gohan or Beerus \n ")
  char=char.lower()

  if char=='vegita' or char=='vegeta':
    print("You Win, Vegita can Win.")
  else:
    print("Only Vegita is the Goku's real Rival who can Win against Ultra Instinct Goku. ")
    print('''

                                     ,
                               ,   ,'|
                             ,/|.-'   \.
                          .-'  '       |.
                    ,  .-'              |
                   /|,'                 |'
                  / '                    |  ,
                 /                       ,'/
              .  |          _              /
               \`' .-.    ,' `.           |
                \ /   \ /      \          /
                 \|    V        |        |  ,
                  (           ) /.--.   ''"/
                  "b.`. ,' _.ee'' 6)|   ,-'
                    \"= --""  )   ' /.-'
                     \ / `---"   ."|'
  V E G I I T A       \"..-    .'  |.
                       `-__..-','   |
                     __.) ' .-'/    /\._
               _.--'/----..--------. _.-""-._
            .-'_)   \.   /     __..-'     _.-'--.
           / -'/      """""""""         ,'-.   . `.
          | ' /                        /    `   `. |
          |   |                        |         | |
           \ .'\                       |     \     |
          / '  | ,'               . -  \`.    |  / /
         / /   | |                      `/"--. -' /|
        | |     \ \                     /     \     |
        | \      | \                  .-|      |    |



    ''')

else:
  print("Both are good but this game's creator like Dragon Ball more. BYE!")
