import time
import random_word
from concurrent.futures import ProcessPoolExecutor, as_completed
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import multiprocessing

# ChromeDriver path
driver_path = "/usr/local/bin/chromedriver"

# Chrome options
options = Options()
options.add_argument("--headless")  # Run Chrome in headless mode
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument(f"--disable-memory-coordinator")
options.add_argument(f"--disable-sync")
options.add_argument(f"--disable-threaded-animation")
options.add_argument(f"--max-memory-percentage=100")

# Set the Chrome binary location
options.binary_location = '/usr/bin/google-chrome-stable'

# Create a new ChromeDriver service
#service = Service(driver_path)

# Start the ChromeDriver
#service.start()

# Create a new WebDriver instance
#driver = webdriver.Chrome(service=service, options=options)

# Number of workers/users
num_workers = multiprocessing.cpu_count()
# num_workers = 16
# Number of searches per worker
num_searches_per_worker = 1

# Initialize random word generator
word_generator = random_word.RandomWords()

# Function to perform a single search
def perform_search():
    # Create a new ChromeDriver service for each worker
    local_service = Service(driver_path)
    local_service.start()

    # Create a new WebDriver instance using the local service and options
    local_driver = webdriver.Chrome(service=local_service, options=options)

    # Generate a random word for the search
    word = word_generator.get_random_word()

    # Start the timer
    start_time = time.time()

    # Navigate to the URL with the random word
    url = f"https://8080-alamin655-websurfx-93hmkbinbg0.ws-us97.gitpod.io/search?q={word}"
    local_driver.get(url)

    # Perform any necessary actions or assertions

    # Calculate the elapsed time
    elapsed_time = time.time() - start_time

    # Quit the WebDriver for the current worker
    local_driver.quit()

    # Stop the ChromeDriver service for the current worker
    local_service.stop()

    return elapsed_time

# Create a ProcessPoolExecutor with the desired number of workers
with ProcessPoolExecutor(max_workers=num_workers) as executor:
    # Submit search tasks to the executor
    futures = []
    for _ in range(num_workers * num_searches_per_worker):
        future = executor.submit(perform_search)
        futures.append(future)

    # Wait for all tasks to complete
    results = []
    for future in as_completed(futures):
        result = future.result()
        results.append(result)

# Process the results
min_time = min(results)
max_time = max(results)
total_time = sum(results)
average_time = total_time / len(results)

# Output the results
print(f"Number of workers/users: {num_workers}")
print(f"Number of searches per worker/user: {num_searches_per_worker}")
print(f"Total time: {total_time:.2f}s")
print(f"Average time per search: {average_time:.2f}s")
print(f"Minimum time: {min_time:.2f}s")
print(f"Maximum time: {max_time:.2f}s")

# Quit the WebDriver and close the associated window
#driver.quit()

# Stop the ChromeDriver service
#service.stop()
