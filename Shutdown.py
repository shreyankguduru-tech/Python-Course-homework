def shutdown(answer):
    if answer == "yes":
        print("shutting down")
    elif answer == "no":
        print("canceling shut down")
    else:
        print("sorry")

shutdown("yes")
