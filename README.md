# Property Builder

Some websites automatically block any kind of scraping, and that’s why I’ll be defining a header to pass along the `get` command, which will basically make our queries to the website look like they are coming from an actual browser. When we run the program, I’ll have a sleep command between pages, so we can mimic a “more human” behavior and don’t overload the site with several requests per second. You will get blocked if you scrape too aggressively, so it’s a nice policy to be polite while scraping.
