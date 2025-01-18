@echo off
color 4
title Messagerie Discord Bot
echo =================================================
echo      Bienvenue dans le Bot Messenger Discord 
echo =================================================
echo.
set /p message=Entrez le message que vous voulez envoyer sur le serveur Discord : 
echo.
echo Merci d'avoir utiliser le programme de Zakxyo !
python send_message.py "%message%"
echo Message envoyer ! Appuyez sur une touche pour quitter...
pause >nul
