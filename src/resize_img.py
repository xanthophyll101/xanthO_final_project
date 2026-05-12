from PIL import Image

def main():
    og_button = Image.open('toolbar_background.png')

    resized_chain = og_button.resize((740, 190))

    resized_chain.save('rendering-button-quality.png')


if __name__ == "__main__":
    main()