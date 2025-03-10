'''
Can you change the self-parameter inside a class to something else (say'harry').
Try changing self to “slf” or “harry” and see the effects.
'''

# It will doesnot effect the output.
# But it will decrease readability.

class Main:
    company = 'Microsoft'
    def __init__(ssr,name,place):
        ssr.name = name
        ssr.place = place

    def greet(ssr):
        print(f'Hello {ssr.name}')


t = Main('Sathvik','Hyderabad')
t.greet()