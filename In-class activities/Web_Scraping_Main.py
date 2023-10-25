import Web_Scraping as wb


def main():
    """
    Main screen for the web scrapping file
    :return:
    """
    main_tree = wb.get_web_tree("https://www.wvu.edu")
    print(main_tree.xpath)
    # Find any tag with the id wvu-main, then go down one level, and obtain whatever text there is.
    # Right-click on your browser and hit Inspect (Chrome is preferable)
    uni_name = main_tree.xpath('//*[@id="wvu-main"]/h1/text()')
    print(uni_name)
    # Let us see how many divs are they under this section
    all_divs = main_tree.xpath('//*[@id="wvu-main"]/div')
    # This will display the number of sections
    print(str(len(all_divs)))
    # Interact with the first div
    first_div = all_divs[0]
    # This will get the number of sections (divs) under the first div.
    print(str(len(first_div)))
    # This will extract the FIND YOUR VIBE statement from the website.
    find_your_vibe = main_tree.xpath('//*[@id="wvu-main"]/div[1]/div[1]/div/h2/span/text()')
    print(find_your_vibe)


if __name__ == "__main__":
    main()
