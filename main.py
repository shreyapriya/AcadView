from spydetails import spy, Spy_info, Chat_msg, myfriends
from termcolor import colored
from steganography.steganography import Steganography
from datetime import datetime
#import library for encoding and decoding data
# justinApp is here declared and if it is true it will run app else not run
# mport library to get information realated to time and period

justinApp = True
while justinApp:

    # Printing something in python
    print 'WELCOME !!!! YOUR APP HAS STARTED'
    # we are creating the variable for status messages
    status_messages = ['cant talk', 'at world tour', 'my life']

    # selecting if we continue as default user or a new user
    ip = 'Do you want to continue as ' + spy.salutation + ' ' + spy.name + '(Y/N)?' + '(i.e our DEFAULT USER???)'
    my_ip = raw_input(ip)

    # here we hawe have created the add status function
    def my_status():
        updated_status = None

        if spy.current_status != None:
            print colored('Your current status msg is : %s \n' % (spy.current_status), 'blue')
        else:
            print "oops!!!you don't have any status msg"

        default = raw_input("Do you want to select from the older status (Y/N) : ")

        if default.upper() == 'N':
            new_status = raw_input('plz enter your new status msg : ')

            # here we are checking that the status is blank or not

            if len(new_status) > 0:
                status_messages.append(new_status)
                updated_status = new_status
            else:
                print 'Plz enter a valid status'

        elif default.upper() == 'Y':
            item_position = 1

            # here we are checking for status in status_message list

            for message in status_messages:
                print '%d. %s' % (item_position, message)
                item_position = item_position + 1

            # here we are selecting a status from the pre-existing status

            message_selection = int(raw_input('\nChoose from above msgs'))

            if len(status_messages) >= message_selection:
                updated_status = status_messages[message_selection - 1]
            else:
                print ''
        else:
            print 'The option is not valid! choose (Y/N) : '

        if updated_status:
            print colored('your updated msg is: %s' % (updated_status), 'blue')
        else:
            print 'sorry !!! You did not update your status'
        return updated_status


    # here we are created the my_friends function and we have created a dictionary of new_friends

    def my_friends():
        new_friends = Spy_info('', '', 0, 0.0)

        new_friends.name = raw_input(" add your friend's name : ")
        new_friends.salutation = raw_input("Are they Mr. or Mrs.or anyone  else? : ")
        new_friends.name = new_friends.name + ' ' + new_friends.salutation
        new_friends.age = int(raw_input('age is : '))
        new_friends.rating = float(raw_input('rating is : '))

        if len(new_friends.name) > 0 and 12 < new_friends.age < 50 and new_friends.rating >= spy.rating:
            myfriends.append(new_friends)
            print 'yayyy !!! your new Friend is  added'
        else:
            print "oops !!! Invaid entry of your friend, he can't be added"
        return len(myfriends)


    # here we are selecting a friend from friends list and then we are returning the index of that  selected friend

    def sel_friend():
        item = 0
        # we have declared a new variable:- friend in which we are taking the value of new added friends
        for friend in myfriends:
            print '%d %s aged %d with rating %.2f is online' % (item + 1, friend.name, friend.age, friend.rating)
            item = item + 1

        choose_friend = raw_input('plz choose from your friends : ')
        choose_friend_position = int(choose_friend) - 1
        return choose_friend_position


    # here we are sending the encripted message via image

    def send_msgs():

        # choose_friend function is recieving friends to which we want to send message & sel_friend function is giving the index of selected friend

        choose_friend = sel_friend()
        my_image = raw_input("plz enter the name of your image : ")
        new_image = "C:\Users\LENOVO\PycharmProjects\spychat\img\output.jpg"
        text = raw_input(colored('Enter your msg here : ', 'red'))
        if text:
            if len(text) < 100:
                Steganography.encode(my_image, new_image, text)
            else:
                print 'length should not go beyond 100'
        else:
            print 'do not enter blank/empty string'
        newchat = Chat_msg(text, True)

        myfriends[choose_friend].chats.append(newchat)
        print 'wow !!! your secret msg is ready! plz check '


    # here we are sending the decripted message via image
    def read_msgs():

        # here we are selecting a friend from whom we want to read messages &  sel_friend function returns the index of selected friend

        sender = sel_friend()
        new_image = raw_input("plz enter file name : ")
        secret_text = Steganography.decode(new_image)
        print colored(secret_text, 'red')

        newchat = Chat_msg(secret_text, False)

        myfriends[sender].chats.append(newchat)

        print "awesome !! Your secret msg has been saved!"


    # here we are displaying the chat history for the selected user

    def read_history():
        read = sel_friend()
        print '\n'

        # here we are returning the index of selected friend for whom you want to read the messages

        for chat in myfriends[read].chats:
            if chat.sent_by_me:
                print colored('[%s] %s: %s' % (chat.time.strftime("%d %B %Y"), 'you said:', chat.message), 'blue')
            else:
                print colored(
                    '[%s] %s said: %s' % (chat.time.strftime("%d %B %Y"), myfriends[read].name, chat.message), 'blue')


    # here we are creating a chat function :- my_chat() in which all the cases and their validations are done

    def my_chat(spy):
        current_status = None

        spy.name = spy.salutation + ' ' + spy.name

        if 12 < spy.age < 50:
            print 'Authentication complete. Welcome ' + spy.name + ' age: ' + str(spy.age) + ' and rating of: ' + str(
                spy.rating) + ' Proud to have you onboard'

            if spy.rating > 4.5:
                print 'Awesome!'
            elif spy.rating > 3.5 and spy.rating <= 4.5:
                print 'Best!'
            elif spy.rating >= 2.5 and spy.rating <= 3.5:
                print 'Good'
            else:
                print 'it should be nice if the spy is nice'

            menu = True

            # here we have created the menu to easily choose an option..

            while menu:
                choices = raw_input(colored(
                    'what do you want to : \n 1. Add a status update \n 2. Add a friend \n 3. Send a secret message \n 4. Read a secret message \n 5. Read Chats from a user \n 6. close application\n ',
                    'green'))
                menu_choice = choices
                if menu_choice.isdigit():
                    if len(menu_choice) > 0:
                        menu_choice = int(menu_choice)

                        # here we are selecting the choices for the menu

                        if menu_choice == 1:
                            print 'you have choosed to update the status'
                            spy.current_status = my_status()

                        elif menu_choice == 2:
                            print 'You have choosed to add a friend'
                            # we got the no of friends from the user
                            number_of_friends = my_friends()
                            print 'You have %d friends' % number_of_friends

                        elif menu_choice == 3:
                            print 'You have choosed to send a secret message'
                            send_msgs()

                        elif menu_choice == 4:
                            print 'You have choosed to read message from user'
                            read_msgs()

                        elif menu_choice == 5:
                            print 'you have choosed to read chat history'
                            read_history()

                        else:
                            menu = False
                    else:
                        print 'alas!!! input was invalid'
                else:
                    print 'alas!!!! input was invalid'
        else:
            print 'alas!!! input was invalid'


    # it is the main code of our program

    if my_ip.upper() == 'Y':
        my_chat(spy)
        justinApp = False
    elif my_ip.upper() == 'N':
        spy = Spy_info('', '', 0, 0.0)
        spy.name = raw_input('Welcome to our spy chat!!!! Enter your spy-name : ')

        # here we are checking for the valid names of spy

        if spy.name.isalpha():
            if len(spy.name) > 0:
                spy.salutation = raw_input('you are a Mr. or Miss. : ')
                spy.age = raw_input('your age is : ')

                # here we are checking for the valid age of spy

                if spy.age.isdigit():
                    spy.age = int(spy.age)
                    spy.rating = float(raw_input('your spy rating is : '))
                    my_chat(spy)

                else:
                    print ' plz enter a valid age....(hint: datatype should be integer)'
            else:
                print 'Plz enter a valid spyname... (hint: datatype should be character & there should be no spaces)'
        else:
            print 'Plz enter a valid spyname... (hint: datatype should be character & there should be no spaces)'
            justinApp = False
    else:
        print " now plz select a response : 'Y' or 'N'"
