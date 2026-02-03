#1
code = int(input("HTTP status kodini kiriting: "))

match code:
    case 200:
        print("OK")
    case 201:
        print("Created")
    case 301:
        print("Moved Permanently")
    case 400:
        print("Bad Request")
    case 403:
        print("Forbidden")
    case 404:
        print("Not Found")
    case 500:
        print("Server Error")
    case 502:
        print("Bad Gateway")
    case _:
        print("Noma'lum status kodi")

#2
shakl = input("Shakl nomini kiriting: ").lower()

match shakl:
    case "uchburchak":
        a = float(input("Asos: "))
        h = float(input("Balandlik: "))
        print("Yuza:", a * h / 2)
    case "kvadrat":
        a = float(input("Tomon: "))
        print("Yuza:", a ** 2)
    case "to'rtburchak":
        a = float(input("Uzunlik: "))
        b = float(input("Kenglik: "))
        print("Yuza:", a * b)
    case "doira":
        r = float(input("Radius: "))
        print("Yuza:", 3.14 * r ** 2)
    case _:
        print("Noto‘g‘ri shakl")
