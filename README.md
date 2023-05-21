# PySearchTimer

PySearchTimer is a Python script that measures the time taken to perform a search using Selenium and a random word generator. It uses ChromeDriver and a headless Chrome browser to navigate to a URL with a randomly generated word as a query parameter. It then records the elapsed time and outputs the results.

## Prerequisites

- Python >=3.7
- Chrome browser
- ChromeDriver

## Installation

Clone the repository:

```bash
git clone https://github.com/alamin655/PySearchTimer.git
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## Windows

### Download and Install ChromeDriver

- Visit the ChromeDriver download page: [ChromeDriver](https://sites.google.com/chromium.org/driver/)
- Download the appropriate ChromeDriver version based on your Chrome browser version. Make sure to choose the version that matches your Chrome browser version (e.g., if you have Chrome version 113, download ChromeDriver version 113).
- Extract the downloaded ZIP file.
- Copy the chromedriver.exe file to a directory of your choice.
- Update the `driver_path` variable in the code to the path where you copied the `chromedriver.exe` file, for example:

  ```python
  # ChromeDriver path
  driver_path = "C:/path/to/chromedriver.exe"
  ```

### Download and Install Google Chrome

- Visit the Google Chrome download page: [Google Chrome](https://www.google.com/chrome/)
- Download the installer for Google Chrome.
- Run the installer and follow the instructions to install Google Chrome.

### Set the Chrome Binary Location

- Find the installation directory of Google Chrome. By default, it is usually located in `C:\Program Files\Google\Chrome\`.
- Update the options.binary_location variable in the code to the path of the Chrome binary, for example:

  ```python
  # Set the Chrome binary location
  options.binary_location = 'C:/Program Files/Google/Chrome/chrome.exe'
  ```

### Run the script:

```bash
python search_timer.py
```

## Linux

### Download and Install ChromeDriver

- Open a terminal.
- Download ChromeDriver using the following command:

  ```bash
  wget https://chromedriver.storage.googleapis.com/113.0.5672.63/chromedriver_linux64.zip
  ```
  Replace `113.0.5672.63` with the appropriate version of ChromeDriver based on your Chrome browser version. You can check the version compatibility on the [ChromeDriver download page](https://sites.google.com/chromium.org/driver/).

- Extract the downloaded ZIP file using the following command:

  ```bash
  unzip chromedriver_linux64.zip
  ```

- Move the extracted `chromedriver` binary to a directory of your choice, for example:

  ```bash
  sudo mv chromedriver /usr/local/bin/
  ```

- Verify that ChromeDriver is correctly installed by running the following command:

  ```bash
  chromedriver --version
  ```

- Update the `driver_path` variable in the code to the path where you moved the `chromedriver` binary, for example:

  ```python
  # ChromeDriver path
  driver_path = "/usr/local/bin/chromedriver"
  ```

### Download and Install Google Chrome Stable

- Open a terminal.
- Run the following commands to download and install Google Chrome Stable:

  ```bash
  wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
  sudo dpkg -i google-chrome-stable_current_amd64.deb
  sudo apt-get install -f
  ```

- Verify that Chrome is correctly installed by running the following command:

  ```bash
  google-chrome-stable --version
  ```

### Set the Chrome Binary Location

- Open a terminal.
- Find the location of the Chrome binary by running the following command:

  ```bash
  which google-chrome-stable
  ```
  
- Update the `options.binary_location` variable in the code to the path of the Chrome binary, for example:

  ```python
  # Set the Chrome binary location
  options.binary_location = '/usr/bin/google-chrome-stable'
  ```

### Run the script:

```bash
python search_timer.py
```

## Configuration

You can customize the following variables in the script:

- The `driver_path` variable specifies the path to the ChromeDriver executable. Make sure to provide the correct path to the `chromedriver` binary based on your operating system (Windows or Linux) as mentioned in the previously.
- The `options` variable holds the configuration options for the Chrome browser. In this code, we are setting options such as running Chrome in headless mode `(--headless)`, disabling the sandbox `(--no-sandbox)`, and disabling the shared memory usage `(--disable-dev-shm-usage)`.
- The `options.binary_location` specifies the path to the Chrome binary. This should be set to the location where you have installed Google Chrome Stable. Update this path based on your operating system (Windows or Linux) as mentioned in the previously.
- `num_workers`: Number of workers/users.
- `num_searches_per_worker`: Number of searches per worker/user.
- In the provided code, the URL is set to `"https://8080-alamin655-websurfx-93hmkbinbg0.ws-us97.gitpod.io/search?q={word}"`. Replace this URL with the appropriate URL for your specific use case or application, for example: `url = f"https://www.google.com/search?q={word}"`

## Results

The script will output the following results:

- Number of workers/users
- Number of searches per worker/user
- Total time taken
- Average time per search
- Minimum time
- Maximum time

Feel free to modify the code according to your requirements.

## License
This project is licensed under the [MIT License](LICENSE)
