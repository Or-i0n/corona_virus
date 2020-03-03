"""
Just press RUN.

-----------------| About |---------------------
>MN908947.3 Severe acute respiratory syndrome coronavirus 2 isolate Wuhan-Hu-1, complete genome

----------------| Reference |------------------
Wu, F., Zhao, S., Yu, B. et al. A new coronavirus associated with human respiratory disease in China. Nature (2020). https://doi.org/10.1038/s41586-020-2008-3

"""

from urllib import request


link = ("https://raw.githubusercontent.com"
        "/Or-i0n/corona_virus/master/"
        "corona_genome.txt")

raw = request.urlopen(link)

genome = raw.read().decode()

for nucleotide in genome:
    if nucleotide != "\n":
        print(nucleotide, end="")
