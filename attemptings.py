def attemptings(attempting, time, cls):
    timing = 14
    print(f"Sorry, but you have tried {attempting} times. You have been locked out of your account. You need to wait 15 seconds before you can attempt again.")
    time.sleep(1)
    while timing >= 1:
        cls()
        if timing != 1:
            print(f"{timing} seconds.")
        else:
            print(f"{timing} second.")
        timing -= 1
        time.sleep(1)
    cls()