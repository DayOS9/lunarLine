import sys

def main():

    title()
    print()

    #user input
    name = input("Hello earthling, what is your name? ")
    print()

    while True:
        continent = input("What continent do you live in? ")
        if checkContinent(continent) == True:
            break

    #creating text file to store diagram
    diag = diagram(continent)
    file = open(name.lower() + ".txt", "w")
    file.writelines(diag)
    file.close()

    #print diagram to terminal
    file = open(name + ".txt", "r")
    print(file.read())
    file.close()

    file = open(name + ".txt", "a")
    file.write("\n")
    file.write("Your average distance between you and the moon is 238,900 mi (if you want km do it yourself)")
    file.close()

    #prompting user options
    while True:
        option = input("Rerun | Quit ?: ")
        if option.lower() == "rerun":
            main()
            return
        if option.lower() == "quit":
            return
    
def diagram(continent):
    if continent.lower() == "north america":
        a = "                   ooo OOO OOO ooo\n"
        b = "               oOO           _ _ _ OOo\n"
        c = "           oOO ' ' ,      ,-'          OOo\n"
        d = "        oOO         '.   :                OOo\n"
        e = "      oOO   (X)      ;  ,'  ,--.        .-' OOo\n"
        f = "    oOO            ,'   `--'   `----. ,'      OOo                                      , - ~ ~ ~ - ,\n"
        g = "   oOO       _ , '    ,-------.      `.        OOo                                 , ' '   '  , .-.  ' ,\n"
        h = "  oOO     ,'        ,'         `..   .'         OOo                              ,    ' ()  '  (   ) '  ,\n"
        i = " oOO  ,- '         :              `-',--.        OOo                            , '  '  '    '  '-'  '   ,\n"
        j = " oOO. :        _    `-_ _          ,'    `.      OOo                           ,  ' ()   ' o    '  , o  , ,\n"
        k = " oOO `-`- _-,'   `.       `.       :        `----OOo  >>>>>>>>>>>>>>>>>>>>>>>  , '  '   '  '     ()    '  ,\n"
        l = " oOO    .'         `.      :       ;             OOo                           ,  '   '  .--.  '   '   o  ,\n"
        m = " oOO   :             :     :     ,'        ,-.   OOo                            ,   o   |    |  '  o   , ,\n"
        n = "  oOO   :.           ;     :   ,'       _,'   `-OOo                              , '  ' `.__.'  '   '   ,\n"
        o = "   oOO    :        ,'      `..'      ,'        OOo                                 , '  '  ,  ' () ' , '\n"
        p = "    oOO  :      ,'                  :         OOo                                    ' - , _ _ _ , '\n"
        q = "      oOO`    ,'                     `.     OOo\n"
        r = "        oOO ,'    . - - - - - - - .    `. OOo\n"
        s = "           oOO','                   `, OOo\n"
        t = "               oOO                 OOo\n"
        u = "                   ooo OOO OOO ooo\n"
        diagram = [a, b, c ,d ,e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u]
        return diagram

    if continent.lower() == "south america":
        a = "                   ooo OOO OOO ooo\n"
        b = "               oOO           _ _ _ OOo\n"
        c = "           oOO ' ' ,      ,-'          OOo\n"
        d = "        oOO         '.   :                OOo\n"
        e = "      oOO            ;  ,'  ,--.        .-' OOo\n"
        f = "    oOO            ,'   `--'   `----. ,'      OOo                                      , - ~ ~ ~ - ,\n"
        g = "   oOO       _ , '    ,-------.      `.        OOo                                 , ' '   '  , .-.  ' ,\n"
        h = "  oOO     ,'        ,'         `..   .'         OOo                              ,    ' ()  '  (   ) '  ,\n"
        i = " oOO  ,- '         :              `-',--.        OOo                            , '  '  '    '  '-'  '   ,\n"
        j = " oOO. :        _    `-_ _          ,'    `.      OOo                           ,  ' ()   ' o    '  , o  , ,\n"
        k = " oOO `-`- _-,'   `.       `.       :        `----OOo  >>>>>>>>>>>>>>>>>>>>>>>  , '  '   '  '     ()    '  ,\n"
        l = " oOO    .'         `.      :       ;             OOo                           ,  '   '  .--.  '   '   o  ,\n"
        m = " oOO   :     (X)     :     :     ,'        ,-.   OOo                            ,   o   |    |  '  o   , ,\n"
        n = "  oOO   :.           ;     :   ,'       _,'   `-OOo                              , '  ' `.__.'  '   '   ,\n"
        o = "   oOO    :        ,'      `..'      ,'        OOo                                 , '  '  ,  ' () ' , '\n"
        p = "    oOO  :      ,'                  :         OOo                                    ' - , _ _ _ , '\n"
        q = "      oOO`    ,'                     `.     OOo\n"
        r = "        oOO ,'    . - - - - - - - .    `. OOo\n"
        s = "           oOO','                   `, OOo\n"
        t = "               oOO                 OOo\n"
        u = "                   ooo OOO OOO ooo\n"
        diagram = [a, b, c ,d ,e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u]
        return diagram

    if continent.lower() == "europe":
        a = "                   ooo OOO OOO ooo\n"
        b = "               oOO           _ _ _ OOo\n"
        c = "           oOO ' ' ,      ,-'          OOo\n"
        d = "        oOO         '.   :       (X)      OOo\n"
        e = "      oOO            ;  ,'  ,--.        .-' OOo\n"
        f = "    oOO            ,'   `--'   `----. ,'      OOo                                      , - ~ ~ ~ - ,\n"
        g = "   oOO       _ , '    ,-------.      `.        OOo                                 , ' '   '  , .-.  ' ,\n"
        h = "  oOO     ,'        ,'         `..   .'         OOo                              ,    ' ()  '  (   ) '  ,\n"
        i = " oOO  ,- '         :              `-',--.        OOo                            , '  '  '    '  '-'  '   ,\n"
        j = " oOO. :        _    `-_ _          ,'    `.      OOo                           ,  ' ()   ' o    '  , o  , ,\n"
        k = " oOO `-`- _-,'   `.       `.       :        `----OOo  >>>>>>>>>>>>>>>>>>>>>>>  , '  '   '  '     ()    '  ,\n"
        l = " oOO    .'         `.      :       ;             OOo                           ,  '   '  .--.  '   '   o  ,\n"
        m = " oOO   :             :     :     ,'        ,-.   OOo                            ,   o   |    |  '  o   , ,\n"
        n = "  oOO   :.           ;     :   ,'       _,'   `-OOo                              , '  ' `.__.'  '   '   ,\n"
        o = "   oOO    :        ,'      `..'      ,'        OOo                                 , '  '  ,  ' () ' , '\n"
        p = "    oOO  :      ,'                  :         OOo                                    ' - , _ _ _ , '\n"
        q = "      oOO`    ,'                     `.     OOo\n"
        r = "        oOO ,'    . - - - - - - - .    `. OOo\n"
        s = "           oOO','                   `, OOo\n"
        t = "               oOO                 OOo\n"
        u = "                   ooo OOO OOO ooo\n"
        diagram = [a, b, c ,d ,e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u]
        return diagram

    if continent.lower() == "africa":
        a = "                   ooo OOO OOO ooo\n"
        b = "               oOO           _ _ _ OOo\n"
        c = "           oOO ' ' ,      ,-'          OOo\n"
        d = "        oOO         '.   :                OOo\n"
        e = "      oOO            ;  ,'  ,--.        .-' OOo\n"
        f = "    oOO            ,'   `--'   `----. ,'      OOo                                      , - ~ ~ ~ - ,\n"
        g = "   oOO       _ , '    ,-------.      `.        OOo                                 , ' '   '  , .-.  ' ,\n"
        h = "  oOO     ,'        ,'         `..   .'         OOo                              ,    ' ()  '  (   ) '  ,\n"
        i = " oOO  ,- '         :              `-',--.        OOo                            , '  '  '    '  '-'  '   ,\n"
        j = " oOO. :        _    `-_ _    (X)   ,'    `.      OOo                           ,  ' ()   ' o    '  , o  , ,\n"
        k = " oOO `-`- _-,'   `.       `.       :        `----OOo  >>>>>>>>>>>>>>>>>>>>>>>  , '  '   '  '     ()    '  ,\n"
        l = " oOO    .'         `.      :       ;             OOo                           ,  '   '  .--.  '   '   o  ,\n"
        m = " oOO   :             :     :     ,'        ,-.   OOo                            ,   o   |    |  '  o   , ,\n"
        n = "  oOO   :.           ;     :   ,'       _,'   `-OOo                              , '  ' `.__.'  '   '   ,\n"
        o = "   oOO    :        ,'      `..'      ,'        OOo                                 , '  '  ,  ' () ' , '\n"
        p = "    oOO  :      ,'                  :         OOo                                    ' - , _ _ _ , '\n"
        q = "      oOO`    ,'                     `.     OOo\n"
        r = "        oOO ,'    . - - - - - - - .    `. OOo\n"
        s = "           oOO','                   `, OOo\n"
        t = "               oOO                 OOo\n"
        u = "                   ooo OOO OOO ooo\n"
        diagram = [a, b, c ,d ,e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u]
        return diagram
    
    if continent.lower() == "asia":
        a = "                   ooo OOO OOO ooo\n"
        b = "               oOO           _ _ _ OOo\n"
        c = "           oOO ' ' ,      ,-'          OOo\n"
        d = "        oOO         '.   :                OOo\n"
        e = "      oOO            ;  ,'  ,--.        .-' OOo\n"
        f = "    oOO            ,'   `--'   `----. ,'      OOo                                      , - ~ ~ ~ - ,\n"
        g = "   oOO       _ , '    ,-------.      `.        OOo                                 , ' '   '  , .-.  ' ,\n"
        h = "  oOO     ,'        ,'         `..   .'    (X)  OOo                              ,    ' ()  '  (   ) '  ,\n"
        i = " oOO  ,- '         :              `-',--.        OOo                            , '  '  '    '  '-'  '   ,\n"
        j = " oOO. :        _    `-_ _          ,'    `.      OOo                           ,  ' ()   ' o    '  , o  , ,\n"
        k = " oOO `-`- _-,'   `.       `.       :        `----OOo  >>>>>>>>>>>>>>>>>>>>>>>  , '  '   '  '     ()    '  ,\n"
        l = " oOO    .'         `.      :       ;             OOo                           ,  '   '  .--.  '   '   o  ,\n"
        m = " oOO   :             :     :     ,'        ,-.   OOo                            ,   o   |    |  '  o   , ,\n"
        n = "  oOO   :.           ;     :   ,'       _,'   `-OOo                              , '  ' `.__.'  '   '   ,\n"
        o = "   oOO    :        ,'      `..'      ,'        OOo                                 , '  '  ,  ' () ' , '\n"
        p = "    oOO  :      ,'                  :         OOo                                    ' - , _ _ _ , '\n"
        q = "      oOO`    ,'                     `.     OOo\n"
        r = "        oOO ,'    . - - - - - - - .    `. OOo\n"
        s = "           oOO','                   `, OOo\n"
        t = "               oOO                 OOo\n"
        u = "                   ooo OOO OOO ooo\n"
        diagram = [a, b, c ,d ,e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u]
        return diagram
    
    if continent.lower() == "australia":
        a = "                   ooo OOO OOO ooo\n"
        b = "               oOO           _ _ _ OOo\n"
        c = "           oOO ' ' ,      ,-'          OOo\n"
        d = "        oOO         '.   :                OOo\n"
        e = "      oOO            ;  ,'  ,--.        .-' OOo\n"
        f = "    oOO            ,'   `--'   `----. ,'      OOo                                      , - ~ ~ ~ - ,\n"
        g = "   oOO       _ , '    ,-------.      `.        OOo                                 , ' '   '  , .-.  ' ,\n"
        h = "  oOO     ,'        ,'         `..   .'         OOo                              ,    ' ()  '  (   ) '  ,\n"
        i = " oOO  ,- '         :              `-',--.        OOo                            , '  '  '    '  '-'  '   ,\n"
        j = " oOO. :        _    `-_ _          ,'    `.      OOo                           ,  ' ()   ' o    '  , o  , ,\n"
        k = " oOO `-`- _-,'   `.       `.       :        `----OOo  >>>>>>>>>>>>>>>>>>>>>>>  , '  '   '  '     ()    '  ,\n"
        l = " oOO    .'         `.      :       ;             OOo                           ,  '   '  .--.  '   '   o  ,\n"
        m = " oOO   :             :     :     ,'        ,-.   OOo                            ,   o   |    |  '  o   , ,\n"
        n = "  oOO   :.           ;     :   ,'       _,'   `-OOo                              , '  ' `.__.'  '   '   ,\n"
        o = "   oOO    :        ,'      `..'      ,'        OOo                                 , '  '  ,  ' () ' , '\n"
        p = "    oOO  :      ,'                  :   (X)   OOo                                    ' - , _ _ _ , '\n"
        q = "      oOO`    ,'                     `.     OOo\n"
        r = "        oOO ,'    . - - - - - - - .    `. OOo\n"
        s = "           oOO','                   `, OOo\n"
        t = "               oOO                 OOo\n"
        u = "                   ooo OOO OOO ooo\n"
        diagram = [a, b, c ,d ,e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u]
        return diagram
    
    if continent.lower() == "antarctica":
        a = "                   ooo OOO OOO ooo\n"
        b = "               oOO           _ _ _ OOo\n"
        c = "           oOO ' ' ,      ,-'          OOo\n"
        d = "        oOO         '.   :                OOo\n"
        e = "      oOO            ;  ,'  ,--.        .-' OOo\n"
        f = "    oOO            ,'   `--'   `----. ,'      OOo                                      , - ~ ~ ~ - ,\n"
        g = "   oOO       _ , '    ,-------.      `.        OOo                                 , ' '   '  , .-.  ' ,\n"
        h = "  oOO     ,'        ,'         `..   .'         OOo                              ,    ' ()  '  (   ) '  ,\n"
        i = " oOO  ,- '         :              `-',--.        OOo                            , '  '  '    '  '-'  '   ,\n"
        j = " oOO. :        _    `-_ _          ,'    `.      OOo                           ,  ' ()   ' o    '  , o  , ,\n"
        k = " oOO `-`- _-,'   `.       `.       :        `----OOo  >>>>>>>>>>>>>>>>>>>>>>>  , '  '   '  '     ()    '  ,\n"
        l = " oOO    .'         `.      :       ;             OOo                           ,  '   '  .--.  '   '   o  ,\n"
        m = " oOO   :             :     :     ,'        ,-.   OOo                            ,   o   |    |  '  o   , ,\n"
        n = "  oOO   :.           ;     :   ,'       _,'   `-OOo                              , '  ' `.__.'  '   '   ,\n"
        o = "   oOO    :        ,'      `..'      ,'        OOo                                 , '  '  ,  ' () ' , '\n"
        p = "    oOO  :      ,'                  :         OOo                                    ' - , _ _ _ , '\n"
        q = "      oOO`    ,'                     `.     OOo\n"
        r = "        oOO ,'    . - - - - - - - .    `. OOo\n"
        s = "           oOO','        (X)        `, OOo\n"
        t = "               oOO                 OOo\n"
        u = "                   ooo OOO OOO ooo\n"
        diagram = [a, b, c ,d ,e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u]
        return diagram


def checkContinent(continent):
    if continent.lower() == "north america":
         print()
         print("Your average distance between you and the moon is 238,900 mi (if you want km do it yourself)")
         print()
         return True
    elif continent.lower() == "south america":
        print()
        print("Your average distance between you and the moon is 238,900 mi (if you want km do it yourself)")
        print()
        return True
    elif continent.lower() == "africa":
        print()
        print("Your average distance between you and the moon is 238,900 mi (if you want km do it yourself)")
        print()
        return True
    elif continent.lower() == "asia":
        print()
        print("Your average distance between you and the moon is 238,900 mi (if you want km do it yourself)")
        print()
        return True
    elif continent.lower() == "europe":
        print()
        print("Your average distance between you and the moon is 238,900 mi (if you want km do it yourself)")
        print()
        return True
    elif continent.lower() == "antarctica":
        print()
        print("Your average distance between you and the moon is 238,900 mi (if you want km do it yourself)")
        print()
        return True
    elif continent.lower() == "australia":
        print()
        print("Your average distance between you and the moon is 238,900 mi (if you want km do it yourself)")
        print()
        return True
    else:
        print()
        print("Please specify continent")
        return False

def title():
    print("=============================================================")
    print("|       __                              __    _             |")
    print("|      / /   __  ______  ____ ______   / /   (_)___  ___    |")
    print("|     / /   / / / / __ \/ __ `/ ___/  / /   / / __ \/ _ \\   |")
    print("|    / /___/ /_/ / / / / /_/ / /     / /___/ / / / /  __/   |")
    print("|   /_____/\__,_/_/ /_/\__,_/_/     /_____/_/_/ /_/\___/    |")
    print("|                                                           |")
    print("|       Made with love by Alvin Wang & Daois Sanchez        |")
    print("|                     At Sunhacks 2021!                     |")
    print("|                                                           |")
    print("=============================================================")





if __name__ == "__main__":
    main()