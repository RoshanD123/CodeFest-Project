'''
This Program is used as a COVID predictor
'''
def travel(x,y):
    acns = ["yes", "no"]
    th = str(
        input("In the last two to three weeks, have you travelled anywhere? "))
    if th not in acns:
        th = th.lower()
        print("Please write the answer again in the proper format. ")
        travel(x,y)
        return
    else:
        if th == "yes":
            fun = str(
                input(
                    "Had you gone to any special events with mass gatherings? "
                ))
            if fun not in acns:
                fun = fun.lower()
                print("Please write the answer again in the proper format. ")
                travel(x,y)
                return
            elif fun == "yes":
                while True:
                    try:
                        peeps = int(
                            input(
                                "Please enter approximately how many people were there - "
                            ))
                    except ValueError:
                        print("Sorry, I didn't understand that.")
                        continue
                        if peeps < 0:
                            print(
                                "It is impossible for the number of people to be negative.  Please keep this in mind when rewriting your response. "
                            )
                            continue
                        else:
                            break
                    if peeps >= 55 and not x == "none":
                        print("Dear",y,", you are at a higher risk to have",x,"please go to a doctor to keep yourself safe")
                        print(
                            "\nThank you so much for using our application.  Hope you get better soon from",x,"(take a COVID test as well)",y,"to ensure that you are safe from errors in our predicitons"
                        )
                        break

                    elif peeps >= 55 and x == "none":
                        print(
                            "Dear",y,", you have a higher risk of catching covid in general, take a test(COVID test) to be sure"
                        )
                        print(
                            "\nThank you so much for using our application.  Hope you get better soon from",x,"(take a COVID test as well)",y,"to ensure that you are safe from errors in our predicitons"
                        )
                        break

                    elif peeps < 55 and x == "none":
                        print(
                            "Dear",y,",  Take care of yourself.  Though there were few people, you still may have a risk of COVID-19. "
                        )
                        print(
                            "\nThank you so much for using our application.  Hope you get better soon from",x,"(take a COVID test as well)",y,"to ensure that you are safe from errors in our predicitons"
                        )
                        break

                    else:
                        print(
                            "Dear",y,", you have a lower risk of having", x,
                            ", but from now on, avoid crowds to ensure your safety"
                        )
                        print(
                            "\nThank you so much for using our application.  Hope you get better soon from",x,"(take a COVID test as well)",y,"to ensure that you are safe from errors in our predicitons"
                        )
                        break
            else:
                print(
                    "Dear",y,",Good job for avoiding mass gatherings, but ensure to stay at home and maintain all social protocols at the place you are at. "
                )
                print(
                    "\nThank you so much for using our application.  Hope you get better soon from",x,"(take a COVID test as well)",y,"to ensure that you are safe from errors in our predicitons"
                )
        else:
            print(
                "Dear",y,",Good Job, but now follow all COVID protocols and don't go to large crowds"
            )
            print(
                "\nThank you so much for using our application.  Hope you get better soon from",x,"(take a COVID test as well)",y,"to ensure that you are safe from errors in our predicitons"
            )


def symptoms(y):
    a = "yes"
    b = "no"
    d = "Delta Variant of COVID"
    o = "omicron Variant of COVID"
    f = "Flu"
    c = "Common Cold"
    acns = ["yes", "no", "YES", "NO", "YEs", "No", "Yes", "yEs", "nO", "yES"]
    input("Please respond to the following questions in a Yes/No format only")
    v = "none"
    while True:
        cough = str(input("Have you been coughing frequently? "))
        cough = cough.lower()
        if cough not in acns:
            print("Please write the answer again in the proper format. ")
            continue
        else:
            break

    while True:
        runny_nose = str(input("Is your nose runny? "))
        runny_nose = runny_nose.lower()
        if runny_nose not in acns:
            print("Please write the answer again in the proper format. ")
            continue
        else:
            break
    while True:
        sneezing = str(input("Have you been sneezing frequently? "))
        sneezing = sneezing.lower()
        if sneezing not in acns:
            print("Please write the answer again in the proper format. ")
            continue
        else:
            break
    while True:
        shortness_of_breath = str(
            input("Do you have any difficulty in  breathing? "))
        shortness_of_breath = shortness_of_breath.lower()
        if shortness_of_breath not in acns:
            shortness_of_breath = shortness_of_breath.lower()
            print("Please write the answer again in the proper format. ")
            continue
        else:
            break
    while True:
        sore_throat = str(input("Do you have a sore throat? "))
        sore_throat = sore_throat.lower()
        if sore_throat not in acns:
            sore_throat = sore_throat.lower()
            print("Please write the answer again in the proper format. ")
            continue
        else:
            break
    while True:
        fever = str(input("Do you have a fever? "))
        fever = fever.lower()
        if fever not in acns:
            fever = fever.lower()
            print("Please write the answer again in the proper format. ")
            continue
        else:
            break
    while True:
        night_sweats = str(input("Do you sweat in the night? "))
        night_sweats = night_sweats.lower()
        if night_sweats not in acns:
            night_sweats = night_sweats.lower()
            print("Please write the answer again in the proper format. ")
            continue
        else:
            break
    while True:
        chills = str(input("Have you been getting chills recently? "))
        chills = chills.lower()
        if chills not in acns:
            chills = chills.lower()
            print("Please write the answer again in the proper format. ")
            continue
        else:
            break
    while True:
        headache = str(input("Have you been getting headaches recently? "))
        headache = headache.lower()
        if headache not in acns:
            print("Please write the answer again in the proper format. ")
            continue
        else:
            break
    while True:
        loss_of_smell = str(input("Have you lost your sense of smell? "))
        loss_of_smell = loss_of_smell.lower()
        if loss_of_smell not in acns:
            print("Please write the answer again in the proper format. ")
            continue
        else:
            break
    while True:
        fatigue = str(
            input(
                "Have you been feeling tired and getting a lot of fatigue? "))
        fatigue = fatigue.lower()
        if fatigue not in acns:
            print("Please write the answer again in the proper format. ")
            continue
        else:
            break
    while True:
        try:
            Time = int(input("How long did it take for symptoms to show? "))
        except ValueError:
            print("Sorry, but you must enter numerical Units. ")
            continue
        if Time < 1 or Time > 5:
            print(
                "Sorry,  Invalid Input, these diseases mostly occur between 1 to 5 days, which are the limitations of the code."
            )
            continue
        else:
            break
    listof = [
        "Cancer", "Chronic kidney disease", "Chronic Lung disease",
        "Dementia", "Neurological Conditions", "Diabetes",
        "Down Syndrome", "Heart conditions", "HIV",
        "Weakened Immune system", "Mental Health conditions",
        "Overweight and obesity", "Sickle cell disease",
        "Smoking, current or former", "Substance use disorders",
        "Tuberculosis"
    ]
    print(listof)
    dis = str(input("Have you got any of these diseases[Yes/No]? "))
    z=" your chronic condition"
    if dis == "yes" and cough == "yes" and runny_nose == "yes" and sneezing == "yes" and shortness_of_breath == "yes" and sore_throat == "yes" and fever == "yes" and night_sweats == "yes" and chills == "yes" and headache == "yes" and loss_of_smell == "yes" and fatigue == "yes":
        print(
            "You are in an extreme chronic condition and so go to a doctor as soon as possible. "
        )
        travel(z,y)
    elif dis == "yes" and cough == "no" and runny_nose == "no" and sneezing == "no" and shortness_of_breath == "no" and sore_throat == "no" and fever == "no" and night_sweats == "no" and chills == "no" and headache == "no" and loss_of_smell == "no" and fatigue == "no":
        print(
            "Be careful as you are in dangerous condition, and maintain COVID protocols all the time to ensure your safety. "
        )
        travel(v,y)

    elif dis == "no" and cough == "yes" or runny_nose == "yes" or sneezing == "yes" or shortness_of_breath == "yes" or sore_throat == "yes" or fever == "yes" or night_sweats == "yes" or chills == "yes" or headache == "yes" or loss_of_smell == "yes" or fatigue == "yes":
        print("Please continue")
        if cough == a and runny_nose == a and sneezing == b and shortness_of_breath == a and sore_throat == a and fever == a and night_sweats == b and chills == a and headache == a and loss_of_smell == a and fatigue == a and Time == 4 or Time == 5:
            print("You are most likely to have Delta Variant of COVID")
            travel(d,y)
        elif cough == a and runny_nose == a and sneezing == a and shortness_of_breath == b and sore_throat == a and fever == a and night_sweats == a and chills == a and headache == a and loss_of_smell == a and fatigue == a and Time == 2 or Time == 3:
            print("You are most likely to have omicron Variant of COVID")
            travel(o,y)

        elif cough == a and runny_nose == a and sneezing == b and shortness_of_breath == b and sore_throat == a and fever == a and night_sweats == b and chills == a and headache == a and loss_of_smell == b and fatigue == a and Time == 2 or Time == 3:
            print("You are most likely to have the flu")
            travel(f,y)

        elif cough == a and runny_nose == a and sneezing == a and shortness_of_breath == b and sore_throat == a and fever == a and night_sweats == b and chills == b and headache == a and loss_of_smell == b and fatigue == a and Time == 1 or Time == 3:
            print("You are most likely to have the common cold")
            travel(c)
        else:
            if cough == b and runny_nose == a and sneezing == a and shortness_of_breath == b and sore_throat == a and fever == b and night_sweats == b and chills == b and headache == a and loss_of_smell == b and fatigue == a and Time == 2 or Time == 3:
                print("You might have omicron Variant of COVID")
                travel(o,y)

            elif cough == a and runny_nose == b and sneezing == b and shortness_of_breath == b and sore_throat == b and fever == a and night_sweats == b and chills == a and headache == a and loss_of_smell == b and fatigue == a and Time == 2 or Time == 4:
                print("You might have the flu")
                travel(f,y)

            elif cough == a and runny_nose == a and sneezing == b and shortness_of_breath == b and sore_throat == a and fever == a and night_sweats == b and chills == b and headache == b and loss_of_smell == a and fatigue == b and Time == 1 or Time == 3:
                print("You might have the common cold")
                travel(c,y)
            else:
                print(
                    "Your inputs did not match any of the symptoms of any of the diseases specifically"
                )
                travel(v,y)

    elif dis == "no" and cough == "no" and runny_nose == "no" and sneezing == "no" and shortness_of_breath == "no" and sore_throat == "no" and fever == "no" and night_sweats == "no" and chills == "no" and headache == "no" and loss_of_smell == "no" and fatigue == "no":
        print(
            "You are in no danger, but be careful and follow all COVID protocols to ensure your safety and the safety of others around you"
        )
        travel(v,y)


print("Welcome to the COVID Predictor")
Name = str(input("What is your name? "))
while True:
    try:
        age = int(input("Please enter your age: "))
    except ValueError:
        print("Sorry, Invalid Input. ")
        continue

    if age < 5 or age > 95:
        print(
            "Sorry, Invalid Input, it should only be in between 5 and 95 years of age as the input for this COVID predictor. "
        )
        continue
    else:
        break
if age >= 60:
    while True:
        try:
            doses = int(input("Please enter the number of doses: "))
        except ValueError:
            print("Sorry, Invalid Input. ")
            continue

        if doses <= 0 or doses > 4:
            print(
                "Sorry, Invalid Input, it can only be in between 1 and 3 doses."
            )
            continue
        else:
            symptoms(Name)
            break

elif age >= 18:
    while True:
        try:
            doses = int(input("Please enter the number of doses taken: "))
        except ValueError:
            print("Sorry, Invalid Input. ")
            continue

        if doses <= 0 or doses >= 3:
            print(
                "Sorry, Invalid Input, it can only be in between 1 and 2 doses."
            )
            continue
        else:
            if doses == 1:
                print("Ensure that you take your", str(2 - doses),
                      "dose, and Follow corona protocols at all times. ")
                symptoms(Name)
                break
            elif doses == 2:
                print("Follow all corona protocols at all times")
                symptoms(Name)
                break
else:
  if age<15:
    print("You can get 0 doses")
    symptoms(Name)
  elif age>=15 and age<=18:
    print("You can get 1 dose of vaccination")
    symptoms(Name)
