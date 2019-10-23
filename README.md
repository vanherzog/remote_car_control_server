# Remote control car

1. GETTING STARTED FROM SCRATCH:
- Since the Pi is dedicated for controlling the car only, we like to do everything in `sudo environment`. This makes interacting with services much easier.
    1. `sudo -i`.
    2. `cd /home/pi`.
    3. `apt-get update && apt-get upgrade`.
    4. `apt-get install git`.
    5. `ssh-keygen -t rsa -b 4096 -C "email@example.com"`
    6. `xclip -sel clip < ~/.ssh/id_ed25519.pub` and paste the content to your `https://gitlab.com/profile/keys`.
    7. `git@gitlab.com:hun.lam97/remote-control-car.git`. After this the code should be in `/home/pi/remote-control-car`
    8. `apt-get update && apt-get upgrade`.

2. RUNNING IT:


    
>  pip3 install flask flask_restful flask_socketio
>  python3 server.py


3. ADVANCED:
- On the Raspberry Pi, we made some service in order to run the server right after boot.
- You can setup the same service by:
    1. Getting to the sudo environment using `sudo -i`.
    2. Create a new Server Service instance using `nano /etc/systemd/system/server.service`. Copy this code to the Service, replace `home/pi/remote-control-car/server.py` with your actual directory.
>             [Unit]
>             Description=Server Service
>             After=network.target
>             
>             [Service]
>             Type=simple
>             Restart=always
>             RestartSec=1
>             User=pi
>             ExecStart=/usr/bin/python3 /home/pi/remote-control-car/server.py
>             
>             [Install]
>             WantedBy=multi-user.target

    3. Create a new Camera Service instance using `nano /etc/systemd/system/camera.service`. Copy this code to the Service, replace `home/pi/remote-control-car/camera.py` with your actual directory.
            > [Unit]
>             Description=Camera Service
>             After=network.target
>             
>             [Service]
>             Type=simple
>             Restart=always
>             RestartSec=1
>             User=pi
>             ExecStart=/usr/bin/python3 /home/pi/remote-control-car/camera.py
>             
>             [Install]
>             WantedBy=multi-user.target

    4. Reload Daemon using `systemctl daemon-reload` and enable Service on boot with `systemctl enable server`
    5. Reboot with `sudo reboot -h now` to check.


