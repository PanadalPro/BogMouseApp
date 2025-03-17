I've put all the files in a zip because it contained the app and a venv, which was very heavy and for some reason I was unable to load it into github. Anyways, if you don't trust this, I left you the python file aswell as the spec (for pyinstaller) file, so that you can make yourself the venv and build the app. Good luck!

By the way, if you download the zip file and open the app and it says it couldn't verify it, right-click the app, hit Open, and then Open in the prompt and the app will open. You'll only need to do this the first time.

### Create venv

    In VSCode, head onto the status bar (bottom bar) and click the python interpreter (the button that shows the python version), choose create virtual environment and choose a .venv environment.

    In this case the environment is already created, so if you want to tinker with it you will need to select it. Go to the button I mentioned above, choose Enter Interpreter Path and type in: ".venv/bin/python".

### Install rumps

    pip install rumps

### Install pynput

    pip install pynput

### Install pyinstaller

    pip install -U pyinstaller

### Build the App

    pyinstaller --noconfirm spec.spec

    --noconfirm automatically overwrites the old build without prompting this.

    This creates the MacOS .app under the dist directory.

### PERMISSIONS!

    When you run the app for the first time, you will need to allow it access to Accessibility and Input Monitoring. Go to System Settings, then Security & Privacy and add or activate the Mouse App under Accessibility and Input Monitoring. Then, enjoy the app!

### Auto Run

    Open System Settings, then in the sidebar click General, scroll down until you see Login Items & Extensions and add the app here. It will automatically start when your computer powers on.
