import requests
from bs4 import BeautifulSoup

class BugTrackingSystem:

    def Generate_Pages(self, initial_link):
        # Create a list to store the links
        page_links = [initial_link]

        # Set a maximum number of pages you want to traverse (change as needed)
        max_pages = 75

        # Initialize a counter
        page_counter = 0

        # Create a session to maintain cookies and headers for requests
        session = requests.Session()

        while page_counter < max_pages and page_links:
            # Get the next link from the list
            link = page_links.pop(0)

            try:
                # Send a GET request to the link
                response = session.get(link)

                # Check if the request was successful
                if response.status_code == 200:
                    # Parse the HTML content of the page
                    soup = BeautifulSoup(response.text, 'html.parser')

                    # Print the current page link
                    print(f"Page {page_counter + 1}: {link}")

                    # Extract links from the page and add them to the list
                    for a_tag in soup.find_all('a', href=True):
                        next_link = a_tag['href']
                        if next_link.startswith("http"):
                            page_links.append(next_link)

                    # Increment the page counter
                    page_counter += 1

            except Exception as e:
                print(f"Error while processing {link}: {e}")

# Usage example
if __name__ == "__main__":
    bug_tracker = BugTrackingSystem()
    initial_link = "https://bugs.launchpad.net/ubuntu/+bugs?field.searchtext=&field.status%3Alist=EXPIRED&field.status%3Alist=CONFIRMED&field.status%3Alist=TRIAGED&field.status%3Alist=INPROGRESS&field.status%3Alist=FIXCOMMITTED&field.status%3Alist=FIXRELEASED&field.importance%3Alist=UNKNOWN&field.importance%3Alist=UNDECIDED&field.importance%3Alist=CRITICAL&field.importance%3Alist=HIGH&field.importance%3Alist=MEDIUM&field.importance%3Alist=LOW&field.importance%3Alist=WISHLIST&field.information_type%3Alist=PUBLIC&field.information_type%3Alist=PUBLICSECURITY&field.information_type%3Alist=PRIVATESECURITY&field.information_type%3Alist=USERDATA&assignee_option=any&field.assignee=&field.bug_reporter=&field.bug_commenter=&field.subscriber=&field.structural_subscriber=&field.component-empty-marker=1&field.tag=&field.tags_combinator=ANY&field.status_upstream-empty-marker=1&field.has_cve.used=&field.omit_dupes.used=&field.omit_dupes=on&field.affects_me.used=&field.has_no_package.used=&field.has_patch.used=&field.has_branches.used=&field.has_branches=on&field.has_no_branches.used=&field.has_no_branches=on&field.has_blueprints.used=&field.has_blueprints=on&field.has_no_blueprints.used=&field.has_no_blueprints=on&search=Search&orderby=-importance&memo=75&start=0"
    bug_tracker.Generate_Pages(initial_link)
