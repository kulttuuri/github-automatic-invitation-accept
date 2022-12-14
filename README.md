# github-automatic-invitation-accept

Ever needed to automatically accept invitations to Github repositories? With this script you can do that!

This script uses official Github API to loop through any new invitations and automatically accepts them.

## Setting Up

1) Clone this repository (or download it as zip archive and extract the archive)
2) Copy ``settings_example.json`` as ``settings.json``
3) Add your Github ``token``, ``username`` in ``settings.json``
4) Run with ``python3 main.py``
5) Enjoy!

## Production Deployment

The script will run forever. It checks for invitations, accepts them and then sleeps for 30 seconds. Rinses and repeats.

To deploy this to production, it would probably be best to use cronjob or process manager like [PM2](https://pm2.io), which can handle system restarts or crashes of the script.
