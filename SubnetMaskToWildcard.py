### [===== SUBNET TO WILDCARD CONVERTER =====] ###
# This also works in reverse

## VARIABLES ##
SubnetParts = []
Wildcard = ""
SubnetMask = input("Subnet mask (EX : 255.255.255.0) >> ")

## MAIN CODE ##
try:
    # Split the subnet into 4 parts.
    SubnetParts = SubnetMask.split('.')

    # Make sure the subnet mask is the correct size
    # If it isn't, throw an error and quit
    if len(SubnetParts) < 4 or len(SubnetParts) > 4:
        raise Exception("Invalid subnet mask! The subnet mask must be 32 bits in size.")
    
    # Loop through all 4 parts of the subnet mask
    # Each value is separated by the a period
    for part in SubnetParts:
        # If a value isn't numeric, throw an error and quit
        # Strip any hashes to ensure negative numbers are also detected correctly
        if not part.lstrip('-').isnumeric():
            raise Exception(f"Invalid subnet mask! The value \"{part}\" is not numeric.")
            sys.exit(0)

        # Convert the part into an 8 bit integer (0 to 255)
        part = int(part)

        # Make sure the value is in range for an 8 bit number (0 to 255)
        # If it's not, throw an error and quit
        if part < 0 or part > 255:
            raise Exception(f"Invalid subnet mask! Values cannot be less than 0 or greater than 255.")
            sys.exit(0)

        # Append a period and the inverted value to the wildcard string
        Wildcard += '.' + str(~part & 0xFF)
        
    # Remove the first character from the wildcard string
    # We don't need a period at the beginning
    Wildcard = Wildcard[1:]

    # Output the result to the console
    print(f"The wildcard for {SubnetMask} is {Wildcard}.")

except Exception as ex:
    print(f"[ERROR] >> {ex}")
    
