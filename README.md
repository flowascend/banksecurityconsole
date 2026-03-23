# Bank security console
![Latest GitHub Release](https://img.shields.io/github/v/release/flowascend/banksecurityconsole?sort=date&display_name=release&style=flat&label=latest)
![Readme For](https://img.shields.io/badge/readme%20for-1.1.0-green)

This bank security console is for the Fufeltshmerts' Pakosti Incorporated bank, better known as FPI. If you've made it into this repository, you won't be able to run this code, since you don't have the rights to connect to DB, but feel free to use the code or its snippets.

## How to install

> Python3 and pip3 should be already installed.
- Download the source code from the [Github Releases page](https://github.com/flowascend/banksecurityconsole/releases/latest)
- Unpack the source code
- Open the command line in the unpacked folder

> Note: it is highly recommended to create a virtual environment before installing dependencies.
> You can do so by running this command to create it:
> ```bash
> python -m venv .venv
> ```
> And then this command to use the command line with it:
> Windows:
> ```bash
> .\.venv\Scripts\activate
> ```
> Linux/MacOS:
> ```bash
> source ./.venv/bin/activate
> ```

Then use `pip` to install dependencies:
```bash
pip install -r requirements.txt
```

Then, create a `.env` file in the source folder.
Paste in this template:
```env
DB_ENGINE=
DB_HOST=
DB_PORT=
DB_NAME=
DB_USER=
DB_PASSWORD=
DB_SECRET_KEY=
```
and fill in the values.

## How to run

Run the following command:
```bash
python main.py
```
