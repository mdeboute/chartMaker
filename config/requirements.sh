#!/bin/bash
# requirements.sh
clear
cd ../chartMaker/
chmod +ux app.sh
cd
clear
echo "Bonjour $USER, ceci est un script de configuration."
echo "Tu as juste à suivre les différentes étapes et à rentrer ton mot de passe mac si on te le demande."
echo "C'est parti !"
echo "(Appuyez sur Entrée pour continuer)"
read
xcode-select --install
echo "(Appuyez sur Entrée pour continuer)"
read
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
echo "(Appuyez sur Entrée pour continuer)"
read
brew install python3
echo "(Appuyez sur Entrée pour continuer)"
read
pip install pandas
echo "(Appuyez sur Entrée pour continuer)"
read
pip install matplotlib
echo "(Appuyez sur Entrée pour continuer)"
read
brew install figlet
echo "(Appuyez sur Entrée pour continuer)"
read
echo "C'est terminé !"
sleep 1s
clear
