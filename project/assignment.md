Instant Search
Build a minimal API that responds to a query term with a list of best possible matches. The source file data.csv contains > 300k names.

Use some data structure, which allows for API to work without iterating through the whole source data. API response time must be as low as possible (say ~10ms).

You can't use any external tool - database/cache

Get started
Install flask:

pip3 install flask
Modify server.py to include your solution. Run it with the following command:

FLASK_APP=server.py flask run -p 8888 --reload
Open index.html to view the autocomplete input box and test your solution.

Results & Ranking
The API must return results only when the query term length is >= 3 characters. And it needs to rank search results according to below criteria (in order of priority)

Results that start with the query term must be given higher priority.
Then, the shortest (in length) result is preferred.
For Bonus Points
Write test cases around the result ranking criteria.
Associate a score/rank along with each result (and show it in the UI)
Evaluation
While use of (appropriate) data-structures is important, the solution will be evaluated largely based on code quality, correctness and ease of understanding (good documentation and clean, structured code goes a long way).

Data structures are just a means to an end; how you use them to write production-level code, and how easy it is to understand is of higher importance here.

