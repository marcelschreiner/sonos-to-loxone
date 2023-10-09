# sonos-to-loxone

![Pylint](https://github.com/marcelschreiner/sonos-to-loxone/actions/workflows/pylint.yml/badge.svg)
[![HitCount](https://hits.dwyl.com/marcelschreiner/sonos-to-loxone.svg?style=flat)](http://hits.dwyl.com/marcelschreiner/sonos-to-loxone)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=marcelschreiner_sonos-to-loxone&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=marcelschreiner_sonos-to-loxone)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=marcelschreiner_sonos-to-loxone&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=marcelschreiner_sonos-to-loxone)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=marcelschreiner_sonos-to-loxone&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=marcelschreiner_sonos-to-loxone)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=marcelschreiner_sonos-to-loxone&metric=bugs)](https://sonarcloud.io/summary/new_code?id=marcelschreiner_sonos-to-loxone)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=marcelschreiner_sonos-to-loxone&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=marcelschreiner_sonos-to-loxone)
[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=marcelschreiner_sonos-to-loxone&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=marcelschreiner_sonos-to-loxone)
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=marcelschreiner_sonos-to-loxone&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=marcelschreiner_sonos-to-loxone)
[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=marcelschreiner_sonos-to-loxone&metric=sqale_index)](https://sonarcloud.io/summary/new_code?id=marcelschreiner_sonos-to-loxone)

This Python script is designed to schedule an alarm on a Sonos speaker based on the time of an alarm clock set on a Loxone Miniserver. It fetches the next alarm time from the Miniserver and schedules it on a specific Sonos speaker.

## Prerequisites

Before using this script, make sure you have the following:

- Python 3.x installed on your system.
- The `requests` library installed. You can install it using `pip`:
   (`pip3` is traditionally used on Rapberry Pis to install libraries for Python 3 other systems may use `pip`)
```shell
pip3 install requests
```

- The `soco` library installed. You can install it using `pip`:

```shell
pip3 install soco
```

## Configuration

Before running the script, you need to configure the following parameters in the code:

- Replace `<USER>` and `<PASSWORD>` with your Miniserver credentials.
- Replace `<MINISERVER_IP>` with the IP address of your Miniserver.
- Replace `<NAME_OR_UUID_OF_ALARM_CLOCK>` with the name or UUID of the alarm clock in your Miniserver.
- Replace `<NAME_OF_YOUR_SONOS_SPEAKER>` with the name of the Sonos speaker you want to set the alarm on.

## Usage

You can run the script by executing the following command in your terminal:

```shell
python3 sonos2lox.py
```

The script does only poll the Miniserver once and quits again. The following example is for a Raspberry Pi to run the script every minute 30 seconds past the minute mark:

```shell
- In the terminal enter: "crontab -e"
- Then add the line "* * * * * ( sleep 30 ; python3 /home/pi/sonos2lox.py )"
- Save and exit
```

## Script Explanation

1. The script sends a request to the Miniserver to fetch the next alarm time.
2. It processes the response to determine the next alarm time.
3. It calculates the day and time of the alarm.
4. It checks if there are any alarms scheduled on the Sonos speaker "Desk Marcel" and filters them.
5. If no alarms are found or more than one alarm is found, the script exits with an error code.
6. If exactly one alarm is found, it schedules the alarm for the next occurrence and exits successfully.

## Error Codes

- `0`: Success - Alarm scheduled successfully.
- `1`: No alarms found on the Sonos speaker.
- `2`: Multiple alarms found on the Sonos speaker.
- `3`: Something went wrong while fetching the alarm data from the Miniserver.
- `4`: The alarm date is far off in the future and not supported by the script.

## Note

- This script assumes that the alarm data from the Miniserver is in a specific **GERMAN** format. Please make adjust the script to match your language settings on the Miniserver.
- Make sure your Sonos speaker is correctly named reachable on your network.

## License

This script is provided under the [MIT License](LICENSE.md). Feel free to modify and use it according to your needs.

<br />

[![SonarCloud](https://sonarcloud.io/images/project_badges/sonarcloud-black.svg)](https://sonarcloud.io/summary/new_code?id=marcelschreiner_sonos-to-loxone)
