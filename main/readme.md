# Simple Speech Bubble Generator for Discord

This small Python project offers the ability to add a speech bubble to any given image or screenshot automatically. After the editing process is complete, the resulting image can be uploaded to the desired Discord webhook.

## How to Use

1. Clone the repository
2. Make sure you have the latest version of python installed
3. Install the required libraries by running `requirements.bat`
4. Set the `WEBHOOK_URL` variable in the `main.py` to your Discord webhook URL
5. Run the script using `python main.py`
6. Follow the instructions in the terminal to provide the image and choose the speech bubble style

### Speech Bubble Styles

- **Prefix 1**: Adds a transparent speech bubble on the image (recommended for Images)
- **Prefix 2**: Adds a speech bubble above the image (recommended for Discord conversations)

### Adding Images

You can add an image by providing a file path, an image URL, or by copying the image to your clipboard if `pyperclip` is available.

## Contact

For any questions, feel free to contact me on Discord: Tap#4369
