#menu driven shell script sample template
## ----------------------------------
# Step #1: Define variables
# ----------------------------------
RED='033[0;41;30m'
STD='033[0;0;39m'

# ----------------------------------
# Step #2: User defined function
# ----------------------------------
pause(){
read -p "Press [Enter] key to continue..." fackEnterKey
}

one(){
clear
nmcli d wifi
break
}

# do something in two()
two(){
clear
sudo ifconfig wlan0 down
sudo iwconfig wlan1 mode monitor
now=$(date +'%mm-%dd-&Y')
sudo xterm -maximized -e horst -i wlan1 -o /home/chip/dumps//horst-$now.txt
break
}
three(){
clear
sudo ifconfig wlan0 down
sudo iwconfig wlan1 mode monitor
sudo airodump-ng wlan1
break
}
four(){
clear
sudo iwlist scan
break
}
five(){
clear
echo "Bringing if up and down"
sudo ifconfig wlan0 up
echo "changing wlan1 mode"
sudo iwconfig wlan1 mode managed
sudo sleep 5
echo "Restarting Network Manager"
sudo service network-manager restart
break
}

# function to display menus
show_menus() {
clear
echo "~~~~~~~~~~~~~~~~~~~~~"
echo "HACK CHIP WIFI TOOLS"
echo "~~~~~~~~~~~~~~~~~~~~~"
echo "1. Network Manger cli wifi scan"
echo "2. horst"
echo "3. Airodump-ng"
echo "4. iwlist scan"
echo "5. Restart Network Manger"
echo "6. Exit"
}

read_options(){
local choice
read -p "Enter choice [ 1 - 6] : " choice
case $choice in
1) one ;;
2) two ;;
3) three ;;
4) four ;;
5) five ;;
6) exit 0;;
*) echo -e "${RED}Error...${STD}" && sleep 2
esac
}

# ----------------------------------------------
# Step #3: Trap CTRL+C, CTRL+Z and quit singles
# ----------------------------------------------
trap '' SIGINT SIGQUIT SIGTSTP

# -----------------------------------
# Step #4: Main logic - infinite loop
# ------------------------------------
while true
do

show_menus
read_options
done