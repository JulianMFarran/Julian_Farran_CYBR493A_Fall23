# Import the required modules
import Web_Scraping as wb

def main():
    """
    Main function for web scraping.
    """
    # Access the web page
    main_tree = wb.get_web_tree("https://www.wvu.edu")

    # Extract and print the first text (Climb Higher)
    first_text = main_tree.xpath('normalize-space(/html/body/main/div[1]/div[1]/div/h1/span/text())')
    print("Text 1 (First Text):", first_text)

    # Extract and print the second text (Future Students)
    second_text = main_tree.xpath('normalize-space(/html/body/main/div[3]/div/div[3]/div[1]/div/h3/text())')
    print("Text 2 (Second Text):", second_text)

    # Extract and print the third text (Admitted Students)
    third_text = main_tree.xpath('normalize-space(/html/body/main/div[3]/div/div[3]/div[2]/div/h3/text())')
    print("Text 3 (Third Text):", third_text)

    # Extract and print the fourth text (See how much you can recieve!)
    fourth_text = main_tree.xpath('normalize-space(/html/body/main/div[1]/div[1]/div/p[2]/text())')
    print("Text 4 (Fourth Text):", fourth_text)

    # Extract and print the fifth text (Families)
    fifth_text = main_tree.xpath('normalize-space(/html/body/main/div[3]/div/div[3]/div[3]/div/h3/text())')
    print("Text 5 (Fifth Text):", fifth_text)

if __name__ == "__main__":
    main()
