from PIL import Image

def main():
    img_chain = Image.open('one-chain-stitch-symbol.jpg')
    img_singleCR = Image.open('single-crochet-stitch.jpg')
    img_doubleCR = Image.open('double-crochet-stitch.jpg')

    resized_chain = img_chain.resize((40, 40))
    resized_singleCR = img_singleCR.resize((40, 44))
    resized_doubleCR = img_doubleCR.resize((40, 50))

    resized_chain.save('chain_button.jpg')
    resized_singleCR.save('singleCR_button.jpg')
    resized_doubleCR.save('doubleCR_button.jpg')


if __name__ == "__main__":
    main()