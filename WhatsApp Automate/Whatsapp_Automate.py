import pywhatkit as what
import emoji
from emoji import emojize

# date = input("Date ")
# start_time = input("StartTime ")
# end_time = input("EndTime ")
# contest_title = input("Title ")
# contest_link = input("Link ")
# todo = input("Which one?")
emoji = "\U0001F601"
# R1 =f"""Reminder!

# Contest: *{contest_title }*
# Date: {date} 
#  *(Tomorrow)* 
# Time: {start_time} - {end_time} 
# Link: {contest_link}

# Happy Solving {emoji}"""

emoji= emojize(":beaming_face_with_smiling_eyes:")
CP_Community = 'F7yGOIUylZN3XJQmoBGgP4'
Trial = 'GzG70VVav0oKxWKcV6b4ML'
Whatsapp_Grp = 'Bykt8XSyo012DFUBavPWxC'
Mom = "+919320343536"
Mantra = '+918238979098'
Pop = "+919320252627"
Me = '+918657642258'
Shruthi = '+916366182979'

# print(emoji)
# message = "This is just the unicode testing  \U0001F91F"
# what.sendwhatmsg_to_group(group_id =Trial, message=emoji,time_hour=19,time_min=4)

# what.sendwhatmsg(phone_no=Mom, message="I love you maa \U+1F600", time_hour=19, time_min=40, wait_time=20, tab_close=True, close_time=5)
# what.sendwhatmsg_instantly(phone_no=Mantra, message=message)
# what.sendwhatmsg(phone_no=Pop, message= "HI this is a test message", time_hour=9, time_min=15, wait_time=15, tab_close=True, close_time=5)

message1 = f'''Hello Junta,
Greetings from The Programming Club, CFI!

Wondering what to do in your Winter Vacations?

Don't worry, The Programming Club has you covered! We're back with exciting sessions and contests coming up this month to help you delve deeper into the world of Competitive Programming through a specially curated workshop: the Winter Programming Camp!
 
 
What can you expect from this Camp?
 
We'll have sessions for Dynamic Programming and Graphs each. We will be covering the theory related to these topics from the very basics, so don't worry if you aren't aware of these concepts :) 
Apart from that, we'll have dedicated problem solving and doubt clarification sessions in order to give you hands-on experience on these topics. 
To reinforce your learning, we would provide a well-curated Problem Set covering all the intricacies of the topics after each session. 

We also have designed a contest in order to help you practice and apply the  knowledge in real-time and also to add a little fun and a healthy competitive spirit to the overall learning process.'''

message2 = ''' What do I need to know beforehand?

Basic Competitive Programming knowledge (Basics of C++, Multidimensional arrays,  functions, recursion and STL data structures - vectors, sets and priority queues) is sufficient to attend and understand everything in the camp. 


I'm new to Competitive Programming. Where can I start?

We have covered the fundamentals of CP & C++ in  Weekend Programming Sessions - G0 and also in the Summer Programming Camp sessions. Do check them out and get started with these basic topics.

Weekend Programming Sessions - G0 : https://www.youtube.com/playlist?list=PLYjg3GwRYFLV6yZUT3ktLKrGBdzlhZ1gH
Summer Programming Camp Sessions :
https://www.youtube.com/playlist?list=PLYjg3GwRYFLUiZ5cMTMaSsIi1rrQN-Wym

For further updates and information , please join this WhatsApp group:
https://chat.whatsapp.com/LOiAfBYdclvDeQvj3rR91f'''

# what.sendwhatmsg_instantly(phone_no=Shruthi, message=message, tab_close= True, close_time=10)
what.sendwhatmsg_to_group_instantly(group_id=Trial, message=message1)
what.sendwhatmsg_to_group_instantly(group_id=Trial, message=message2)

