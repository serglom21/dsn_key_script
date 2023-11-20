if [ ! -d "./venv" ]; then
    bash ./install.sh
    echo $GREEN; printf -- "-%.0s" $(seq $(tput cols)); echo $RESET
    echo $GREEN;echo "Running script"; echo $RESET
fi

source venv/bin/activate
python3 main.py