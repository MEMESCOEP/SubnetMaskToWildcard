### [===== SUBNET TO WILDCARD CONVERTER =====] ###
# For IPv4 networks; This can also convert wildcards to subnet masks
# Requires Python 3.3 or later

## IMPORTS ##
import ipaddress

## VARIABLES ##
SubnetParts = []
SubnetMask = ""
PrefixLen = 0
Wildcard = ""

## MAIN CODE ##
try:
    # Ask the user to enter an IPv4 subnet mask
    SubnetMask = input("Enter an IPv4 subnet mask (EX: 255.255.255.0) >> ")
    
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
        if part not in range(0, 256):
            raise Exception(f"Invalid subnet mask! Values cannot be less than 0 or greater than 255.")
            sys.exit(0)

        # Append a period and the inverted value to the wildcard string
        # 0xFF limits the value to be inside the uint8 range (0 to 255) (uint8 = 8 bit unsigned integer)
        # The '~' (bitwise NOT/invert) operator inverts the bits of the subnet part
        # The '&' (bitwise AND) operator results in 1 if both bits are 1, otherwise, it results in 0
        # See https://www.geeksforgeeks.org/python-bitwise-operators/ for more information
        Wildcard += '.' + str(~part & 0xFF)

        # Find the prefix length from the subnet mask in bits (Slash notation)
        PrefixLen = ipaddress.IPv4Network((0, SubnetMask)).prefixlen
        
    # Remove the first character from the wildcard string
    # We don't need a period at the beginning, and it just looks wrong lol
    Wildcard = Wildcard[1:]

    # Output the result to the console
    print(f"The wildcard for [/{PrefixLen}] {SubnetMask} is {Wildcard}")

except Exception as ex:
    print(f"[ERROR] >> {ex}")
    
