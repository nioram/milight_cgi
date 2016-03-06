# milight_cgi


a simple cgi to control milight lights

## Installation:

    1. Place cgi script in cgi-bin folder and make it executable.
    
    2. [Download](http://iqjar.com/download/jar/milight/milight_sources.zip) Milight Commandline Utility
    
    3. Extract Zip in Home folder and rename it to milight
    
    4. compile it (its cpp code)
    
    5. edit the this line in the cgi to the path where your tool is located :  echo "$(/home/insertyourusername/milight/milight     $ARGX $ARGY $ARGZ)"
    
    6. Profit!

## USAGE:

The optional ZONE argument specifies which bulb zone the command refers to.
If this argument is omitted, the command is considered to refer to all zones.

Possible values:

    ALL/0 - All zones
    
    1     - Zone 1
    
    2     - Zone 2
    
    3     - Zone 3
    
    4     - Zone 4
    
    ON                 - Turn the bulbs in the given zone on. 
    
    OFF                - Turn the bulbs in the given zone off.
    
    WHITE/W            - Set the color of the bulbs in the given zone to white.
    
    DISCO/D [+/-]      - If no parameter is specified, turn disco mode on.
                         The '+' optional parameter increases the disco speed.
                         The '-' optional parameter decreases the disco speed.
    
    BRIGHTNESS/B VALUE - Set the brightness of the bulbs in the given zone.
                         The VALUE mandatory parameter specifies the brightness
                         and must be an integer number in the range 1-19.
    
    COLOR/C VALUE      - Set the color of the bulbs in the given zone.
                         The VALUE mandatory parameter specifies the color
                         and must be an integer number in the range 0-255.

## Examples:
    myip/cgi-bin/milight.cgi?zone=0&cm=B&var=19

