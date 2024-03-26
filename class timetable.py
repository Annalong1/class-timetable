##
#class timetable

def create_timetable():
    """combining lists to make timetable"""
    periods = [1, 2, 3, 4, 5]

    subjects = [["maths", "english", "CSP", "art", "science"], 
                ["science", "english", "biology", "CSP", "maths"], 
                ["english", "CS", "chemestry", "maths", "biology"],
               ["englihs", "art", "PE", "walking", "maths"],
               ["physics", "chemstiry", "biology", "maths", "CSP"]]

    #creating dictionarys
    monday = dict(zip(periods, subjects[0]))

    tuesday = dict(zip(periods, subjects[1]))

    wednesday = dict(zip(periods, subjects[2]))

    thursday = dict(zip(periods, subjects[3]))

    friday = dict(zip(periods, subjects[4]))
 
    return monday, tuesday, wednesday, thursday, friday, periods

#main
if __name__ == "__main__":
    #defining timetable for each day using create timetable function
    monday, tuesday, wednesday, thursday, friday, periods = create_timetable()

    #force valid day
    while True:
        day = input("What day is it? ").strip().lower()
        if day == "monday" or day == "tuesday" or day == "wednesday" or day == "thursday" or day == "friday":
            break
        else:
            print("That is not a vaild day")

    #force valid period
    while True:
        try:
            period = int(input("What period in number? "))
            if period <= len(periods):
                break

            else:
                print("That is not a valid period")

        except ValueError:
            print("Enter the period as a number")



    #printing appropriate statement
    if day == "monday":
        print("The subject you have is",monday[period])
        
    elif day == "tuesday":
        print("The subject you have is",tuesday[period])
        
    elif day == "wednesday":  
        print("The subject you have is",wednesday[period])
        
    elif day == "thursday":
        print("The subject you have is",thursday[period])
        
    elif day == "friday":
        print("The subject you have is",friday[period])
        
    else:
        print("That is not a vaild day")