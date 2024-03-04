from text_extractor import TextExtractor

if __name__ == "__main__":
    
    # fichiers CV à extraire
    file_paths = ["./assets/CV_Appolinaire_ADANDE (1).pdf"]

    for file_path in file_paths:
        text_extractor = TextExtractor(file_path)
        text = text_extractor.extract()
        print(f"Fichier {file_path} \n\n {text} \n\n\n")
        