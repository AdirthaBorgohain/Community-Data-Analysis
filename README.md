# Community-Data-Analysis

Data and Visual Analysis on several different communities generated using Louvain Algorithm in Neo4j on the dblp dataset.

### Steps to run:

1. Install libraries and modules listed in requirements.txt. `pip install -r requirements.txt`
2. Download fasttext magnitude vectors from http://magnitude.plasticity.ai/fasttext/medium/wiki-news-300d-1M-subword.magnitude . Create a directory named `vectors` and place the downloaded magnitude file inside it.
3. To generate the complete JSON file for analysis, run the `generate_complete_JSON.py` file once.
4. All the individual notebooks with community id can be run independently for analysis of that specific community. The`Top10CommunitiesAnalysis.ipynb` file can be run for performing analysis as a whole for all the communities.