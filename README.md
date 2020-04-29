# covid-19 scraper

Note: This project is still under development

> Data scraper for covid-19 data

The aim of this project is to scrape publicly available covid-19 data and provide it in form of a HTTP Rest API

## Prerequisites

This project runs on python 3.7+. You can find installation instructions [here](https://python.org)

## Development setup

It is recommended that you create a virtual environment to manage the pythondependencies for this project. You can either use [virtualenv](https://virtualenv.pypa.io/en/latest/) or [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/) or any other recommended dependency management tool for python.

1. Activate your environment
2. Navigate to the root of this project and install dependencies
   ```
   pip install -r requirements.text
   ```
3. Make a `.env` file in the root of the project and copy the contents of `.env-example`, replacing the values with your own specific values
4. Run the application.
   ```
   python app.py
   ```

## Meta

Antonio Maina – [@\_\_r0b0t\_\_](https://twitter.com/__r0b0t__) – antoniomainakn@gmail.com

Distributed under the MIT license. See `LICENSE` for more information.

## Contributing

1. Fork the project
2. Create your feature branch from the develop branch(`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request
