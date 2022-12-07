import boto3

ec2 = boto3.resource('ec2')
ec2client = boto3.client('ec2')
keypairinfo = ec2client.describe_key_pairs()


def ListInstance():
    print('\nListInstance\n')
    for instance in ec2.instances.all():
        print("ID : "+instance.id + '\n',
              "Type : "+instance.instance_type + '\n',
              "Ami : "+instance.image.id + '\n',
              "State : "+instance.state.get('Name') + '\n')


def AvailableZone():
    print('\nAvailable Zone\n')
    Available_Zone_Arr = ec2client.describe_availability_zones().get('AvailabilityZones')
    for ZoneInfo in Available_Zone_Arr:
        print(
            '[Id] : '+ZoneInfo.get('ZoneId'),
            '[Region] : '+ZoneInfo.get('RegionName'),
            '[Zone] : '+ZoneInfo.get('ZoneName')
        )


def StartInstance():
    print('\nStartInstance\n')
    Instance_list()
    id = str(input('Enter instance id : '))
    ec2client.start_instances(InstanceIds=[id, ])
    print("Successfully started instance" + id)


def AvailableRegions():
    print('\nAvailable Regions\n')
    AvailableRegionArr = ec2client.describe_regions().get('Regions')
    for RegionInfo in AvailableRegionArr:
        print('[Region] : '+RegionInfo.get('RegionName'),
              ' [Endpoint] : '+RegionInfo.get('Endpoint'))


def StopInstance():
    print('\nStopInstance\n')
    Instance_list()
    id = str(input('Enter instance id : '))
    ec2client.stop_instances(InstanceIds=[id, ])
    print("Successfully stopped instance" + id)


def CreateInstance():
    ec2.create_instances(
        ImageId='ami-0eddbd81024d3fbdd',
        InstanceType='t2.micro',
        KeyName='keypair',
        MinCount=1,
        MaxCount=1
    )
    print('Successfully Create Instance\n')


def RebootInstance():
    print('\nRebootInstance\n')
    Instance_list()
    id = str(input('Enter instance id : '))
    response = ec2client.reboot_instances(
        InstanceIds=[id, ]
    )
    print('Susccess', response)


# Instance list menu
def Instance_list():
    print('----------------------인스턴스 리스트--------------------------\n')
    for instance in ec2.instances.all():
        print('[Instance ID] '+instance.instance_id,
              ' [Instance State] '+instance.state.get('Name'))
    print('--------------------------------------------------------------\n')
