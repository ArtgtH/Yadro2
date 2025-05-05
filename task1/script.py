import logging
import requests

logging.basicConfig(
	level=logging.INFO,
	format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
	handlers=[logging.StreamHandler()],
)
logger = logging.getLogger("statuses_checker")

URL = "https://httpstat.us/random/100,200,300,400,500"


def main():
	for _ in range(5):
		try:
			response = requests.get(URL)

			if response.status_code // 100 in (1, 2, 3):
				logger.info(f"Status: {response.status_code}; Body: {response.text}")
			else:
				raise Exception(f"Error: Status {response.status_code}")

		except Exception as e:
			logger.error(f"Got error: {e}")


if __name__ == "__main__":
	main()
