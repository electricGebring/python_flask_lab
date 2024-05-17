Johans flask app

1. Checka ut projektet
2. Se till att du har Python3 installerat
3. Skapa en virtual environment och aktivera den (python3 -m venv venv && source venv/bin/activate)
4. Installera alla dependencies från requirements.txt (pip install -r requirements.txt)

Varje gång du sedan behöver lägga till ett nytt dependency, så installerar du den ("pip install whatever_lib"),
och sedan så sparar du den uppdaterade listan med installerade dependencies till requirements.txt (pip freeze > requirements.txt), och så checkar du in den filen.


