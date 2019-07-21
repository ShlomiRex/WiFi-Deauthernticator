sudo ifconfig $1 down
sudo iwconfig $1 mode monitor
sudo ifconfig $1 up

