import boto3
import function


def Menu():
    print('--------------------------------------------------\n')
    print('        Amazon AWS Control Panel using SKD\n')
    print('--------------------------------------------------\n')
    print('1. list instance             2. available zones\n')
    print('3. start instance            4. available regions\n')
    print('5. stop instance             6. create instance\n')
    print('7. reboot instance           8. list images\n')
    print('9. terminate instance       99. quit\n')
    print('--------------------------------------------------\n')
    print('--------------------------------------------------\n')


Menu()

while True:
    num = int(input('Enter an Integer : '))
    if num == 1:
        function.ListInstance()
    elif num == 2:
        function.AvailableZone()
    elif num == 3:
        function.StartInstance()
    elif num == 4:
        function.AvailableRegions()
    elif num == 5:
        function.StopInstance()
    elif num == 6:
        function.CreateInstance()
    elif num == 7:
        function.RebootInstance()
    elif num == 8:
        function.ListImages()
    elif num == 9:
        function.TerminateInstance()
    elif num == 99:
        break

    Menu()
print('Quit')
