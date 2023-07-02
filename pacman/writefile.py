import os

fileName = 'all_data_pacman.arff'
#fileName = 'filter_data_pacman_manual1.arff'
#fileName = 'filter_data_pacman_manual2.arff'
os.path.exists(fileName)

f = open(fileName, "a")
f.write("@RELATION all-data-pacman\n\n\n")
#f.write("@RELATION filter_data_pacman_manual1\n\n\n")
#f.write("@RELATION2filter_data_pacman_manual2\n\n\n")

f.write("   @ATTRIBUTE PosX NUMERIC\n")
f.write("   @ATTRIBUTE PosY NUMERIC\n")
f.write("   @ATTRIBUTE LastDirection {East, West, North, South, Stop}\n")
f.write("   @ATTRIBUTE Ghost1X NUMERIC\n")
f.write("   @ATTRIBUTE Ghost1Y NUMERIC\n")
f.write("   @ATTRIBUTE Ghost2X NUMERIC\n")
f.write("   @ATTRIBUTE Ghost2Y NUMERIC\n")
f.write("   @ATTRIBUTE Ghost3X NUMERIC\n")
f.write("   @ATTRIBUTE Ghost3Y NUMERIC\n")
f.write("   @ATTRIBUTE Ghost4X NUMERIC\n")
f.write("   @ATTRIBUTE Ghost4Y NUMERIC\n")
f.write("   @ATTRIBUTE CloseGhostDist NUMERIC\n")
f.write("   @ATTRIBUTE Score NUMERIC\n")
f.write("   @ATTRIBUTE Direction {East, West, North, South, Stop}\n\n")
f.write("   @data\n")
