# Capstone_3_GPT-2-Relationship-Advice

Robert Malka
Springboard Data Science Career Track, March 2020 cohort

Capstone Project III

### Problem Statement: 

How can we use GPT-2 to give relationship advice?

### Background:

What if we could create a model that reliably gives relationship advice to anyone who needs it, aggregated from millions (or more!) posts on a subreddit such as r/relationship_advice? It might enable some who can’t bring themselves to reach out to others, particularly in these isolated times, to post their question into a simple app and get some crowdsourced advice that helps them see their situation in a new way, with the full awareness that an AI won’t (cannot) judge them.

We scraped Reddit’s r/relationship advice, specifically focusing on the post titles and comments and ran them through GPT-2, in order to test the efficacy of such advice. We also performed a light EDA on the dataset, seeing reading level, wordclouds, and sentiment polarity, along with performing a Latent Dirichlet Allocation (LDA) to see how best to cluster the different post titles and comments. 

The business problem may not have a specific timespan or clear numerical benchmark attached to it, but that does not stop it from being potentially useful to a group wanting to optimize such advice. We will post some of the best answers GPT-2 has provided, grapple with how it understands the data it’s received and processed, and discuss ways to further improve its output.

There is also a huge optional aside at the end discussing the philosophical dangers of taking this project seriously, or even attempting to improve the output of such a project – remarks that too few people in the field are making, and should perhaps make more often.

Finally, this version of GPT-2 will be put on a website for others to test (along with the philosophical and practical caveats this enterprise deserves). Link forthcoming.

### Data Source:

My data was scraped from Reddit’s r/relationship_advice, where I used PSAW (Python Pushshift API Wrapper) to collect data. I managed to collect a million posts, and three million comments (many of which were multiple, sometimes hundreds, of comments for a single thread). I simply joined all comments with the same ID into a single cell, and then linked that ID to the post it was connected to. Doing so reduced the overall size of the dataset to ~184,000 rows. This meant deleting approximately 800k rows of threads, for which I could not pull the comments. GPT-2 was trained ~8,000 steps over a total of ~75MM tokens.

Objectives:

    Scrape Reddit's r/relationship_advice
    Perform an EDA on the data to get a broad sense of the issues covered and advice given
    Effectively train GPT-2 on that data
    Create a website where users can generate text from GPT-2 based on their own issues (Forthcoming)

Reports

[Jupyter notebook for data scraping, data cleaning, & Exploratory Data Analysis](https://github.com/rjmalka/Capstone_3_GPT-2-Relationship-Advice/blob/main/notebook/Relationship%20Advice_Capstone%20Three.ipynb)

[Google Colab notebook to train & generate text from GPT-2](https://github.com/rjmalka/Capstone_3_GPT-2-Relationship-Advice/blob/main/notebook/GPT_2's_Relationship_Advice.ipynb)

[Capstone Project III Final Report](https://github.com/rjmalka/Capstone_3_GPT-2-Relationship-Advice/blob/main/report/GPT-2%20Relationship%20Advice%20Report.pdf)

[Capstone Project III Final Presentation](https://github.com/rjmalka/Capstone_3_GPT-2-Relationship-Advice/blob/main/report/GPT-2_Capstone_Final_Slides.pdf)

[Sample text generated from GPT-2](https://github.com/rjmalka/Capstone_3_GPT-2-Relationship-Advice/tree/main/text%20from%20gpt-2)
