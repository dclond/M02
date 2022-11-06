"""
David Clond
SDEV 220 M02
clond_m02_lab.py


This application takes a student's last name from the user. If the input equals
 'ZZZ' the program exits.Otherwise, it then promps for the student's first name
 and GPA. The GPA is then tested to see if the student qualifies for the Dean's 
 list and Honor Roll.
"""

deans_list_gpa = 3.5
honor_roll_gpa = 3.25
#gpa_domain_floor = 0.0
#gpa_domain_ceiling = 4.0
exit_string = "ZZZ"

last_name_prompt = f"Enter the student's last name, or {exit_string} to quit: "
first_name_prompt = "Enter the student's first name: "
gpa_prompt = "Enter student's GPA: "
deans_list_msg = "has made the Dean's List."
honor_roll_msg = "has made the Honor Roll."
rejection_msg = "'s GPA is not sufficient to receive honors."

# ask for student's last nam
last_name = input(last_name_prompt)

# quit if last name is 'ZZZ'
while(last_name != exit_string):
    # ask for  and accpet studen's first name
    first_name = input(first_name_prompt)

    # ask for student's GPA as a float
    valid_input = False
    while( not valid_input):
        try:
            gpa = float(input(gpa_prompt))
            # Test input against accepted gpa doman
            #
            # the gpa domain is not defined for this assignment
            #if(gpa_domain_floor <= gpa <= gpa_domain_ceiling):
            #    valid_input = True
            #else:
            #    valid_input = False

            valid_input = True
        except:
            print("Invalid entry.")

    # if GPA is 3.5 or higher, print msg indicating student is on the Dean's List
    if(gpa >= deans_list_gpa):
        print(f"\t{first_name} {last_name} {deans_list_msg}")

    # if GPA is 3.25 or higher, print msg indicating student has made the Honor Roll
    if(gpa >= honor_roll_gpa):
        print(f"\t{first_name} {last_name} {honor_roll_msg}")

    # else print, print msg indicating student gpa is not high enough
    else:
        print(f"\t{first_name} {last_name}{rejection_msg}")

    # ask for student's last name
    last_name = input(last_name_prompt)

print("Exiting")
