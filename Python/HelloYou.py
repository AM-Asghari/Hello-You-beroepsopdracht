while True:
    print("Hello You!, ik ben Mosawer")
    print("Wie ben jij?")
    x = input()
    print("Hello " + x)

    import datetime

    datetime_object = datetime.datetime.now()
    print("het is momenteel:", datetime_object)

    print("Wil jij dit programma nog een keer doen?")
    print("Type yes/no")
    inputText = input()
    print("input:", inputText)
    if inputText == "no":
        break