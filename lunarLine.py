def title():
    print("==============================================================================================================")
    print("|                               __                              __    _                                      |")
    print("|                              / /   __  ______  ____ ______   / /   (_)___  ___                             |")
    print("|                             / /   / / / / __ \/ __ `/ ___/  / /   / / __ \/ _ \\                            |")
    print("|                            / /___/ /_/ / / / / /_/ / /     / /___/ / / / /  __/                            |")
    print("|                           /_____/\__,_/_/ /_/\__,_/_/     /_____/_/_/ /_/\___/                             |")
    print("|                                                                                                            |")
    print("|                                Made with love by Alvin Wang & Daois Sanchez                                |")
    print("|                                             At Sunhacks 2021!                                              |")
    print("|                                                                                                            |")
    print("==============================================================================================================")
    print()

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

title()