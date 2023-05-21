# PySearchTimer

PySearchTimer is a Python script that measures the time taken to perform a search using Selenium and a random word generator. It uses ChromeDriver and a headless Chrome browser to navigate to a URL with a randomly generated word as a query parameter. It then records the elapsed time and outputs the results.

## Prerequisites

- Python >=3.7
- Chrome browser
- ChromeDriver

## Installation

1. Clone the repository:

```bash
git clone https://github.com/alamin655/PySearchTimer.git
```

2. Install the required packages:

```bash
pip install -r requirements.txt
```

3. Download and install ChromeDriver from the official website: [ChromeDriver](https://sites.google.com/chromium.org/driver/)

4. Set the ChromeDriver path in the code:

```python
# ChromeDriver path
driver_path = "/usr/local/bin/chromedriver"
```

5. Run the script:

```bash
python search_timer.py
```

## Configuration
You can customize the following variables in the script:

- `num_workers`: Number of workers/users.
- `num_searches_per_worker`: Number of searches per worker/user.

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
