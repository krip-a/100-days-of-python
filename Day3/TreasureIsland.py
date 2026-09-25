print('''
                            _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'  ||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-.-'       o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
               '-._'-. || |' `_.-'
                    '-.||_/.-'
  
 ''')

print('''
        Welcome to Treasure Island!\n 
        Your mission is to find the treasure.  
        ''')

print('''
        You went on a hike looking for a treasure.\n
        Unfortunately, you lost your map and are at a crossroad. Would you like to go left or right?
        ''')
choice = input("type 'left' to go left and 'right' to go right.\n ").upper()

if choice == "RIGHT":
    print('''
            You have reached a lake. There is an island at the middle of the lake.\n 
            A boat is rowing towards you. Would you like to wait for the boat or swim to the island?
            ''')
    choice2 = input("Type 'swim' to swim across and 'wait' to wait for the boat.\n ").upper()

    if choice2 == 'WAIT':
        print('''
                       __/\__
                    ~~~\____/~~~~~~
                         ~  ~~~   ~.     
                ''')
        print("The boat is here! Get on the boat and go to the island.")
        print('''
                
                                _
                                ;`',
                                `,  `,
                                ',   ;   ,,-""==..,
                                \    ','           '
                        ,-""'-., ;    '    __.-="-.;
                        ," ,,_    "       _."
                    ;,'   ''-,          "=--,_
                            ,-''    _  _       `,
                            /   ,.-+(_)(_) --.,   ;
                            ,'  /   ; (_)       `\ ,
                            ; ,/    ;._.;         ;
                            !,'     ;   ;
                             '      ;   ;
                                    ;._.;
                                    ;   ;
                                    ;   ;        ~
                    ~               ;._.;
                            ~       ;   ;
                                   .    `.                ~
                            __,.--;.___.;--.,___
                    _,,-""      ;     ;       ""-,,_
                .-              ;     ;             ``-.
                ",                      `               ,"        ~
                    "-_                                _-"
                ~       ``----..,_          __,,.....-
                                ````````````
             ''')

        print('''You're at the island now.
            There are three doors in front of you, Red, Yellow and Blue.
            Which door would you like to choose?
            ''')
        choice3 = input ("Type 'Red', 'Yellow' or 'Blue'.\n ").upper()

        if choice3 == "RED":
            print('''    
                     __________
                    |  __  __  |
                    | |  ||  | |
                    | |  ||  | |
                    | |__||__| |
                    |  __  __()|
                    | |  ||  | |
                    | |  ||  | |
                    | |  ||  | |
                    | |  ||  | |
                    | |__||__| |
                    |__________|
                ''')
            print("Uh-oh. A pirate was waiting to kidnap you. Good Luck!")
        elif choice3 == "YELLOW":
            print("Congratulations! You found the treasure. \n It's a $10 giftcard to Walmart!")

        elif choice3 == "BLUE":
            print('''    
                                            
                                          ,.
                                    ,_> `.   ,';
                                ,-`'      `'   '`'._
                            ,,-) ---._   |   .---''`-),.
                        ,'      `.  \  ;  /   _,'     `,
                        ,--' ____       \   '  ,'    ___  `-,
                    _>   /--. `-.              .-'.--\   \__
                    '-,  (    `.  `.,`~ \~'-. ,' ,'    )    _
                    _>    \     \ ,'  ') )   `. /     /    <,.
                ,-'   _,  \    ,'    ( /      `.    /        `-,
                `-.,-'     `.,'       `         `.,'  `\    ,-'
                    ,'       _  /   ,,,      ,,,     \     `-. `-._
                /-,     ,'  ;   ' _ \    / _ `     ; `.     `(`-
                    /-,        ;    (o)      (o)      ;          `'`,
                ,~-'  ,-'    \     '        `      /     \      <_
                /-. ,'        \                   /       \     ,-'
                    '`,     ,'   `-/             \-' `.      `-. <
                    /_    /      /   (_     _)   \    \          `,
                    `-._;  ,' |  .::.`-.-' :..  |       `-.    _
                        _/       \  `:: ,^. :.:' / `.        \,-'
                    '`.   ,-'  /`-..-'-.-`-..-'\            `-.
                        >_ /     ;  (\/( ' )\/)  ;     `-.    _<
                        ,-'      `.  \`-^^^-'/  ,'        \ _<
                        `-,  ,'   `. `"""""' ,'   `-.   <`'
                            ')        `._.,,_.'        \ ,-'
                            '._        '`'`'   \       <
                                >   ,'       ,   `-.   <`'
                                `,/          \      ,-`
                                `,   ,' |   /     /
                                '; /   ;        (
                                    _)|   `     (
                                    `')       .-'
                                      <_ \   /   
                                        \   /\(
                                         `;/  `

                    ''')
            print("Uh-oh. A hungry lion was waiting for food. Good Luck!")

    elif choice2 == "SWIM":
        print('''
             
                    .-._   _ _ _ _ _ _ _ _
         .-''-.__.-'00  '-' ' ' ' ' ' ' ' '-.
         '.___ '    .   .--_'-' '-' '-' _'-' '._
          V: V 'vv-'   '_   '.       .'  _..' '.'.
            '=.____.=_.--'   :_.__.__:_   '.   : :
                    (((____.-'        '-.  /   : :
                                      (((-'\ .' /
                                    _____..'  .'
                                   '-._____.-'  
        ''')
        print("Uh-oh a crocodile got you. Good Luck!")

elif choice == "LEFT":
    
    print('''Uh-oh. There was a cliff on the right.
            You fell off the cliff.
             Good Luck!  ''')

else:
    print("Invalid choice. You have been eliminated. ")