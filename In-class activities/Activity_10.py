import requests
from bs4 import BeautifulSoup
# Package to connect to PostgreSQL
import psycopg2

class MyDB(object):
    _db_connection = None
    _db_cur = None

    def __init__(self):
        # Replace 'your_user' and 'your_password' with your PostgreSQL username and password
        self._db_connection = psycopg2.connect(host='localhost', user='cybrUser', password='c-4-9-3-A', dbname='cybrDB', port='5432')
        self._db_connection.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
        self._db_cur = self._db_connection.cursor()

    def query(self, query, params):
        first_return = self._db_cur.execute(query, params)
        try:
            return_me = self._db_cur.fetchall()
        except Exception:
            return_me = first_return
        return return_me

    def __del__(self):
        if self._db_connection is not None:
            self._db_connection.close()


# Function to extract bug information from the provided URL
def extract_bug_info(url):
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to retrieve the web page")
        return []

    soup = BeautifulSoup(response.content, 'html.parser')

    bug_info = []

    bug_rows = soup.find_all('div', class_='buglisting-row')

    for row in bug_rows:
        bug_number_elem = row.find('span', class_='bugnumber')
        status_elem = row.find('div', class_='status')
        heat_elem = row.find('span', class_='sprite flame')
        title_elem = row.find('a', class_='bugtitle')

        if bug_number_elem and status_elem and heat_elem and title_elem:
            bug_number = bug_number_elem.get_text().strip()
            status = status_elem.get_text().strip()
            heat = heat_elem.get_text().strip()
            title = title_elem.get_text().strip()

            bug_info.append((bug_number, status, heat, title))

    return bug_info

# URL of the bug page
bug_page_url = "https://bugs.launchpad.net/ubuntu/+bugs?field.searchtext=&field.status%3Alist=EXPIRED&field.status%3Alist=CONFIRMED&field.status%3Alist=TRIAGED&field.status%3Alist=INPROGRESS&field.status%3Alist=FIXCOMMITTED&field.status%3Alist=FIXRELEASED&field.importance%3Alist=UNKNOWN&field.importance%3Alist=UNDECIDED&field.importance%3Alist=CRITICAL&field.importance%3Alist=HIGH&field.importance%3Alist=MEDIUM&field.importance%3Alist=LOW&field.importance%3Alist=WISHLIST&field.information_type%3Alist=PUBLIC&field.information_type%3Alist=PUBLICSECURITY&field.information_type%3Alist=PRIVATESECURITY&field.information_type%3Alist=USERDATA&assignee_option=any&field.assignee=&field.bug_reporter=&field.bug_commenter=&field.subscriber=&field.structural_subscriber=&field.component-empty-marker=1&field.tag=&field.tags_combinator=ANY&field.status_upstream-empty-marker=1&field.has_cve.used=&field.omit_dupes.used=&field.omit_dupes=on&field.affects_me.used=&field.has_no_package.used=&field.has_patch.used=&field.has_branches.used=&field.has_branches=on&field.has_no_branches.used=&field.has_no_branches=on&field.has_blueprints.used=&field.has_blueprints=on&field.has_no_blueprints.used=&field.has_no_blueprints=on&search=Search&orderby=-importance&memo=75&start=0"

# Extract bug information
bug_info = extract_bug_info(bug_page_url)

if bug_info:
    db = MyDB()  # Create a MyDB instance

    table_name = "BugData"  # Modify the table name as needed

    # Define the SQL query with placeholders
    insert_query = f"INSERT INTO {table_name} (bug_number, status, heat, title) VALUES (%s, %s, %s, %s)"

    # Execute the query for each bug
    for bug in bug_info:
        db.query(insert_query, bug)

    # Close the database connection
    del db

    print(f"Inserted {len(bug_info)} bugs into the database.")
else:
    print("No bug information to insert.")
