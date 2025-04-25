import argparse
from playwright.sync_api import sync_playwright



def take_screenshot(url: str, width: int, height: int, output_file: str):
	with sync_playwright() as p:
		browser = p.chromium.launch()
		context = browser.new_context(
			viewport={'width': width, 'height': height}
		)
		page = context.new_page()
		page.goto(url)
		page.screenshot(path=output_file, full_page=True)
		print(f"Screenshot saved to {output_file}")
		browser.close()


def main():
	parser = argparse.ArgumentParser(description="Take a screenshot of a webpage.")
	parser.add_argument("--url", type=str, default="https://chances.netlify.app", help="URL of the webpage")
	parser.add_argument("--width", type=int, default=960, help="Viewport width")
	parser.add_argument("--height", type=int, default=960, help="Viewport height")
	parser.add_argument("--output", type=str, default="screenshot.png", help="Output file path")

	args = parser.parse_args()

	take_screenshot(
		url=args.url,
		width=args.width,
		height=args.height,
		output_file=args.output
	)


if __name__ == '__main__':
	main()
