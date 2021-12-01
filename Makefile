install-geckodriver:
	# "-nc" skips downloads if file already there	
	wget -nc https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-linux64.tar.gz 
	tar xvfz geckodriver-v0.30.0-linux64.tar.gz
	mv geckodriver ~/.local/bin
	rm geckodriver-v0.30.0-linux64.tar.gz

clean-geckodriver:
	rm ~/.local/bin/geckodriver