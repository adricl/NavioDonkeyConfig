
import sys
from  donkeycar.management  import base
import donkeycar as dk
"""
This is the fuction linked to the "donkey" terminal command.
"""



if __name__ == '__main__':
    commands = {
            'createcar': base.CreateCar,
            'findcar': base.FindCar,
            'calibrate': base.CalibrateCar,
            'tubclean': base.TubManager,
            'tubhist': base.ShowHistogram,
            'tubplot': base.ShowPredictionPlots,
            'tubcheck': base.TubCheck,
            'makemovie': base.MakeMovie,
            'sim': base.Sim,
                }

    args = sys.argv[:]
    command_text = args[1]

    if command_text in commands.keys():
        command = commands[command_text]
        c = command()
        c.run(args[2:])
    else:
        dk.util.proc.eprint('Usage: The availible commands are:')
        dk.util.proc.eprint(list(commands.keys()))    