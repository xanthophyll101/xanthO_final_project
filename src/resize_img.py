from PIL import Image

def main():
    og_button = Image.open('render-button.jpg')

    resized_chain = og_button.resize((190, 40))

    resized_chain.save('rendering-button.jpg')


if __name__ == "__main__":
    main()