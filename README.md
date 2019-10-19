# Remote control car

1. GETTING STARTED:

`
    pip3 install flask flask_restful flask_socketio
    python3 server.py
`

2. ADVANCED:
- On the Raspberry Pi, we made some service in order to run the server right after boot.
- You can setup the same service by:
    - Step 1: Getting to the sudo environment using `sudo -i`.
    - Step 2: Create a new Service instance using `nano /etc/systemd/system/server.service`
    - Step 3: Copy this code to the Service, replace `home/pi/remote-control-car/server.py` with your actual directory.
        `
            
            Description=Server Service
            After=network.target
            
            [Service]
            Type=simple
            Restart=always
            RestartSec=1
            User=pi
            ExecStart=/usr/bin/python3 /home/pi/remote-control-car/server.py
            
            [Install]
            WantedBy=multi-user.target
        `
    - Step 4: Reload Daemon using `systemctl daemon-reload` and enable Service on boot with `systemctl enable server`
    - Step 5: Reboot to check.

