import requests
from bs4 import BeautifulSoup

def main():
    main_link = "https://bugs.launchpad.net/ubuntu/+bugs?field.searchtext=&field.status%3Alist=EXPIRED&field.status%3Alist=CONFIRMED&field.status%3Alist=TRIAGED&field.status%3Alist=INPROGRESS&field.status%3Alist=FIXCOMMITTED&field.status%3Alist=FIXRELEASED&field.importance%3Alist=UNKNOWN&field.importance%3Alist=UNDECIDED&field.importance%3Alist=CRITICAL&field.importance%3Alist=HIGH&field.importance%3Alist=MEDIUM&field.importance%3Alist=LOW&field.importance%3Alist=WISHLIST&field.information_type%3Alist=PUBLIC&field.information_type%3Alist=PUBLICSECURITY&field.information_type%3Alist=PRIVATESECURITY&field.information_type%3Alist=USERDATA&assignee_option=any&field.assignee=&field.bug_reporter=&field.bug_commenter=&field.subscriber=&field.structural_subscriber=&field.component-empty-marker=1&field.tag=&field.tags_combinator=ANY&field.status_upstream-empty-marker=1&field.has_cve.used=&field.omit_dupes.used=&field.omit_dupes=on&field.affects_me.used=&field.has_no_package.used=&field.has_patch.used=&field.has_branches.used=&field.has_branches=on&field.has_no_branches.used=&field.has_no_branches=on&field.has_blueprints.used=&field.has_blueprints=on&field.has_no_blueprints.used=&field.has_no_blueprints=on&search=Search&orderby=-importance&memo=0&start=0"

    user_input = input('Enter "p" to get pages or "d" to display bug details: ')

    if user_input == 'p':
        page_number = int(input('Enter the page number to view (0-5508): '))
        if 0 <= page_number <= 5508:
            page_links = generate_links(main_link)
            selected_page_link = page_links[page_number]
            print(f"Link for Page {page_number}: {selected_page_link}")
        else:
            print("Invalid page number. Please enter a number between 0 and 5508.")
    elif user_input == 'd':
        page_number = int(input('Enter the page number to display bugs: '))
        if 0 <= page_number <= 5508:
            links = generate_links(main_link)
            selected_page_link = links[page_number]
            display_bugs_info(selected_page_link)
        else:
            print("Invalid page number. Please enter a number between 0 and 5508.")
    else:
        print("Invalid choice. Please enter 'p' or 'd.")

def generate_links(start_link):
    list_of_links = []

    # Calculate the links to pages
    for page_number in range(5509):  # 0 to 5508
        page_link = f"{start_link}&start={page_number * 75}"
        list_of_links.append(page_link)

    return list_of_links

def display_bugs_info(bugs_page):
    response = requests.get(bugs_page)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        bug_entries = soup.find_all('div', class_='buglisting-col2')  # Adjust the class name as needed

        for bug_entry in bug_entries:
            # Extract and display Bug Number and Title
            bug_number = bug_entry.find('span', class_='bugnumber').text.strip()
            bug_title = bug_entry.find('a', class_='bugtitle').text.strip()

            # Check if bug importance and heat elements exist before extracting
            bug_importance_element = bug_entry.find('span', class_='sprite package-source field')
            bug_heat_element = bug_entry.find('span', class_='sprite flame')

            if bug_importance_element:
                bug_importance = bug_importance_element.text.strip()
            else:
                bug_importance = "Importance not found"

            if bug_heat_element:
                bug_heat = bug_heat_element.text.strip()
            else:
                bug_heat = "Heat not found"

            print(f"Bug Number: {bug_number}")
            print(f"Title: {bug_title}")
            print(f"Importance: {bug_importance}")
            print(f"Heat: {bug_heat}")
            print()
    else:
        print(f"Failed to retrieve page: {bugs_page}")

if __name__ == "__main__":
    main()
