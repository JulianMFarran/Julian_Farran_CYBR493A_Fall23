# Import the required modules
import Web_Scraping as wb

def main():
    """
    Main function for web scraping.
    """
    # Access the web page
    main_tree = wb.get_web_tree("https://www.wvu.edu")

    # Extract and print the first text
    university_name = main_tree.xpath('normalize-space(/html/body/main/div[1]/div[1]/div/h1/span/text())')
    print("Text 1 (First Text):", university_name)

    # Extract and print the second text (Number of divs under the specified section)
    div1_text = main_tree.xpath('normalize-space(/html/body/main/div[3]/div/div[3]/div[1]/div/h3/text())')
    print("Text 2 (Second Text):", div1_text)

    # Extract and print the third text (Number of divs under the specified section)
    div2_text = main_tree.xpath('normalize-space(/html/body/main/div[3]/div/div[3]/div[2]/div/h3/text())')
    print("Text 3 (Third Text):", div2_text)

    # Extract and print the fourth text (Find Your Vibe statement)
    find_your_vibe = main_tree.xpath('normalize-space(/html/body/main/div[1]/div[1]/div/p[2]/text())')
    print("Text 4 (Fourth Text):", find_your_vibe)

    # Extract and print the fifth text (Additional text)
    div3_text = main_tree.xpath('normalize-space(/html/body/main/div[3]/div/div[3]/div[3]/div/h3/text())')
    print("Text 5 (Fifth Text):", div3_text)

if __name__ == "__main__":
    main()
