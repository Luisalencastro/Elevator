import time
floors = ['G','1','2','3','4','5']
uses = 0


def request_floor():
        floor_choice_file = open('floor_file.txt','r')
        global floor_choice
        floor_choice = floor_choice_file.read()    #open file n read
        floor_choice_file.close()
        
        print('You are currently on the floor %s' % floor_choice)
        print('please enter the floor you would like to travel to')
        global old_floor
        old_floor = floor_choice
        global floor_choice_verify
        floor_choice_verify = input().upper() #user input
        verify_floor()


def verify_floor():
        if floor_choice_verify in floors: #verify if input in floors
                global floor_choice
                floor_choice = floor_choice_verify #if true then save as floor_choice
                floor_choice_file = open('floor_file.txt','w+')
                floor_choice_file.write(floor_choice) 
                floor_choice_file.close()
                travel_to_floor()
        else:
                print('That floor does not exist, please try again')
                request_floor()


def travel_to_floor():
        global old_floor
        global floor_choice
        if old_floor > floor_choice:
                old_floor = int(old_floor)
                floor_choice = int(floor_choice)
                while old_floor != floor_choice:
                        old_floor = old_floor - 1
                        time.sleep(1)
                        print('floor %d' % old_floor)
                time.sleep(1)
                print('Reached floor %d, please exit.' %floor_choice)
                time.sleep(1)

        elif old_floor < floor_choice:
                old_floor = int(old_floor)
                floor_choice = int(floor_choice)
                while old_floor != floor_choice:
                        old_floor = old_floor + 1
                        time.sleep(1)
                        print('floor %d' % old_floor)
                time.sleep(1)
                print('Reached floor %d, please exit.' %floor_choice)
                time.sleep(1)

                

        request_floor()
                
request_floor()
