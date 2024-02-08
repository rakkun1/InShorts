"""import gensim
from gensim.summarization import summarize

text = "Your input text goes here. this is a very big text, it shall be summarized"

# Perform text summarization using Gensim's TextRank
summary = summarize(text)

# Print the summary
print(summary)
"""

import gensim

# List the attributes of the Gensim library
module_list = dir(gensim)

# Filter and print only the modules
module_list = [item for item in module_list if not item.startswith("__")]
print(module_list)
