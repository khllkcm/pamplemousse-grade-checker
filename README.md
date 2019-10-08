This script, run periodically by cron, will check for any changes on the ENSAE grades page on Pamplemousse and notify the user if *any* change is found.

## Configuration

1 - Edit the `config.json` file accordingly.

- `pamp_username`: Your Pamplemousse username.
- `pamp_password`: Your Pamplemousse password.
- `gmail_login`: The login for the gmail account that notfies the user (see the note below).
- `gmail_password`: The password for the gmail account that notfies the user.
- `recipient_address`: The email address of the user to be notified.
- `old_hash`: Leave blank, the script will fill it automatically.

2 - Edit the `crontab` with the desired periodicity (every hour by default) and the *absolute* path to the `PGC.py` file.


**Note**

Sendng emails is hard! The easiest way to make sure the notification email lands in the user's inbox and not their spam box is to send it from a gmail account. You can create a throwaway account and make sure to [turn on Less Secure App Access for that account](https://support.google.com/accounts/answer/6010255).
